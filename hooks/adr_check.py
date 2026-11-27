#!/usr/bin/env python3
"""Antigravity Stop hook: validate reverse-chronological [DD.MM.YYYY] ADR entries in decision.md."""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from datetime import date
from pathlib import Path
from typing import Any

HEADING_RE = re.compile(r"^###\s+(.+)$")
VALID_DATE_HEADING_RE = re.compile(r"^###\s+\[(\d{2})\.(\d{2})\.(\d{4})\]\s+-\s+\S.*$")
REQUIRED_FIELDS = (
    ("- **Origin:**", "Origin"),
    ("- **Context:**", "Context"),
    ("- **Decision:**", "Decision"),
    ("- **Impact:**", "Impact"),
)


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


def _decision_md_modified(cwd: str) -> bool:
    """Return True if decision.md has staged, unstaged, or untracked modifications."""
    try:
        proc = subprocess.run(
            ["git", "-C", cwd, "status", "--porcelain", "--", "decision.md"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=5,
            check=False,
        )
        return proc.returncode == 0 and bool(proc.stdout.strip())
    except (OSError, subprocess.SubprocessError):
        return False


def validate_decision_log(content: str) -> list[str]:
    """Validate reverse-chronological [DD.MM.YYYY] headings and required ADR fields.

    Returns a list of human-readable error strings (empty list means valid).
    """
    errors: list[str] = []
    lines = content.splitlines()

    entry_indices: list[int] = [
        i for i, line in enumerate(lines) if HEADING_RE.match(line)
    ]
    if not entry_indices:
        return ["No ADR entries found (expected `### [DD.MM.YYYY] - <Title>`)."]

    parsed_dates: list[tuple[date, str]] = []

    for pos, start_idx in enumerate(entry_indices):
        end_idx = entry_indices[pos + 1] if pos + 1 < len(entry_indices) else len(lines)
        heading = lines[start_idx].strip()
        block = "\n".join(lines[start_idx + 1 : end_idx])

        match = VALID_DATE_HEADING_RE.match(heading)
        if not match:
            errors.append(
                f"Invalid ADR heading at line {start_idx + 1}: `{heading}` "
                "(expected `### [DD.MM.YYYY] - <Title>`)."
            )
        else:
            day_s, month_s, year_s = match.groups()
            try:
                entry_date = date(int(year_s), int(month_s), int(day_s))
                parsed_dates.append((entry_date, heading))
            except ValueError:
                errors.append(
                    f"Invalid calendar date in ADR heading at line {start_idx + 1}: `{heading}`."
                )

        missing = [label for marker, label in REQUIRED_FIELDS if marker not in block]
        if missing:
            errors.append(
                f"ADR `{heading}` is missing required field(s): {', '.join(missing)}."
            )

    for i in range(len(parsed_dates) - 1):
        newer_date, newer_heading = parsed_dates[i]
        older_date, older_heading = parsed_dates[i + 1]
        if newer_date < older_date:
            errors.append(
                f"ADR entries are not in reverse-chronological order: "
                f"`{newer_heading}` precedes newer `{older_heading}`."
            )

    return errors


def evaluate_stop(payload: dict[str, Any]) -> dict[str, Any]:
    """Evaluate a Stop hook payload and block stop if modified decision.md is invalid."""
    if payload.get("continuationActive"):
        return {"decision": "allow"}

    termination_reason = payload.get("terminationReason", "")
    if termination_reason in ("USER_CANCELED", "ERROR"):
        return {"decision": "allow"}

    cwd = _resolve_cwd(payload)
    decision_path = Path(cwd) / "decision.md"
    if not decision_path.is_file() or not _decision_md_modified(cwd):
        return {"decision": "allow"}

    content = decision_path.read_text(encoding="utf-8")
    errors = validate_decision_log(content)
    if not errors:
        return {"decision": "allow"}

    bullet_list = "\n".join(f"- {err}" for err in errors)
    return {
        "decision": "continue",
        "reason": (
            "[vibe-coding-guardrail] `decision.md` failed ADR validation:\n"
            f"{bullet_list}\n"
            "Fix `decision.md` so all entries use reverse-chronological `[DD.MM.YYYY]` "
            "headings and include Origin, Context, Decision, and Impact."
        ),
    }


def main() -> int:
    raw = sys.stdin.read().strip()
    try:
        payload = json.loads(raw) if raw else {}
    except json.JSONDecodeError:
        payload = {}
    if not isinstance(payload, dict):
        payload = {}

    result = evaluate_stop(payload)
    sys.stdout.write(json.dumps(result) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
