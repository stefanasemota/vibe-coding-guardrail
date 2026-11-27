#!/usr/bin/env python3
"""Antigravity PreToolUse hook: deterministically block direct commits/pushes to main/master."""

from __future__ import annotations

import json
import os
import re
import shlex
import subprocess
import sys
from pathlib import Path
from typing import Any

PROTECTED_BRANCHES = frozenset({"main", "master"})
SEGMENT_SPLIT_RE = re.compile(r"\s*(?:&&|\|\||;|\n)\s*")


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


def _current_branch(repo_dir: str) -> str:
    try:
        proc = subprocess.run(
            ["git", "-C", repo_dir, "branch", "--show-current"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=5,
            check=False,
        )
        return proc.stdout.strip() if proc.returncode == 0 else ""
    except (OSError, subprocess.SubprocessError):
        return ""


def _parse_git_invocation(segment: str) -> tuple[str | None, str | None, list[str]]:
    """Return (repo_override, subcommand, subcommand_args) if segment invokes git."""
    try:
        tokens = shlex.split(segment)
    except ValueError:
        tokens = segment.split()

    if not tokens:
        return None, None, []

    # Find `git` binary (handles leading env assignments like FOO=bar git ...)
    idx = 0
    while idx < len(tokens) and "=" in tokens[idx] and not tokens[idx].startswith("-"):
        idx += 1
    if idx >= len(tokens):
        return None, None, []

    if Path(tokens[idx]).name != "git":
        return None, None, []

    idx += 1
    repo_override: str | None = None
    while idx < len(tokens) and tokens[idx].startswith("-"):
        flag = tokens[idx]
        if flag == "-C" and idx + 1 < len(tokens):
            repo_override = tokens[idx + 1]
            idx += 2
        elif flag.startswith("-C") and len(flag) > 2:
            repo_override = flag[2:]
            idx += 1
        elif flag in ("-c", "--git-dir", "--work-tree") and idx + 1 < len(tokens):
            idx += 2
        else:
            idx += 1

    if idx >= len(tokens):
        return repo_override, None, []

    return repo_override, tokens[idx], tokens[idx + 1 :]


def _push_targets_protected(args: list[str]) -> str | None:
    """Return protected branch name if push explicitly targets main/master."""
    non_flags: list[str] = []
    skip_next = False
    for tok in args:
        if skip_next:
            skip_next = False
            continue
        if tok in ("-o", "--push-option", "--repo", "--receive-pack", "--exec"):
            skip_next = True
            continue
        if tok.startswith("-"):
            continue
        non_flags.append(tok)

    # First positional arg is typically the remote (e.g. origin); remaining are refspecs.
    refspecs = non_flags[1:] if len(non_flags) >= 2 else []
    for refspec in refspecs:
        target = refspec.split(":", 1)[-1].lstrip("+")
        if target.startswith("refs/heads/"):
            target = target[len("refs/heads/") :]
        if target in PROTECTED_BRANCHES:
            return target
    return None


def _is_non_protected_remote_delete(args: list[str]) -> bool:
    """Allow `git push origin --delete <feature-branch>` while still blocking protected deletes."""
    is_delete = "--delete" in args or "-d" in args
    if not is_delete:
        return False
    return _push_targets_protected(args) is None


def evaluate_tool_call(payload: dict[str, Any]) -> dict[str, Any]:
    """Evaluate a PreToolUse payload and return allow/deny decision."""
    tool_call = payload.get("toolCall")
    if not isinstance(tool_call, dict):
        return {"decision": "allow"}

    args_obj = tool_call.get("args")
    if not isinstance(args_obj, dict):
        return {"decision": "allow"}

    command_line = args_obj.get("CommandLine") or args_obj.get("command") or ""
    if not isinstance(command_line, str) or not command_line.strip():
        return {"decision": "allow"}

    base_cwd = _resolve_cwd(payload)
    for segment in SEGMENT_SPLIT_RE.split(command_line):
        segment = segment.strip()
        if not segment:
            continue
        repo_override, subcmd, subargs = _parse_git_invocation(segment)
        if subcmd not in ("commit", "push"):
            continue

        if "--no-verify" in subargs or (subcmd == "commit" and "-n" in subargs):
            return {
                "decision": "deny",
                "reason": (
                    "[vibe-coding-guardrail] Blocked: bypassing Git hooks with "
                    "`--no-verify` is prohibited."
                ),
            }

        repo_dir = base_cwd
        if repo_override:
            candidate = Path(repo_override)
            repo_dir = str(candidate if candidate.is_absolute() else Path(base_cwd) / candidate)

        if subcmd == "push":
            explicit_target = _push_targets_protected(subargs)
            if explicit_target:
                return {
                    "decision": "deny",
                    "reason": (
                        f"[vibe-coding-guardrail] Blocked: pushing directly to protected "
                        f"branch '{explicit_target}' is prohibited. Push an isolated branch "
                        "and open a Draft PR instead."
                    ),
                }
            if _is_non_protected_remote_delete(subargs):
                continue

        branch = _current_branch(repo_dir)
        if branch in PROTECTED_BRANCHES:
            return {
                "decision": "deny",
                "reason": (
                    f"[vibe-coding-guardrail] Blocked: `git {subcmd}` on protected branch "
                    f"'{branch}' is prohibited. Create an isolated branch "
                    "(feature/<slug>, fix/<slug>, chore/<slug>) first."
                ),
            }

    return {"decision": "allow"}


def main() -> int:
    raw = sys.stdin.read().strip()
    try:
        payload = json.loads(raw) if raw else {}
    except json.JSONDecodeError:
        payload = {}
    if not isinstance(payload, dict):
        payload = {}

    result = evaluate_tool_call(payload)
    sys.stdout.write(json.dumps(result) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
