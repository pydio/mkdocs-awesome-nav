def test(mkdocs):
    mkdocs.docs(
        """
        foo/
            a.md
            b.md
        .nav.yml
        | nav:
        |   - foo
        """
    )
    mkdocs.build().assert_nav(
        """
        - Foo:
            - A: foo/a.md
            - B: foo/b.md
        """
    )


def test_dot_slash(mkdocs):
    mkdocs.docs(
        """
        foo/
            a.md
            b.md
        .nav.yml
        | nav:
        |   - ./foo
        """
    )
    mkdocs.build().assert_nav(
        """
        - Foo:
            - A: foo/a.md
            - B: foo/b.md
        """
    )


def test_trailing_slash(mkdocs):
    mkdocs.docs(
        """
        foo/
            a.md
            b.md
        .nav.yml
        | nav:
        |   - foo/
        """
    )
    mkdocs.build().assert_nav(
        """
        - Foo:
            - A: foo/a.md
            - B: foo/b.md
        """
    )


def test_deep(mkdocs):
    mkdocs.docs(
        """
        foo/
            bar/
                foo.md
        .nav.yml
        | nav:
        |   - foo/bar
        """
    )
    mkdocs.build().assert_nav(
        """
        - Bar:
            - Foo: foo/bar/foo.md
        """
    )


def test_title(mkdocs):
    mkdocs.docs(
        """
        foo/
            a.md
            b.md
        .nav.yml
        | nav:
        |   - Title: foo
        """
    )
    mkdocs.build().assert_nav(
        """
        - Title:
            - A: foo/a.md
            - B: foo/b.md
        """
    )


def test_duplicate(mkdocs):
    mkdocs.docs(
        """
        foo/
            a.md
            b.md
        .nav.yml
        | nav:
        |   - foo
        |   - foo
        """
    )
    mkdocs.build().assert_nav(
        """
        - Foo:
            - A: foo/a.md
            - B: foo/b.md
        """
    )


def test_resolve_directory_before_pattern(mkdocs):
    mkdocs.docs(
        """
        foo/
            foo.md
        bar.md
        .nav.yml
        | nav:
        |   - "*"
        |   - foo
        """
    )
    mkdocs.build().assert_nav(
        """
        - Bar: bar.md
        - Foo:
            - Foo: foo/foo.md
        """
    )


def test_resolve_deep_directory_before_other_directory(mkdocs):
    mkdocs.docs(
        """
        foo/
            foo.md
            bar/
                bar.md
        .nav.yml
        | nav:
        |   - foo
        |   - foo/bar
        """
    )
    mkdocs.build().assert_nav(
        """
        - Foo:
            - Foo: foo/foo.md
        - Bar:
            - Bar: foo/bar/bar.md
        """
    )


def test_unknown(mkdocs, logs):
    mkdocs.docs(
        """
        foo.md
        .nav.yml
        | nav:
        |   - foo
        """
    )
    mkdocs.build().assert_nav_empty()
    assert logs.from_plugin == [
        logs.warning("awesome-nav: The nav item 'foo' doesn't match any files or directories [.nav.yml]"),
    ]


def test_unknown_with_title(mkdocs, logs):
    mkdocs.docs(
        """
        foo.md
        .nav.yml
        | nav:
        |   - Title: foo
        """
    )
    mkdocs.build().assert_nav(
        """
        - Title: foo
        """
    )
    assert logs.from_plugin == []
    assert (
        logs.warning(
            "A reference to 'foo' is included in the 'nav' configuration, "
            "which is not found in the documentation files."
        )
        in logs.all
    )


def test_empty_directory_nav(mkdocs, logs):
    mkdocs.docs(
        """
        foo/
            bar.md
            .nav.yml
            | nav: []
        .nav.yml
        | nav:
        |   - foo
        """
    )
    mkdocs.build().assert_nav_empty()
    assert logs.from_plugin == []
