def test_glob(mkdocs):
    mkdocs.files(
        """
        docs/
            foo.md
            bar.md
        mkdocs.yml
        | site_name: Test
        | plugins:
        |   - awesome-nav
        |   - exclude:
        |       glob:
        |         - foo.md
        """
    )

    mkdocs.build().assert_nav(
        """
        - Bar: bar.md
        """
    )
