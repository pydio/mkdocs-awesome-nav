import pytest


@pytest.fixture(autouse=True)
def _test_files(mkdocs):
    mkdocs.docs(
        """
        2.md
        | Title: 2
        2-suffix.md
        | Title: 2 suffix
        2.5.md
        | Title: 2.5
        2.5-suffix.md
        | Title: 2.5 suffix
        10.md
        | Title: 10
        10-suffix.md
        | Title: 10 suffix
        A-upper.md
        | Title: A
        A-upper-suffix.md
        | Title: A suffix
        a-lower.md
        | Title: a
        a-lower-suffix.md
        | Title: a suffix
        B-upper.md
        | Title: B
        B-upper-suffix.md
        | Title: B suffix
        b-lower.md
        | Title: b
        b-lower-suffix.md
        | Title: b suffix
        c.2.md
        | Title: c.2
        c.2.5.md
        | Title: c.2.5
        c.10.md
        | Title: c.10
        """
    )


def test_default(mkdocs):
    mkdocs.build().assert_nav(
        """
        - "2": 2.md
        - "2 suffix": 2-suffix.md
        - "2.5": 2.5.md
        - "2.5 suffix": 2.5-suffix.md
        - "10": 10.md
        - "10 suffix": 10-suffix.md
        - "A": A-upper.md
        - "A suffix": A-upper-suffix.md
        - "a": a-lower.md
        - "a suffix": a-lower-suffix.md
        - "B": B-upper.md
        - "B suffix": B-upper-suffix.md
        - "b": b-lower.md
        - "b suffix": b-lower-suffix.md
        - "c.2": c.2.md
        - "c.2.5": c.2.5.md
        - "c.10": c.10.md
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
        - "2": 2.md
        - "2 suffix": 2-suffix.md
        - "2.5": 2.5.md
        - "2.5 suffix": 2.5-suffix.md
        - "10": 10.md
        - "10 suffix": 10-suffix.md
        - "A": A-upper.md
        - "A suffix": A-upper-suffix.md
        - "a": a-lower.md
        - "a suffix": a-lower-suffix.md
        - "B": B-upper.md
        - "B suffix": B-upper-suffix.md
        - "b": b-lower.md
        - "b suffix": b-lower-suffix.md
        - "c.2": c.2.md
        - "c.2.5": c.2.5.md
        - "c.10": c.10.md
        """
    )


def test_natural(mkdocs):
    mkdocs.docs(
        """
        .nav.yml
        | sort:
        |   type: natural
        """
    )
    mkdocs.build().assert_nav(
        """
        - "2": 2.md
        - "2 suffix": 2-suffix.md
        - "2.5": 2.5.md
        - "2.5 suffix": 2.5-suffix.md
        - "10": 10.md
        - "10 suffix": 10-suffix.md
        - "A": A-upper.md
        - "A suffix": A-upper-suffix.md
        - "a": a-lower.md
        - "a suffix": a-lower-suffix.md
        - "B": B-upper.md
        - "B suffix": B-upper-suffix.md
        - "b": b-lower.md
        - "b suffix": b-lower-suffix.md
        - "c.2": c.2.md
        - "c.2.5": c.2.5.md
        - "c.10": c.10.md
        """
    )


def test_natural_title(mkdocs):
    mkdocs.docs(
        """
        .nav.yml
        | sort:
        |   type: natural
        |   by: title
        """
    )
    mkdocs.build().assert_nav(
        """
        - "2": 2.md
        - "2 suffix": 2-suffix.md
        - "2.5": 2.5.md
        - "2.5 suffix": 2.5-suffix.md
        - "10": 10.md
        - "10 suffix": 10-suffix.md
        - "A": A-upper.md
        - "A suffix": A-upper-suffix.md
        - "a": a-lower.md
        - "a suffix": a-lower-suffix.md
        - "B": B-upper.md
        - "B suffix": B-upper-suffix.md
        - "b": b-lower.md
        - "b suffix": b-lower-suffix.md
        - "c.2": c.2.md
        - "c.2.5": c.2.5.md
        - "c.10": c.10.md
        """
    )


def test_alphabetical(mkdocs):
    mkdocs.docs(
        """
        .nav.yml
        | sort:
        |   type: alphabetical
        """
    )
    mkdocs.build().assert_nav(
        """
        - "10 suffix": 10-suffix.md
        - "10": 10.md
        - "2 suffix": 2-suffix.md
        - "2.5 suffix": 2.5-suffix.md
        - "2.5": 2.5.md
        - "2": 2.md
        - "A suffix": A-upper-suffix.md
        - "A": A-upper.md
        - "B suffix": B-upper-suffix.md
        - "B": B-upper.md
        - "a suffix": a-lower-suffix.md
        - "a": a-lower.md
        - "b suffix": b-lower-suffix.md
        - "b": b-lower.md
        - "c.10": c.10.md
        - "c.2.5": c.2.5.md
        - "c.2": c.2.md
        """
    )


def test_alphabetical_title(mkdocs):
    mkdocs.docs(
        """
        .nav.yml
        | sort:
        |   type: alphabetical
        |   by: title
        """
    )
    mkdocs.build().assert_nav(
        """
        - "10": 10.md
        - "10 suffix": 10-suffix.md
        - "2": 2.md
        - "2 suffix": 2-suffix.md
        - "2.5": 2.5.md
        - "2.5 suffix": 2.5-suffix.md
        - "A": A-upper.md
        - "A suffix": A-upper-suffix.md
        - "B": B-upper.md
        - "B suffix": B-upper-suffix.md
        - "a": a-lower.md
        - "a suffix": a-lower-suffix.md
        - "b": b-lower.md
        - "b suffix": b-lower-suffix.md
        - "c.10": c.10.md
        - "c.2": c.2.md
        - "c.2.5": c.2.5.md
        """
    )
