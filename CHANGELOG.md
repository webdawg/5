# CHANGELOG

Notable changes to the spec and its supporting docs. This exists as a first, deliberately lightweight
answer to `SPEC.md`'s open question about whether/how the spec versions over time — dated entries for
now, not a formal version scheme, since nothing yet depends on addressing a spec by version number.
Revisit this format once `ROADMAP.md` Phase 4 (traceability: "which spec version produced this output")
actually needs one. Follows [Keep a Changelog](https://keepachangelog.com)'s spirit, not its exact format.

## [Unreleased]

Nothing pending.

## 2026-08-19

### Added
- `mediawiki-input/`, `mediawiki-output/` — first concrete case made real: one file per MediaWiki page,
  filename as the literal page title. Currently just plain git files.
- `LATER.md` — concretely-scoped, deliberately-deferred work, distinct from `IDEAS.md` and `ROADMAP.md`.
  Primed with the first entry: importing `mediawiki-input/`/`mediawiki-output/` into real running
  MediaWiki instances.

### Changed
- `SPEC.md` — "First concrete case" now names `mediawiki-input/`/`mediawiki-output/` directly and
  states the file-per-page/filename-as-title representation; `Layout` updated to list them.
- `ROADMAP.md` — Phase 1 now points at `mediawiki-input/`/`mediawiki-output/` as the working
  representation, with the real-instance import deferred to `LATER.md`.

## 2026-08-18

### Added
- `PRD.md` — problem, goals, phased requirements, success criteria.
- `CHANGELOG.md` — this file.
- `examples/` — a worked, illustrative (non-binding) input/output pair, since Phase 0's input/output
  format question is still open.
- `ROADMAP.md`, `CODEBOT.md`, `prompt-log/` — phased plan, code-generation principles, and a raw
  verbatim prompt log, pulled in from patterns validated in repos 1–4.
- `.gitignore`.
- Initial scaffold: `README.md`, `LICENSE` (AGPL-3.0-or-later), `INTENT.md`, `SPEC.md`, `AGENTS.md`,
  `CLAUDE.md`, `agents/` role stubs, empty `inputs/`/`outputs/`.

### Changed
- `INTENT.md` — new addendum: AI can control both the input and output sides, not just one; a
  MediaWiki instance is the first concrete input/output target; physical-resource access (and raising
  real instances against it) is explicitly deferred to later.
- `ROADMAP.md` — Phase 1 now names MediaWiki as its first concrete target; added Phase 5 (physical
  resources), deliberately least-defined and not actionable yet.
- `AGENTS.md` — new open question: if AI can author both the input and the output, what keeps Validator
  checks meaningful rather than the pipeline grading its own homework.
- `INTENT.md` — second addendum: the input wiki holds things + instructions; the output wiki holds
  rendered output or, when the real output isn't wiki-content-shaped (e.g. a created git repo), a link
  to it instead.
- `SPEC.md` — Core idea reworded from "two sides, each with its own inputs/outputs" to "an input side
  and an output side," matching the clarified shape; new "First concrete case" section describing the
  input wiki / output wiki split; new open questions on output-as-link traceability and wiki cardinality.
- `ROADMAP.md` — Phase 1's target reworded from one MediaWiki instance to two (input wiki, output wiki).

### Added
- `IDEAS.md` — low-ceremony backlog of ideas not yet vetted into the curated docs, primed with the
  first idea: chaining wiki instances (one's output wiki as another's input wiki) for multi-stage
  agentic production, not yet promoted to `ROADMAP.md`.
