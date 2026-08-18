# SPEC

See [`INTENT.md`](INTENT.md) for why this exists, and [`AGENTS.md`](AGENTS.md) for the multi-agent
roles that operate against this contract.

## Core idea

A spec-driven architecture where the spec itself — along with everything derived from it — lives in
git. The system has two sides, each with its own `inputs/` and `outputs/`. The primary motivator: turn
every input into an output instantly.

"Spec-driven agentic coding" means the spec is the source of truth an agent works from to go from input
to output, rather than input being handled by ad hoc one-off logic per case.

## Layout

- `inputs/` — things that arrive and need to become an output.
- `outputs/` — what gets produced from an input.
- `SPEC.md` (this file) — the shared contract both sides work from.

## Open questions

- What counts as an "input" and "output" concretely (files? structured records? something else)?
- What does "instantly" require — synchronous generation, a watch/trigger loop, something else?
- What is "each side" — two processes, two machines, two roles in one pipeline?
- Is the spec itself versioned/changed over time, and how do input/output pairs stay valid across spec
  revisions?

This doc will fill in as those get answered.
