#!/usr/bin/env python3
"""Antigravity SessionStart hook: 100% local, read-only Git branch check.

Never executes `git fetch`, `git pull`, or any `.git/` mutation.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Any

PROTECTED_BRANCHES = frozenset({"main", "master", "development", "develop"})
BASE_CANDIDATES = ("main", "master")


def _run_git_readonly(cwd: str, args: list[str]) -> tuple[int, str]:
    """Run a strictly read-only git command locally without network or lock writes."""
    try:
        proc = subprocess.run(
            ["git", "-C", cwd, *args],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=5,
            check=False,
        )
        return proc.returncode, proc.stdout.strip()
    except (OSError, subprocess.SubprocessError):
        return 1, ""


def _resolve_cwd(payload: dict[str, Any]) -> str:
    cwd = payload.get("cwd")
    if isinstance(cwd, str) and cwd and Path(cwd).is_dir():
        return cwd
    workspaces = payload.get("workspacePaths")
    if isinstance(workspaces, list) and workspaces:
        first = workspaces[0]
        if isinstance(first, str) and first and Path(first).is_dir():
            return first
    return os.getcwd()


def _is_merged_into_local_base(cwd: str, branch: str) -> str | None:
    """Return the local base branch name if `branch` is strictly behind and merged into it."""
    rc_head, head_sha = _run_git_readonly(cwd, ["rev-parse", "HEAD"])
    if rc_head != 0 or not head_sha:
        return None

    for base in BASE_CANDIDATES:
        rc_base, base_sha = _run_git_readonly(cwd, ["rev-parse", "--verify", f"refs/heads/{base}"])
        if rc_base != 0 or not base_sha:
            continue
        # A freshly created branch at the exact same commit as base is not stale.
        if head_sha == base_sha:
            continue
        rc_anc, _ = _run_git_readonly(cwd, ["merge-base", "--is-ancestor", head_sha, base_sha])
        if rc_anc == 0:
            return base
    return None


def evaluate_session_start(payload: dict[str, Any]) -> dict[str, Any]:
    """Inspect local branch state and return a SessionStart hook response."""
    cwd = _resolve_cwd(payload)
    rc, inside = _run_git_readonly(cwd, ["rev-parse", "--is-inside-work-tree"])
    if rc != 0 or inside != "true":
        return {}

    rc_branch, branch = _run_git_readonly(cwd, ["branch", "--show-current"])
    if rc_branch != 0 or not branch:
        return {}

    warning: str | None = None
    if branch in PROTECTED_BRANCHES:
        warning = (
            f"[vibe-coding-guardrail] Active branch is protected branch '{branch}'. "
            "Do not commit or push directly to protected branches. Create an isolated "
            "branch (feature/<slug>, fix/<slug>, chore/<slug>) before editing or committing."
        )
    else:
        merged_base = _is_merged_into_local_base(cwd, branch)
        if merged_base is not None:
            warning = (
                f"[vibe-coding-guardrail] Active branch '{branch}' appears already merged "
                f"into local '{merged_base}'. Create a fresh branch from '{merged_base}' "
                "before making new commits, or run /aos-vibecode-update to clean obsolete branches."
            )

    if not warning:
        return {}

    return {
        "injectSteps": [
            {
                "systemMessage": {
                    "systemMessage": warning,
                }
            }
        ]
    }


def main() -> int:
    raw = sys.stdin.read().strip()
    try:
        payload = json.loads(raw) if raw else {}
    except json.JSONDecodeError:
        payload = {}
    if not isinstance(payload, dict):
        payload = {}

    result = evaluate_session_start(payload)
    sys.stdout.write(json.dumps(result) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
