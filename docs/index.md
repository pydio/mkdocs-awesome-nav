# Awesome Nav for MkDocs

> Formerly known as `mkdocs-awesome-pages-plugin`. [Read more about the change :material-arrow-right:](migration-v3.md)

This MkDocs plugin gives you full control over your navigation structure without having to write the entire thing by hand. Whether you just want to add an external link or restructure the entire navigation tree, `awesome-nav` has you covered.

## Feature Highlights

- **Adjusting Item Order**: Manually re-order navigation items or use the extensive sorting options.
- **Adding Sections & Links:** Create sections and add external links.
- **Customizing Titles**: Change the title of sections and override page titles.
- **Hiding Pages**: Hide pages or entire sections from the navigation, making them only accessible by url.
- **Using Glob Patterns**: Match files using glob patterns to show or hide them.

## Installation

Install using a python package manager of your choice:

/// tab | pip
```shell
pip install mkdocs-awesome-nav
```
///

/// tab | uv
```shell
uv add mkdocs-awesome-nav
```
///

Then enable the plugin in `mkdocs.yml`:
```yaml
plugins:
   - search
   - awesome-nav
```
