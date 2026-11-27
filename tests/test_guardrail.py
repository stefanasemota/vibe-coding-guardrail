"""Zero-dependency unittest suite for vibe-coding-guardrail v2.0.

Enforces Single Source of Truth skill-drift checks across skills/*/SKILL.md,
plugin.json, README.md, and Architecture.md, validates decision.md, and tests
all Antigravity lifecycle hooks (session_start.py, branch_guard.py, adr_check.py).
"""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
HOOKS_DIR = REPO_ROOT / "hooks"
if str(HOOKS_DIR) not in sys.path:
    sys.path.insert(0, str(HOOKS_DIR))

import adr_check  # noqa: E402
import branch_guard  # noqa: E402
import session_start  # noqa: E402

ALLOWED_PLUGIN_FIELDS = frozenset(
    {
        "name",
        "displayName",
        "version",
        "description",
        "logo",
        "author",
        "homepage",
        "repository",
        "suggestedPrompts",
        "disabled",
    }
)


def _discover_skills() -> list[str]:
    skills_dir = REPO_ROOT / "skills"
    return sorted(
        p.parent.name
        for p in skills_dir.glob("*/SKILL.md")
        if p.is_file()
    )


def _git(repo: Path, *args: str) -> subprocess.CompletedProcess[str]:
    env = os.environ.copy()
    env.setdefault("GIT_AUTHOR_NAME", "Test User")
    env.setdefault("GIT_AUTHOR_EMAIL", "test@example.com")
    env.setdefault("GIT_COMMITTER_NAME", "Test User")
    env.setdefault("GIT_COMMITTER_EMAIL", "test@example.com")
    return subprocess.run(
        ["git", "-C", str(repo), *args],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        env=env,
        check=True,
    )


def _init_temp_repo(tmp_path: Path, default_branch: str = "main") -> Path:
    repo = tmp_path / "repo"
    repo.mkdir(parents=True, exist_ok=True)
    _git(repo, "init", "-b", default_branch)
    (repo / "README.md").write_text("# Temp Repo\n", encoding="utf-8")
    _git(repo, "add", "README.md")
    _git(repo, "commit", "-m", "chore: initial commit")
    return repo


def _run_hook_subprocess(script: Path, payload: dict[str, object]) -> dict[str, object]:
    proc = subprocess.run(
        [sys.executable, str(script)],
        input=json.dumps(payload),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=True,
        timeout=10,
    )
    return json.loads(proc.stdout)


class TestSingleSourceOfTruth(unittest.TestCase):
    """Zero-drift assertions anchored to skills/*/SKILL.md on disk."""

    def test_legacy_node_and_vendor_files_removed(self) -> None:
        forbidden = [
            REPO_ROOT / "package.json",
            REPO_ROOT / "package-lock.json",
            REPO_ROOT / ".nvmrc",
            REPO_ROOT / "ai-rules.json",
            REPO_ROOT / "bin",
            REPO_ROOT / ".agent",
            REPO_ROOT / "tests" / "guardrail.test.mjs",
        ]
        for path in forbidden:
            self.assertFalse(path.exists(), f"Legacy path should be removed: {path}")

    def test_skills_frontmatter_and_structure(self) -> None:
        skills = _discover_skills()
        self.assertGreaterEqual(len(skills), 1, "Expected at least one skill in skills/")
        for skill_name in skills:
            skill_md = REPO_ROOT / "skills" / skill_name / "SKILL.md"
            text = skill_md.read_text(encoding="utf-8")
            self.assertTrue(text.startswith("---\n"), f"{skill_md} missing YAML frontmatter")
            self.assertIn(f"name: {skill_name}\n", text, f"{skill_md} name mismatch")
            self.assertRegex(text, r"(?m)^description:\s+\S+", f"{skill_md} missing description")
            self.assertNotIn(
                "disable-model-invocation: true",
                text,
                f"{skill_md} must allow automatic model invocation",
            )

    def test_plugin_json_matches_skills_on_disk(self) -> None:
        skills = _discover_skills()
        plugin_data = json.loads((REPO_ROOT / "plugin.json").read_text(encoding="utf-8"))

        unknown_fields = set(plugin_data.keys()) - ALLOWED_PLUGIN_FIELDS
        self.assertEqual(unknown_fields, set(), f"Unknown plugin.json fields: {unknown_fields}")
        self.assertEqual(plugin_data["name"], "vibe-coding-guardrail")
        self.assertEqual(plugin_data["version"], "2.0.0")

        desc = plugin_data["description"]
        self.assertRegex(
            desc,
            rf"\b{len(skills)}\s+skills\b",
            f"plugin.json description must state '{len(skills)} skills'",
        )
        for skill in skills:
            self.assertIn(skill, desc, f"plugin.json description missing skill '{skill}'")

    def test_readme_matches_skills_on_disk(self) -> None:
        skills = _discover_skills()
        readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
        plugin_version = json.loads((REPO_ROOT / "plugin.json").read_text(encoding="utf-8"))["version"]

        self.assertIn(f"version-{plugin_version}-blue.svg", readme)
        self.assertRegex(
            readme,
            rf"(?i)\b{len(skills)}\s+skills\b",
            f"README.md must list exact skill count ({len(skills)} skills)",
        )
        for skill in skills:
            self.assertIn(f"`{skill}`", readme, f"README.md missing skill `{skill}`")
        self.assertIn("Powered by <a href=\"https://github.com/stefanasemota/vibe-coding-guardrail\">", readme)

    def test_architecture_matches_skills_on_disk(self) -> None:
        skills = _discover_skills()
        arch = (REPO_ROOT / "Architecture.md").read_text(encoding="utf-8")

        self.assertRegex(
            arch,
            rf"(?i)\b{len(skills)}\s+skills\b",
            f"Architecture.md must state exact skill count ({len(skills)} skills)",
        )
        for skill in skills:
            self.assertIn(
                f"skills/{skill}/SKILL.md",
                arch,
                f"Architecture.md missing skill path skills/{skill}/SKILL.md",
            )

    def test_hooks_json_schema_and_targets(self) -> None:
        hooks_path = REPO_ROOT / "hooks.json"
        self.assertTrue(hooks_path.is_file(), "hooks.json must live at plugin root")
        data = json.loads(hooks_path.read_text(encoding="utf-8"))
        self.assertIn("vibe-coding-guardrail", data)

        bundle = data["vibe-coding-guardrail"]
        self.assertIn("SessionStart", bundle)
        self.assertIn("PreToolUse", bundle)
        self.assertIn("Stop", bundle)

        # Verify every command script exists on disk
        commands = [
            bundle["SessionStart"][0]["command"],
            bundle["PreToolUse"][0]["hooks"][0]["command"],
            bundle["Stop"][0]["command"],
        ]
        for cmd in commands:
            parts = cmd.split()
            script_rel = parts[-1]
            script_path = (REPO_ROOT / script_rel).resolve()
            self.assertTrue(script_path.is_file(), f"Hook script missing: {script_rel}")

    def test_decision_md_valid_and_preserves_history(self) -> None:
        content = (REPO_ROOT / "decision.md").read_text(encoding="utf-8")
        errors = adr_check.validate_decision_log(content)
        self.assertEqual(errors, [], f"decision.md validation errors: {errors}")
        headings = re.findall(r"^###\s+\[\d{2}\.\d{2}\.\d{4}\]\s+-\s+.+$", content, re.MULTILINE)
        self.assertGreaterEqual(len(headings), 18, "All 17 historical ADRs + v2.0 ADR must be preserved")

    def test_agents_md_has_no_backticked_local_hook_paths(self) -> None:
        agents_text = (REPO_ROOT / "rules" / "AGENTS.md").read_text(encoding="utf-8")
        self.assertNotRegex(
            agents_text,
            r"`hooks(?:/[^`]+|\.json)`",
            "rules/AGENTS.md must reference guardrail hooks without backticked local paths",
        )

    def test_skills_session_termination_tokens_default_false(self) -> None:
        for skill_name in _discover_skills():
            text = (REPO_ROOT / "skills" / skill_name / "SKILL.md").read_text(encoding="utf-8")
            self.assertIn(
                "VIBE_CODER_SHOW_TOKENS",
                text,
                f"skills/{skill_name}/SKILL.md must reference VIBE_CODER_SHOW_TOKENS toggle",
            )
            self.assertIn(
                "false",
                text.lower(),
                f"skills/{skill_name}/SKILL.md must default VIBE_CODER_SHOW_TOKENS to false",
            )


class TestSessionStartHook(unittest.TestCase):
    """Tests for hooks/session_start.py (offline/read-only safety + branch detection)."""

    def test_non_git_directory_returns_empty(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            res = _run_hook_subprocess(HOOKS_DIR / "session_start.py", {"cwd": tmp})
            self.assertEqual(res, {})

    def test_warns_on_main_and_never_creates_fetch_head(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo = _init_temp_repo(Path(tmp), default_branch="main")
            res = _run_hook_subprocess(HOOKS_DIR / "session_start.py", {"cwd": str(repo)})
            self.assertIn("injectSteps", res)
            msg = res["injectSteps"][0]["systemMessage"]["systemMessage"]
            self.assertIn("main", msg)
            self.assertFalse((repo / ".git" / "FETCH_HEAD").exists())

    def test_clean_feature_branch_returns_empty(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo = _init_temp_repo(Path(tmp), default_branch="main")
            _git(repo, "checkout", "-b", "feature/new-work")
            res = session_start.evaluate_session_start({"cwd": str(repo)})
            self.assertEqual(res, {})

    def test_warns_on_already_merged_branch(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo = _init_temp_repo(Path(tmp), default_branch="main")
            _git(repo, "checkout", "-b", "feature/old-work")
            (repo / "old.txt").write_text("done\n", encoding="utf-8")
            _git(repo, "add", "old.txt")
            _git(repo, "commit", "-m", "feat: old work")
            _git(repo, "checkout", "main")
            _git(repo, "merge", "--no-ff", "feature/old-work", "-m", "Merge feature/old-work")
            _git(repo, "checkout", "feature/old-work")

            res = session_start.evaluate_session_start({"cwd": str(repo)})
            self.assertIn("injectSteps", res)
            msg = res["injectSteps"][0]["systemMessage"]["systemMessage"]
            self.assertIn("already merged", msg)

    def test_no_network_git_commands_in_source(self) -> None:
        source = (HOOKS_DIR / "session_start.py").read_text(encoding="utf-8")
        self.assertNotIn('"fetch"', source)
        self.assertNotIn('"pull"', source)


class TestBranchGuardHook(unittest.TestCase):
    """Tests for hooks/branch_guard.py (PreToolUse commit/push guard)."""

    def test_blocks_commit_and_push_on_main(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo = _init_temp_repo(Path(tmp), default_branch="main")
            for cmd in ("git commit -m 'feat: x'", "git push", "git add . && git commit -m 'x'"):
                payload = {
                    "cwd": str(repo),
                    "toolCall": {"name": "run_command", "args": {"CommandLine": cmd}},
                }
                res = _run_hook_subprocess(HOOKS_DIR / "branch_guard.py", payload)
                self.assertEqual(res["decision"], "deny", f"Expected deny for: {cmd}")

    def test_allows_commit_and_push_on_feature_branch(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo = _init_temp_repo(Path(tmp), default_branch="main")
            _git(repo, "checkout", "-b", "feature/safe")
            for cmd in (
                "git commit -m 'feat: safe'",
                "git push -u origin feature/safe",
                "git push origin --delete feature/obsolete",
                "python3 -m unittest discover -s tests -v",
            ):
                payload = {
                    "cwd": str(repo),
                    "toolCall": {"name": "run_command", "args": {"CommandLine": cmd}},
                }
                res = branch_guard.evaluate_tool_call(payload)
                self.assertEqual(res["decision"], "allow", f"Expected allow for: {cmd}")

    def test_blocks_explicit_push_to_main_or_no_verify_from_feature_branch(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo = _init_temp_repo(Path(tmp), default_branch="main")
            _git(repo, "checkout", "-b", "feature/safe")
            for cmd in (
                "git push origin main",
                "git push origin HEAD:master",
                "git push origin --delete main",
                "git commit --no-verify -m 'chore: bypass'",
                "git commit -n -m 'chore: bypass'",
            ):
                payload = {
                    "cwd": str(repo),
                    "toolCall": {"name": "run_command", "args": {"CommandLine": cmd}},
                }
                res = branch_guard.evaluate_tool_call(payload)
                self.assertEqual(res["decision"], "deny", f"Expected deny for: {cmd}")


class TestAdrCheckHook(unittest.TestCase):
    """Tests for hooks/adr_check.py (Stop hook ADR validator)."""

    def test_valid_reverse_chronological_entries(self) -> None:
        sample = (
            "# Decision Log\n\n"
            "### [27.11.2026] - Second Decision\n"
            "- **Origin:** Human Request\n"
            "- **Context:** C2\n"
            "- **Decision:** D2\n"
            "- **Impact:** I2\n\n"
            "### [19.11.2026] - First Decision\n"
            "- **Origin:** Agent Proposal\n"
            "- **Context:** C1\n"
            "- **Decision:** D1\n"
            "- **Impact:** I1\n"
        )
        self.assertEqual(adr_check.validate_decision_log(sample), [])

    def test_invalid_date_order_and_missing_fields(self) -> None:
        bad_format = (
            "### [2026-11-27] - Wrong Date Format\n"
            "- **Origin:** Human Request\n"
            "- **Context:** C\n"
            "- **Decision:** D\n"
        )
        errors = adr_check.validate_decision_log(bad_format)
        self.assertTrue(any("Invalid ADR heading" in e for e in errors))
        self.assertTrue(any("Impact" in e for e in errors))

        wrong_order = (
            "### [01.11.2026] - Older First\n"
            "- **Origin:** Human Request\n"
            "- **Context:** C1\n"
            "- **Decision:** D1\n"
            "- **Impact:** I1\n\n"
            "### [27.11.2026] - Newer Second\n"
            "- **Origin:** Human Request\n"
            "- **Context:** C2\n"
            "- **Decision:** D2\n"
            "- **Impact:** I2\n"
        )
        order_errors = adr_check.validate_decision_log(wrong_order)
        self.assertTrue(any("reverse-chronological" in e for e in order_errors))

    def test_stop_hook_blocks_invalid_modified_decision_md_and_respects_continuation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo = _init_temp_repo(Path(tmp), default_branch="main")
            # Unmodified -> allow
            self.assertEqual(
                adr_check.evaluate_stop({"cwd": str(repo), "continuationActive": False})["decision"],
                "allow",
            )

            # Modified with invalid ADR -> continue (block stop)
            (repo / "decision.md").write_text("### [2026-11-27] - Bad\n", encoding="utf-8")
            res_bad = _run_hook_subprocess(
                HOOKS_DIR / "adr_check.py",
                {"cwd": str(repo), "continuationActive": False, "terminationReason": "NO_TOOL_CALL"},
            )
            self.assertEqual(res_bad["decision"], "continue")
            self.assertIn("ADR validation", res_bad["reason"])

            # continuationActive=True -> allow (prevent infinite loop)
            res_loop = adr_check.evaluate_stop({"cwd": str(repo), "continuationActive": True})
            self.assertEqual(res_loop["decision"], "allow")

            # Modified with valid ADR -> allow
            (repo / "decision.md").write_text(
                "### [27.11.2026] - Good ADR\n"
                "- **Origin:** Human Request\n"
                "- **Context:** Context\n"
                "- **Decision:** Decision\n"
                "- **Impact:** Impact\n",
                encoding="utf-8",
            )
            res_good = adr_check.evaluate_stop({"cwd": str(repo), "continuationActive": False})
            self.assertEqual(res_good["decision"], "allow")


if __name__ == "__main__":
    unittest.main()
