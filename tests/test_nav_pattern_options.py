def test_flatten_single_child_sections(mkdocs):
    mkdocs.docs(
        """
        foo/
            foo.md
        bar/
            bar.md
        .nav.yml
        | nav:
        |   - foo
        |   - glob: "*"
        |     flatten_single_child_sections: true
        """
    )
    mkdocs.build().assert_nav(
        """
        - Foo:
            - Foo: foo/foo.md
        - Bar: bar/bar.md
        """
    )


def test_flatten_single_child_sections_override(mkdocs):
    mkdocs.docs(
        """
        foo/
            foo.md
        bar/
            bar.md
        .nav.yml
        | flatten_single_child_sections: true
        | nav:
        |   - foo
        |   - glob: "*"
        |     flatten_single_child_sections: false
        """
    )
    mkdocs.build().assert_nav(
        """
        - Foo: foo/foo.md
        - Bar:
            - Bar: bar/bar.md
        """
    )


def test_preserve_directory_names(mkdocs):
    mkdocs.docs(
        """
        foo-bar/
            foo.md
        bar-foo/
            bar.md
        .nav.yml
        | nav:
        |   - foo-bar
        |   - glob: "*"
        |     preserve_directory_names: true
        """
    )
    mkdocs.build().assert_nav(
        """
        - Foo bar:
            - Foo: foo-bar/foo.md
        - bar-foo:
            - Bar: bar-foo/bar.md
        """
    )


def test_preserve_directory_names_override(mkdocs):
    mkdocs.docs(
        """
        foo-bar/
            foo.md
        bar-foo/
            bar.md
        .nav.yml
        | preserve_directory_names: true
        | nav:
        |   - foo-bar
        |   - glob: "*"
        |     preserve_directory_names: false
        """
    )
    mkdocs.build().assert_nav(
        """
        - foo-bar:
            - Foo: foo-bar/foo.md
        - Bar foo:
            - Bar: bar-foo/bar.md
        """
    )


def test_ignore(mkdocs):
    mkdocs.docs(
        """
        foo.md
        foobar.md
        bar.md
        barfoo.md
        .nav.yml
        | nav:
        |   - glob: "*"
        |     ignore: "*bar.md"
        |   - Rest:
        |       - "*"
        """
    )
    mkdocs.build().assert_nav(
        """
        - Barfoo: barfoo.md
        - Foo: foo.md
        - Rest:
            - Bar: bar.md
            - Foobar: foobar.md
        """
    )


def test_ignore_override(mkdocs):
    mkdocs.docs(
        """
        foo.md
        foobar.md
        bar.md
        barfoo.md
        .nav.yml
        | ignore: "foo*.md"
        | nav:
        |   - glob: "*"
        |     ignore: "*bar.md"
        |   - Rest:
        |       - "*"
        """
    )
    mkdocs.build().assert_nav(
        """
        - Barfoo: barfoo.md
        - Foo: foo.md
        - Rest:
            - Bar: bar.md
        """
    )


def test_sort_direction(mkdocs):
    mkdocs.docs(
        """
        a.md
        b.md
        c.md
        .nav.yml
        | nav:
        |   - a.md
        |   - glob: "*"
        |     sort:
        |       direction: desc
        """
    )
    mkdocs.build().assert_nav(
        """
        - A: a.md
        - C: c.md
        - B: b.md
        """
    )


def test_sort_direction_override(mkdocs):
    mkdocs.docs(
        """
        a1.md
        a2.md
        b1.md
        b2.md
        .nav.yml
        | sort:
        |   direction: desc
        | nav:
        |   - glob: "*1.md"
        |     sort:
        |       direction: asc
        |   - "*2.md"
        """
    )
    mkdocs.build().assert_nav(
        """
        - A1: a1.md
        - B1: b1.md
        - B2: b2.md
        - A2: a2.md
        """
    )


def test_append_unmatched(mkdocs):
    mkdocs.docs(
        """
        foo/
            foo.md
            bar.md
            .nav.yml
            | nav:
            |   - foo.md
        bar/
            foo.md
            bar.md
            .nav.yml
            | nav:
            |   - foo.md
        .nav.yml
        | nav:
        |   - foo
        |   - glob: "*"
        |     append_unmatched: true
        """
    )
    mkdocs.build().assert_nav(
        """
        - Foo:
            - Foo: foo/foo.md
        - Bar:
            - Foo: bar/foo.md
            - Bar: bar/bar.md
        """
    )


def test_no_matches(mkdocs, logs):
    mkdocs.docs(
        """
        foo.md
        .nav.yml
        | nav:
        |   - foo.md
        |   - glob: "*"
        |     flatten_single_child_sections: true
        """
    )
    mkdocs.build().assert_nav(
        """
        - Foo: foo.md
        """
    )
    assert logs.from_plugin == [
        logs.warning("awesome-nav: The nav item '*' doesn't match any files or directories [.nav.yml]")
    ]


def test_ignore_no_matches(mkdocs, logs):
    mkdocs.docs(
        """
        foo.md
        .nav.yml
        | nav:
        |   - foo.md
        |   - glob: "*"
        |     ignore_no_matches: true
        """
    )
    mkdocs.build().assert_nav(
        """
        - Foo: foo.md
        """
    )
    assert logs.from_plugin == []


def test_only_pattern_is_interpreted_as_link(mkdocs, logs):
    mkdocs.docs(
        """
        foo.md
        .nav.yml
        | nav:
        |   - glob: "*"
        """
    )
    mkdocs.build().assert_nav(
        """
        - glob: "*"
        """
    )
