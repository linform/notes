# 我的学习笔记

使用 MkDocs Material 将 `docs/` 下的 Markdown 笔记发布为静态网站。

- 网站：<https://linform.github.io/notes/>
- 部署记录：<https://github.com/linform/notes/actions>
- 写作说明：[Markdown 使用手册](docs/Markdown使用说明.md)

## 首次安装（Windows）

安装 Git 和 Python 3.12，在项目根目录打开 PowerShell：

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
powershell -NoProfile -ExecutionPolicy Bypass -File .\start-preview.ps1
```

无需激活虚拟环境。预览地址以终端输出为准，默认通常是 `http://127.0.0.1:8000/notes/`。端口冲突时可使用 `-Address 127.0.0.1:8001`。

每个新克隆或工作树都需要创建自己的 `.venv`；它不受 Git 管理。启动脚本在环境缺失时会显示安装命令。

## 日常写作

1. 在 VS Code 中打开项目根目录。如果 VS Code 提示是否允许运行自动任务，了解下面的同步行为后再启用。
2. 在 `docs/` 中创建或编辑 `.md`，保存后检查本地预览。
3. 新文章加入 `mkdocs.yml` 的 `nav`，图片等资源放在 `docs/` 内，使用相对路径引用。
4. 在主工作目录的 `main` 分支使用自动同步。分离 HEAD 和功能分支只用于本地编辑或预览，脚本会拒绝自动提交和推送。
5. 推送完成后，到 Actions 查看部署结果。Git 推送成功不等于网站部署成功。

VS Code 的两个后台任务分别启动本地预览和自动同步；可以通过“任务：终止任务”或任务终端的 Ctrl+C 停止。未启用自动任务时，也可以通过“任务：运行任务”手工启动。

## 自动同步的范围与边界

```powershell
# 持续运行，每 60 秒检查一次
powershell -NoProfile -ExecutionPolicy Bypass -File .\auto-sync.ps1

# 立即执行一轮；成功退出码 0，失败或不适用退出码 1
powershell -NoProfile -ExecutionPolicy Bypass -File .\auto-sync.ps1 -Once
```

- 仅自动提交 `docs/` 和 `mkdocs.yml` 的新增、修改、删除。
- README、依赖、脚本、测试和工作流的修改需要手工提交。推送 main 会包含该分支上所有尚未推送的提交。
- 先检查 main 分支及 Git 操作状态；有合并、变基等操作或未解决冲突时跳过。
- 同一 Windows 登录会话中，同一仓库只允许运行一个同步进程（包括关联工作树）。重复启动会提示并退出；使用 `-Once` 前先停止已有同步任务。进程异常退出后可正常重新启动，无需删除锁文件。
- 本地提交后读取远端 main，仅允许正常快进推送，并核验远端确实收到目标提交。
- 网络失败时保留本地提交，后续重试；远端领先或分叉时提示人工处理，不自动拉取、合并、变基或强制推送。
- 仓库和网站公开，放入 `docs/` 的内容应适合公开发布。

## 验证与部署

```powershell
.\.venv\Scripts\python.exe -m pip check
.\.venv\Scripts\python.exe -m mkdocs build --strict
py -3.12 -m unittest discover -s tests -v
```

同步测试只创建临时本地 Git 仓库，不访问 GitHub。GitHub Actions 对 PR 和 main 执行严格构建与同步测试，只有 main 在两项检查通过后部署 Pages。首次使用仓库时，在 GitHub 的 Pages 设置中选择 GitHub Actions 作为发布来源。

## 常见问题

| 情况 | 处理 |
| --- | --- |
| 缺少 `.venv` 或依赖 | 按首次安装命令创建环境、安装依赖 |
| 当前是 detached HEAD 或功能分支 | 在此预览即可；将修改正常合并到主工作目录的 main 后再同步，不要强制切换覆盖未保存的工作 |
| Remote main has changes | 停止同步、检查 `git status`，手工获取并整合远端变化后重试 |
| Git 验证或网络失败 | 本地提交仍保留；恢复访问后重试 |
| 推送成功但网站未更新 | 查看 Actions 的构建、同步测试和部署状态 |
| 公式没有显示 | 检查 MathJax CDN 是否可访问；字体使用系统字体，不再请求 Google Fonts |

`docs/原神.md` 保留旧文章地址入口，`docs/test.md` 保留原测试页面，两者不出现在主导航中。

网站首页是文件选择界面，卡片在 `docs/index.md` 中维护。新增笔记后，在首页复制一个 `notes-file` 卡片并修改标题、描述和 Markdown 相对链接，同时按需加入 `mkdocs.yml` 的 `nav`。首页隐藏侧栏；文章继续使用左上角抽屉菜单和宽屏右侧目录，可从抽屉中的“首页”返回文件选择界面。

宽屏右侧目录用细线与正文分隔，可点击“收起目录”释放阅读空间，再通过右侧的“展开目录”恢复。选择保存在当前浏览器中，刷新或切换文章后沿用；窄屏保持主题原有布局。交互在 `docs/javascripts/toc-toggle.js` 中维护，浏览器禁止存储时仍可切换，但不会跨页面记忆。
