def test(mkdocs):
    mkdocs.docs(
        """
        foo.md
        .nav.yml
        | nav:
        |   - foo.md
        """
    )
    mkdocs.build().assert_nav(
        """
        - Foo: foo.md
        """
    )


def test_dot_slash(mkdocs):
    mkdocs.docs(
        """
        foo.md
        .nav.yml
        | nav:
        |   - ./foo.md
        """
    )
    mkdocs.build().assert_nav(
        """
        - Foo: foo.md
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
        |   - foo/bar/foo.md
        """
    )
    mkdocs.build().assert_nav(
        """
        - Foo: foo/bar/foo.md
        """
    )


def test_title(mkdocs):
    mkdocs.docs(
        """
        foo.md
        .nav.yml
        | nav:
        |   - Title: foo.md
        """
    )
    mkdocs.build().assert_nav(
        """
        - Title: foo.md
        """
    )


def test_duplicate(mkdocs):
    mkdocs.docs(
        """
        foo.md
        .nav.yml
        | nav:
        |   - foo.md
        |   - foo.md
        """
    )
    mkdocs.build().assert_nav(
        """
        - Foo: foo.md
        - Foo: foo.md
        """
    )


def test_resolve_file_before_directory(mkdocs):
    mkdocs.docs(
        """
        foo/
            a.md
            b.md
        .nav.yml
        | nav:
        |   - foo
        |   - foo/a.md
        """
    )
    mkdocs.build().assert_nav(
        """
        - Foo:
            - B: foo/b.md
        - A: foo/a.md
        """
    )


def test_resolve_file_before_pattern(mkdocs):
    mkdocs.docs(
        """
        a.md
        b.md
        .nav.yml
        | nav:
        |   - "*"
        |   - a.md
        """
    )
    mkdocs.build().assert_nav(
        """
        - B: b.md
        - A: a.md
        """
    )


def test_unknown(mkdocs, logs):
    mkdocs.docs(
        """
        foo.md
        .nav.yml
        | nav:
        |   - bar.md
        """
    )
    mkdocs.build().assert_nav_empty()
    assert logs.from_plugin == [
        logs.warning("awesome-nav: The nav item 'bar.md' doesn't match any files or directories [.nav.yml]"),
    ]


def test_unknown_with_title(mkdocs, logs):
    mkdocs.docs(
        """
        foo.md
        .nav.yml
        | nav:
        |   - Title: bar.md
        """
    )
    mkdocs.build().assert_nav(
        """
        - Title: bar.md
        """
    )
    assert logs.from_plugin == []
    assert (
        logs.warning(
            "A reference to 'bar.md' is included in the 'nav' configuration, "
            "which is not found in the documentation files."
        )
        in logs.all
    )
