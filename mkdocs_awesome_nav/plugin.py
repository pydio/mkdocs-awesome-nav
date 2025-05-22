import os
import yaml
from mkdocs.config import Config, config_options
from mkdocs.config.defaults import MkDocsConfig
from mkdocs.plugins import BasePlugin, event_priority
from mkdocs.structure.files import Files
from mkdocs.structure.nav import Navigation, get_navigation
from mkdocs.structure.pages import Page

from mkdocs_awesome_nav.log import log_warning
from mkdocs_awesome_nav.nav.context import MkdocsFilesContext
from mkdocs_awesome_nav.nav.directory import RootNavDirectory


class AwesomeNavConfig(Config):
    filename = config_options.Type(str, default=".nav.yaml")


class AwesomeNavPlugin(BasePlugin[AwesomeNavConfig]):
    @event_priority(100)
    def on_nav(self, nav, config, files):
        for item in nav.items:
            self._apply_slug_to_nav_item(item, config, config.docs_dir)
        nav.items = sorted(nav.items, key=self._nav_sort_key)
        return nav

    def _apply_slug_to_nav_item(self, item, config, root_docs_dir):
        if hasattr(item, 'children') and item.children:
            for child in item.children:
                self._apply_slug_to_nav_item(child, config, root_docs_dir)

            # Try to infer folder path from first child
            if hasattr(item.children[0], 'file') and item.children[0].file:
                first_file_path = os.path.join(root_docs_dir, item.children[0].file.src_path)
                section_path = os.path.dirname(first_file_path)
                nav_file = os.path.join(section_path, '.nav.yaml')
                if os.path.isfile(nav_file):
                    try:
                        with open(nav_file, 'r') as f:
                            nav_meta = yaml.safe_load(f)
                            section_title = nav_meta.get('title')
                            if section_title:
                                item.title = section_title
                            section_weight = nav_meta.get('weight')
                            if section_weight is not None:
                                item.weight = section_weight
                    except:
                        pass

            item.children = sorted(item.children, key=self._nav_sort_key)

        if hasattr(item, 'file') and item.file:
            file_path = os.path.join(config.docs_dir, item.file.src_path)
            slug_parts = self._build_slug_path(file_path, config)
            item.file.url = '/'.join(slug_parts) + '/'

            # Try to load page weight from frontmatter
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                if lines and lines[0].strip() == '---':
                    end = lines[1:].index('---\n') + 1 if '---\n' in lines[1:] else None
                    frontmatter = yaml.safe_load(''.join(lines[1:end])) if end else {}
                    weight = frontmatter.get('weight')
                    if weight is not None:
                        item.weight = weight
            except:
                pass

    def _nav_sort_key(self, item):
        return (getattr(item, 'weight', 9999), (item.title or '').lower())

    def on_page_context(self, context, page, config, nav, **kwargs):
        file_path = os.path.join(config.docs_dir, page.file.src_path)
        slug_parts = self._build_slug_path(file_path, config)

        # slug_url = '/'.join(slug_parts) + '/'
        # dest_path = os.path.join(*slug_parts, 'index.html')
        
        # Check if the source file is index.md
        if os.path.basename(file_path) == 'index.md':
            # For index.md, use the directory path without appending 'index'
            dest_path = os.path.join(*slug_parts, 'index.html')
        else:
            # For other files, keep the existing behavior
            dest_path = os.path.join(*slug_parts, 'index.html')
            slug_url = '/'.join(slug_parts) + '/'
            
        page.file.dest_path = dest_path
        page.file.abs_dest_path = os.path.join(config.site_dir, dest_path)

        return context

    def on_pre_page(self, page, config, files):
        file_path = os.path.join(config.docs_dir, page.file.src_path)
        slug_parts = self._build_slug_path(file_path, config)
        
        # slug_url = '/'.join(slug_parts) + '/'
        # For index.md, use directory path without appending 'index'
        if os.path.basename(file_path) == 'index.md':
            slug_url = '/'.join(slug_parts) + '/'
        else:
            slug_url = '/'.join(slug_parts) + '/'

        # override early enough for sitemap
        page.canonical_url = config.site_url.rstrip('/') + '/' + slug_url if config.site_url else '/' + slug_url
        return page

    def _build_slug_path(self, file_path, config):
        slugs = []
        folder = os.path.dirname(file_path)

        # Walk upward and collect .nav.yaml slugs
        while os.path.commonpath([folder, config.docs_dir]) == config.docs_dir and folder != config.docs_dir:
            folder_slug = None
            nav_file = os.path.join(folder, '.nav.yaml')
            if os.path.isfile(nav_file):
                try:
                    with open(nav_file, 'r') as f:
                        nav_meta = yaml.safe_load(f)
                        folder_slug = nav_meta.get('slug')
                except:
                    pass
            slugs.insert(0, folder_slug or os.path.basename(folder))
            folder = os.path.dirname(folder)

        # Add page slug from frontmatter
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            if lines and lines[0].strip() == '---':
                end = lines[1:].index('---\n') + 1 if '---\n' in lines[1:] else None
                frontmatter = yaml.safe_load(''.join(lines[1:end])) if end else {}
                page_slug = frontmatter.get('slug')
                if page_slug:
                    slugs.append(page_slug)
                    return slugs
        except:
            pass

        slugs.append(os.path.splitext(os.path.basename(file_path))[0])
        return slugs
