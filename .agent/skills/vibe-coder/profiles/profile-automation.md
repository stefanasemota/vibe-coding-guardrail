---
engine_name: "automation"
execution_mode: "parallel-subagents"
max_patch_size: 50
patch_strategy: "surgical-unified-diff"
type_safety: "strict"
gate_behavior: "advisory"
review_depth: "multi-aspect-audit"
---

# Engine Profile: `automation` (Unattended Scheduled Guardrail Profile)

Engine profile designed for **unattended scheduled background runs** in the Antigravity **Automations** tab (`~/.gemini/config/sidecars/<id>/sidecar.json` using `"builtin": "schedule"`).

---

## Operating Parameters

| Parameter | Value | Enforcement Rule |
| :--- | :--- | :--- |
| `engine_name` | `automation` | Loaded when `$PROFILE=automation` is specified in scheduled background tasks. |
| `execution_mode` | `parallel-subagents` | Parallel exploration and multi-aspect audit checks across the target repository. |
| `max_patch_size` | `50` | Strict adherence to `<= 50` lines if updating audit/report markdown files (`aos-audit.md`). |
| `patch_strategy` | `surgical-unified-diff` | Targeted report updates only; **never mutate application source code** during unattended runs. |
| `type_safety` | `strict` | Zero-warning lint gate, strict schema validation, and clean typecheck/build in `aos-verify`. |
| `gate_behavior` | `advisory` | **Never block or pause on `ask_question` or wait for `"proceed"`.** Log findings directly to `aos-audit.md` or the conversation summary and finish cleanly. |
| `review_depth` | `multi-aspect-audit` | Full 3-point static audit (Simplicity/DRY, Functional Correctness, Conventions) + defensive security scan (`aos-check-for-security-issues`). |
