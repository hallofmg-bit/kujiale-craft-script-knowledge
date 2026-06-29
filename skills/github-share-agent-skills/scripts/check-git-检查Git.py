#!/usr/bin/env python3
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
        print("未找到 Git。请读取 references/git-install-安装Git.md。")
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
