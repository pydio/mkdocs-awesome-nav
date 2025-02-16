def test_hide(mkdocs):
    mkdocs.docs(
        """
        getting-started.md
        api/
            apps.md
            users.md
            .nav.yml
            | hide: true
        """
    )
    mkdocs.build().assert_nav(
        """
        - Getting started: getting-started.md
        """
    )


def test_ignore(mkdocs):
    mkdocs.docs(
        """
        getting-started.md
        faq.hidden.md
        .nav.yml
        | ignore: "*.hidden.md"
        """
    )
    mkdocs.build().assert_nav(
        """
        - Getting started: getting-started.md
        """
    )
