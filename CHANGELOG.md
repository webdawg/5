# CHANGELOG

Notable changes to the spec and its supporting docs. This exists as a first, deliberately lightweight
answer to `SPEC.md`'s open question about whether/how the spec versions over time — dated entries for
now, not a formal version scheme, since nothing yet depends on addressing a spec by version number.
Revisit this format once `ROADMAP.md` Phase 4 (traceability: "which spec version produced this output")
actually needs one. Follows [Keep a Changelog](https://keepachangelog.com)'s spirit, not its exact format.

## [Unreleased]

Nothing pending.

## 2026-08-31

### Changed
- `mediawiki-output/Infinity_0` renamed to `mediawiki-output/Infinity_0_Series` — the first story being
  written shares the book's own title ("Infinity 0"), colliding with the series index page's filename.
  The index moved so `mediawiki-output/Infinity_0` is free for the actual story.

## 2026-08-30

### Added
- `core-inputs/README.md`, `core-inputs/input-book/README.md` — the second concrete input case: raw
  source content by input type, for material too large to be a single wiki page. Book inputs get one
  folder per story (`<N>-<Story_Title>/`), with `priority.txt` (a single integer) as the authoritative
  order — not the folder-name number — and `manuscript.txt` for the raw text. No real story folders yet.

### Changed
- `INTENT.md` — new addendum capturing this structure and its ordering mechanism.
- `SPEC.md` — new "Second concrete case" section; `Layout` updated to list `core-inputs/`.
- `mediawiki-input/Infinity_0` — links to `core-inputs/input-book/` for the raw text; "Granularity" and
  "Ordering mechanism" open questions resolved.
- `README.md`, `CLAUDE.md` — registered `core-inputs/` alongside the other top-level directories.

## 2026-08-29

### Added
- `agents/narrative-reviewer/README.md`, `agents/narrative-reviewer/memory/README.md` — The Narrative
  Reviewer: a stateful, trainable agent (unlike every other agent here) that reviews 3D scene-breakdown
  decisions for narrative sense, alongside full human review, not instead of it. Given its own subfolder
  since it accumulates memory over time rather than being a stateless role description.

### Changed
- `INTENT.md` — new addendum naming and motivating this stateful-agent pattern.
- `AGENTS.md` — registered The Narrative Reviewer as a third named book-input-pipeline agent.
- `agents/validator.md` — narrative-review open question answered: a dedicated agent, not this role.
- `mediawiki-input/Infinity_0_Interview` — fifth and (for now) final pass: 3D tech stack settled as
  Three.js (matching repo 3's precedent) with glTF assets; narrative review assigned to The Narrative
  Reviewer. Every requirement raised so far is now resolved.

## 2026-08-28

### Changed
- `mediawiki-input/Infinity_0_Interview` — fourth interview pass: 3D scene granularity is dynamic (as
  many scenes as a given input unit needs, not a fixed ratio), and every scene-breakdown decision
  requires a narrative review before being final.
- `agents/validator.md` — new open question on whether narrative review belongs to the Validator role
  or is a distinct review step.

## 2026-08-27

### Changed
- `mediawiki-input/Infinity_0_Interview` — third interview pass: LaTeX front/back matter (full: title
  page, table of contents, copyright page) and house style (generic professional novel layout); new
  "Ordering" section resolving the general open question — each output type orders independently of the
  input's unordered state. Remaining open items narrowed to 3D scene granularity and WebGL asset format.
- `mediawiki-output/Infinity_0` — Ordering open question marked resolved, same answer.

## 2026-08-26

### Changed
- `mediawiki-input/Infinity_0_Interview` — second interview pass: LaTeX trim size (5.5"x8.5"), webpage
  hosting (static, e.g. GitHub Pages)/audio (AI-generated)/images (AI-generated), and 3D model tech
  stack (TypeScript + WebGL, static-hosted, no server), scene-generation approach (whole input in, one
  scene out — granularity not yet settled), and fidelity (concept-level blockout). New "Cross-cutting
  technical constraint" section: webpage and 3D outputs are both static-only, no backend server.
- `mediawiki-output/Infinity_0` — status line updated to match the fuller requirements.

## 2026-08-25

### Added
- `mediawiki-input/Infinity_0_Interview` — first interview log, run by The Storyized Interviewer:
  output types requested for `Infinity 0` (LaTeX print PDF, rich-multimedia linear webpage, 3D
  scene/environment models) and their open follow-up requirements.

### Changed
- `mediawiki-input/Infinity_0` — links to the new interview page.
- `mediawiki-output/Infinity_0` — records the three requested output types and a new open question on
  whether they fan out from the raw input or the human-edited output (chaining).
- `agents/storyized-interviewer.md` — resolved the "where does the interview log live" open question:
  a separate linked `<Input>_Interview` page.

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
