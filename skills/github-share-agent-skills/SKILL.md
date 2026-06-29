---
name: github-share-agent-skills
description: 使用 Git 和 GitHub 制作、上传、下载、更新、安装与复用开放 Agent Skills。用于安装或配置 Git、克隆和推送 GitHub 仓库、通过分支和 PR 共享 Skill、制作可被 Codex、Claude Code、TRAE 等工具使用的 SKILL.md、安装下载的 Skill，或排查 Git/GitHub/Skill 分发问题。
---

# GitHub 共享 Agent Skills

## 快速路线

| 任务 | 操作 |
| --- | --- |
| 检查 Git 环境 | 运行 `scripts/check-git-检查Git.py` |
| 下载仓库 | `git clone <仓库地址>` |
| 更新仓库 | 工作区干净时运行 `git pull --ff-only` |
| 制作 Skill | 创建 `<skill-name>/SKILL.md` |
| 校验 Skill | 运行 `scripts/validate-skill-校验Skill.py <目录>` |
| 安装 Skill | 运行 `scripts/install-skill-安装Skill.py` |
| 上传共享 | 分支、提交、推送、创建 Pull Request |

## Git 安装与配置

先检查：

```bash
git --version
```

未安装时使用官方渠道：

```powershell
# Windows
winget install --id Git.Git -e --source winget
```

```bash
# macOS
xcode-select --install
# 或 brew install git

# Debian/Ubuntu
sudo apt-get update
sudo apt-get install git

# Fedora
sudo dnf install git
```

官方入口：`https://git-scm.com/install/`

配置身份：

```bash
git config --global user.name "YOUR_NAME"
git config --global user.email "YOUR_EMAIL"
```

不要替用户猜邮箱。GitHub HTTPS 推送不能使用账户密码，选择 GitHub CLI 浏览器登录、Git Credential Manager 或 SSH；禁止把 Token 写进远程 URL。

检查当前环境：

```bash
python scripts/check-git-检查Git.py
git config --list --show-origin
git remote -v
git status --short --branch
```

## GitHub 下载、更新与上传

首次下载：

```bash
git clone https://github.com/OWNER/REPO.git
cd REPO
```

已有仓库更新：

```bash
git status --short --branch
git pull --ff-only
```

工作区不干净时先理解本地改动，不直接拉取或覆盖。

共享修改：

```bash
git switch -c skill/short-topic
git status --short
git diff
python validate-skills-校验技能.py
git add <明确文件>
git diff --cached --check
git diff --cached
git commit -m "Update shared skill for <topic>"
git push -u origin skill/short-topic
```

随后在 GitHub 创建 Pull Request。共享仓库后续改动优先走分支和 PR，不默认直接推送 `main`。

空仓库首次上传：

```bash
git add --all
git commit -m "Initialize shared agent skills"
git push -u origin main
```

## 制作可共享 Skill

按稳定能力或业务领域拆分，不按作者拆分，也不要为每个小函数单独建 Skill。最小结构：

```text
skill-name/
└─ SKILL.md
```

只有确有需要时才增加：

```text
scripts/     # 可重复执行的确定性程序
references/  # 很长且仅特定场景需要的资料
assets/      # 输出模板或资源
```

不要在单个 Skill 内增加 README、安装指南、快速参考和变更日志。功能文档较短时直接合入 `SKILL.md`，避免一个流程需要跳转多个文件。

`SKILL.md` 模板：

```markdown
---
name: example-skill
description: 说明能力、触发场景、常见术语和错误关键词。
---

# 标题

## 核心流程

1. ...

## 已验证案例

...
```

规则：

- 目录名与 frontmatter `name` 一致，只用小写英文、数字和连字符。
- frontmatter 仅保留 `name` 和 `description`。
- `description` 同时说明“做什么”和“何时触发”。
- `SKILL.md` 保留决策流程、操作步骤和常用案例。
- 只有资料很长或很少使用时才拆进 `references/`。
- 成功经验写明入口、依赖、完整脱敏内容、正反验证、失败原因和限制。
- 推断与待验证内容不得标记为成功案例。

校验：

```bash
python scripts/validate-skill-校验Skill.py path/to/skill
```

## 在 AI 工具中安装

### Codex

```text
~/.codex/skills/<skill-name>/SKILL.md
```

可用 `$skill-name` 显式调用。

### Claude Code

```text
~/.claude/skills/<skill-name>/SKILL.md
.claude/skills/<skill-name>/SKILL.md
```

可用 `/skill-name` 显式调用，也可由 `description` 自动触发。

### TRAE

```text
Settings -> Rule & Skills -> Skills -> Create
```

导入包含 `SKILL.md` 的整个目录。不要把完整 Skill 改写成长驻 Rules。

### 安装脚本

```bash
python scripts/install-skill-安装Skill.py \
  --source <skill目录> \
  --tool codex
```

Claude Code 使用 `--tool claude`；其他工具可用 `--target <Skills根目录>`。

更新时先在知识仓库运行 `git pull --ff-only`，再重新安装整个 Skill 目录。覆盖已有目录前确认其中没有未同步修改。

## 常见错误

### non-fast-forward

远端有本地没有的提交。先运行：

```bash
git fetch origin
git status --short --branch
```

再按团队策略合并或变基，不直接强推。

### Authentication failed

检查仓库写权限、HTTPS 凭据、SSH Key 和组织 SSO 授权。

### Failed to connect、timeout 或 connection reset

这是网络问题，不等于认证失败。保留本地提交，检查代理、防火墙、DNS 和 GitHub 服务状态后重试。

### Push protection

提交包含疑似密钥。删除敏感内容、清理相关提交并轮换密钥，不绕过保护。

## 安全边界

- 不提交 `.env`、Token、密码、客户 JSON、完整日志和企业专属映射。
- 不在 URL、命令或文档中保存 PAT。
- 使用 `git status`、`git diff` 和 `git diff --cached` 审核范围。
- 不用 `git reset --hard`、强制推送或历史重写处理普通冲突。
- 删除、重写历史和强制推送前必须获得明确确认。
- 网络失败时保留本地提交并报告原始错误。

## 官方来源

- Git 安装：`https://git-scm.com/install/`
- GitHub 克隆：`https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository`
- GitHub 推送：`https://docs.github.com/en/get-started/using-git/pushing-commits-to-a-remote-repository`
- GitHub 认证：`https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/about-authentication-to-github`
- Claude Code Skills：`https://code.claude.com/docs/en/slash-commands`
- TRAE Skills：`https://www.trae.ai/blog/trae_tutorial_0115`
