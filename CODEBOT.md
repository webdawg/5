# CODEBOT

General principles for any agent generating code or output in this repository — the *how to write it*,
distinct from `INTENT.md` (the *why*), `SPEC.md` (the *what*), `AGENTS.md` (the *who*), and `ROADMAP.md`
(the *what's next*). Applies to Producer-role work especially, but to any code generation in this repo.
Living document — update it when a new principle gets established, not just when asked.

## No premature abstraction

Build the minimum the current phase (`ROADMAP.md`) actually needs. Don't build the Orchestrator/Producer/
Validator split before Phase 1's single-agent loop works; don't add config/flags for handoff mechanisms
that haven't been decided yet (`AGENTS.md`'s open questions).

## Comments explain why, not what

Names should already say what code does. A comment earns its place by capturing something a future
reader can't get from the code itself — a non-obvious invariant, a workaround, a design decision that
looks arbitrary until you know why.

## One source of truth for anything two roles need to agree on

If the Orchestrator and Validator both need to know what makes an input "ready" or an output "correct,"
that logic lives in one place both call — not duplicated and liable to drift.

## Traceability over cleverness

Every output should be traceable back to the input and spec version that produced it (`ROADMAP.md`
Phase 4). Prefer an explicit, boring record of that link over an implicit one that's fast to write but
impossible to audit later.

## Update the docs in the same change as the code

`SPEC.md`, `AGENTS.md`, and `ROADMAP.md` get updated alongside any behavior change, not as an
afterthought — a design decision or discovered gotcha is worth exactly as much as the reasoning behind
it, and that reasoning is cheapest to capture the moment it happens.

## Git discipline

Commit and push only when explicitly asked. Never force-push, skip hooks, or amend a shared commit
without being told to. Prefer a new commit over rewriting history.
