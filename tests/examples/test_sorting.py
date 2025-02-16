def test_direction_desc(mkdocs):
    mkdocs.docs(
        """
        getting-started.md
        support.md
        guides/
            authentication.md
            error-handling.md
        .nav.yml
        | sort:
        |   direction: desc
        """
    )
    mkdocs.build().assert_nav(
        """
        - Support: support.md
        - Getting started: getting-started.md
        - Guides:
            - Error handling: guides/error-handling.md
            - Authentication: guides/authentication.md
        """
    )


def test_direction_asc(mkdocs):
    mkdocs.docs(
        """
        getting-started.md
        support.md
        guides/
            authentication.md
            error-handling.md
        .nav.yml
        | sort:
        |   direction: asc
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


def test_sections_first(mkdocs):
    mkdocs.docs(
        """
        getting-started.md
        support.md
        guides/
            authentication.md
            error-handling.md
        .nav.yml
        | sort:
        |   sections: first
        """
    )
    mkdocs.build().assert_nav(
        """
        - Guides:
            - Authentication: guides/authentication.md
            - Error handling: guides/error-handling.md
        - Getting started: getting-started.md
        - Support: support.md
        """
    )


def test_sections_mixed(mkdocs):
    mkdocs.docs(
        """
        getting-started.md
        support.md
        guides/
            authentication.md
            error-handling.md
        .nav.yml
        | sort:
        |   sections: mixed
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


def test_sections_last(mkdocs):
    mkdocs.docs(
        """
        getting-started.md
        support.md
        guides/
            authentication.md
            error-handling.md
        .nav.yml
        | sort:
        |   sections: last
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


def test_type_alphabetical(mkdocs):
    mkdocs.docs(
        """
        version-9.0.md
        version-9.1.md
        version-10.0.md
        .nav.yml
        | sort:
        |   type: alphabetical
        """
    )
    mkdocs.build().assert_nav(
        """
        - Version 10.0: version-10.0.md
        - Version 9.0: version-9.0.md
        - Version 9.1: version-9.1.md
        """
    )


def test_type_natural(mkdocs):
    mkdocs.docs(
        """
        version-9.0.md
        version-9.1.md
        version-10.0.md
        .nav.yml
        | sort:
        |   type: natural
        """
    )
    mkdocs.build().assert_nav(
        """
        - Version 9.0: version-9.0.md
        - Version 9.1: version-9.1.md
        - Version 10.0: version-10.0.md
        """
    )


def test_ignore_case_true(mkdocs):
    mkdocs.docs(
        """
        getting-started.md
        LICENSE.md
        support.md
        .nav.yml
        | sort:
        |   ignore_case: true
        |   type: alphabetical
        """
    )
    mkdocs.build().assert_nav(
        """
        - Getting started: getting-started.md
        - LICENSE: LICENSE.md
        - Support: support.md
        """
    )


def test_ignore_case_false(mkdocs):
    mkdocs.docs(
        """
        getting-started.md
        LICENSE.md
        support.md
        .nav.yml
        | sort:
        |   ignore_case: false
        |   type: alphabetical
        """
    )
    mkdocs.build().assert_nav(
        """
        - LICENSE: LICENSE.md
        - Getting started: getting-started.md
        - Support: support.md
        """
    )


def test_by_filename(mkdocs):
    mkdocs.docs(
        """
        getting-started.md
        support.md
        guides/
            authentication.md
            error-handling.md
        .nav.yml
        | sort:
        |   by: filename
        | nav:
        |   - "**/*.md"
        """
    )
    mkdocs.build().assert_nav(
        """
        - Authentication: guides/authentication.md
        - Error handling: guides/error-handling.md
        - Getting started: getting-started.md
        - Support: support.md
        """
    )


def test_by_path(mkdocs):
    mkdocs.docs(
        """
        getting-started.md
        support.md
        guides/
            authentication.md
            error-handling.md
        .nav.yml
        | sort:
        |   by: path
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
