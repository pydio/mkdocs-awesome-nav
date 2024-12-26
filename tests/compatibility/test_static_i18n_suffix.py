import pytest


@pytest.fixture(autouse=True)
def _test_files(mkdocs):
    mkdocs.files(
        """
        docs/
            foo.en.md
            | # Foo EN
            foo.de.md
            | # Foo DE
        mkdocs.yml
        | site_name: Test
        | plugins:
        |   - awesome-nav
        |   - i18n:
        |       docs_structure: suffix
        |       languages:
        |         - locale: en
        |           default: true
        |           name: English
        |         - locale: de
        |           name: Deutsch
        """
    )


def test_default_nav(mkdocs):
    mkdocs.build().assert_nav(
        """
        - Foo EN: foo.en.md
        """,
        """
        - Foo DE: foo.de.md
        """,
    )


def test_page(mkdocs):
    mkdocs.docs(
        """
        .nav.yml
        | nav:
        |   - foo.md
        """
    )

    mkdocs.build().assert_nav(
        """
        - Foo EN: foo.en.md
        """,
        """
        - Foo DE: foo.de.md
        """,
    )


def test_page_title(mkdocs):
    mkdocs.docs(
        """
        .nav.yml
        | nav:
        |   - Title: foo.md
        """
    )

    mkdocs.build().assert_nav(
        """
        - Title: foo.en.md
        """,
        """
        - Title: foo.de.md
        """,
    )


def test_page_specific_language(mkdocs, logs):
    mkdocs.docs(
        """
        .nav.yml
        | nav:
        |   - foo.de.md
        """
    )

    mkdocs.build().assert_nav(
        """
        []
        """,
        """
        - Foo DE: foo.de.md
        """,
    )

    assert logs.from_plugin == [
        logs.warning("awesome-nav: The nav item 'foo.de.md' doesn't match any files or directories [.nav.yml]"),
    ]


def test_pattern(mkdocs):
    mkdocs.docs(
        """
        .nav.yml
        | nav:
        |   - foo.*.md
        """
    )

    mkdocs.build().assert_nav(
        """
        - Foo EN: foo.en.md
        """,
        """
        - Foo DE: foo.de.md
        """,
    )


def test_pattern_without_suffix(mkdocs, logs):
    mkdocs.docs(
        """
        .nav.yml
        | nav:
        |   - "*foo.md"
        """
    )

    mkdocs.build().assert_nav(
        """
        []
        """,
        """
        []
        """,
    )

    assert logs.from_plugin == [
        logs.warning("awesome-nav: The nav item '*foo.md' doesn't match any files or directories [.nav.yml]"),
        logs.warning("awesome-nav: The nav item '*foo.md' doesn't match any files or directories [.nav.yml]"),
    ]


def test_config_with_suffix_en(mkdocs):
    mkdocs.docs(
        """
        .nav.en.yml
        | nav:
        |   - Title: foo.md
        """
    )

    mkdocs.build().assert_nav(
        """
        - Title: foo.en.md
        """,
        """
        - Title: foo.de.md
        """,
    )


def test_config_with_suffix_de(mkdocs):
    mkdocs.docs(
        """
        .nav.de.yml
        | nav:
        |   - Title: foo.md
        """
    )

    mkdocs.build().assert_nav(
        """
        - Foo EN: foo.en.md
        """,
        """
        - Title: foo.de.md
        """,
    )


def test_nav_translations(mkdocs):
    mkdocs.files(
        """
        docs/
            .nav.yml
            | nav:
            |   - Title EN: foo.md
        mkdocs.yml
        | site_name: Test
        | plugins:
        |   - awesome-nav
        |   - i18n:
        |       docs_structure: suffix
        |       languages:
        |         - locale: en
        |           default: true
        |           name: English
        |         - locale: de
        |           name: Deutsch
        |           nav_translations:
        |             Title EN: Title DE
        """
    )

    mkdocs.build().assert_nav(
        """
        - Title EN: foo.en.md
        """,
        """
        - Title DE: foo.de.md
        """,
    )
