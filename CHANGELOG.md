# CHANGELOG

Notable changes to the spec and its supporting docs. This exists as a first, deliberately lightweight
answer to `SPEC.md`'s open question about whether/how the spec versions over time — dated entries for
now, not a formal version scheme, since nothing yet depends on addressing a spec by version number.
Revisit this format once `ROADMAP.md` Phase 4 (traceability: "which spec version produced this output")
actually needs one. Follows [Keep a Changelog](https://keepachangelog.com)'s spirit, not its exact format.

## [Unreleased]

Nothing pending.

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
