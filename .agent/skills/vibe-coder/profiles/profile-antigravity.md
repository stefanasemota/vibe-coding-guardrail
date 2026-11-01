---
engine_name: "antigravity"
execution_mode: "parallel-subagents"
max_patch_size: 50
patch_strategy: "surgical-unified-diff"
type_safety: "strict"
gate_behavior: "explicit-pause-and-wait"
review_depth: "multi-aspect-audit"
---

# Engine Profile: `antigravity` (Default Production Profile)

High-rigor engineering baseline where the **human is the driver** and the **AI is the execution engine**.

---

## Operating Parameters

| Parameter | Value | Enforcement Rule |
| :--- | :--- | :--- |
| `engine_name` | `antigravity` | Default production profile loaded by `vibe-coder`. |
| `execution_mode` | `parallel-subagents` | Use parallel exploration paths (Phase 2) and multi-angle quality/security review checks (Phase 6). |
| `max_patch_size` | `50` | Strict adherence to `<= 50` lines per atomic micro-patch in `aos-vibecode`. |
| `patch_strategy` | `surgical-unified-diff` | Apply targeted, minimal diffs preserving surrounding state, routes, and exports. Never rewrite whole files unnecessarily. |
| `type_safety` | `strict` | Zero-warning lint gate (`no-explicit-any`, `no-unused-imports`), strict schema validation, and clean typecheck/build in `aos-verify`. |
| `gate_behavior` | `explicit-pause-and-wait` | Mandatory human pause-and-wait checkpoints at **Phase 3**, **Phase 4**, and **Phase 6**. |
| `review_depth` | `multi-aspect-audit` | Full 3-point static audit (Simplicity/DRY, Functional Correctness, Conventions) + defensive security scan. |
