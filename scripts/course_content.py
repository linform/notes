"""Build complete editions and study exports from the editable course chapters.

Every ``docs/courses/<name>/course.json`` lists chapter files in reading order.
Optional ``edition`` settings create a merged compatibility page in ``docs/``;
optional ``quiz`` settings name the shared question bank and its Anki export.
Only the standard library is required, including in the Windows sync tests.
"""
import argparse
import csv
import html
import io
import json
from pathlib import Path
import re
import textwrap

START = '<!-- course:body -->'
END = '<!-- /course:body -->'
QUESTION = re.compile(r'<!-- question:(q\d+) -->\s*(.*?)\s*<!-- /question -->', flags=re.S)
QUESTION_TITLE = re.compile(r'^\?\?\?\+?\s+question\s+"(.*)"\s*$')
MATH = re.compile(r'(\$\$.*?\$\$|\$[^$\n]+?\$)', flags=re.S)


def body(text):
    if text.count(START) != 1 or text.count(END) != 1 or text.index(START) >= text.index(END):
        raise ValueError('Each course source needs exactly one course:body pair')
    return text.split(START, 1)[1].split(END, 1)[0].strip()


def question_bank(review):
    pairs = QUESTION.findall(review)
    questions = dict(pairs)
    if len(questions) != len(pairs):
        raise ValueError('Duplicate quiz question IDs')
    return questions


def expand_quizzes(text, review):
    questions = question_bank(review)

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


def course_dirs(docs):
    return sorted(path.parent for path in (Path(docs) / 'courses').glob('*/course.json'))


def load_plan(course):
    return json.loads((Path(course) / 'course.json').read_text(encoding='utf-8'))


def shift_headings(text, delta=1):
    """Demote Markdown ATX headings outside fenced code blocks by ``delta`` levels."""
    if not delta:
        return text
    lines = []
    fence = None
    for line in text.splitlines():
        stripped = line.lstrip()
        match_fence = re.match(r'^(`{3,}|~{3,})', stripped)
        if match_fence:
            marker = match_fence[1]
            if fence is None:
                fence = marker
            elif stripped.startswith(fence):
                fence = None
            lines.append(line)
            continue
        if fence is None and re.match(r'^#{1,5}\s', line):
            lines.append('#' * delta + line)
        else:
            lines.append(line)
    return '\n'.join(lines)


def compose_edition(docs, course, plan):
    docs, course = Path(docs), Path(course)
    edition = plan['edition']
    if Path(edition['output']).name != edition['output']:
        raise ValueError(f'{course.name}: the complete edition must be saved directly in docs/')
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
        # Chapter assets are relative to courses/<name>; the edition stays at docs/.
        text = text.replace('(../../assets/', '(assets/')
        if 'heading' in entry:
            text = shift_headings(text, entry.get('shift_headings', 1))
        sections.append(entry.get('heading', '') + '\n\n' + text)
    # JSON strings are valid YAML scalars and preserve punctuation and line breaks.
    return (f'---\ntitle: {json.dumps(edition["title"], ensure_ascii=False)}\n'
            f'description: {json.dumps(edition["description"], ensure_ascii=False)}\n'
            'search:\n  exclude: true\n---\n\n'
            f'# {edition["heading"]}\n\n'
            f'> 完整阅读版由分章笔记自动合并。日常学习可从[课程概览](courses/{course.name}/index.md)进入；'
            '本页保留原有章节链接。\n\n' + '\n\n'.join(sections).strip() + '\n')


def compose(docs):
    """Return every complete edition as {path relative to docs: Markdown}."""
    result = {}
    for course in course_dirs(docs):
        plan = load_plan(course)
        if 'edition' not in plan:
            continue
        output = plan['edition']['output']
        if output in result:
            raise ValueError(f'Two courses write the same complete edition: {output}')
        result[output] = compose_edition(docs, course, plan)
    return result


def prepare(root):
    docs = Path(root) / 'docs'
    result = compose(docs)
    for output, text in result.items():
        target = docs / output
        if not target.exists() or target.read_text(encoding='utf-8') != text:
            target.write_text(text, encoding='utf-8', newline='\n')
    return result


def quiz_sources(docs):
    """Map course folders (prefix keys) and complete editions to their question banks."""
    banks = {}
    for course in course_dirs(docs):
        plan = load_plan(course)
        quiz = plan.get('quiz')
        if not quiz:
            continue
        review = (course / quiz['bank']).read_text(encoding='utf-8')
        question_bank(review)
        banks[f'courses/{course.name}/'] = review
        if 'edition' in plan:
            banks[plan['edition']['output']] = review
    return banks


def bank_for(src_uri, banks):
    for key, review in banks.items():
        if src_uri == key or (key.endswith('/') and src_uri.startswith(key)):
            return review
    return None


def _card_html(text):
    """Escape plain text for Anki, keeping TeX for Anki's built-in MathJax."""
    parts = []
    for index, part in enumerate(MATH.split(text)):
        if index % 2:
            if part.startswith('$$'):
                parts.append('\\[' + html.escape(part[2:-2].strip(), quote=False) + '\\]')
            else:
                parts.append('\\(' + html.escape(part[1:-1], quote=False) + '\\)')
        else:
            part = html.escape(part, quote=False)
            part = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', part)
            part = re.sub(r'`([^`\n]+)`', r'<code>\1</code>', part)
            parts.append(part.replace('\n', '<br>'))
    return ''.join(parts)


def flashcards(review):
    """Return (id, question, answer) for every question in the shared bank."""
    cards = []
    for key, block in question_bank(review).items():
        lines = block.splitlines()
        for index, line in enumerate(lines):
            title = QUESTION_TITLE.match(line.strip())
            if title:
                break
        else:
            raise ValueError(f'{key}: expected a line like ??? question "Question"')
        answer = textwrap.dedent('\n'.join(lines[index + 1:])).strip()
        if not answer:
            raise ValueError(f'{key}: the answer is empty')
        cards.append((key, title[1], answer))
    return cards


def anki_csv(review, deck, tag):
    """Anki 2.1.55+ text import: Front, Back, Tags with HTML and TeX enabled."""
    buffer = io.StringIO()
    buffer.write(f'#separator:Comma\n#html:true\n#notetype:Basic\n#deck:{deck}\n#tags column:3\n')
    writer = csv.writer(buffer, lineterminator='\n')
    for key, question, answer in flashcards(review):
        writer.writerow([_card_html(question), _card_html(answer), f'{tag} {tag}::{key}'])
    return buffer.getvalue()


def exports(docs, site_url):
    """Return downloadable files as {path relative to site/downloads: text}."""
    docs = Path(docs)
    result = {}

    def add(name, text):
        if name in result:
            raise ValueError(f'Two courses write the same download: {name}')
        result[name] = text

    for course in course_dirs(docs):
        plan = load_plan(course)
        edition = plan.get('edition') or {}
        if edition.get('download'):
            # A real Markdown download, with absolute links for readers saving it elsewhere.
            content = (docs / edition['output']).read_text(encoding='utf-8')
            content = content.replace('(assets/', f'({site_url}assets/')
            content = content.replace(f'(courses/{course.name}/index.md)', f'({site_url}courses/{course.name}/)')
            add(edition['download'], content)
        quiz = plan.get('quiz') or {}
        if quiz.get('anki'):
            review = (course / quiz['bank']).read_text(encoding='utf-8')
            add(quiz['anki'], anki_csv(review, quiz.get('deck', course.name), course.name))
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    if args.check:
        docs = args.root / 'docs'
        stale = [output for output, text in compose(docs).items()
                 if not (docs / output).exists() or (docs / output).read_text(encoding='utf-8') != text]
        if stale:
            parser.exit(1, f'Complete edition is stale: {", ".join(stale)}. Run scripts/course_content.py first.\n')
    else:
        prepare(args.root)
