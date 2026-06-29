---
name: github-share-agent-skills
description: 使用 Git 和 GitHub 制作、上传、下载、更新、安装与复用开放 Agent Skills。用于用户需要安装或配置 Git、克隆和推送 GitHub 仓库、通过分支和 PR 共享 Skill、制作可被 Codex、Claude Code、TRAE 等工具使用的 SKILL.md、安装下载的 Skill，或排查 Git/GitHub/Skill 分发问题。
---

# GitHub 共享 Agent Skills

## 核心原则

1. 先确认 Git、认证方式、仓库权限和网络，再修改仓库。
2. 使用开放 Agent Skills 核心格式，只维护一份知识正文。
3. 按能力/业务领域拆 Skill，不按作者拆。
4. 先验证再提交，先同步远端再推送。
5. 公开仓库必须脱敏，不把 Token、密码或客户数据写入文件、命令和远程 URL。
6. 保留用户已有变更，不用破坏性 Git 命令解决普通冲突。

## 工作流选择

### Git 尚未安装或不可用

读取 [git-install-安装Git.md](references/git-install-安装Git.md)，使用官方渠道安装并运行：

```text
git --version
```

可运行 `scripts/check-git-检查Git.py` 检查 Git、身份、仓库和远程状态。

### 从 GitHub 下载或更新 Skill

读取 [github-workflow-GitHub共享流程.md](references/github-workflow-GitHub共享流程.md)：

- 首次下载使用 `git clone`；
- 已有仓库使用 `git pull --ff-only`；
- 不确定本地状态时先运行 `git status --short --branch`。

安装到 AI 工具时读取 [tool-application-AI工具套用.md](references/tool-application-AI工具套用.md)，或运行：

```text
python scripts/install-skill-安装Skill.py --source <skill目录> --tool codex
```

### 制作可共享 Skill

读取 [skill-authoring-共享Skill制作.md](references/skill-authoring-共享Skill制作.md)。

最低结构：

```text
skill-name/
├─ SKILL.md
├─ references/
└─ scripts/
```

仅在确有需要时创建 `references/`、`scripts/`、`assets/`。不要在单个 Skill 内增加 README、安装指南和变更日志。

完成后运行：

```text
python scripts/validate-skill-校验Skill.py <skill目录>
```

### 上传与协作

1. 查看状态和差异。
2. 拉取远端更新。
3. 创建功能分支。
4. 修改并验证。
5. 暂存明确文件。
6. 检查暂存差异。
7. 提交。
8. 推送分支。
9. 创建 PR。

不要默认直接向共享仓库 `main` 推送。

## 安全规则

- 优先使用 GitHub CLI 浏览器登录、Git Credential Manager 或 SSH。
- GitHub 不支持用账户密码进行 Git HTTPS 推送；使用安全认证方式。
- 不把 PAT 写入 `https://TOKEN@github.com/...`。
- 不提交 `.env`、凭证、客户 JSON、完整日志和企业专属映射。
- 推送被 secret scanning 阻止时，删除密钥并轮换，不盲目绕过保护。
- 删除、重写历史、强制推送前必须获得明确确认。

## Git 操作规则

- 搜索和读取后再修改。
- 使用 `git diff`、`git diff --cached` 和 `git status` 审核范围。
- 本地落后时先 `git fetch`，再选择合并或变基；不使用 `git reset --hard`。
- 推送被拒绝时检查 non-fast-forward、分支保护、认证和网络。
- 网络失败不等于认证失败；保留本地提交并报告具体错误。

## 来源

- Git 官方安装文档：`https://git-scm.com/install/`
- GitHub 克隆文档：`https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository`
- GitHub 推送文档：`https://docs.github.com/en/get-started/using-git/pushing-commits-to-a-remote-repository`
- GitHub 认证文档：`https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/about-authentication-to-github`
- Claude Code Skills：`https://code.claude.com/docs/en/slash-commands`
- TRAE Skills：`https://www.trae.ai/blog/trae_tutorial_0115`
