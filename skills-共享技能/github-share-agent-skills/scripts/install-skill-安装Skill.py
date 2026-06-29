#!/usr/bin/env python3
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
    parser.add_argument("--source", required=True, type=Path, help="包含 SKILL.md 的 Skill 目录")
    parser.add_argument("--tool", choices=["codex", "claude", "generic"], default="generic")
    parser.add_argument("--scope", choices=["user", "project"], default="user")
    parser.add_argument("--project-dir", type=Path)
    parser.add_argument("--target", type=Path, help="自定义 Skills 根目录")
    parser.add_argument("--force", action="store_true", help="覆盖已存在的同名 Skill")
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
