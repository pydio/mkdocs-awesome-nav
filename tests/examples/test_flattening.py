def test_true(mkdocs):
    mkdocs.docs(
        """
        architecture/
            architecture.md
            deployment.png
            system-context.png
        .nav.yml
        | flatten_single_child_sections: true
        """
    )
    mkdocs.build().assert_nav(
        """
        - Architecture: architecture/architecture.md
        """
    )


def test_false(mkdocs):
    mkdocs.docs(
        """
        architecture/
            architecture.md
            deployment.png
            system-context.png
        .nav.yml
        | flatten_single_child_sections: false
        """
    )
    mkdocs.build().assert_nav(
        """
        - Architecture:
            - Architecture: architecture/architecture.md
        """
    )


def test_pattern(mkdocs):
    mkdocs.docs(
        """
        guides/
            authentication.md
            error-handling.md
        .nav.yml
        | nav:
        |   - guides/*
        """
    )
    mkdocs.build().assert_nav(
        """
        - Authentication: guides/authentication.md
        - Error handling: guides/error-handling.md
        """
    )
