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
from scripts.course_content import expand_quizzes, prepare
from scripts.site_quality import discovery_errors, built_link_errors

log = logging.getLogger('mkdocs.content-quality')


def on_pre_build(config):
    try:
        prepare(ROOT)
    except (ValueError, OSError) as error:
        raise PluginError(f'Course preparation failed: {error}') from error
    raw = yaml.safe_load(Path(config.config_file_path).read_text(encoding='utf-8'))
    docs = Path(config.docs_dir)
    pages = {p.relative_to(docs).as_posix(): p for p in docs.rglob('*.md')}
    home = (docs / 'index.md').read_text(encoding='utf-8')
    home_links = {'index.md'} | set(re.findall(r'\]\(([^)#]+)(?:#[^)]*)?\)', home))
    errors = discovery_errors(pages, raw['nav'], raw.get('not_in_nav', ''), home_links)
    for name, path in pages.items():
        text = path.read_text(encoding='utf-8')
        front = text.split('---', 2)
        try:
            meta = yaml.safe_load(front[1]) if len(front) == 3 and text.startswith('---\n') else {}
        except yaml.YAMLError as error:
            errors.append(f'{name}: invalid metadata: {error}')
            continue
        if not isinstance(meta, dict):
            meta = {}
        for key in ('title', 'description'):
            if not isinstance(meta.get(key), str) or not meta[key].strip():
                errors.append(f'{name}: missing {key} metadata')
    if errors:
        raise PluginError('Content checks failed:\n' + '\n'.join(errors))
    log.info('Checked navigation, home entries and metadata for %d pages.', len(pages))


def on_page_markdown(markdown, page, config, files):
    review = (Path(config.docs_dir) / 'courses/solid-state/review.md').read_text(encoding='utf-8')
    try:
        return expand_quizzes(markdown, review)
    except ValueError as error:
        raise PluginError(f'{page.file.src_uri}: {error}') from error


def on_post_build(config):
    # A real Markdown download, with absolute image links for readers saving it elsewhere.
    target = Path(config.site_dir) / 'downloads/solid-state.md'
    target.parent.mkdir(parents=True, exist_ok=True)
    content = (Path(config.docs_dir) / '固体物理.md').read_text(encoding='utf-8')
    content = content.replace('(assets/', f'({config.site_url}assets/')
    content = content.replace('(courses/solid-state/index.md)', f'({config.site_url}courses/solid-state/')
    target.write_text(content, encoding='utf-8')
    errors = built_link_errors(config.site_dir, urlsplit(config.site_url).path)
    if errors:
        raise PluginError('Built-site link checks failed:\n' + '\n'.join(errors))
    log.info('Checked built links and anchors; complete Markdown download is ready.')
