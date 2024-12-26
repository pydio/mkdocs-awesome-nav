def test_url(mkdocs):
    mkdocs.docs(
        """
        .nav.yml
        | nav:
        |   - Link: https://lukasgeiter.github.io/mkdocs-awesome-nav
        """
    )
    mkdocs.build().assert_nav(
        """
        - Link: https://lukasgeiter.github.io/mkdocs-awesome-nav
        """
    )


def test_absolute_path(mkdocs):
    mkdocs.docs(
        """
        .nav.yml
        | nav:
        |   - Link: /foo
        """
    )
    mkdocs.build().assert_nav(
        """
        - Link: /foo
        """
    )


def test_relative_path(mkdocs):
    mkdocs.docs(
        """
        .nav.yml
        | nav:
        |   - Link: ../foo
        """
    )
    mkdocs.build().assert_nav(
        """
        - Link: ../foo
        """
    )
