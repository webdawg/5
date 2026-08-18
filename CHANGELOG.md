# CHANGELOG

Notable changes to the spec and its supporting docs. This exists as a first, deliberately lightweight
answer to `SPEC.md`'s open question about whether/how the spec versions over time — dated entries for
now, not a formal version scheme, since nothing yet depends on addressing a spec by version number.
Revisit this format once `ROADMAP.md` Phase 4 (traceability: "which spec version produced this output")
actually needs one. Follows [Keep a Changelog](https://keepachangelog.com)'s spirit, not its exact format.

## [Unreleased]

Nothing pending.

## 2026-08-24

### Added
- `agents/storyized-interviewer.md` — The Storyized Interviewer: runs the intake interview for a new
  input, collecting the input and asking the human which output types are needed and what each requires.
- `agents/exceptional-doer.md` — The Exceptional Do-er: takes the Interviewer's completed input +
  requirements record and produces every output type it identified.

### Changed
- `INTENT.md` — new addendum naming these two agents for the first book-input pipeline.
- `AGENTS.md` — new "Named agents: the book-input pipeline" section; relationship to the generic
  Orchestrator/Producer/Validator roles left as an open question per-agent rather than forced now.
- `SPEC.md` — fan-out open question "how output types get decided" now has a first answer: The Storyized
  Interviewer asks the human directly.

## 2026-08-23

### Changed
- `INTENT.md` — new addendum: one input can fan out to multiple outputs of different types (e.g. a book
  input producing LaTeX, webpage, and 3D-model outputs), each with its own agent and context window.
- `SPEC.md` — new "Fan-out" section describing one-input-to-many-output-types, resolving the old "one
  input wiki / one output wiki" cardinality open question; new fan-out-specific open questions added.
- `AGENTS.md`, `agents/producer.md` — Producer redefined as scoped to one (input, output type) pair, not
  one input; new open question on cross-output-type coordination and Validator scope under fan-out.
- `ROADMAP.md` — Phase 1 now explicitly single-output-type only; Phase 2 gained a fan-out checklist item.

## 2026-08-22

### Added
- `mediawiki-output/Infinity_0` — output-side counterpart to `mediawiki-input/Infinity_0`: currently
  empty (no story has an edited output yet), documents that edited stories are rendered content (not
  links), and carries over the input side's open questions on ordering, traceability, and re-editing.

## 2026-08-21

### Fixed
- `mediawiki-input/README.md` and `mediawiki-output/README.md` were Markdown, breaking the "every file
  in these directories is a MediaWiki page" rule. Renamed to `README` (no extension) and rewritten in
  wikitext.

### Changed
- `SPEC.md` — "Representation, for now" now says explicitly: MediaWiki wikitext only in
  `mediawiki-input/`/`mediawiki-output/`, never Markdown, no exceptions, including README/documentation
  files.

## 2026-08-20

### Added
- `mediawiki-input/Infinity_0` — first real input page: a sub-specification for the ''Infinity 0''
  scifi book series (495+ unedited pages/stories). Establishes a human-in-the-loop pattern where inputs
  arrive as the outputs of human edits, and stories are deliberately unordered for now, with ordering
  subject to change over time.

### Changed
- `SPEC.md`, `mediawiki-input/README.md`, `mediawiki-output/README.md`, `ROADMAP.md`, `CLAUDE.md`,
  `LATER.md` — clarified the filename-as-page-title convention: spaces become underscores, matching
  MediaWiki's own URL convention. Renamed `mediawiki-input/Infinity 0` → `mediawiki-input/Infinity_0`
  to match.

## 2026-08-19

### Added
- `mediawiki-input/`, `mediawiki-output/` — first concrete case made real: one file per MediaWiki page,
  filename as the page title with spaces as underscores. Currently just plain git files.
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
