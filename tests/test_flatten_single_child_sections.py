def test(mkdocs):
    mkdocs.docs(
        """
        foo/
            bar.md
        .nav.yml
        | flatten_single_child_sections: true
        """
    )
    mkdocs.build().assert_nav(
        """
        - Bar: foo/bar.md
        """
    )


def test_root(mkdocs):
    mkdocs.docs(
        """
        foo.md
        .nav.yml
        | flatten_single_child_sections: true
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
        a/
            b/
                c/
                    foo.md
        .nav.yml
        | flatten_single_child_sections: true
        """
    )
    mkdocs.build().assert_nav(
        """
        - Foo: a/b/c/foo.md
        """
    )


def test_override(mkdocs):
    mkdocs.docs(
        """
        a/
            b/
                c/
                    foo.md
                .nav.yml
                | flatten_single_child_sections: false
        .nav.yml
        | flatten_single_child_sections: true
        """
    )
    mkdocs.build().assert_nav(
        """
        - B:
            - C:
                - Foo: a/b/c/foo.md
        """
    )


def test_directory(mkdocs):
    mkdocs.docs(
        """
        a/
            b/
                foo.md
                bar.md
        .nav.yml
        | flatten_single_child_sections: true
        """
    )
    mkdocs.build().assert_nav(
        """
        - B:
            - Bar: a/b/bar.md
            - Foo: a/b/foo.md
        """
    )


def test_hide(mkdocs):
    mkdocs.docs(
        """
        foo/
            foo.md
            bar/
                bar.md
                .nav.yml
                | hide: true
        .nav.yml
        | flatten_single_child_sections: true
        """
    )
    mkdocs.build().assert_nav(
        """
        - Foo: foo/foo.md
        """
    )


def test_sort_by_default(mkdocs):
    mkdocs.docs(
        """
        a/
            c.md
        b.md
        .nav.yml
        | flatten_single_child_sections: true
        """
    )
    mkdocs.build().assert_nav(
        """
        - C: a/c.md
        - B: b.md
        """
    )


def test_sort_by_path(mkdocs):
    mkdocs.docs(
        """
        a/
            c.md
        b.md
        .nav.yml
        | flatten_single_child_sections: true
        | sort:
        |   by: path
        """
    )
    mkdocs.build().assert_nav(
        """
        - C: a/c.md
        - B: b.md
        """
    )


def test_sort_by_filename(mkdocs):
    mkdocs.docs(
        """
        a/
            c.md
        b.md
        .nav.yml
        | flatten_single_child_sections: true
        | sort:
        |   by: filename
        """
    )
    mkdocs.build().assert_nav(
        """
        - B: b.md
        - C: a/c.md
        """
    )


def test_sort_by_title(mkdocs):
    mkdocs.docs(
        """
        a/
            c.md
            | Title: C
        b.md
        | Title: B
        .nav.yml
        | flatten_single_child_sections: true
        | sort:
        |   by: title
        """
    )
    mkdocs.build().assert_nav(
        """
        - B: b.md
        - C: a/c.md
        """
    )


def test_sort_sections_default(mkdocs):
    mkdocs.docs(
        """
        a/
            foo.md
            bar.md
        b/
            foo.md
        .nav.yml
        | flatten_single_child_sections: true
        """
    )
    mkdocs.build().assert_nav(
        """
        - Foo: b/foo.md
        - A:
            - Bar: a/bar.md
            - Foo: a/foo.md
        """
    )


def test_sort_sections_last(mkdocs):
    mkdocs.docs(
        """
        a/
            foo.md
            bar.md
        b/
            foo.md
        .nav.yml
        | flatten_single_child_sections: true
        | sort:
        |   sections: last
        """
    )
    mkdocs.build().assert_nav(
        """
        - Foo: b/foo.md
        - A:
            - Bar: a/bar.md
            - Foo: a/foo.md
        """
    )


def test_sort_sections_first(mkdocs):
    mkdocs.docs(
        """
        a/
            foo.md
            bar.md
        b/
            foo.md
        .nav.yml
        | flatten_single_child_sections: true
        | sort:
        |   sections: first
        """
    )
    mkdocs.build().assert_nav(
        """
        - A:
            - Bar: a/bar.md
            - Foo: a/foo.md
        - Foo: b/foo.md
        """
    )


def test_sort_sections_mixed(mkdocs):
    mkdocs.docs(
        """
        a/
            foo.md
            bar.md
        b/
            foo.md
        .nav.yml
        | flatten_single_child_sections: true
        | sort:
        |   sections: mixed
        """
    )
    mkdocs.build().assert_nav(
        """
        - A:
            - Bar: a/bar.md
            - Foo: a/foo.md
        - Foo: b/foo.md
        """
    )


def test_link(mkdocs):
    mkdocs.docs(
        """
        foo/
            bar.md
            .nav.yml
            | nav:
            |   - Link: https://lukasgeiter.github.io/mkdocs-awesome-nav
        .nav.yml
        | flatten_single_child_sections: true
        """
    )
    mkdocs.build().assert_nav(
        """
        - Foo:
            - Link: https://lukasgeiter.github.io/mkdocs-awesome-nav
        """
    )


def test_section(mkdocs):
    mkdocs.docs(
        """
        foo/
            bar.md
            .nav.yml
            | nav:
            |   - Section:
            |       - bar.md
        .nav.yml
        | flatten_single_child_sections: true
        """
    )
    mkdocs.build().assert_nav(
        """
        - Section:
            - Bar: foo/bar.md
        """
    )


def test_section_sort_default(mkdocs):
    mkdocs.docs(
        """
        a/
            foo.md
            .nav.yml
            | nav:
            |   - Section:
            |       - foo.md
        b/
            foo.md
            bar.md
        .nav.yml
        | flatten_single_child_sections: true
        """
    )
    mkdocs.build().assert_nav(
        """
        - Section:
            - Foo: a/foo.md
        - B:
            - Bar: b/bar.md
            - Foo: b/foo.md
        """
    )


def test_section_sort_by_title(mkdocs):
    mkdocs.docs(
        """
        a/
            foo.md
            .nav.yml
            | nav:
            |   - Section:
            |       - foo.md
        b/
            foo.md
            bar.md
        .nav.yml
        | flatten_single_child_sections: true
        | sort:
        |   by: title
        """
    )
    mkdocs.build().assert_nav(
        """
        - B:
            - Bar: b/bar.md
            - Foo: b/foo.md
        - Section:
            - Foo: a/foo.md
        """
    )
