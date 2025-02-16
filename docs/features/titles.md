# Section Titles

## Custom Section Title

Set a custom section title for a directory:

<div class="awesome-example" markdown>
```yaml title=".nav.yml"
title: API Endpoints
```

```title="File Structure"
docs/
└─ api/
   ├─ .nav.yml
   ├─ apps.md
   └─ users.md
```

- API Endpoints
    - Apps
    - Users
</div>

!!! info "Title from `nav`"
    Adding a title to the [directory in `nav`](nav.md#directories) overrides this custom title.

## Preserve Directory Names

Just like MkDocs, `awesome-nav` automatically transforms directory names into nicely formatted titles.  
Enable `preserve_directory_names` to use the exact directory name as title:

/// tab | `true`
<div class="awesome-example" markdown>
```yaml title=".nav.yml"
preserve_directory_names: true
```

```title="File Structure"
docs/
└─ awesome-nav
   ├─ .nav.yml
   ├─ getting-started.md
   └─ support.md
```

- awesome-nav
    - Getting started
    - Support
</div>
///

/// tab | `false` (default)
<div class="awesome-example" markdown>
```yaml title=".nav.yml"
preserve_directory_names: false
```

```title="File Structure"
docs/
└─ awesome-nav
   ├─ .nav.yml
   ├─ getting-started.md
   └─ support.md
```

- Awesome nav
    - Getting started
    - Support
</div>
///

??? tip "Child directories inherit this setting"
    `preserve_directory_names` applies to all child directories as well, unless it's overridden by a `.nav.yml` there.
