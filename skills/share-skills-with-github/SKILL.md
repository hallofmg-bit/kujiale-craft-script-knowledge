---
name: share-skills-with-github
description: 使用 Git 和 GitHub 制作、上传、下载、更新、安装与复用开放 Agent Skills。用于安装或配置 Git、克隆和推送 GitHub 仓库、通过分支和 PR 共享 Skill、制作可被 Codex、Claude Code、TRAE 等工具使用的 SKILL.md、安装下载的 Skill，或排查 Git/GitHub/Skill 分发问题。
---

# 使用 GitHub 共享与复用 AI 技能

## 快速路线

| 任务 | 操作 |
| --- | --- |
| 检查 Git 环境 | 按“Git 环境检查”执行 |
| 下载仓库 | `git clone <仓库地址>` |
| 更新仓库 | 工作区干净时运行 `git pull --ff-only` |
| 制作 Skill | 创建 `<skill-name>/SKILL.md` |
| 校验 Skill | 按“Skill 校验”执行 |
| 安装 Skill | 按“在 AI 工具中安装”复制整个 Skill 目录 |
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
git --version
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

按共享人建目录，每人维护自己的 Skill；不要为每个小函数单独建 Skill。最小结构：

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

仓库提供根目录批量校验器时运行：

```bash
python validate-skills-校验技能.py
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

### 安装步骤

将包含 `SKILL.md` 的整个 Skill 目录复制到目标工具的 Skills 根目录。目标目录已存在时，先确认其中没有未同步修改，再决定是否覆盖。

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

## 内置自动化参考

以下源码已直接收录在 Skill 中，不再依赖 `scripts/` 文件夹。需要自动化时，让 AI 将对应代码写入临时 `.py` 文件并执行；任务完成后清理临时文件。

### Git 环境检查

```python
from __future__ import annotations

import shutil
import subprocess
from pathlib import Path


def run(*args: str) -> tuple[int, str]:
    completed = subprocess.run(
        args,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    return completed.returncode, completed.stdout.strip()


def main() -> int:
    git = shutil.which("git")
    if git is None:
        print("未找到 Git，请先按本 Skill 的安装说明安装。")
        return 1

    _, version = run(git, "--version")
    print(version)

    for key in ("user.name", "user.email"):
        code, value = run(git, "config", "--get", key)
        print(f"{key}: {value if code == 0 and value else '未配置'}")

    code, inside = run(git, "rev-parse", "--is-inside-work-tree")
    if code != 0 or inside != "true":
        print(f"当前目录不是 Git 仓库: {Path.cwd()}")
        return 0

    _, status = run(git, "status", "--short", "--branch")
    _, remotes = run(git, "remote", "-v")
    print(status)
    print(remotes if remotes else "未配置远程仓库")

    if "@" in remotes and "https://" in remotes:
        print("警告：检查 HTTPS 远程 URL，确保没有嵌入 Token。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

### Skill 安装

```python
from __future__ import annotations

import argparse
import shutil
from pathlib import Path


def default_target(tool: str, scope: str, project_dir: Path | None) -> Path:
    home = Path.home()
    if tool == "codex":
        if scope != "user":
            raise ValueError("Codex 默认安装器仅支持 user scope；项目级请使用 --target")
        return home / ".codex" / "skills"
    if tool == "claude":
        if scope == "user":
            return home / ".claude" / "skills"
        if project_dir is None:
            raise ValueError("Claude project scope 需要 --project-dir")
        return project_dir.resolve() / ".claude" / "skills"
    raise ValueError("该工具没有已确认的默认目录，请使用 --target")


def main() -> int:
    parser = argparse.ArgumentParser(description="安装开放 Agent Skill")
    parser.add_argument("--source", required=True, type=Path)
    parser.add_argument("--tool", choices=["codex", "claude", "generic"], default="generic")
    parser.add_argument("--scope", choices=["user", "project"], default="user")
    parser.add_argument("--project-dir", type=Path)
    parser.add_argument("--target", type=Path)
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    source = args.source.resolve()
    if not (source / "SKILL.md").exists():
        print(f"源目录缺少 SKILL.md: {source}")
        return 1

    try:
        target_root = args.target.resolve() if args.target else default_target(
            args.tool, args.scope, args.project_dir
        )
    except ValueError as exc:
        print(exc)
        return 1

    destination = target_root / source.name
    if destination.exists():
        if not args.force:
            print(f"目标已存在，未覆盖: {destination}")
            return 2
        shutil.rmtree(destination)

    target_root.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source, destination)
    print(f"已安装: {destination}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

### Skill 校验

```python
from __future__ import annotations

import argparse
import re
from pathlib import Path


NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        raise ValueError("SKILL.md 缺少 YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise ValueError("SKILL.md frontmatter 未闭合")

    result: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if not line.strip():
            continue
        if ":" not in line:
            raise ValueError(f"无效 frontmatter 行: {line}")
        key, value = line.split(":", 1)
        result[key.strip()] = value.strip().strip("\"'")
    return result


def validate(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        return ["缺少 SKILL.md"]

    text = skill_md.read_text(encoding="utf-8")
    try:
        frontmatter = parse_frontmatter(text)
    except ValueError as exc:
        return [str(exc)]

    name = frontmatter.get("name", "")
    description = frontmatter.get("description", "")
    if not NAME_PATTERN.fullmatch(name):
        errors.append("name 必须使用小写英文、数字和连字符")
    if name != skill_dir.name:
        errors.append("frontmatter name 必须与目录名一致")
    if not description:
        errors.append("缺少 description")
    pending_marker = "TO" + "DO"
    if pending_marker in text:
        errors.append(f"SKILL.md 仍包含 {pending_marker}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="校验开放 Agent Skill")
    parser.add_argument("skill_dir", type=Path)
    args = parser.parse_args()

    skill_dir = args.skill_dir.resolve()
    errors = validate(skill_dir)
    if errors:
        print("Skill 校验失败：")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Skill 校验通过: {skill_dir.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```
