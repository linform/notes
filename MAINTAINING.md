# 笔记项目维护

## 内容来源与组织

每门课程的可编辑正文位于 `docs/courses/<name>/`，由该目录下的 `course.json` 声明完整阅读版（`edition`）、自测题库与 Anki 导出（`quiz`）及章节拼接顺序（`parts`）；导航仍在 `mkdocs.yml` 中明确排列。

可以使用脚手架快速初始化一门新课程的目录、概览、首章模板与复习题库：

```powershell
.\.venv\Scripts\python.exe scripts/new_course.py <slug> "<课程名称>"
```

运行后按终端提示将输出的导航片段加入 `mkdocs.yml` 的 `课程笔记` 下，并在 `docs/index.md` 补充入口。

`<!-- course:body -->` 与结束标记之间是完整阅读版使用的正文。章节目标、小结和指向分章页面的学习导航位于标记外（避免合并到 `docs/<课程>.md` 后相对路径失效）；改动正文时保留这对标记。`docs/固体物理.md` 为自动合并结果，保留在版本控制中以兼容旧网址、章节锚点、GitHub 仓库直接预览以及不经过构建的 `auto-sync.ps1 -Once`；不要直接编辑该生成文件，运行 `python scripts/course_content.py` 可刷新，构建和发布也会自动准备。

自测题与答案只在课程题库（如 `review.md`）的 `question:qNN` 标记内维护。章节末的 `quiz:qNN,qNN` 标记由构建钩子展开，避免答案重复维护；题库同时可按 `course.json` 导出为 Anki 记忆卡 CSV。缺少题号或格式不符会使构建失败。

专业缩写词条在 `docs/includes/abbreviations.md` 中统一维护，由 `pymdownx.snippets` 自动附加到页面末尾并生成悬停提示；该目录已在 `mkdocs.yml` 的 `exclude_docs` 中排除，不作为独立文章发布。

## 发布与体积检查

`hooks/content_quality.py` 在构建前生成各课程完整阅读版，并核验页面元数据（`title`、`description`、在 `extra.status` 中登记的 `status` 及 `tags` 列表）、导航和首页栏目入口；构建后生成 `site/downloads/` 下的课程导出文件（如 `solid-state.md` 与 `solid-state-anki.csv`），并检查站内链接、锚点、附件阅读入口与文件体积上限（单文件默认不超过 20 MiB、构建产物总体积不超过 250 MiB）。它仅在预览／构建时运行，不建立常驻同步任务。

新文章加入 `mkdocs.yml`。主页链接到各栏目的首个导航页面，分章文章通过课程概览进入。兼容页（`docs/原神.md`，保留旧手册地址入口）和内部排版测试页（`docs/test.md`）须在 `not_in_nav` 明确声明并设置 `search.exclude: true`，不出现在主导航或公开指南链接中。

完整阅读版使用旧章标题和原有锚点；新例题稳定 ID 作为额外锚点保留，不能替换旧锚点。旧手册页保留兼容入口，不再复制整份正文。

## 前端交互与依赖基线

- **右侧目录折叠**：宽屏右侧目录用细线与正文分隔，可通过 `docs/javascripts/toc-toggle.js` 提供的“收起／展开目录”按钮切换并跨页面记忆状态（窄屏保持主题默认抽屉布局）。
- **MathJax 自托管与即时导航**：公式渲染使用 `docs/javascripts/vendor/mathjax/` 下自托管的 MathJax 3.2.2（含 CHTML/SVG 渲染器与 SRE 无障碍语音规则，不依赖第三方 CDN），由 `docs/javascripts/mathjax.js` 配合 Material 的 `navigation.instant` 在切换文章时清理 CHTML 样式缓存并串行重排，生命周期回归测试位于 `tests/test_mathjax_lifecycle.js`。
- **框架版本约束**：MkDocs 保持在 `1.6.x`（MkDocs 2.x 移除了 Material 依赖的插件与主题系统）；迁移至 Zensical 前须先确认 `tags`、`git-revision-date-localized` 及构建钩子 `hooks/content_quality.py` 的等价替代方案。

参考 CS 自学指南的分目标阅读路线、《动手学深度学习》的章节小结和练习，以及 Material 官方的栏目概览导航：
- https://csdiy.wiki/使用指南/
- https://zh.d2l.ai/chapter_preliminaries/linear-algebra.html
- https://squidfunk.github.io/mkdocs-material/setup/setting-up-navigation/#section-index-pages

## 课件整理记录

整理方法参考已安装的 Presentations skill，并核查了 [Anthropic 官方 PPTX skill](https://github.com/anthropics/skills/blob/main/skills/pptx/SKILL.md) 的读取流程：逐页提取文本与公式、保留页面定位，再对照图片核查。技能仅辅助读取与校验，物理结论以本课程课件、推导和上列讲义为依据。
