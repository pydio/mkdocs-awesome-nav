def test(mkdocs):
    mkdocs.docs(
        """
        foo.md
        bar/
            foo.md
            .nav.yml
            | hide: true
        """
    )
    mkdocs.build().assert_nav(
        """
        - Foo: foo.md
        """
    )


def test_explicit_reference(mkdocs):
    mkdocs.docs(
        """
        foo.md
        bar/
            foo.md
            .nav.yml
            | hide: true
        .nav.yml
        | nav:
        |   - foo.md
        |   - bar
        """
    )
    mkdocs.build().assert_nav(
        """
        - Foo: foo.md
        - Bar:
            - Foo: bar/foo.md
        """
    )


def test_file_pattern(mkdocs):
    mkdocs.docs(
        """
        foo.md
        bar/
            foo.md
            .nav.yml
            | hide: true
        .nav.yml
        | nav:
        |   - "**/*"
        """
    )
    mkdocs.build().assert_nav(
        """
        - Foo: bar/foo.md
        - Foo: foo.md
        """
    )


def test_root(mkdocs, logs):
    mkdocs.docs(
        """
        foo.md
        .nav.yml
        | hide: true
        """
    )
    mkdocs.build().assert_nav(
        """
        - Foo: foo.md
        """
    )
    assert logs.from_plugin == [logs.warning("awesome-nav: 'hide' option has no effect at the top level [.nav.yml]")]
