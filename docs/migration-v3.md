# Migration from v2 to v3

Version 3 has been developed from scratch to address some of the shortcomings of version 2 using a new approach. While the previous version modifies the navigation that MkDocs generates, version 3 generates the entire navigation on its own. This results in more powerful features and better compatibility with other plugins.

This page outlines the changes in version 3 of the plugin. If you're having trouble migrating, [open a GitHub issue](https://github.com/lukasgeiter/mkdocs-awesome-nav/issues/new).

The documentation and code of version 2 is still available on the [v2 branch](https://github.com/lukasgeiter/mkdocs-awesome-nav/tree/v2).

## Name Change

The plugin has been renamed from `mkdocs-awesome-pages-plugin` to `mkdocs-awesome-nav`.

The `pages` in the original name referred to the key in `mkdocs.yml`, which since has been renamed to `nav`. Additionally, `nav` fits much better because the plugin is about customizing the navigation and not the pages themselves.

The `-plugin` suffix has been dropped for conciseness.

## Migrating

1. Uninstall `mkdocs-awesome-pages-plugin`
2. Install `mkdocs-awesome-nav`
3. Replace `awesome-pages` with `awesome-nav` in the `plugins` list in `mkdocs.yml`
4. Update `mkdocs.yml` and `.pages` according to the changes listed below

## Changes in `mkdocs.yml`

### `nav`

In version 3, the plugin ignores a `nav` that is defined in `mkdocs.yml`.

If you have one that you want to keep, move it to `docs/.nav.yml` and read the [chapter on `nav` below](#nav_1).

### Plugin Options

Most plugin options have been dropped in favor of configuring them in `docs/.nav.yml`.

| v2                      | v3                                                                                              |
|-------------------------|-------------------------------------------------------------------------------------------------|
| `collapse_single_pages` | [`flatten_single_child_sections`](features/flattening.md) in `docs/.nav.yml`                    |
| `strict`                | [`strict` from MkDocs](https://www.mkdocs.org/user-guide/configuration/#strict)                 |
| `order`                 | [`sort.direction`](features/sorting.md#sort-direction) in `docs/.nav.yml`                       |
| `sort_type`             | [`sort.type`](features/sorting.md#sort-type) in `docs/.nav.yml`                                 |
| `ignore_case`           | [`sort.ignore_case`](features/sorting.md#sort-ignore-case) in `docs/.nav.yml`                   |
| `order_by`              | [`sort.by`](features/sorting.md#sort-by) in `docs/.nav.yml`                                     |
| `filename`              | [`filename`](reference.md#plugin-options) (the default has changed from `.pages` to `.nav.yml`) |


## Changes in `.pages`

In version 3, the `.pages` file is called `.nav.yml` by default. It's recommended that you rename your files accordingly. Alternatively, you may configure the `filename` in the plugin options.

Continue reading for the changes to the file contents. Note that unchanged or new features are not listed.

### `arrange`

`arrange` was deprecated in version 2 and has now been removed in favor of `nav`.

### `nav`

The special `...` entry has been replaced by [glob patterns](features/nav.md#glob-patterns).

While plain `...` entries can be replaced with `"*"`, filtering expressions will require some more attention. Read the documentation for [glob patterns](features/nav.md#glob-patterns) and [ignore patterns](features/hiding.md#ignore-patterns) for more information.

The effect of `| flat` can be achieved by using a [deep glob pattern](features/nav.md#deep-matches).

!!! info "Regular Expressions"
    Support for regex has been removed. If you have a use-case that you believe can only be solved using regex, please [open an issue on GitHub](https://github.com/lukasgeiter/mkdocs-awesome-nav/issues/new).

### `collapse_single_pages`

`collapse_single_pages` has been renamed to `flatten_single_child_sections`.

### `collapse`

`collapse` has been removed, you should be able to achieve the same by using `flatten_single_child_sections`.

### Sorting

In version 3, the default sorting behaves slightly differently than before. This is mostly because of [natural sorting](features/sorting.md#sort-type).

These are all the sorting related changes:

| v2            | v3                                                                                 |
|---------------|------------------------------------------------------------------------------------|
| `order`       | [`sort.direction`](features/sorting.md#sort-direction)                             |
| `order_by`    | [`sort.by`](features/sorting.md#sort-by) - note the caveat when sorting by `title` |
| `sort_type`   | [`sort.type`](features/sorting.md#sort-type) - `natural` is now the default        |
| `ignore_case` | [`sort.ignore_case`](features/sorting.md#sort-ignore-case)                         |

