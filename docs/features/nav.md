# Custom Navigation

The `nav` option gives you full control over the navigation structure. The basic syntax is the same as in `mkdocs.yml`, but it can be defined in any directory and has more powerful features like glob patterns.

This example shows off the different kinds of `nav` entries:

<div class="awesome-example" markdown>
```yaml title=".nav.yml"
nav:
  - getting-started.md #(1)!
  - guides #(2)!
  - More Resources: #(3)!
    - "*" #(4)!
    - MkDocs: https://mkdocs.org #(5)!
```

1. Insert individual pages  
   [Read more below :material-arrow-down:](#pages)
2. Insert entire directories as sections  
   [Read more below :material-arrow-down:](#directories)
3. Create sections  
   [Read more below :material-arrow-down:](#sections)
4. Insert all files and directories that match glob patterns  
   [Read more below :material-arrow-down:](#glob-patterns)
5. Create external links  
   [Read more below :material-arrow-down:](#links)

```title="File Structure"
docs/
├─ .nav.yml
├─ getting-started.md
├─ support.md
└─ guides/
   ├─ authentication.md
   └─ error-handling.md
```

- Getting started
- Guides
    - Authentication
    - Error handling
- More Resources
    - Support
    - MkDocs
</div>


## Pages

Reference a markdown file to insert that page into that spot in the navigation:

<div class="awesome-example" markdown>
```yaml title=".nav.yml"
nav:
  - support.md
```

```title="File Structure"
docs/
├─ .nav.yml
└─ support.md
```

- Support
</div>

The markdown file can be located in a different directory:

<div class="awesome-example" markdown>
```yaml title=".nav.yml"
nav:
  - help/support.md
```

```title="File Structure"
docs/
├─ .nav.yml
└─ help/
   └─ support.md
```

- Support
</div>

You can also override the title that is displayed in the navigation:

<div class="awesome-example" markdown>
```yaml title=".nav.yml"
nav:
  - Help: support.md
```

```title="File Structure"
docs/
├─ .nav.yml
└─ support.md
```

- Help
</div>

## Directories

Reference a directory to insert it as section into that spot in the navigation:

<div class="awesome-example" markdown>
```yaml title=".nav.yml"
nav:
  - guides
```

```title="File Structure"
docs/
├─ .nav.yml
└─ guides/
   ├─ authentication.md
   └─ error-handling.md
```

- Guides
    - Authentication
    - Error handling
</div>

This can be a sub-directory as well:

<div class="awesome-example" markdown>
```yaml title=".nav.yml"
nav:
  - resources/guides
```

```title="File Structure"
docs/
├─ .nav.yml
└─ resources/
   └─ guides/
      ├─ authentication.md
      └─ error-handling.md
```

- Guides
    - Authentication
    - Error handling
</div>

You can also override the title that is displayed in the navigation:

<div class="awesome-example" markdown>
```yaml title=".nav.yml"
nav:
  - User Guides: guides
```

```title="File Structure"
docs/
├─ .nav.yml
└─ guides/
   ├─ authentication.md
   └─ error-handling.md
```

- User Guides
    - Authentication
    - Error handling
</div>

!!! tip
    If the referenced directory contains a `.nav.yml` file, it will of course be taken into account when generating the section.  
    A title defined here takes precedence over the title in the `.nav.yml` from inside the directory.

## Glob Patterns

Specify a glob pattern to insert all files and directories that match it.

Let's begin a with a simple example, `*` matches everything in the current directory:

<div class="awesome-example" markdown>
```yaml title=".nav.yml"
nav:
  - "*"
```

```title="File Structure"
docs/
├─ .nav.yml
├─ getting-started.md
├─ support.md
└─ guides/
   ├─ authentication.md
   └─ error-handling.md
```

- Getting started
- Support
- Guides
    - Authentication
    - Error handling
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

On its own, the `*` pattern isn't very useful. Omitting `nav` entirely would've had the same result. It becomes really useful when combined with other entries however. You can explicitly specify the entries that you want to control and have the rest of the navigation filled in automatically:

<div class="awesome-example" markdown>
```yaml title=".nav.yml"
nav:
  - getting-started.md
  - "*"
  - MkDocs: https://mkdocs.org
```

```title="File Structure"
docs/
├─ .nav.yml
├─ getting-started.md
├─ support.md
└─ guides/
   ├─ authentication.md
   └─ error-handling.md
```

- Getting started
- Support
- Guides
    - Authentication
    - Error handling
- MkDocs
</div>

!!! info "No repeated matches"
    Notice how `getting-started.md` does not appear twice in the navigation. Glob patterns will never match files or directories that are already part of the navigation.
    If you're looking to create a navigation item for a page without excluding it from a glob pattern, [create a link](#links) instead of the page entry.

### Examples

Glob patterns allow you to do a lot more than just `*` of course. Here are some examples of what's possible:

/// tab | Only markdown files
<div class="awesome-example" markdown>
```yaml title=".nav.yml"
nav:
  - "*.md"
```

```title="File Structure"
docs/
├─ .nav.yml
├─ getting-started.md
├─ support.md
└─ guides/
   ├─ authentication.md
   └─ error-handling.md
```

- Getting started
- Support
</div>
///

/// tab | Only directories
<div class="awesome-example" markdown>
```yaml title=".nav.yml"
nav:
  - "*/"
```

```title="File Structure"
docs/
├─ .nav.yml
├─ getting-started.md
├─ support.md
└─ guides/
   ├─ authentication.md
   └─ error-handling.md
```

- Guides
    - Authentication
    - Error handling
</div>
///

/// tab | Files with a suffix
<div class="awesome-example" markdown>
```yaml title=".nav.yml"
nav:
  - "*.public.md"
```

```title="File Structure"
docs/
├─ .nav.yml
├─ getting-started.public.md
└─ support.md
```

- Getting started
</div>
///

/// tab | Logical OR
<div class="awesome-example" markdown>
```yaml title=".nav.yml"
nav:
  - "*.@(public|published).md"
```

```title="File Structure"
docs/
├─ .nav.yml
├─ getting-started.public.md
├─ release-notes.published.md
└─ support.md
```

- Getting started
- Release notes
</div>
///


!!! info "Pattern syntax"
    This feature uses [`wcmatch`](https://facelessuser.github.io/wcmatch/) under the hood. Check out their documentation for more [details on the pattern syntax](https://facelessuser.github.io/wcmatch/glob). Enabled flags: `GLOBSTAR | EXTGLOB`

### Deep Matches

Patterns can also target files in nested directories:

/// tab | All pages
<div class="awesome-example" markdown>
```yaml title=".nav.yml"
nav:
  - "**/*.md"
```

```title="File Structure"
docs/
├─ .nav.yml
├─ getting-started.md
├─ support.md
└─ guides/
   ├─ authentication.md
   └─ error-handling.md
```

- Getting started
- Authentication
- Error handling
- Support
</div>
///

/// tab | One level deep
<div class="awesome-example" markdown>
```yaml title=".nav.yml"
nav:
  - "*/index.md"
```

```title="File Structure"
docs/
├─ .nav.yml
├─ guides
│  ├─ authentication.md
│  ├─ index.md
│  └─ error-handling.md
└─ help
   ├─ index.md
   └─ support.md
```

- Guides
- Help
</div>
///

!!! info "Flattening"
    Matching files and directories are inserted into the navigation as a flat list. By default, they are still sorted by path though. This can be changed using the [`sort.by` option](sorting.md#sort-by).

### Options

To set additional options for a glob pattern, use the following syntax:

```yaml
nav:
  - glob: "*"
    sort:
      direction: desc
```

These are all the available options:

/// tab | Table
| <div style="min-width: 240px">Option</div>                                     | Description                                                                                            |
|---------------------------------|---------------------------------------------------------------------------------------------|
| `ignore_no_matches`             | Set to `true` to disable the message that is printed when this glob pattern doesn't match any files or directories. |
| `preserve_directory_names`      | Disable formatting of generated directory titles. [Read more :material-arrow-right:](titles.md#preserve-directory-names)                                                                                            |
| `flatten_single_child_sections` | For sections with a single child, show the child instead of the section. [Read more :material-arrow-right:](flattening.md#single-child)                                                                                            |
| `ignore`                        | Everything that matches this glob pattern is hidden. [Read more :material-arrow-right:](hiding.md#ignore-patterns)                                                                                            |
| `sort`                          | All the regular sorting options. [Read more :material-arrow-right:](sorting.md)                                                                                            |
| `append_unmatched`              | Add unmatched files at the end. This applies to child directories, not the pattern itself. [Read more :material-arrow-right:](nav.md#unmatched-files)                                                                                            |
///

/// tab | Example
```yaml
nav:
  - glob: "*"
    ignore_no_matches: true
    preserve_directory_names: true
    flatten_single_child_sections: true
    ignore: "*.hidden.md"
    sort:
      direction: asc
      type: natural
      by: filename
      sections: last
```
///


## Sections

You can create a section that is not derived from a file directory like this: 

<div class="awesome-example" markdown>
```yaml title=".nav.yml"
nav:
  - More Resources:
    - support.md
```

```title="File Structure"
docs/
├─ .nav.yml
└─ support.md
```

- More Resources
    - Support
</div>

!!! tip
    Inside the section you can use all the same entries as at the top level - including nested sections.


## Links

You may add external links to the navigation:

```yaml title=".nav.yml"
nav:
  - Full Url: https://lukasgeiter.github.io/mkdocs-awesome-nav
  - Relative Path: ../
```

## Unmatched Files

Files and directories that are not referenced by your `nav` configuration will not be included in the navigation. If this happens, MkDocs prints an info message listing the files:

```
INFO    -  The following pages exist in the docs directory, but are not included in the "nav" configuration:
             - support.md
```

!!! info "Hidden pages"
    Unmatched pages are still built and accessible by going to their url. Use the [`exclude_docs` option from MkDocs](https://www.mkdocs.org/user-guide/configuration/#exclude_docs){:target="_blank"} to completely exclude files.

If you'd like the file to be included, either add a [page entry](#pages) or a [glob pattern](#glob-patterns) that matches it.

Alternatively, you may turn on `append_unmatched` to automatically add unmatched files and directories at the end of your `nav`. This is equivalent to adding a `*` glob pattern at the end. In the following example, `support.md` is omitted from `nav`:

/// tab | `true`
<div class="awesome-example" markdown>
```yaml title=".nav.yml"
append_unmatched: true
nav:
  - getting-started.md
  - guides
```

```title="File Structure"
docs/
├─ .nav.yml
├─ getting-started.md
├─ support.md
└─ guides/
   ├─ authentication.md
   └─ error-handling.md
```

- Getting started
- Guides
    - Authentication
    - Error handling
- Support
</div>
///

/// tab | `false` (default)
<div class="awesome-example" markdown>
```yaml title=".nav.yml"
append_unmatched: false
nav:
  - getting-started.md
  - guides
```

```title="File Structure"
docs/
├─ .nav.yml
├─ getting-started.md
├─ support.md
└─ guides/
   ├─ authentication.md
   └─ error-handling.md
```

- Getting started
- Guides
    - Authentication
    - Error handling
</div>
///

??? tip "Child directories inherit this setting"
    `append_unmatched` applies to all child directories as well, unless it's overridden by a `.nav.yml` there.