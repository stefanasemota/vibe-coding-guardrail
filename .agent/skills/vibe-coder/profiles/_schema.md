# Engine Profile Schema Contract (`_schema.md`)

All engine profiles in `.agent/skills/vibe-coder/profiles/profile-<name>.md` must define the following 7 fields in their YAML frontmatter and body specification.

---

## Required Profile Fields

| Field | Type / Allowed Values | Default | Description |
| :--- | :--- | :--- | :--- |
| `engine_name` | `string` | `"antigravity"` | Unique identifier for the AI model engine or execution environment. |
| `execution_mode` | `"parallel-subagents"` \| `"sequential-multi-turn"` | `"parallel-subagents"` | Whether codebase exploration and verification run via parallel subagents or sequential turns. |
| `max_patch_size` | `integer` (lines) | `50` | Maximum lines changed per atomic micro-patch in `aos-vibecode`. |
| `patch_strategy` | `"surgical-unified-diff"` \| `"full-module-rewrite"` | `"surgical-unified-diff"` | How code modifications are applied to existing files. |
| `type_safety` | `"strict"` \| `"permissive"` | `"strict"` | Static analysis and TypeScript enforcement level in `aos-verify`. |
| `gate_behavior` | `"explicit-pause-and-wait"` \| `"advisory"` | `"explicit-pause-and-wait"` | Checkpoint behavior at Phase 3 (Spec Freeze), Phase 4 (Architecture Matrix), and Phase 6 (QA Review). |
| `review_depth` | `"multi-aspect-audit"` \| `"quick-lint"` | `"multi-aspect-audit"` | Depth of static, DRY, functional correctness, and security checks in `aos-verify` and `aos-check-for-security-issues`. |

---

## Template Structure

```markdown
---
engine_name: "<name>"
execution_mode: "parallel-subagents"
max_patch_size: 50
patch_strategy: "surgical-unified-diff"
type_safety: "strict"
gate_behavior: "explicit-pause-and-wait"
review_depth: "multi-aspect-audit"
---

# Engine Profile: `<name>`

## Operating Constraints
- **Execution Mode:** `<execution_mode>`
- **Max Patch Size:** `<= <max_patch_size> lines`
- **Patch Strategy:** `<patch_strategy>`
- **Type Safety:** `<type_safety>`
- **Gate Behavior:** `<gate_behavior>` (Phases 3, 4, and 6)
- **Review Depth:** `<review_depth>`
```
