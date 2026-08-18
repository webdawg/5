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
- [`IDEAS.md`](IDEAS.md) — a low-ceremony backlog of ideas not yet vetted or promoted into the docs
  above. Lighter weight than `INTENT.md`'s addenda — capture ideas here first if they're not yet clearly
  founding intent.
- [`LATER.md`](LATER.md) — concretely-scoped work that's deliberately deferred. Different from
  `IDEAS.md` (unproven ideas) and `ROADMAP.md` (sequenced next steps) — this is decided work, just not
  time for it yet.
- [`CODEBOT.md`](CODEBOT.md) — the *how to write it*: code generation principles, distinct from all of
  the above.
- [`CHANGELOG.md`](CHANGELOG.md) — dated record of notable spec/doc changes. Update it alongside any
  change to `PRD.md`/`INTENT.md`/`SPEC.md`/`AGENTS.md`, same change, not an afterthought.

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
- `mediawiki-input/`, `mediawiki-output/` — the first concrete input/output case (`SPEC.md`), one file
  per MediaWiki page, filename as the page title with spaces as underscores. Plain git files for now —
  see `LATER.md` for the deferred real-instance import.
- `core-inputs/` — the second concrete case (`SPEC.md`): raw source content by input type, for material
  too large/unstructured to be one wiki page (e.g. `core-inputs/input-book/`, one folder per story, with
  a `priority.txt` as the authoritative order). See `core-inputs/README.md`.
- `agents/` — one doc per agent role (`orchestrator.md`, `producer.md`, `validator.md`).
- `prompt-log/` — raw, verbatim history of prompts given to the AI assistant on this project, separate
  from the curated docs above. See `prompt-log/README.md` for format and cadence — a live instance of
  this project's own input/output pattern, not just process hygiene.
- `examples/` — a hand-authored, illustrative (non-binding) input→output walkthrough. See
  `examples/README.md` — do not treat this as the real input/output format.

`inputs/` and `outputs/` are currently empty scaffolding (`.gitkeep` only) — no input/output format,
storage convention, or processing pipeline has been decided yet. Don't assume a schema; check SPEC.md's
open questions before inventing one. Likewise, no agent runtime (separate processes vs. phases of one
run) has been decided — check AGENTS.md's open questions first.

## Current status

Scaffolding only: docs (`PRD.md`, `INTENT.md`, `SPEC.md`, `AGENTS.md`, `ROADMAP.md`, `IDEAS.md`,
`LATER.md`, `CODEBOT.md`, `CHANGELOG.md`), role stubs under `agents/` (generic: orchestrator, producer,
validator; named book-input pipeline: `storyized-interviewer.md`, `exceptional-doer.md`, and the
stateful `narrative-reviewer/` subfolder with its own `memory/`), one illustrative example under
`examples/`, `mediawiki-input/`/`mediawiki-output/` with the first real input (`Infinity_0`, fully
interviewed — see `Infinity_0_Interview`), a renamed series index (`Infinity_0_Series`, since the first
story shares the book's own title), `core-inputs/input-book/` scaffolded but with no real story folders
yet (the corpus hasn't been split into named stories), empty `inputs/`/`outputs/`/`prompt-log/`. No code,
no language/runtime chosen, no Phase 0 open question answered yet — see `ROADMAP.md`.
