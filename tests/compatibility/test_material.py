import pytest


@pytest.fixture(autouse=True)
def _test_files(mkdocs):
    mkdocs.files(
        """
        docs/
            foo.md
            blog/
                posts/
                    post.md
                    | ---
                    | date: 2024-01-31
                    | ---
                index.md
        mkdocs.yml
        | site_name: Test
        | theme: material
        | plugins:
        |   - awesome-nav
        |   - blog
        """
    )


def test_blog_default_nav(mkdocs):
    mkdocs.build().assert_nav(
        """
        - Foo: foo.md
        - Blog:
            - Index: blog/index.md
            - Archive:
                - "2024": blog/archive/2024.md
        """
    )


def test_blog_explicit_nav(mkdocs):
    mkdocs.files(
        """
        docs/
            .nav.yml
            | nav:
            |   - Section:
            |       - blog/index.md
            |   - foo.md
        """
    )

    mkdocs.build().assert_nav(
        """
        - Section:
            - Index: blog/index.md
            - Archive:
                - "2024": blog/archive/2024.md
        - Foo: foo.md
        """
    )
