"""Build the compatibility edition from the editable course chapters.

Only the standard library is required, including in the Windows sync tests.
"""
import argparse
import json
from pathlib import Path
import re

START = '<!-- course:body -->'
END = '<!-- /course:body -->'


def body(text):
    if text.count(START) != 1 or text.count(END) != 1 or text.index(START) >= text.index(END):
        raise ValueError('Each course source needs exactly one course:body pair')
    return text.split(START, 1)[1].split(END, 1)[0].strip()


def expand_quizzes(text, review):
    pairs = re.findall(r'<!-- question:(q\d+) -->\s*(.*?)\s*<!-- /question -->', review, flags=re.S)
    questions = dict(pairs)
    if len(questions) != len(pairs):
        raise ValueError('Duplicate quiz question IDs')
    def replace(match):
        ids = match[1].split(',')
        missing = set(ids) - questions.keys()
        if missing:
            raise ValueError(f'Unknown quiz questions: {sorted(missing)}')
        return '\n\n'.join(questions[key] for key in ids)
    result = re.sub(r'<!-- quiz:(q\d+(?:,q\d+)*) -->', replace, text)
    if '<!-- quiz:' in result:
        raise ValueError('Invalid quiz directive')
    return result


def compose(docs):
    docs = Path(docs)
    course = docs / 'courses/solid-state'
    plan = json.loads((course / 'course.json').read_text(encoding='utf-8'))
    sections = []
    seen = set()
    for entry in plan['parts']:
        if entry['file'] in seen:
            raise ValueError(f'Duplicate course source: {entry["file"]}')
        seen.add(entry['file'])
        try:
            text = body((course / entry['file']).read_text(encoding='utf-8'))
        except ValueError as error:
            raise ValueError(f'{entry["file"]}: {error}') from error
        # Chapter assets are relative to courses/solid-state; compatibility stays at docs/.
        text = text.replace('(../../assets/', '(assets/')
        sections.append(entry.get('heading', '') + '\n\n' + text)
    return ('---\ntitle: 固体物理完整阅读版\n'
            'description: 由分章笔记自动合并的课程完整阅读版，兼容原有链接。\n'
            'search:\n  exclude: true\n---\n\n'
            '# 固体物理学习笔记\n\n'
            '> 完整阅读版由分章笔记自动合并。日常学习可从[课程概览](courses/solid-state/index.md)进入；'
            '本页保留原有章节链接。\n\n' + '\n\n'.join(sections).strip() + '\n')


def prepare(root):
    root = Path(root)
    result = compose(root / 'docs')
    target = root / 'docs/固体物理.md'
    if not target.exists() or target.read_text(encoding='utf-8') != result:
        target.write_text(result, encoding='utf-8', newline='\n')
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    if args.check:
        actual = (args.root / 'docs/固体物理.md').read_text(encoding='utf-8')
        if actual != compose(args.root / 'docs'):
            parser.exit(1, 'Complete edition is stale. Run scripts/course_content.py first.\n')
    else:
        prepare(args.root)
