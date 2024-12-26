import pytest


@pytest.fixture(autouse=True)
def _test_files(mkdocs):
    mkdocs.docs(
        """
        a.md
        | Title: A
        b.md
        | Title: B
        """
    )


def test_default(mkdocs):
    mkdocs.build().assert_nav(
        """
        - A: a.md
        - B: b.md
        """
    )


def test_default_title(mkdocs):
    mkdocs.docs(
        """
        .nav.yml
        | sort:
        |   by: title
        """
    )
    mkdocs.build().assert_nav(
        """
        - A: a.md
        - B: b.md
        """
    )


def test_default_asc(mkdocs):
    mkdocs.docs(
        """
        .nav.yml
        | sort:
        |   direction: asc
        """
    )
    mkdocs.build().assert_nav(
        """
        - A: a.md
        - B: b.md
        """
    )


def test_default_asc_title(mkdocs):
    mkdocs.docs(
        """
        .nav.yml
        | sort:
        |   direction: asc
        |   by: title
        """
    )
    mkdocs.build().assert_nav(
        """
        - A: a.md
        - B: b.md
        """
    )


def test_default_desc(mkdocs):
    mkdocs.docs(
        """
        .nav.yml
        | sort:
        |   direction: desc
        """
    )
    mkdocs.build().assert_nav(
        """
        - B: b.md
        - A: a.md
        """
    )


def test_default_desc_title(mkdocs):
    mkdocs.docs(
        """
        .nav.yml
        | sort:
        |   direction: desc
        |   by: title
        """
    )
    mkdocs.build().assert_nav(
        """
        - B: b.md
        - A: a.md
        """
    )
