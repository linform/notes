"""Content consistency is enforced by every preview, strict build and deployment."""
import logging
from pathlib import Path
import re
import sys
from urllib.parse import urlsplit

from mkdocs.exceptions import PluginError
import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from scripts.course_content import bank_for, expand_quizzes, exports, prepare, quiz_sources
from scripts.site_quality import discovery_errors, built_link_errors

log = logging.getLogger('mkdocs.content-quality')
_banks = {}


class _ConfigLoader(yaml.SafeLoader):
    """Read mkdocs.yml as data; Python tags such as custom fence formatters stay unevaluated."""


_ConfigLoader.add_multi_constructor('', lambda loader, suffix, node: None)


def on_pre_build(config):
    docs = Path(config.docs_dir)
    try:
        prepare(ROOT)
        _banks.clear()
        _banks.update(quiz_sources(docs))
    except (ValueError, OSError, KeyError) as error:
        raise PluginError(f'Course preparation failed: {error}') from error
    raw = yaml.load(Path(config.config_file_path).read_text(encoding='utf-8'), Loader=_ConfigLoader)
    excluded = config.exclude_docs
    pages = {}
    for path in docs.rglob('*.md'):
        name = path.relative_to(docs).as_posix()
        # Snippet sources such as the glossary are excluded from the site, not articles.
        if not (excluded and excluded.match_file(name)):
            pages[name] = path
    home = (docs / 'index.md').read_text(encoding='utf-8')
    home_links = {'index.md'} | set(re.findall(r'\]\(([^)#]+)(?:#[^)]*)?\)', home))
    errors = discovery_errors(pages, raw['nav'], raw.get('not_in_nav', ''), home_links)
    statuses = config['extra'].get('status') or {}
    for name, path in pages.items():
        text = path.read_text(encoding='utf-8')
        front = re.match(r'\A---\n(.*?)\n---(?:\n|\Z)', text, flags=re.S)
        try:
            meta = yaml.safe_load(front[1]) if front else {}
        except yaml.YAMLError as error:
            errors.append(f'{name}: invalid metadata: {error}')
            continue
        if not isinstance(meta, dict):
            meta = {}
        for key in ('title', 'description'):
            if not isinstance(meta.get(key), str) or not meta[key].strip():
                errors.append(f'{name}: missing {key} metadata')
        if 'status' in meta and meta['status'] not in statuses:
            errors.append(f'{name}: unknown status {meta["status"]!r}; use one defined in extra.status')
        if 'tags' in meta and not (isinstance(meta['tags'], list) and all(isinstance(t, str) for t in meta['tags'])):
            errors.append(f'{name}: tags must be a list of names')
    if errors:
        raise PluginError('Content checks failed:\n' + '\n'.join(errors))
    log.info('Checked navigation, home entries and metadata for %d pages.', len(pages))


def on_page_markdown(markdown, page, config, files):
    if '<!-- quiz:' not in markdown:
        return markdown
    review = bank_for(page.file.src_uri, _banks)
    if review is None:
        raise PluginError(f'{page.file.src_uri}: quiz directives need a course with a question bank')
    try:
        return expand_quizzes(markdown, review)
    except ValueError as error:
        raise PluginError(f'{page.file.src_uri}: {error}') from error


def on_post_build(config):
    downloads = Path(config.site_dir) / 'downloads'
    try:
        files = exports(config.docs_dir, config.site_url)
    except (ValueError, OSError, KeyError) as error:
        raise PluginError(f'Download preparation failed: {error}') from error
    for name, content in files.items():
        target = downloads / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding='utf-8')
    errors = built_link_errors(config.site_dir, urlsplit(config.site_url).path)
    if errors:
        raise PluginError('Built-site link checks failed:\n' + '\n'.join(errors))
    log.info('Checked built links and anchors; %d course downloads are ready.', len(files))
