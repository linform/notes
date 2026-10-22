# 我的学习笔记

使用 MkDocs Material 将 `docs/` 下的 Markdown 笔记发布为静态网站。

- 网站：<https://linform.github.io/notes/>
- 部署记录：<https://github.com/linform/notes/actions>
- 写作说明：[Markdown 使用手册](docs/Markdown使用说明.md)
- 维护约定：[MAINTAINING.md](MAINTAINING.md) · [AGENTS.md](AGENTS.md)

## 首次安装（Windows）

安装 Git 和 Python 3.12，在项目根目录打开 PowerShell：

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
powershell -NoProfile -ExecutionPolicy Bypass -File .\start-preview.ps1
```

无需激活虚拟环境。预览地址以终端输出为准，默认通常是 `http://127.0.0.1:8000/notes/`。端口冲突时可使用 `-Address 127.0.0.1:8001`。每个新克隆或工作树都需要创建自己的 `.venv`；它不受 Git 管理。

## 日常写作与单次发布

1. 在 `docs/` 中创建或编辑 `.md`（新建课程可用 `.\.venv\Scripts\python.exe scripts/new_course.py <slug> "<课程名>"` 生成脚手架）。
2. 新文章填写 `title`、`description` 并加入 `mkdocs.yml` 的 `nav`；新栏目在首页添加入口；图片与附件放在 `docs/` 内并使用相对链接。
3. 完成编辑后，双击桌面“笔记单次同步”快捷方式，或在终端运行：

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\publish-notes.ps1

# 当前工作树缺少 .venv 时，可显式指定已有环境
powershell -NoProfile -ExecutionPolicy Bypass -File .\publish-notes.ps1 -PythonPath 'C:\path\to\python.exe'
```

4. 发布成功后，查看**本次 SHA 对应**的 [GitHub Actions](https://github.com/linform/notes/actions)，等待 `build`、`test-sync`、`deploy` 全部成功。

发布命令适用于 `main`、功能分支和 detached HEAD：自动刷新课程完整阅读版、执行严格构建校验、仅提交 `docs/` 和 `mkdocs.yml`、快进合并到 `main` 并核验远端 SHA。若修改了项目脚本、测试或配置说明，先检查差异并明确提交这些任务文件，再加 `-IncludeCommittedProjectChanges` 发布已审核的提交。

## 后台同步状态与底层脚本

Windows 登录自启和异常恢复任务默认关闭，VS Code 打开文件夹时也不会启动 Git 同步。如其他电脑曾安装过登录启动任务，可运行 `powershell -NoProfile -ExecutionPolicy Bypass -File .\install-auto-sync.ps1 -Uninstall` 移除。

底层脚本 `auto-sync.ps1 -Once` 仅供在 `main` 上按需执行一轮 Git 同步（不执行 MkDocs 构建）；日常发布请优先使用 `publish-notes.ps1`。

## 验证与测试

```powershell
.\.venv\Scripts\python.exe -m pip check
.\.venv\Scripts\python.exe -m mkdocs build --strict
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

## 常见问题

| 情况 | 处理 |
| --- | --- |
| 缺少 `.venv` 或依赖 | 按首次安装命令创建环境、安装依赖 |
| 当前是 detached HEAD 或功能分支 | 编辑完成后运行 `publish-notes.ps1`，无需原地切换到 main；失败时按提示整合差异后重试 |
| Remote main has changes | 停止同步、检查 `git status`，手工获取并整合远端变化后重试 |
| Git 验证或网络失败 | 本地提交仍保留；恢复访问后重试 |
| 推送成功但网站未更新 | 查看 Actions 的构建、同步测试和部署状态 |
| 公式没有显示 | 检查公式语法是否闭合；MathJax 与字体均已站内自托管，不依赖第三方 CDN 或 Google Fonts |

页面组织、完整阅读版生成、题库复用与内容检查细节见 [MAINTAINING.md](MAINTAINING.md)。
