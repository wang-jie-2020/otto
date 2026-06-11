#!/usr/bin/env python3
"""Link local skills into .agents/skills and .claude/skills.

- Source: ./skills/<skill-name>
- Targets: ./.agents/skills/<skill-name>, ./.claude/skills/<skill-name>

On Windows this creates directory junctions (mklink /J), which usually work
without administrator privileges.
"""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE_SKILLS_DIR = ROOT / "skills"
TARGET_SKILLS_DIRS = (
    ROOT / ".agents" / "skills",
    ROOT / ".claude" / "skills",
)


def lexists(path: Path) -> bool:
    return os.path.lexists(path)


def resolves_to(path: Path, target: Path) -> bool:
    try:
        return path.resolve(strict=False) == target.resolve(strict=False)
    except OSError:
        return False


def create_dir_link(link_path: Path, target_path: Path) -> None:
    if os.name == "nt":
        # Directory junction: works on Windows without admin in most setups.
        result = subprocess.run(
            ["cmd", "/c", "mklink", "/J", str(link_path), str(target_path)],
            capture_output=True,
            text=True,
            check=False,
        )
        if result.returncode != 0:
            details = (result.stderr or result.stdout or "mklink failed").strip()
            raise RuntimeError(details)
        return

    link_path.symlink_to(target_path, target_is_directory=True)


def main() -> int:
    if not SOURCE_SKILLS_DIR.is_dir():
        print(f"[error] skills source directory not found: {SOURCE_SKILLS_DIR}")
        return 1

    for target_dir in TARGET_SKILLS_DIRS:
        target_dir.mkdir(parents=True, exist_ok=True)

    skill_dirs = sorted([p for p in SOURCE_SKILLS_DIR.iterdir() if p.is_dir()])
    if not skill_dirs:
        print(f"[warn] no skill directory found under {SOURCE_SKILLS_DIR}")
        return 0

    created = 0
    unchanged = 0
    conflicts = 0

    for skill_dir in skill_dirs:
        for target_root in TARGET_SKILLS_DIRS:
            link_path = target_root / skill_dir.name

            if lexists(link_path):
                if resolves_to(link_path, skill_dir):
                    print(f"[ok]   {link_path} -> {skill_dir}")
                    unchanged += 1
                else:
                    print(
                        "[skip] "
                        f"{link_path} already exists and points elsewhere "
                        "(leave unchanged)"
                    )
                    conflicts += 1
                continue

            try:
                create_dir_link(link_path, skill_dir)
            except Exception as exc:  # noqa: BLE001
                print(f"[error] failed to link {link_path} -> {skill_dir}: {exc}")
                conflicts += 1
                continue

            print(f"[link] {link_path} -> {skill_dir}")
            created += 1

    print(
        f"\nDone. created={created}, unchanged={unchanged}, conflicts={conflicts}"
    )

    return 0 if conflicts == 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())
