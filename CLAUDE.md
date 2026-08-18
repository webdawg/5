# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

Read these in order before making design decisions here — they must stay aligned:

- [`INTENT.md`](INTENT.md) — the *why*: the motivating problem and why it's multi-agent.
- [`SPEC.md`](SPEC.md) — the *how*: the input/output contract and architecture, with open questions.
- [`AGENTS.md`](AGENTS.md) — the *who*: the Orchestrator/Producer/Validator roles and their handoffs;
  per-role detail in `agents/`.

This project is early-stage; treat these docs as the source of truth to update as decisions get made,
not as a fixed design.

## Layout

- `inputs/` — arriving things that need to become an output.
- `outputs/` — what gets produced from an input.
- `agents/` — one doc per agent role (`orchestrator.md`, `producer.md`, `validator.md`).

`inputs/` and `outputs/` are currently empty scaffolding (`.gitkeep` only) — no input/output format,
storage convention, or processing pipeline has been decided yet. Don't assume a schema; check SPEC.md's
open questions before inventing one. Likewise, no agent runtime (separate processes vs. phases of one
run) has been decided — check AGENTS.md's open questions first.
