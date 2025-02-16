def test(mkdocs):
    mkdocs.docs(
        """
        api/
            apps.md
            users.md
            .nav.yml
            | title: API Endpoints
        """
    )
    mkdocs.build().assert_nav(
        """
        - API Endpoints:
            - Apps: api/apps.md
            - Users: api/users.md
        """
    )


def test_preserve_directory_names_true(mkdocs):
    mkdocs.docs(
        """
        awesome-nav/
            getting-started.md
            support.md
            .nav.yml
            | preserve_directory_names: true
        """
    )
    mkdocs.build().assert_nav(
        """
        - awesome-nav:
            - Getting started: awesome-nav/getting-started.md
            - Support: awesome-nav/support.md
        """
    )


def test_preserve_directory_names_false(mkdocs):
    mkdocs.docs(
        """
        awesome-nav/
            getting-started.md
            support.md
            .nav.yml
            | preserve_directory_names: false
        """
    )
    mkdocs.build().assert_nav(
        """
        - Awesome nav:
            - Getting started: awesome-nav/getting-started.md
            - Support: awesome-nav/support.md
        """
    )
