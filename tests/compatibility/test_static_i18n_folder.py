import pytest


@pytest.fixture(autouse=True)
def _test_files(mkdocs):
    mkdocs.files(
        """
        docs/
            en/
                foo.md
                | # Foo EN
            de/
                foo.md
                | # Foo DE
        mkdocs.yml
        | site_name: Test
        | plugins:
        |   - awesome-nav
        |   - i18n:
        |       docs_structure: folder
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
        - Foo EN: en/foo.md
        """,
        """
        - Foo DE: de/foo.md
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
        - Foo EN: en/foo.md
        """,
        """
        - Foo DE: de/foo.md
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
        - Title: en/foo.md
        """,
        """
        - Title: de/foo.md
        """,
    )


def test_page_specific_language(mkdocs, logs):
    mkdocs.docs(
        """
        .nav.yml
        | nav:
        |   - de/foo.md
        """
    )

    mkdocs.build().assert_nav(
        """
        []
        """,
        """
        - Foo DE: de/foo.md
        """,
    )

    assert logs.from_plugin == [
        logs.warning("awesome-nav: The nav item 'de/foo.md' doesn't match any files or directories [.nav.yml]"),
    ]


def test_page_title_en(mkdocs):
    mkdocs.docs(
        """
        en/
            .nav.yml
            | nav:
            |   - Title EN: foo.md
        """
    )

    mkdocs.build().assert_nav(
        """
        - Title EN: en/foo.md
        """,
        """
        - Title EN: de/foo.md
        """,
    )


def test_page_title_de(mkdocs):
    mkdocs.docs(
        """
        de/
            .nav.yml
            | nav:
            |   - Title DE: foo.md
        """
    )

    mkdocs.build().assert_nav(
        """
        - Foo EN: en/foo.md
        """,
        """
        - Title DE: de/foo.md
        """,
    )


def test_pattern(mkdocs):
    mkdocs.docs(
        """
        .nav.yml
        | nav:
        |   - */foo.md
        """
    )

    mkdocs.build().assert_nav(
        """
        - Foo EN: en/foo.md
        """,
        """
        - Foo DE: de/foo.md
        """,
    )


def test_pattern_without_folder(mkdocs, logs):
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


def test_config_in_folder_en(mkdocs):
    mkdocs.docs(
        """
        en/
            .nav.yml
            | nav:
            |   - Title: foo.md
        """
    )

    mkdocs.build().assert_nav(
        """
        - Title: en/foo.md
        """,
        """
        - Title: de/foo.md
        """,
    )


def test_config_in_folder_de(mkdocs):
    mkdocs.docs(
        """
        de/
            .nav.yml
            | nav:
            |   - Title: foo.md
        """
    )

    mkdocs.build().assert_nav(
        """
        - Foo EN: en/foo.md
        """,
        """
        - Title: de/foo.md
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
        |       docs_structure: folder
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
        - Title EN: en/foo.md
        """,
        """
        - Title DE: de/foo.md
        """,
    )
