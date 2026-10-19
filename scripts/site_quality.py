"""Offline discovery and built-link checks, shared by MkDocs and regression tests."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import fnmatch


def navigation_paths(nav):
    paths = set()
    if isinstance(nav, str):
        if not urlsplit(nav).scheme:
            paths.add(nav)
    elif isinstance(nav, list):
        for item in nav:
            paths.update(navigation_paths(item))
    elif isinstance(nav, dict):
        for item in nav.values():
            paths.update(navigation_paths(item))
    return paths


def discovery_errors(pages, nav, exclusions, landing_links):
    """Every article has navigation; every top-level section has a home entry."""
    errors = []
    paths = navigation_paths(nav)
    patterns = [p.strip().lstrip('/') for p in exclusions.splitlines() if p.strip()]
    for path in sorted(pages):
        if path not in paths and not any(fnmatch.fnmatchcase(path, p) for p in patterns):
            errors.append(f'Article has no navigation entry: {path}')
    for path in sorted(paths - set(pages)):
        errors.append(f'Navigation target is missing: {path}')
    for section in nav:
        first = next(iter(_ordered_paths(section)), None)
        if first and first not in landing_links:
            errors.append(f'Home page has no entry for navigation section: {first}')
    return errors


def _ordered_paths(value):
    if isinstance(value, str):
        if not urlsplit(value).scheme:
            yield value
    elif isinstance(value, (dict, list)):
        for item in value.values() if isinstance(value, dict) else value:
            yield from _ordered_paths(item)


class HtmlPage(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.ids, self.links = set(), []
        self.duplicate_ids = set()
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if values.get('id'):
            if values['id'] in self.ids:
                self.duplicate_ids.add(values['id'])
            self.ids.add(values['id'])
        for name in ('href', 'src'):
            if values.get(name):
                self.links.append(values[name])


def built_link_errors(directory, base='/'):
    root = Path(directory).resolve()
    pages = {p.resolve(): HtmlPage(p.read_text(encoding='utf-8')) for p in root.rglob('*.html')}
    errors = []
    referenced = set()
    for path, page in pages.items():
        for duplicate in sorted(page.duplicate_ids):
            errors.append(f'{path.relative_to(root)}: duplicate anchor: {duplicate}')
        for link in page.links:
            url = urlsplit(link)
            if url.scheme or url.netloc or not (url.path or url.fragment):
                continue
            relative = unquote(url.path)
            if relative.startswith('/'):
                # Only same-site references under the configured Pages prefix.
                if base != '/' and not relative.startswith(base):
                    errors.append(f'{path.relative_to(root)}: outside site prefix: {link}')
                    continue
                target = root / relative.removeprefix(base).lstrip('/')
            else:
                target = path.parent / relative if relative else path
            if target.is_dir():
                target /= 'index.html'
            target = target.resolve()
            referenced.add(target)
            if not target.is_relative_to(root) or not target.exists():
                errors.append(f'{path.relative_to(root)}: missing target: {link}')
            elif url.fragment and target in pages and unquote(url.fragment) not in pages[target].ids:
                errors.append(f'{path.relative_to(root)}: missing anchor: {link}')
    attachments = {'.pdf', '.epub', '.pptx', '.docx', '.zip', '.csv', '.xlsx'}
    for target in root.rglob('*'):
        if target.is_file() and target.suffix.lower() in attachments and target.resolve() not in referenced:
            errors.append(f'Attachment has no reading link: {target.relative_to(root)}')
    return errors
