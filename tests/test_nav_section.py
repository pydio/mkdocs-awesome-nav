def test(mkdocs):
    mkdocs.docs(
        """
        foo.md
        .nav.yml
        | nav:
        |   - Foo:
        |       - foo.md
        """
    )
    mkdocs.build().assert_nav(
        """
        - Foo:
            - Foo: foo.md
        """
    )


def test_empty(mkdocs):
    mkdocs.docs(
        """
        .nav.yml
        | nav:
        |   - Foo: []
        """
    )
    mkdocs.build().assert_nav(
        """
        - Foo: []
        """
    )


def test_empty_due_to_no_matches(mkdocs, logs):
    mkdocs.docs(
        """
        .nav.yml
        | nav:
        |   - Foo:
        |       - foo.md
        """
    )
    mkdocs.build().assert_nav(
        """
        - Foo: []
        """
    )
    assert logs.from_plugin == [
        logs.warning("awesome-nav: The nav item 'foo.md' doesn't match any files or directories [.nav.yml]"),
    ]


def test_nested(mkdocs):
    mkdocs.docs(
        """
        foo.md
        .nav.yml
        | nav:
        |   - Foo:
        |       - Bar:
        |           - foo.md
        """
    )
    mkdocs.build().assert_nav(
        """
        - Foo:
            - Bar:
                - Foo: foo.md
        """
    )


def test_resolve_with_same_priority(mkdocs):
    mkdocs.docs(
        """
        foo/
            a.md
            b.md
        .nav.yml
        | nav:
        |   - foo
        |   - Section:
        |       - foo/a.md
        """
    )
    mkdocs.build().assert_nav(
        """
        - Foo:
            - B: foo/b.md
        - Section:
            - A: foo/a.md
        """
    )
