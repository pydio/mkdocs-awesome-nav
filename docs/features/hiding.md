# Hiding Pages

!!! info "Hidden pages"
    Hidden pages are still built and accessible by going to their url. Use the [`exclude_docs` option from MkDocs](https://www.mkdocs.org/user-guide/configuration/#exclude_docs){:target="_blank"} to completely exclude files.

## Hiding a Directory

Hide a directory and all its children from the navigation:

<div class="awesome-example" markdown>
```yaml title=".nav.yml"
hide: true
```

```title="File Structure"
docs/
├─ getting-started.md
└─ api/
   ├─ .nav.yml
   ├─ apps.md
   └─ users.md
```

- Getting started
</div>

## Ignore Patterns

Hide directories and pages using `.gitignore`-style glob patterns:

<div class="awesome-example" markdown>
```yaml title=".nav.yml"
ignore: "*.hidden.md"
```

```title="File Structure"
docs/
├─ getting-started.md
└─ faq.hidden.md
```

- Getting started
</div>

??? warning "Patterns that start with `*` need to be wrapped in quotes"
    YAML uses `*` at the beginning of nodes for [aliases](https://yaml.org/spec/1.2.2/#alias-nodes). Make sure to wrap your pattern in quotes if it starts with `*`.

    Without the quotes, you get the following error:
    ```
    ERROR   -  awesome-nav: Parsing error [.nav.yml]
               while scanning an alias
                 in "<unicode string>", line 4, column 5:
                     - *
                       ^
               expected alphabetic or numeric character, but found '\x00'
                 in "<unicode string>", line 4, column 6:
                     - *
                        ^
    ```

Make it a list if you have multiple patterns:

```yaml title=".nav.yml"
ignore:
  - "*.hidden.md"
  - hidden/
```

??? tip "Child directories inherit this setting"
    `ignore` applies to all child directories as well, unless it's overridden by a `.nav.yml` there.

If you want to keep the inherited ignore patterns and extend them with additional ones, use the special `$inherit` value:

```yaml title=".nav.yml"
ignore:
  - $inherit
  - "*.hidden.md"
```

Take a look at the [glob patterns section of the `nav`](nav.md#glob-patterns) documentation for some more examples of patterns.

!!! tip
    The [`not_in_nav` option from MkDocs](https://www.mkdocs.org/user-guide/configuration/#not_in_nav){:target="_blank"} provides a similar feature. `awesome-nav` is fully compatible and will take `not_in_nav` into account.