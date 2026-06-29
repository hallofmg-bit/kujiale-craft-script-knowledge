# Git 安装与基础配置

## 1. 先检查

```bash
git --version
```

能输出版本时不要重复安装。

## 2. 官方安装

### Windows

推荐：

```powershell
winget install --id Git.Git -e --source winget
```

或从 Git 官方页面下载安装：

```text
https://git-scm.com/install/windows.html
```

### macOS

任选一种官方文档列出的方式：

```bash
xcode-select --install
```

```bash
brew install git
```

官方页面：

```text
https://git-scm.com/install/mac.html
```

### Linux

使用发行版包管理器，例如：

```bash
sudo apt-get update
sudo apt-get install git
```

```bash
sudo dnf install git
```

官方页面：

```text
https://git-scm.com/install/linux.html
```

## 3. 配置提交身份

全局配置：

```bash
git config --global user.name "YOUR_NAME"
git config --global user.email "YOUR_EMAIL"
```

只配置当前仓库：

```bash
git config user.name "YOUR_NAME"
git config user.email "YOUR_EMAIL"
```

不要替用户猜测真实邮箱。若使用 GitHub noreply 邮箱，先从 GitHub 账户设置确认正确地址。

## 4. GitHub 认证

支持 HTTPS 和 SSH。

推荐选择：

- GitHub CLI：`gh auth login`，通过浏览器授权；
- HTTPS + Git Credential Manager；
- SSH Key。

不要使用 GitHub 账户密码进行 Git HTTPS 推送，也不要把 Token 嵌入远程 URL。

## 5. 检查配置

```bash
git config --list --show-origin
git remote -v
git status --short --branch
```

远程 URL 只能展示仓库地址，不能包含 Token。
