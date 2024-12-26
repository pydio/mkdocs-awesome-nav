import pytest


@pytest.fixture(autouse=True)
def _test_files(mkdocs):
    mkdocs.files(
        """
        mkdocs.yml
        | site_name: Test
        | plugins:
        |   - awesome-nav
        |   - mktheapidocs:
        |       modules:
        |         mktheapidocs_test_module:
        |           section: ""
        |           source_repo: "https://github.com/lukasgeiter/mkdocs-awesome-nav"
        """
    )


def test_default_nav(mkdocs):
    mkdocs.docs(
        """
        foo.md
        """
    )

    mkdocs.build().assert_nav(
        """
        - Foo: foo.md
        - Mktheapidocs test module:
            - mktheapidocs_test_module: mktheapidocs_test_module/__init__.py
            - foo: mktheapidocs_test_module/foo.py
        """
    )


def test_nav(mkdocs):
    mkdocs.docs(
        """
        foo.md
        .nav.yml
        | nav:
        |   - Section:
        |       - foo.md
        |       - API: mktheapidocs_test_module
        """
    )

    mkdocs.build().assert_nav(
        """
        - Section:
            - Foo: foo.md
            - API:
                - mktheapidocs_test_module: mktheapidocs_test_module/__init__.py
                - foo: mktheapidocs_test_module/foo.py
        """
    )
