def test_default(mkdocs):
    mkdocs.docs(
        """
        a/
            c.md
        b.md
        .nav.yml
        | nav:
        |   - "**"
        """
    )
    mkdocs.build().assert_nav(
        """
        - C: a/c.md
        - B: b.md
        """
    )


def test_path(mkdocs):
    mkdocs.docs(
        """
        a/
            c.md
        b.md
        .nav.yml
        | sort:
        |   by: path
        | nav:
        |   - "**"
        """
    )
    mkdocs.build().assert_nav(
        """
        - C: a/c.md
        - B: b.md
        """
    )


def test_filename(mkdocs):
    mkdocs.docs(
        """
        a/
            b.md
            c.md
        b.md
        .nav.yml
        | sort:
        |   by: filename
        | nav:
        |   - "**"
        """
    )
    mkdocs.build().assert_nav(
        """
        - B: a/b.md
        - B: b.md
        - C: a/c.md
        """
    )


def test_title_yaml(mkdocs):
    mkdocs.docs(
        """
        1.md
        | ---
        | title: B
        | ---
        2.md
        | ---
        | title: A
        | ---
        .nav.yml
        | sort:
        |   by: title
        """
    )
    mkdocs.build().assert_nav(
        """
        - A: 2.md
        - B: 1.md
        """
    )


def test_title_multimarkdown(mkdocs):
    mkdocs.docs(
        """
        1.md
        | Title: B
        2.md
        | Title: A
        .nav.yml
        | sort:
        |   by: title
        """
    )
    mkdocs.build().assert_nav(
        """
        - A: 2.md
        - B: 1.md
        """
    )


def test_title_section(mkdocs):
    mkdocs.docs(
        """
        1/
            foo.md
            .nav.yml
            | title: B
        2/
            foo.md
            .nav.yml
            | title: A
        .nav.yml
        | sort:
        |   by: title
        """
    )
    mkdocs.build().assert_nav(
        """
        - A:
            - Foo: 2/foo.md
        - B:
            - Foo: 1/foo.md
        """
    )


def test_title_missing(mkdocs):
    mkdocs.docs(
        """
        1.md
        | Title: C
        2.md
        | Title: A
        b.md
        .nav.yml
        | sort:
        |   by: title
        """
    )
    mkdocs.build().assert_nav(
        """
        - A: 2.md
        - B: b.md
        - C: 1.md
        """
    )


def test_title_identical(mkdocs):
    mkdocs.docs(
        """
        1.md
        | Title: Foo
        2.md
        | Title: Foo
        .nav.yml
        | sort:
        |   by: title
        """
    )
    mkdocs.build().assert_nav(
        """
        - Foo: 1.md
        - Foo: 2.md
        """
    )
