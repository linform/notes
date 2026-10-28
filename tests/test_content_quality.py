"""Content failures that must stop a normal build before publication."""
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from scripts.course_content import (
    anki_csv,
    bank_for,
    body,
    compose,
    expand_quizzes,
    exports,
    prepare,
    quiz_sources,
)
from scripts.site_quality import asset_size_errors, built_link_errors, discovery_errors
from scripts.new_course import scaffold_course


class ContentQualityTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix='notes-content-test-')
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)

    def test_navigation_and_home_require_discoverable_articles(self):
        nav = [{'首页': 'index.md'}, {'课程': ['course/index.md', {'第一章': 'course/a.md'}]}]
        pages = ['index.md', 'course/index.md', 'course/a.md', 'old.md']
        self.assertEqual(discovery_errors(pages, nav, '/old.md\n', {'index.md', 'course/index.md'}), [])
        errors = discovery_errors(pages + ['forgotten.md'], nav, '/old.md', {'index.md'})
        self.assertTrue(any('forgotten.md' in e for e in errors))
        self.assertTrue(any('Home page' in e and 'course/index.md' in e for e in errors))
        errors = discovery_errors(['index.md'], nav, '', {'index.md', 'course/index.md'})
        self.assertTrue(any('missing: course/a.md' in e for e in errors))

    def test_links_resolve_pages_prefix_unicode_attachments_and_anchors(self):
        (self.root / 'course').mkdir()
        (self.root / '资料.pdf').write_bytes(b'%PDF-fixture')
        (self.root / 'index.html').write_text(
            '<a href="/notes/course/#target">chapter</a>'
            '<a href="%E8%B5%84%E6%96%99.pdf">PDF</a>', encoding='utf-8')
        (self.root / 'course/index.html').write_text('<h1 id="target">ok</h1>')
        self.assertEqual(built_link_errors(self.root, '/notes/'), [])
        (self.root / 'index.html').write_text('<a href="course/#wrong">broken</a><img src="lost.png">')
        errors = built_link_errors(self.root, '/notes/')
        self.assertTrue(any('missing anchor' in e for e in errors))
        self.assertTrue(any('lost.png' in e for e in errors))
        self.assertTrue(any('Attachment has no reading link' in e for e in errors))

    def test_a_wrong_pages_prefix_and_escape_are_not_silently_accepted(self):
        (self.root / 'index.html').write_text('<a href="/course/">wrong</a><a href="../private.pdf">escape</a>')
        errors = built_link_errors(self.root, '/notes/')
        self.assertEqual(len(errors), 2)

    def test_duplicate_anchors_are_reported(self):
        (self.root / 'index.html').write_text('<h2 id="same">one</h2><span id="same"></span>')
        self.assertTrue(any('duplicate anchor: same' in e for e in built_link_errors(self.root)))

    def test_complete_edition_updates_from_canonical_source_without_rewriting_when_unchanged(self):
        course = self.root / 'docs/courses/solid-state'
        course.mkdir(parents=True)
        (course / 'course.json').write_text(json.dumps({
            'edition': {
                'output': '固体物理.md',
                'title': '固体物理完整阅读版',
                'description': '由分章笔记自动合并的课程完整阅读版，兼容原有链接。',
                'heading': '固体物理学习笔记',
                'download': 'solid-state.md',
            },
            'quiz': {
                'bank': 'review.md',
                'anki': 'solid-state-anki.csv',
                'deck': '固体物理',
            },
            'parts': [{'file': 'a.md', 'heading': '## One'}],
        }), encoding='utf-8')
        chapter = course / 'a.md'
        chapter.write_text(
            '# Page\n<!-- course:body -->\n## 1.1 Sub\n![fig](../../assets/fig.png)\nformula $(x)$\n<!-- /course:body -->\nExtra footer',
            encoding='utf-8',
        )
        (course / 'review.md').write_text(
            '<!-- question:q01 -->\n<span id="q01"></span>\n\n??? question "What is $E$?"\n    Energy **value** `k`\n<!-- /question -->\n',
            encoding='utf-8',
        )
        result = prepare(self.root)['固体物理.md']
        self.assertIn('## One\n\n### 1.1 Sub\n![fig](assets/fig.png)\nformula $(x)$', result)
        self.assertNotIn('Extra footer', result)
        target = self.root / 'docs/固体物理.md'
        timestamp = target.stat().st_mtime_ns
        self.assertEqual(prepare(self.root)['固体物理.md'], result)
        self.assertEqual(target.stat().st_mtime_ns, timestamp)
        chapter.write_text(chapter.read_text(encoding='utf-8').replace('$(x)$', '$(y)$'), encoding='utf-8')
        self.assertIn('$(y)$', prepare(self.root)['固体物理.md'])
        self.assertEqual(target.read_text(encoding='utf-8'), compose(self.root / 'docs')['固体物理.md'])

        banks = quiz_sources(self.root / 'docs')
        self.assertIsNotNone(bank_for('courses/solid-state/a.md', banks))
        self.assertIsNotNone(bank_for('固体物理.md', banks))
        self.assertIsNone(bank_for('courses/other/a.md', banks))

        files = exports(self.root / 'docs', 'https://example.com/notes/')
        self.assertIn('(https://example.com/notes/assets/fig.png)', files['solid-state.md'])
        self.assertIn('(https://example.com/notes/courses/solid-state/)', files['solid-state.md'])
        self.assertIn(r'What is \(E\)?', files['solid-state-anki.csv'])
        self.assertIn('Energy <b>value</b> <code>k</code>', files['solid-state-anki.csv'])

    def test_complete_edition_metadata_preserves_punctuation_and_line_breaks(self):
        course = self.root / 'docs/courses/quantum'
        course.mkdir(parents=True)
        metadata = {
            'title': '量子力学: "入门" # 第一讲\n第二行',
            'description': '说明: 含 # 号、"引号"和中文。\n---\nsearch: false',
        }
        (course / 'course.json').write_text(json.dumps({
            'edition': {'output': 'quantum.md', 'heading': '量子力学', **metadata},
            'parts': [],
        }), encoding='utf-8')
        text = compose(self.root / 'docs')['quantum.md']
        front = text.split('---\n', 2)[1]
        # Check the YAML-compatible JSON scalars even in the dependency-free sync job.
        scalars = {}
        for line in front.splitlines():
            key, _, value = line.partition(': ')
            if key in metadata:
                scalars[key] = json.loads(value)
        self.assertEqual(scalars, metadata)
        try:
            import yaml
        except ImportError:
            return
        self.assertEqual(yaml.safe_load(front), {**metadata, 'search': {'exclude': True}})

    def test_pre_build_accepts_generated_metadata_containing_dashes(self):
        try:
            import mkdocs
            import yaml
        except ImportError:
            self.skipTest('MkDocs and PyYAML are only installed in the build environment')
        from hooks import content_quality
        from mkdocs.config import load_config

        docs = self.root / 'docs'
        course = docs / 'courses/quantum'
        course.mkdir(parents=True)
        (course / 'course.json').write_text(json.dumps({
            'edition': {
                'output': 'quantum.md',
                'heading': '量子力学',
                'title': '量子力学: "入门" # 第一讲\n第二行',
                'description': '说明: 含 # 号、"引号"和中文。\n---\nsearch: false',
            },
            'parts': [],
        }), encoding='utf-8')
        (docs / 'index.md').write_text(
            '---\ntitle: 首页\ndescription: 测试课程入口\n---\n[课程](quantum.md)\n',
            encoding='utf-8',
        )
        config_path = self.root / 'mkdocs.yml'
        config_path.write_text(
            'site_name: Fixture\nnav:\n  - 首页: index.md\n  - 课程: quantum.md\n',
            encoding='utf-8',
        )
        config = load_config(config_file=str(config_path))
        with patch.object(content_quality, 'ROOT', self.root):
            content_quality.on_pre_build(config)
        self.assertTrue((docs / 'quantum.md').is_file())

    def test_missing_or_reversed_source_markers_cannot_lose_content_silently(self):
        for text in ('# no markers', '<!-- /course:body --><!-- course:body -->'):
            with self.subTest(text=text), self.assertRaises(ValueError):
                body(text)

    def test_quizzes_share_answers_and_reject_missing_duplicate_or_invalid_ids(self):
        review = '<!-- question:q01 -->??? question "Question"\n    Answer<!-- /question -->'
        self.assertIn('Answer', expand_quizzes('<!-- quiz:q01 -->', review))
        for directive in ('<!-- quiz:q99 -->', '<!-- quiz:q01, -->'):
            with self.subTest(directive=directive), self.assertRaises(ValueError):
                expand_quizzes(directive, review)
        with self.assertRaises(ValueError):
            expand_quizzes('<!-- quiz:q01 -->', review + review)
        with self.assertRaises(ValueError):
            anki_csv('<!-- question:q01 -->not a collapsible question<!-- /question -->', 'Deck', 'tag')

    def test_asset_size_limits_catch_oversized_files_and_totals(self):
        (self.root / 'small.bin').write_bytes(b'x' * 100)
        self.assertEqual(asset_size_errors(self.root, max_single_bytes=200, max_total_bytes=500), [])
        (self.root / 'huge.bin').write_bytes(b'x' * 300)
        errors = asset_size_errors(self.root, max_single_bytes=200, max_total_bytes=350)
        self.assertTrue(any('single-file limit' in e and 'huge.bin' in e for e in errors))
        self.assertTrue(any('total size limit' in e for e in errors))

    def test_new_course_scaffold_integrates_with_course_pipeline(self):
        info = scaffold_course(self.root, 'quantum', '量子力学')
        self.assertTrue((info['course_dir'] / 'course.json').is_file())
        self.assertTrue(info['nav_snippet'].startswith('      - 量子力学:'))
        editions = prepare(self.root)
        self.assertIn('量子力学.md', editions)
        self.assertNotIn('(intro.md)', editions['量子力学.md'])
        self.assertNotIn('(review.md)', editions['量子力学.md'])
        banks = quiz_sources(self.root / 'docs')
        self.assertIsNotNone(bank_for('courses/quantum/intro.md', banks))
        expanded = expand_quizzes((info['course_dir'] / 'intro.md').read_text(encoding='utf-8'), banks['courses/quantum/'])
        self.assertIn('核心假设', expanded)
        files = exports(self.root / 'docs', 'https://example.com/notes/')
        self.assertIn('quantum.md', files)
        self.assertIn('quantum-anki.csv', files)
        # Verify download links from both index (depth 2) and review (depth 3) resolve cleanly.
        site = self.root / 'site'
        for name, content in files.items():
            target = site / 'downloads' / name
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(content, encoding='utf-8')
        (site / 'courses/quantum/review').mkdir(parents=True, exist_ok=True)
        (site / 'courses/quantum/index.html').write_text(
            (info['course_dir'] / 'index.md').read_text(encoding='utf-8'), encoding='utf-8')
        (site / 'courses/quantum/review/index.html').write_text(
            (info['course_dir'] / 'review.md').read_text(encoding='utf-8'), encoding='utf-8')
        self.assertEqual(built_link_errors(site, '/notes/'), [])
        with self.assertRaises(FileExistsError):
            scaffold_course(self.root, 'quantum', '量子力学')
        with self.assertRaises(ValueError):
            scaffold_course(self.root, 'bad slug', '量子力学')


if __name__ == '__main__':
    unittest.main()
