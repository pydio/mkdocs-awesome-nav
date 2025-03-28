import logging
from pathlib import Path

import pytest


@pytest.fixture
def _test_validation_error(mkdocs, logs):
    mkdocs.docs(
        """
        foo.md
        """
    )

    def run(config: str):
        Path("docs/.nav.yml").write_text(config)
        mkdocs.build().assert_nav(
            """
            - Foo: foo.md
            """
        )
        assert len(logs.from_plugin) == 1
        assert logs.from_plugin[0][0] == logging.ERROR
        assert logs.from_plugin[0][1].startswith("awesome-nav: Validation error [.nav.yml]\n")
        return logs.from_plugin[0][1]

    return run


def test_title_wrong_type(_test_validation_error):
    error = _test_validation_error(
        """
        title: 42
        """
    )
    assert "Input should be a valid string" in error


def test_title_empty_string(_test_validation_error):
    error = _test_validation_error(
        """
        title: ""
        """,
    )
    assert "String should have at least 1 character" in error


def test_hide_wrong_type(_test_validation_error):
    error = _test_validation_error(
        """
        hide: foo
        """
    )
    assert "Input should be a valid boolean" in error


def test_flatten_single_child_sections_wrong_type(_test_validation_error):
    error = _test_validation_error(
        """
        flatten_single_child_sections: foo
        """
    )
    assert "Input should be a valid boolean" in error


def test_preserve_directory_names_wrong_type(_test_validation_error):
    error = _test_validation_error(
        """
        preserve_directory_names: foo
        """
    )
    assert "Input should be a valid boolean" in error


def test_sort_wrong_type(_test_validation_error):
    error = _test_validation_error(
        """
        sort: foo
        """
    )
    assert "Input should be a valid dictionary" in error


def test_sort_by_invalid_value(_test_validation_error):
    error = _test_validation_error(
        """
        sort:
          by: foo
        """
    )
    assert "Input should be 'path', 'filename' or 'title'" in error


def test_sort_direction_invalid_value(_test_validation_error):
    error = _test_validation_error(
        """
        sort:
          direction: foo
        """
    )
    assert "Input should be 'asc' or 'desc'" in error


def test_sort_type_invalid_value(_test_validation_error):
    error = _test_validation_error(
        """
        sort:
          type: foo
        """
    )
    assert "Input should be 'natural' or 'alphabetical'" in error


def test_sort_sections_invalid_value(_test_validation_error):
    error = _test_validation_error(
        """
        sort:
          sections: foo
        """
    )
    assert "Input should be 'first', 'last' or 'mixed'" in error


def test_sort_ignore_case_invalid_value(_test_validation_error):
    error = _test_validation_error(
        """
        sort:
          ignore_case: foo
        """
    )
    assert "Input should be a valid boolean" in error


def test_ignore_wrong_type(_test_validation_error):
    error = _test_validation_error(
        """
        ignore: 42
        """
    )
    assert "Input should be a valid string" in error


def test_ignore_empty_string(_test_validation_error):
    error = _test_validation_error(
        """
        ignore: ""
        """
    )
    assert "String should have at least 1 character" in error


def test_ignore_list_wrong_type(_test_validation_error):
    error = _test_validation_error(
        """
        ignore:
          - 42
        """
    )
    assert "Input should be a valid string" in error


def test_ignore_list_empty_string(_test_validation_error):
    error = _test_validation_error(
        """
        ignore:
          - ""
        """
    )
    assert "String should have at least 1 character" in error


def test_nav_item_wrong_type(_test_validation_error):
    error = _test_validation_error(
        """
        nav:
          - 42
        """
    )
    assert "Input should be a valid string" in error


def test_nav_item_empty_string(_test_validation_error):
    error = _test_validation_error(
        """
        nav:
          - ""
        """
    )
    assert "String should have at least 1 character" in error


def test_nav_item_value_wrong_type(_test_validation_error):
    error = _test_validation_error(
        """
        nav:
          - Title: 42
        """
    )
    assert "Input should be a valid string" in error


def test_nav_item_value_empty_string(_test_validation_error):
    error = _test_validation_error(
        """
        nav:
          - Title: ""
        """
    )
    assert "String should have at least 1 character" in error


def test_nav_item_title_wrong_type(_test_validation_error):
    error = _test_validation_error(
        """
        nav:
          - 42: foo.md
        """
    )
    assert "Input should be a valid string" in error


def test_nav_item_title_empty_string(_test_validation_error):
    error = _test_validation_error(
        """
        nav:
          - "": foo.md
        """
    )
    assert "String should have at least 1 character" in error


def test_nav_item_pattern_options_wrong_type(_test_validation_error):
    error = _test_validation_error(
        """
        nav:
          - glob: 42
            ignore_no_matches: true
        """
    )
    assert "Input should be a valid string" in error


def test_nav_item_pattern_options_empty_string(_test_validation_error):
    error = _test_validation_error(
        """
        nav:
          - glob: ""
            ignore_no_matches: true
        """
    )
    assert "String should have at least 1 character" in error


def test_nav_item_empty_dict(_test_validation_error):
    error = _test_validation_error(
        """
        nav:
          - {}
        """
    )
    assert "Dictionary should have at least 1 item after validation, not 0" in error


def test_nav_item_arbitrary_dict(_test_validation_error):
    error = _test_validation_error(
        """
        nav:
          - foo: a
            bar: b
        """
    )
    assert "Dictionary should have at most 1 item after validation, not 2" in error


def test_append_unmatched(_test_validation_error):
    error = _test_validation_error(
        """
        append_unmatched: foo
        """
    )
    assert "Input should be a valid boolean" in error


def test_invalid_yml(mkdocs, logs):
    mkdocs.docs(
        """
        foo.md
        .nav.yml
        | nav:
        |   - *.bar.md
        """
    )

    mkdocs.build().assert_nav(
        """
        - Foo: foo.md
        """
    )

    assert len(logs.from_plugin) == 1
    assert logs.from_plugin[0][0] == logging.ERROR
    assert logs.from_plugin[0][1].startswith("awesome-nav: Parsing error [.nav.yml]\n")
