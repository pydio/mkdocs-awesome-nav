import pytest


@pytest.fixture(autouse=True)
def _test_files(mkdocs):
    mkdocs.docs(
        """
        a/
            foo.md
        b.md
        c/
            bar.md
        d.md
        """
    )


def test_default(mkdocs):
    mkdocs.build().assert_nav(
        """
        - B: b.md
        - D: d.md
        - A:
            - Foo: a/foo.md
        - C:
            - Bar: c/bar.md
        """
    )


def test_last(mkdocs):
    mkdocs.docs(
        """
        .nav.yml
        | sort:
        |   sections: last
        """
    )
    mkdocs.build().assert_nav(
        """
        - B: b.md
        - D: d.md
        - A:
            - Foo: a/foo.md
        - C:
            - Bar: c/bar.md
        """
    )


def test_first(mkdocs):
    mkdocs.docs(
        """
        .nav.yml
        | sort:
        |   sections: first
        """
    )
    mkdocs.build().assert_nav(
        """
        - A:
            - Foo: a/foo.md
        - C:
            - Bar: c/bar.md
        - B: b.md
        - D: d.md
        """
    )


def test_mixed(mkdocs):
    mkdocs.docs(
        """
        .nav.yml
        | sort:
        |   sections: mixed
        """
    )
    mkdocs.build().assert_nav(
        """
        - A:
            - Foo: a/foo.md
        - B: b.md
        - C:
            - Bar: c/bar.md
        - D: d.md
        """
    )


def test_sort_direction(mkdocs):
    mkdocs.docs(
        """
        .nav.yml
        | sort:
        |   direction: desc
        |   sections: first
        """
    )
    mkdocs.build().assert_nav(
        """
        - C:
            - Bar: c/bar.md
        - A:
            - Foo: a/foo.md
        - D: d.md
        - B: b.md
        """
    )
