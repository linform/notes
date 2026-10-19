# 笔记项目维护

## 内容来源与组织

固体物理的可编辑正文位于 `docs/courses/solid-state/`。`course.json` 只维护完整阅读版的拼接顺序和原有章标题；导航仍在 `mkdocs.yml` 中明确排列。

`<!-- course:body -->` 与结束标记之间是完整阅读版使用的正文。章节目标、小结和学习导航位于标记外；改动正文时保留这对标记。`docs/固体物理.md` 为自动合并结果，不直接编辑；运行 `python scripts/course_content.py` 可刷新，构建和发布也会自动准备。

自测题与答案只在 `review.md` 的 `question:qNN` 标记内维护。章节末的 `quiz:qNN,qNN` 标记由构建钩子展开，避免答案重复维护。缺少题号会使构建失败。

## 发布检查

`hooks/content_quality.py` 在构建前生成完整阅读版，并核验页面元数据、导航和首页栏目入口；构建后检查站内链接、锚点与附件阅读入口，生成 `site/downloads/solid-state.md`。它仅在预览／构建时运行，不建立常驻同步任务。

新文章加入 `mkdocs.yml`。主页链接到各栏目的首个导航页面，分章文章通过课程概览进入。兼容页和测试页须在 `not_in_nav` 明确声明，不能无意遗漏。

完整阅读版使用旧章标题和原有锚点；新例题稳定 ID 作为额外锚点保留，不能替换旧锚点。旧手册页保留兼容入口，不再复制整份正文。

参考 CS 自学指南的分目标阅读路线、《动手学深度学习》的章节小结和练习，以及 Material 官方的栏目概览导航：
- https://csdiy.wiki/使用指南/
- https://zh.d2l.ai/chapter_preliminaries/linear-algebra.html
- https://squidfunk.github.io/mkdocs-material/setup/setting-up-navigation/#section-index-pages

## 课件整理记录

整理方法参考已安装的 Presentations skill，并核查了 [Anthropic 官方 PPTX skill](https://github.com/anthropics/skills/blob/main/skills/pptx/SKILL.md) 的读取流程：逐页提取文本与公式、保留页面定位，再对照图片核查。技能仅辅助读取与校验，物理结论以本课程课件、推导和上列讲义为依据。
