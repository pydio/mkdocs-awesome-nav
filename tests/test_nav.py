def test_default_index(mkdocs):
    mkdocs.docs(
        """
        foo.md
        index.md
        """
    )
    mkdocs.build().assert_nav(
        """
        - Home: index.md
        - Foo: foo.md
        """
    )


def test_default_readme(mkdocs):
    mkdocs.docs(
        """
        foo.md
        README.md
        """
    )
    mkdocs.build().assert_nav(
        """
        - Home: README.md
        - Foo: foo.md
        """
    )


def test_default_readme_and_index(mkdocs):
    mkdocs.docs(
        """
        foo.md
        index.md
        README.md
        """
    )
    mkdocs.build().assert_nav(
        """
        - Home: index.md
        - Foo: foo.md
        """
    )


def test_empty(mkdocs):
    mkdocs.docs(
        """
        foo.md
        .nav.yml
        | nav: []
        """
    )
    mkdocs.build().assert_nav_empty()


def test_omitted_file(mkdocs, logs):
    mkdocs.docs(
        """
        foo.md
        bar.md
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
    assert (
        logs.info(
            'The following pages exist in the docs directory, but are not included in the "nav" configuration:\n'
            "  - bar.md"
        )
        in logs.all
    )


def test_append_unmatched(mkdocs):
    mkdocs.docs(
        """
        foo.md
        bar.md
        .nav.yml
        | append_unmatched: true
        | nav:
        |   - foo.md
        """
    )
    mkdocs.build().assert_nav(
        """
        - Foo: foo.md
        - Bar: bar.md
        """
    )


def test_append_unmatched_inheritance(mkdocs):
    mkdocs.docs(
        """
        foo/
            foo.md
            bar.md
            .nav.yml
            | nav:
            |   - foo.md
        .nav.yml
        | append_unmatched: true
        """
    )
    mkdocs.build().assert_nav(
        """
        - Foo:
            - Foo: foo/foo.md
            - Bar: foo/bar.md
        """
    )
