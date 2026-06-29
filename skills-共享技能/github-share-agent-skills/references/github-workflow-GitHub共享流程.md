# GitHub 上传、下载与协作

## 下载仓库

```bash
git clone https://github.com/OWNER/REPO.git
cd REPO
```

已有仓库更新：

```bash
git status --short --branch
git pull --ff-only
```

工作区不干净时不要直接 pull。先理解本地改动，再提交、暂存或与用户确认。

## 新增或修改 Skill

```bash
git switch -c skill/short-topic
```

修改后：

```bash
git status --short
git diff
python scripts/validate-skill-校验Skill.py path/to/skill
```

暂存并复核：

```bash
git add path/to/skill
git diff --cached --check
git diff --cached
```

提交并推送：

```bash
git commit -m "Add shared skill for <topic>"
git push -u origin skill/short-topic
```

然后通过 GitHub 创建 Pull Request。

## 首次上传空仓库

```bash
git clone https://github.com/OWNER/REPO.git
cd REPO
```

添加文件后：

```bash
git add --all
git commit -m "Initialize shared agent skills"
git push -u origin main
```

共享仓库后续改动优先走分支和 PR。

## 常见错误

### non-fast-forward

远端包含本地没有的提交。先：

```bash
git fetch origin
git status --short --branch
```

再根据团队策略合并或变基。不要直接强推。

### Authentication failed

检查：

- 是否对仓库有写权限；
- HTTPS 凭据是否有效；
- SSH Key 是否已添加；
- 组织 SSO 是否需要授权。

### Failed to connect / timeout

这是网络问题，不等于认证失败。保留本地提交，检查代理、防火墙、DNS 和 GitHub 服务状态后重试。

### Push protection

说明提交包含疑似密钥。删除敏感内容、清理相关提交并轮换密钥，不要默认绕过保护。

## 下载单个 Skill

最稳妥方式是克隆仓库后复制目标 Skill 目录。需要持续更新时保留克隆仓库并定期 `git pull --ff-only`。
