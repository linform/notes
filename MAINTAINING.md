# 笔记项目维护

## 内容来源与组织

每门课程的可编辑正文位于 `docs/courses/<name>/`，由该目录下的 `course.json` 声明完整阅读版（`edition`）、自测题库与 Anki 导出（`quiz`）及章节拼接顺序（`parts`）；导航仍在 `mkdocs.yml` 中明确排列。

可以使用脚手架快速初始化一门新课程的目录、概览、首章模板与复习题库：

```powershell
.\.venv\Scripts\python.exe scripts/new_course.py <slug> "<课程名称>"
```

运行后按终端提示将输出的导航片段加入 `mkdocs.yml`，并在 `docs/index.md` 补充入口。

`<!-- course:body -->` 与结束标记之间是完整阅读版使用的正文。章节目标、小结和学习导航位于标记外；改动正文时保留这对标记。`docs/固体物理.md` 为自动合并结果，不直接编辑；运行 `python scripts/course_content.py` 可刷新，构建和发布也会自动准备。

自测题与答案只在课程题库（如 `review.md`）的 `question:qNN` 标记内维护。章节末的 `quiz:qNN,qNN` 标记由构建钩子展开，避免答案重复维护；题库同时可按 `course.json` 导出为 Anki 记忆卡 CSV。缺少题号或格式不符会使构建失败。

专业缩写词条在 `docs/includes/abbreviations.md` 中统一维护，由 `pymdownx.snippets` 自动附加到页面末尾并生成悬停提示；该目录已在 `mkdocs.yml` 的 `exclude_docs` 中排除，不作为独立文章发布。

## 发布与体积检查

`hooks/content_quality.py` 在构建前生成各课程完整阅读版，并核验页面元数据（`title`、`description`、在 `extra.status` 中登记的 `status` 及 `tags` 列表）、导航和首页栏目入口；构建后生成 `site/downloads/` 下的课程导出文件（如 `solid-state.md` 与 `solid-state-anki.csv`），并检查站内链接、锚点、附件阅读入口与文件体积上限（单文件默认不超过 20 MiB、构建产物总体积不超过 250 MiB）。它仅在预览／构建时运行，不建立常驻同步任务。

新文章加入 `mkdocs.yml`。主页链接到各栏目的首个导航页面，分章文章通过课程概览进入。兼容页和测试页须在 `not_in_nav` 明确声明，不能无意遗漏。

完整阅读版使用旧章标题和原有锚点；新例题稳定 ID 作为额外锚点保留，不能替换旧锚点。旧手册页保留兼容入口，不再复制整份正文。

参考 CS 自学指南的分目标阅读路线、《动手学深度学习》的章节小结和练习，以及 Material 官方的栏目概览导航：
- https://csdiy.wiki/使用指南/
- https://zh.d2l.ai/chapter_preliminaries/linear-algebra.html
- https://squidfunk.github.io/mkdocs-material/setup/setting-up-navigation/#section-index-pages

## 课件整理记录

整理方法参考已安装的 Presentations skill，并核查了 [Anthropic 官方 PPTX skill](https://github.com/anthropics/skills/blob/main/skills/pptx/SKILL.md) 的读取流程：逐页提取文本与公式、保留页面定位，再对照图片核查。技能仅辅助读取与校验，物理结论以本课程课件、推导和上列讲义为依据。
