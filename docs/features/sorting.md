Use these options to customize the sorting of pages and sections. They affect all items that aren't explicitly ordered using `nav`.

??? tip "Child directories inherit these settings"
    Sorting options apply to all child directories as well, unless they're overridden by a `.nav.yml` there.

## Sort Direction

Use this option to change the direction from ascending to descending.

/// tab | `desc`
<div class="awesome-example" markdown>
```yaml title=".nav.yml"
sort:
  direction: desc
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

- Support
- Getting started
- Guides
    - Error handling
    - Authentication
</div>
///

/// tab | `asc` (default)
<div class="awesome-example" markdown>
```yaml title=".nav.yml"
sort:
  direction: asc
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
///

## Sort Sections

By default, sections are always sorted after all pages. Use this option to have them before or mixed in with pages.

/// tab | `first`
<div class="awesome-example" markdown>
```yaml title=".nav.yml"
sort:
  sections: first
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
- Getting started
- Support
</div>
///

/// tab | `mixed`
<div class="awesome-example" markdown>
```yaml title=".nav.yml"
sort:
  sections: mixed
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

/// tab | `last` (default)
<div class="awesome-example" markdown>
```yaml title=".nav.yml"
sort:
  sections: last
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
///

## Sort Type

`awesome-nav` uses [natural sorting](https://en.wikipedia.org/wiki/Natural_sort_order){:target="_blank"} by default. Set this option for strictly alphabetical sorting.

/// tab | `alphabetical`
<div class="awesome-example" markdown>
```yaml title=".nav.yml"
sort:
  type: alphabetical
```

```title="File Structure"
docs/
├─ version-9.0.md
├─ version-9.1.md
└─ version-10.0.md
```

- Version 10.0
- Version 9.0
- Version 9.1
</div>
///

/// tab | `natural` (default)
<div class="awesome-example" markdown>
```yaml title=".nav.yml"
sort:
  type: natural
```

```title="File Structure"
docs/
├─ version-9.0.md
├─ version-9.1.md
└─ version-10.0.md
```

- Version 9.0
- Version 9.1
- Version 10.0
</div>
///

## Sort Ignore Case

Enable case-insensitive sorting.

!!! info "Natural sorting"
    Note that [`natural` sorting](#sort-type) (which is the default) already makes sure that lowercase and uppercase are grouped together.  
    Therefore the option makes most sense when combined with [`alphabetical` sorting](#sort-type).

/// tab | `true`
<div class="awesome-example" markdown>
```yaml title=".nav.yml"
sort:
  ignore_case: true
  type: alphabetical
```

```title="File Structure"
docs/
├─ .nav.yml
├─ getting-started.md
├─ LICENSE.md
└─ support.md
```

- Getting started
- LICENSE
- Support
</div>
///

/// tab | `false` (default)
<div class="awesome-example" markdown>
```yaml title=".nav.yml"
sort:
  ignore_case: false
  type: alphabetical
```

```title="File Structure"
docs/
├─ .nav.yml
├─ getting-started.md
├─ LICENSE.md
└─ support.md
```

- LICENSE
- Getting started
- Support
</div>
///

## Sort By

Configure which attribute is used for sorting.

### Path & Filename

The difference between `path` and `filename` is only relevant with [deep glob patterns](nav.md#deep-matches), otherwise their behavior is identical.

/// tab | `filename`
<div class="awesome-example" markdown>
```yaml title=".nav.yml"
sort:
  by: filename
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

- Authentication
- Error handling
- Getting started
- Support
</div>
///

/// tab | `path` (default)
<div class="awesome-example" markdown>
```yaml title=".nav.yml"
sort:
  by: path
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

### Title

Sort sections and pages based on their title instead of path or filename.

```yaml title=".nav.yml"
sort:
  by: title
```

!!! warning "Limitation"
    Since MkDocs extracts the markdown title when it renders the page, it is not available when `awesome-nav` is sorting the pages.  
    In order to have pages properly sorted by their title, add the title to the [meta-data at the beginning of the markdown file](https://www.mkdocs.org/user-guide/writing-your-docs/#meta-data):

    ```yaml
    ---
    title: Getting started
    ---
    ```
    
    Without a title in the meta-data, sorting falls back to the filename.
