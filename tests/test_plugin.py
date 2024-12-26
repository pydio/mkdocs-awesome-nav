def test_filename(mkdocs):
    mkdocs.files(
        """
        docs/
            foo.md
            bar.md
            .nav.yml
            | nav:
            |   - foo.md
            awesome_nav.yml
            | nav:
            |   - bar.md
        mkdocs.yml
        | site_name: Test
        | plugins:
        |   - awesome-nav:
        |       filename: awesome_nav.yml
        """
    )
    mkdocs.build().assert_nav(
        """
        - Bar: bar.md
        """
    )


def test_no_files(mkdocs):
    mkdocs.build().assert_nav_empty()
