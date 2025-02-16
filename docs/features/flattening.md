# Flattening Sections

## Single Child

Sometimes it's nice to put a single page into its own directory to group it with related files such as images. Unfortunately this directory will show up in the navigation as a section containing a single page

Enable `flatten_single_child_sections` to automatically flatten those sections in the navigation. Sections that are [manually created with `nav`](nav.md#sections) remain unaffected by this, even if they have only one child.

/// tab | `true`
<div class="awesome-example" markdown>
```yaml title=".nav.yml"
flatten_single_child_sections: true
```

```title="File Structure"
docs/
├─ .nav.yml
└─ architecture
   ├─ architecture.md
   ├─ deployment.png
   └─ system-context.png
```

- Architecture
</div>
///

/// tab | `false` (default)
<div class="awesome-example" markdown>
```yaml title=".nav.yml"
flatten_single_child_sections: false
```

```title="File Structure"
docs/
├─ .nav.yml
└─ architecture
   ├─ architecture.md
   ├─ deployment.png
   └─ system-context.png
```

- Architecture
    - Architecture
</div>
///

??? tip "Child directories inherit this setting"
    `flatten_single_child_sections` applies to all child directories as well, unless it's overridden by a `.nav.yml` there.

## Multiple Children

While there is no setting to flatten a section with multiple children, it can be accomplished using a [glob pattern in `nav`](nav.md#glob-patterns):

<div class="awesome-example" markdown>
```yaml title=".nav.yml"
nav:
  - guides/*
```

```title="File Structure"
docs/
├─ .nav.yml
└─ guides
   ├─ authentication.md
   └─ error-handling.md
```

- Authentication
- Error handling
</div>
