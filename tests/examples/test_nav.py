def test(mkdocs):
    mkdocs.docs(
        """
        getting-started.md
        support.md
        guides/
            authentication.md
            error-handling.md
        .nav.yml
        | nav:
        |   - getting-started.md
        |   - guides
        |   - More Resources:
        |     - "*"
        |     - MkDocs: https://mkdocs.org
        """
    )
    mkdocs.build().assert_nav(
        """
        - Getting started: getting-started.md
        - Guides:
            - Authentication: guides/authentication.md
            - Error handling: guides/error-handling.md
        - More Resources:
            - Support: support.md
            - MkDocs: https://mkdocs.org
        """
    )


def test_pages(mkdocs):
    mkdocs.docs(
        """
        support.md
        .nav.yml
        | nav:
        |   - support.md
        """
    )
    mkdocs.build().assert_nav(
        """
        - Support: support.md
        """
    )


def test_pages_deep(mkdocs):
    mkdocs.docs(
        """
        help/
            support.md
        .nav.yml
        | nav:
        |   - help/support.md
        """
    )
    mkdocs.build().assert_nav(
        """
        - Support: help/support.md
        """
    )


def test_pages_title(mkdocs):
    mkdocs.docs(
        """
        support.md
        .nav.yml
        | nav:
        |   - Help: support.md
        """
    )
    mkdocs.build().assert_nav(
        """
        - Help: support.md
        """
    )


def test_directories(mkdocs):
    mkdocs.docs(
        """
        guides/
            authentication.md
            error-handling.md
        .nav.yml
        | nav:
        |   - guides
        """
    )
    mkdocs.build().assert_nav(
        """
        - Guides:
            - Authentication: guides/authentication.md
            - Error handling: guides/error-handling.md
        """
    )


def test_directories_deep(mkdocs):
    mkdocs.docs(
        """
        resources/
            guides/
                authentication.md
                error-handling.md
        .nav.yml
        | nav:
        |   - resources/guides
        """
    )
    mkdocs.build().assert_nav(
        """
        - Guides:
            - Authentication: resources/guides/authentication.md
            - Error handling: resources/guides/error-handling.md
        """
    )


def test_directories_title(mkdocs):
    mkdocs.docs(
        """
        guides/
            authentication.md
            error-handling.md
        .nav.yml
        | nav:
        |   - User Guides: guides
        """
    )
    mkdocs.build().assert_nav(
        """
        - User Guides:
            - Authentication: guides/authentication.md
            - Error handling: guides/error-handling.md
        """
    )


def test_patterns(mkdocs):
    mkdocs.docs(
        """
        getting-started.md
        support.md
        guides/
            authentication.md
            error-handling.md
        .nav.yml
        | nav:
        |   - "*"
        """
    )
    mkdocs.build().assert_nav(
        """
        - Getting started: getting-started.md
        - Support: support.md
        - Guides:
            - Authentication: guides/authentication.md
            - Error handling: guides/error-handling.md
        """
    )


def test_patterns_other_entries(mkdocs):
    mkdocs.docs(
        """
        getting-started.md
        support.md
        guides/
            authentication.md
            error-handling.md
        .nav.yml
        | nav:
        |   - getting-started.md
        |   - "*"
        |   - MkDocs: https://mkdocs.org
        """
    )
    mkdocs.build().assert_nav(
        """
        - Getting started: getting-started.md
        - Support: support.md
        - Guides:
            - Authentication: guides/authentication.md
            - Error handling: guides/error-handling.md
        - MkDocs: https://mkdocs.org
        """
    )


def test_patterns_only_files(mkdocs):
    mkdocs.docs(
        """
        getting-started.md
        support.md
        guides/
            authentication.md
            error-handling.md
        .nav.yml
        | nav:
        |   - "*.md"
        """
    )
    mkdocs.build().assert_nav(
        """
        - Getting started: getting-started.md
        - Support: support.md
        """
    )


def test_patterns_only_directories(mkdocs):
    mkdocs.docs(
        """
        getting-started.md
        support.md
        guides/
            authentication.md
            error-handling.md
        .nav.yml
        | nav:
        |   - "*/"
        """
    )
    mkdocs.build().assert_nav(
        """
        - Guides:
            - Authentication: guides/authentication.md
            - Error handling: guides/error-handling.md
        """
    )


def test_patterns_suffix(mkdocs):
    mkdocs.docs(
        """
        getting-started.public.md
        | # Getting started
        support.md
        .nav.yml
        | nav:
        |   - "*.public.md"
        """
    )
    mkdocs.build().assert_nav(
        """
        - Getting started: getting-started.public.md
        """
    )


def test_patterns_logical_or(mkdocs):
    mkdocs.docs(
        """
        getting-started.public.md
        | # Getting started
        release-notes.published.md
        | # Release notes
        support.md
        .nav.yml
        | nav:
        |   - "*.@(public|published).md"
        """
    )
    mkdocs.build().assert_nav(
        """
        - Getting started: getting-started.public.md
        - Release notes: release-notes.published.md
        """
    )


def test_patterns_app_pages(mkdocs):
    mkdocs.docs(
        """
        getting-started.md
        support.md
        guides/
            authentication.md
            error-handling.md
        .nav.yml
        | nav:
        |   - "**/*.md"
        """
    )
    mkdocs.build().assert_nav(
        """
        - Getting started: getting-started.md
        - Authentication: guides/authentication.md
        - Error handling: guides/error-handling.md
        - Support: support.md
        """
    )


def test_patterns_one_level_deep(mkdocs):
    mkdocs.docs(
        """
        getting-started.md
        guides/
            authentication.md
            index.md
            | # Guides
            error-handling.md
        help/
            index.md
            | # Help
            support.md
        .nav.yml
        | nav:
        |   - "*/index.md"
        """
    )
    mkdocs.build().assert_nav(
        """
        - Guides: guides/index.md
        - Help: help/index.md
        """
    )


def test_sections(mkdocs):
    mkdocs.docs(
        """
        support.md
        .nav.yml
        | nav:
        |   - More Resources:
        |     - support.md
        """
    )
    mkdocs.build().assert_nav(
        """
        - More Resources:
            - Support: support.md
        """
    )


def test_append_unmatched_true(mkdocs):
    mkdocs.docs(
        """
        getting-started.md
        support.md
        guides/
            authentication.md
            error-handling.md
        .nav.yml
        | append_unmatched: true
        | nav:
        |   - getting-started.md
        |   - guides
        """
    )
    mkdocs.build().assert_nav(
        """
        - Getting started: getting-started.md
        - Guides:
            - Authentication: guides/authentication.md
            - Error handling: guides/error-handling.md
        - Support: support.md
        """
    )


def test_append_unmatched_false(mkdocs):
    mkdocs.docs(
        """
        getting-started.md
        support.md
        guides/
            authentication.md
            error-handling.md
        .nav.yml
        | append_unmatched: false
        | nav:
        |   - getting-started.md
        |   - guides
        """
    )
    mkdocs.build().assert_nav(
        """
        - Getting started: getting-started.md
        - Guides:
            - Authentication: guides/authentication.md
            - Error handling: guides/error-handling.md
        """
    )
