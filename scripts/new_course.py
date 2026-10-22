"""Scaffold a new course directory under docs/courses/<slug>/ with standard templates."""
import argparse
import json
from pathlib import Path


def scaffold_course(root, slug, title, description=None, first_chapter_title='第一章　绪论'):
    slug = slug.strip().strip('/\\')
    if not slug or any(c in slug for c in ('/', '\\', ' ', ':')):
        raise ValueError(f'Invalid course slug: {slug!r}')
    if not title or not title.strip():
        raise ValueError('Course title must not be empty')
    title = title.strip()
    description = (description or f'按章节学习{title}：阅读路线、学习目标、推导小结与自测。').strip()

    docs = Path(root) / 'docs'
    course_dir = docs / 'courses' / slug
    if course_dir.exists():
        raise FileExistsError(f'Course directory already exists: {course_dir}')
    course_dir.mkdir(parents=True, exist_ok=False)

    plan = {
        'edition': {
            'output': f'{title}.md',
            'title': f'{title}完整阅读版',
            'description': f'由分章笔记自动合并的{title}完整阅读版。',
            'heading': f'{title}学习笔记',
            'download': f'{slug}.md',
        },
        'quiz': {
            'bank': 'review.md',
            'anki': f'{slug}-anki.csv',
            'deck': title,
        },
        'parts': [
            {'file': 'index.md'},
            {'file': 'intro.md', 'heading': f'## {first_chapter_title}'},
            {'file': 'review.md', 'heading': '## 复习速查与自测'},
        ],
    }
    (course_dir / 'course.json').write_text(
        json.dumps(plan, ensure_ascii=False, indent=2) + '\n',
        encoding='utf-8',
        newline='\n',
    )

    index_md = f"""---
title: {title} · 课程概览
description: {description}
status: 草稿
tags:
  - 课程概览
---

# {title}

<!-- Links to chapters stay outside course:body: the complete edition is saved in docs/. -->
- [{first_chapter_title}](intro.md)：核心概念、基本假设与主要推导。
- [复习速查与自测](review.md)：核心公式速查与闭卷自测题库。
- **连续阅读或保存**：[完整阅读版](../../{title}.md) · <a href="../../downloads/{slug}.md" download="{title}.md">下载合并后的 Markdown</a> · <a href="../../downloads/{slug}-anki.csv" download="{title}-Anki自测卡.csv">下载 Anki 记忆卡（CSV）</a>

<!-- course:body -->

## 课程简介

说明课程范围、主要参考资料与推荐阅读顺序。

<!-- /course:body -->
"""
    (course_dir / 'index.md').write_text(index_md, encoding='utf-8', newline='\n')

    intro_md = f"""---
title: {first_chapter_title}
description: {title}{first_chapter_title}的核心概念、公式推导与自测练习。
status: 草稿
tags:
  - 课程概览
---

# {first_chapter_title}

[课程概览](index.md) · [复习速查与自测](review.md)

## 学习目标

- 明确本章研究对象、基本假设与适用条件。
- 掌握核心公式的物理图像与量纲检验。

## 核心内容

<!-- course:body -->

### 1.1 基本概念

在此处编写正文与推导。

<!-- /course:body -->

## 本章小结

总结本章核心结论与适用边界。

## 自测与练习

<!-- quiz:q01 -->

## 下一步

[返回课程概览](index.md) · [下一单元：复习速查与自测](review.md)
"""
    (course_dir / 'intro.md').write_text(intro_md, encoding='utf-8', newline='\n')

    review_md = f"""---
title: {title} · 复习速查与自测
description: {title}关键概念对比、常见易错点与可展开答案的闭卷自测题库。
status: 草稿
tags:
  - 习题与自测
---

# {title} · 复习速查与自测

[返回课程概览](index.md) · <a href="../../../downloads/{slug}-anki.csv" download="{title}-Anki自测卡.csv">下载 Anki 记忆卡（CSV）</a>

<!-- course:body -->

## 闭卷自测 {{#self-test}}

<!-- question:q01 -->
<span id="q01"></span>

??? question "1. 本章的核心假设与适用条件是什么？"
    在此处填写标准答案与关键推导步骤。
<!-- /question -->

<!-- /course:body -->
"""
    (course_dir / 'review.md').write_text(review_md, encoding='utf-8', newline='\n')

    # Indented for placement under the existing `  - 课程笔记:` section.
    nav_snippet = f"""      - {title}:
          - courses/{slug}/index.md
          - {first_chapter_title}: courses/{slug}/intro.md
          - 复习速查与自测: courses/{slug}/review.md
          - 完整阅读版: {title}.md"""
    return {
        'course_dir': course_dir,
        'nav_snippet': nav_snippet,
        'home_link': f'courses/{slug}/index.md',
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('slug', help='URL-safe directory name under docs/courses/, e.g. quantum-mechanics')
    parser.add_argument('title', help='Display title of the course, e.g. 量子力学')
    parser.add_argument('--description', help='Short course overview description')
    parser.add_argument('--first-chapter', default='第一章　绪论', help='Heading of the initial chapter')
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    info = scaffold_course(args.root, args.slug, args.title, args.description, args.first_chapter)
    print(f"Created course scaffold at: {info['course_dir']}")
    print('\nAdd the following under `nav -> 课程笔记` in mkdocs.yml:\n')
    print(info['nav_snippet'])
    print(f"\nAnd link `{info['home_link']}` on docs/index.md if appropriate.")


if __name__ == '__main__':
    main()
