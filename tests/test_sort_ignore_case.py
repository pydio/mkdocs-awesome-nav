import pytest


@pytest.fixture(autouse=True)
def _test_files(mkdocs):
    mkdocs.docs(
        """
        A-upper.md
        | Title: A
        a-lower.md
        | Title: a
        B-upper.md
        | Title: B
        b-lower.md
        | Title: b
        """
    )


def test_default(mkdocs):
    mkdocs.build().assert_nav(
        """
        - A: A-upper.md
        - a: a-lower.md
        - B: B-upper.md
        - b: b-lower.md
        """
    )


def test_default_ignore_case(mkdocs):
    mkdocs.docs(
        """
        .nav.yml
        | sort:
        |   ignore_case: true
        """
    )
    mkdocs.build().assert_nav(
        """
        - a: a-lower.md
        - A: A-upper.md
        - b: b-lower.md
        - B: B-upper.md
        """
    )


def test_filename(mkdocs):
    mkdocs.docs(
        """
        .nav.yml
        | sort:
        |   by: filename
        """
    )
    mkdocs.build().assert_nav(
        """
        - A: A-upper.md
        - a: a-lower.md
        - B: B-upper.md
        - b: b-lower.md
        """
    )


def test_filename_ignore_case(mkdocs):
    mkdocs.docs(
        """
        .nav.yml
        | sort:
        |   by: filename
        |   ignore_case: true
        """
    )
    mkdocs.build().assert_nav(
        """
        - a: a-lower.md
        - A: A-upper.md
        - b: b-lower.md
        - B: B-upper.md
        """
    )


def test_title(mkdocs):
    mkdocs.docs(
        """
        .nav.yml
        | sort:
        |   by: title
        """
    )
    mkdocs.build().assert_nav(
        """
        - A: A-upper.md
        - a: a-lower.md
        - B: B-upper.md
        - b: b-lower.md
        """
    )


def test_title_ignore_case(mkdocs):
    mkdocs.docs(
        """
        .nav.yml
        | sort:
        |   by: title
        |   ignore_case: true
        """
    )
    mkdocs.build().assert_nav(
        """
        - a: a-lower.md
        - A: A-upper.md
        - b: b-lower.md
        - B: B-upper.md
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
        - A: A-upper.md
        - B: B-upper.md
        - a: a-lower.md
        - b: b-lower.md
        """
    )


def test_alphabetical_ignore_case(mkdocs):
    mkdocs.docs(
        """
        .nav.yml
        | sort:
        |   type: alphabetical
        |   ignore_case: true
        """
    )
    mkdocs.build().assert_nav(
        """
        - a: a-lower.md
        - A: A-upper.md
        - b: b-lower.md
        - B: B-upper.md
        """
    )


def test_alphabetical_filename(mkdocs):
    mkdocs.docs(
        """
        .nav.yml
        | sort:
        |   type: alphabetical
        |   by: filename
        """
    )
    mkdocs.build().assert_nav(
        """
        - A: A-upper.md
        - B: B-upper.md
        - a: a-lower.md
        - b: b-lower.md
        """
    )


def test_alphabetical_filename_ignore_case(mkdocs):
    mkdocs.docs(
        """
        .nav.yml
        | sort:
        |   type: alphabetical
        |   by: filename
        |   ignore_case: true
        """
    )
    mkdocs.build().assert_nav(
        """
        - a: a-lower.md
        - A: A-upper.md
        - b: b-lower.md
        - B: B-upper.md
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
        - A: A-upper.md
        - B: B-upper.md
        - a: a-lower.md
        - b: b-lower.md
        """
    )


def test_alphabetical_title_ignore_case(mkdocs):
    mkdocs.docs(
        """
        .nav.yml
        | sort:
        |   type: alphabetical
        |   by: title
        |   ignore_case: true
        """
    )
    mkdocs.build().assert_nav(
        """
        - a: a-lower.md
        - A: A-upper.md
        - b: b-lower.md
        - B: B-upper.md
        """
    )
