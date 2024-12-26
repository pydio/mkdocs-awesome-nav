def test_relative(mkdocs):
    mkdocs.docs(
        """
        foo.md
        foo.hidden.md
        bar/
            bar.md
            bar.hidden.md
        .nav.yml
        | ignore: "*.hidden.md"
        """
    )
    mkdocs.build().assert_nav(
        """
        - Foo: foo.md
        - Bar:
            - Bar: bar/bar.md
        """
    )


def test_relative_deep_pattern(mkdocs):
    mkdocs.docs(
        """
        foo.md
        foo.hidden.md
        bar/
            bar.md
            bar.hidden.md
        .nav.yml
        | ignore: "*.hidden.md"
        | nav:
        |   - "**"
        """
    )
    mkdocs.build().assert_nav(
        """
        - Bar: bar/bar.md
        - Foo: foo.md
        """
    )


def test_absolute(mkdocs):
    mkdocs.docs(
        """
        foo.md
        foo.hidden.md
        bar/
            bar.md
            bar.hidden.md
        .nav.yml
        | ignore: /*.hidden.md
        """
    )
    mkdocs.build().assert_nav(
        """
        - Foo: foo.md
        - Bar:
            - Bar: bar/bar.md
            - Bar.hidden: bar/bar.hidden.md
        """
    )


def test_absolute_deep(mkdocs):
    mkdocs.docs(
        """
        foo.md
        foo.hidden.md
        bar/
            bar.md
            bar.hidden.md
        .nav.yml
        | ignore: /bar/*.hidden.md
        """
    )
    mkdocs.build().assert_nav(
        """
        - Foo: foo.md
        - Foo.hidden: foo.hidden.md
        - Bar:
            - Bar: bar/bar.md
        """
    )


def test_absolute_deep_pattern(mkdocs):
    mkdocs.docs(
        """
        foo.md
        foo.hidden.md
        bar/
            bar.md
            bar.hidden.md
        .nav.yml
        | ignore: /*.hidden.md
        | nav:
        |   - "**"
        """
    )
    mkdocs.build().assert_nav(
        """
        - Bar: bar/bar.md
        - Bar.hidden: bar/bar.hidden.md
        - Foo: foo.md
        """
    )


def test_absolute_scoped_to_directory(mkdocs):
    mkdocs.docs(
        """
        foo/
            foo.md
            foo.hidden.md
            bar/
                bar.md
                bar.hidden.md
            .nav.yml
            | ignore: /*.hidden.md
        """
    )
    mkdocs.build().assert_nav(
        """
        - Foo:
            - Foo: foo/foo.md
            - Bar:
                - Bar: foo/bar/bar.md
                - Bar.hidden: foo/bar/bar.hidden.md
        """
    )


def test_only_directories(mkdocs):
    mkdocs.docs(
        """
        hidden_foo/
            foo.md
        hidden_bar.md
        .nav.yml
        | ignore: hidden_*/
        """
    )
    mkdocs.build().assert_nav(
        """
        - Hidden bar: hidden_bar.md
        """
    )


def test_multiple(mkdocs):
    mkdocs.docs(
        """
        foo.md
        foo.hidden.md
        bar/
            foo.md
            hidden/
                foo.md
        .nav.yml
        | ignore:
        |   - hidden
        |   - "*.hidden.md"
        """
    )
    mkdocs.build().assert_nav(
        """
        - Foo: foo.md
        - Bar:
            - Foo: bar/foo.md
        """
    )


def test_explicit(mkdocs):
    mkdocs.docs(
        """
        foo.hidden.md
        .nav.yml
        | ignore: "*.hidden.md"
        | nav:
        |   - foo.hidden.md
        """
    )
    mkdocs.build().assert_nav(
        """
        - Foo.hidden: foo.hidden.md
        """
    )


def test_override(mkdocs):
    mkdocs.docs(
        """
        foo.md
        bar.md
        foo/
            foo.md
            bar.md
            other.md
            .nav.yml
            | ignore: foo.md
        .nav.yml
        | ignore: bar.md
        """
    )
    mkdocs.build().assert_nav(
        """
        - Foo: foo.md
        - Foo:
            - Bar: foo/bar.md
            - Other: foo/other.md
        """
    )


def test_inherit(mkdocs):
    mkdocs.docs(
        """
        foo.md
        bar.md
        foo/
            foo.md
            bar.md
            other.md
            .nav.yml
            | ignore:
            |   - $inherit
            |   - foo.md
        .nav.yml
        | ignore: bar.md
        """
    )
    mkdocs.build().assert_nav(
        """
        - Foo: foo.md
        - Foo:
            - Other: foo/other.md
        """
    )
