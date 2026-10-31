# Agent Commit Instructions

You are a **Conventional Committer**. Every change you make must be committed
with a clear, semantically typed prefix. Never use generic messages like
"updated code" or "changes".

## Required Format
`type(optional-scope): short description`

## Allowed Types
| Type | When to Use |
|---|---|
| feat | A new feature visible to the user |
| fix | A bug fix |
| docs | Documentation only changes |
| chore | Build, config, or tooling changes |
| refactor | Code restructured with no behavior change |
| test | Adding or correcting tests |
| style | Formatting changes only |
| perf | Performance improvements |

## ❌ Rejected by CI
- "updated code"
- "changes"
- "WIP"
- Any message without a type: prefix
