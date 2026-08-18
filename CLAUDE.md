# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

Read these in order before making design decisions here — they must stay aligned:

- [`PRD.md`](PRD.md) — the *what and for whom*: problem, goals, requirements, success criteria.
- [`INTENT.md`](INTENT.md) — the *why*: the motivating problem and why it's multi-agent.
- [`SPEC.md`](SPEC.md) — the *how*: the input/output contract and architecture, with open questions.
- [`AGENTS.md`](AGENTS.md) — the *who*: the Orchestrator/Producer/Validator roles and their handoffs;
  per-role detail in `agents/`.
- [`ROADMAP.md`](ROADMAP.md) — the *what's next*: phased plan derived from the open questions above.
  Check it at the start of a session before starting new work.
- [`CODEBOT.md`](CODEBOT.md) — the *how to write it*: code generation principles, distinct from all of
  the above.

This project is early-stage; treat these docs as the source of truth to update as decisions get made,
not as a fixed design.

## Capturing new intent

When the user drops a raw elaboration of the idea (new scope, a changed motivator, a constraint), append
it to `INTENT.md` under `## Addenda` as a dated entry, then pull anything concrete enough to build from
into `SPEC.md`/`AGENTS.md`/`ROADMAP.md`. See `INTENT.md`'s own "Capturing new intent" section. Do this
automatically, without being asked each time — then do whatever was actually asked in the same message.

## Layout

- `inputs/` — arriving things that need to become an output.
- `outputs/` — what gets produced from an input.
- `agents/` — one doc per agent role (`orchestrator.md`, `producer.md`, `validator.md`).
- `prompt-log/` — raw, verbatim history of prompts given to the AI assistant on this project, separate
  from the curated docs above. See `prompt-log/README.md` for format and cadence — a live instance of
  this project's own input/output pattern, not just process hygiene.

`inputs/` and `outputs/` are currently empty scaffolding (`.gitkeep` only) — no input/output format,
storage convention, or processing pipeline has been decided yet. Don't assume a schema; check SPEC.md's
open questions before inventing one. Likewise, no agent runtime (separate processes vs. phases of one
run) has been decided — check AGENTS.md's open questions first.

## Current status

Scaffolding only: docs (`PRD.md`, `INTENT.md`, `SPEC.md`, `AGENTS.md`, `ROADMAP.md`, `CODEBOT.md`), role stubs
under `agents/`, empty `inputs/`/`outputs/`/`prompt-log/`. No code, no language/runtime chosen, no
Phase 0 open question answered yet — see `ROADMAP.md`.
