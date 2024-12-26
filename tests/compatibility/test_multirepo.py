import subprocess
import sys

import pytest

if sys.platform.startswith("win"):
    pytest.skip("multirepo doesn't work on windows as it requires bash", allow_module_level=True)


@pytest.fixture(autouse=True)
def _test_files(mkdocs):
    mkdocs.files(
        """
        mkdocs.yml
        | site_name: Test
        | plugins:
        |   - awesome-nav
        |   - multirepo:
        |       repos:
        |         - section: repo
        |           import_url: ../repo?edit_uri=/
        """
    )


def _init_repo():
    subprocess.run(
        """
        git init -b master
        git add --all
        git -c user.name="Test" -c user.email="test@test.com" commit -m "Initial commit"
        """,
        cwd="repo",
        shell=True,
    )


def test_default_nav(mkdocs):
    mkdocs.files(
        """
        docs/
            foo.md
        repo/
            docs/
                bar.md
        """
    )

    _init_repo()

    mkdocs.build().assert_nav(
        """
        - Foo: foo.md
        - Repo:
            - Bar: repo/bar.md
        """
    )


def test_nav(mkdocs):
    mkdocs.files(
        """
        docs/
            foo.md
            .nav.yml
            | nav:
            |   - Title: repo
            |   - foo.md
        repo/
            docs/
                bar.md
        """
    )

    _init_repo()

    mkdocs.build().assert_nav(
        """
        - Title:
            - Bar: repo/bar.md
        - Foo: foo.md
        """
    )


def test_nav_in_imported_repo_default_filename(mkdocs):
    mkdocs.files(
        """
        docs/
            foo.md
        repo/
            docs/
                bar.md
                .nav.yml
                | nav:
                |   - Title: bar.md
        """
    )

    _init_repo()

    # .nav.yml has no effect because mkdocs-multirepo-plugin ignores it when preparing the cloned repo
    mkdocs.build().assert_nav(
        """
        - Foo: foo.md
        - Repo:
            - Bar: repo/bar.md
        """
    )


def test_nav_in_imported_repo_custom_filename(mkdocs):
    mkdocs.files(
        """
        docs/
            foo.md
        repo/
            docs/
                bar.md
                nav.yml
                | nav:
                |   - Title: bar.md
        mkdocs.yml
        | site_name: Test
        | plugins:
        |   - awesome-nav:
        |       filename: nav.yml
        |   - multirepo:
        |       repos:
        |         - section: repo
        |           import_url: ../repo?edit_uri=/
        """
    )

    _init_repo()

    mkdocs.build().assert_nav(
        """
        - Foo: foo.md
        - Repo:
            - Title: repo/bar.md
        """
    )
