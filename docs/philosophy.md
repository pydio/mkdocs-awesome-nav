# Philosophy

## Granular Control

With MkDocs, if you want to diverge in any way from the automatically generated navigation, you have to define the entire structure in `mkdocs.yml` by hand. You have to pick between the maintainability of the generated navigation and the flexibility of a custom one.

With the `awesome-nav` plugin, you get the best of both worlds. The navigation is generated based on your file structure, but you can make granular adjustments where needed. To do so, you create a `.nav.yml` file anywhere in your `docs` directory and use the [various features](features/nav.md) to customize your navigation.

To achieve this, `awesome-nav` completely discards the navigation that MkDocs and other plugins generate.

## File Structure First

While you absolutely can write out the entire navigation in `docs/.nav.yml` independently of the file structure, `awesome-nav` really shines when you align your file structure with the intended navigation and use a `.nav.yml` file here and there to augment it.

## Inheritance

Many settings in `.nav.yml` are inherited by child directories. This allows you to affect a large section of your docs or even the entire site by placing the configuration at the root in `docs/.nav.yml`.

## Limitations

The `awesome-nav` plugin allows you to customize the navigation **structure**. It can't influence how the links are rendered. Such customizations are usually handled by [themes](https://www.mkdocs.org/user-guide/choosing-your-theme/).
