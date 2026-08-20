# CHANGELOG

Notable changes to the spec and its supporting docs. This exists as a first, deliberately lightweight
answer to `SPEC.md`'s open question about whether/how the spec versions over time — dated entries for
now, not a formal version scheme, since nothing yet depends on addressing a spec by version number.
Revisit this format once `ROADMAP.md` Phase 4 (traceability: "which spec version produced this output")
actually needs one. Follows [Keep a Changelog](https://keepachangelog.com)'s spirit, not its exact format.

## [Unreleased]

Nothing pending.

## 2026-09-09

### Added
- `publish-output/` — new top-level folder for final, ready-to-publish deliverables only, resolving
  part of `SPEC.md`'s long-open "Publishing" question (where "published" concretely lives).
  `core-outputs/` keeps generation code and iteration history exactly as already spec'd; nothing else
  about its structure changed.

### Changed
- `publish-output/web-book/` (was `core-outputs/output-book/web-book/`) — moved whole (source and
  render together, since it has no iteration history of its own to leave behind). `src/build.py`'s path
  constants rewired for the new location and re-run to confirm identical output.
- `SPEC.md` — "Publishing" section marked partially resolved (location decided; deployment/hosting still
  fully open); "Webpage output" section's location updated; `Layout` registers `publish-output/`.
- `CLAUDE.md` — registers `publish-output/` alongside the other top-level directories.
- `agents/output-format-interviewer.md`, `core-outputs/output-book/0-Title_Page/README.md`,
  `publish-output/web-book/README.md` — path references updated.

### Not done yet
- Scope deliberately incremental, not decided all at once: whether any of the title page's other seven
  format variants (print, mobile, AI-accessible, human-accessible, interactive, puzzle, age-censored)
  also count as "final" and move to `publish-output/` — left for later, per the user's own instruction.
- Actual deployment/hosting of `publish-output/web-book/` — still just a location, not a live site.

## 2026-09-08

### Added
- `SPEC.md` — new "Webpage output: a click-through directory of HTML pages" section, fleshing out the
  webpage output type first named in the 2026-08-23 addendum but never shaped: one HTML page per input
  asset/story (mirrors `core-inputs/input-book/<N>-<Name>/` 1:1), ordered by `priority.txt`, in a new
  dedicated `core-outputs/output-book/web-book/` folder — not nested inside any one asset's own folder.
- `core-outputs/output-book/web-book/` — the webpage output's home: `src/build.py` (scans
  `core-inputs/input-book/*/priority.txt`, embeds each asset's `render/web/*.png` into a self-contained
  HTML page, links consecutive pages with "← Previous"/"Next →", generates `index.html`) and
  `render/pages/` (currently: `index.html`, `page-000-title-page.html`).
- `core-inputs/input-book/0-Title_Page/priority.txt` (`0`) — front-matter folders now carry
  `priority.txt` too, extending the existing story-only convention so the webpage builder has one
  ordering source across every kind of asset.

### Changed
- `INTENT.md` — new addendum: the 2026-09-04 "web" answer was a misclassification, not just
  underspecified — corrected to the webpage output type above.
- `SPEC.md`'s "Format variants" section — corrected: "web" removed from the format-variant list: it's an
  output *type*, not a repackaging of one asset. The format-variant/output-type line
  (`agents/output-format-interviewer.md`) held up on its first real test.
- `core-inputs/input-book/README.md` — documents `priority.txt` on every folder, not just story folders.
- `core-outputs/output-book/0-Title_Page/README.md` — corrects `render/web/`'s own description: it's an
  independently-useful image variant, not itself the webpage deliverable; now embedded in
  `web-book/render/pages/page-000-title-page.html` instead.
- `agents/output-format-interviewer.md` — interview log and open questions updated with the correction.

### Not done yet
- A future story's webpage page needs real typeset prose content, not an embedded image — `SPEC.md`'s
  new open question, not resolved here.
- `web-book/` isn't published anywhere reachable yet — same "published, not rendered" gap as every other
  variant.

## 2026-09-07

### Added
- `core-outputs/output-book/0-Title_Page/src/generate_ai_accessible.py`, `render/ai-accessible/` — a
  structured JSON description of the title page (layers, colors, text, layout) for AI/programmatic
  consumption, sourced from `generate.py`'s own design constants.
- `.../src/generate_human_accessible.py`, `render/human-accessible/` — a WCAG-1.1.1-style plain-language
  long description, written for a screen reader.
- `.../src/generate_interactive.py`, `render/interactive/` — a self-contained HTML page (embedded web
  PNG, vanilla CSS/JS, no external requests): pannable by drag, zoomable by scroll/pinch, slow ambient
  zoom animation. Deliberately stayed a single dependency-free file rather than a new web/JS output type,
  since that stack hasn't been decided for the project generally.
- `.../src/generate_puzzle.py`, `render/puzzle/` — a self-contained HTML tap-to-swap tile puzzle (4x5
  grid, CSS background-position slicing of the mobile PNG, no server-side slicing or game framework).
  The file itself is deterministic; the shuffle re-randomizes every page load, on purpose.
- `.../src/generate_age_censored.py`, `render/age-censored/` — the actual age-censoring mechanism (a
  list of regions to Gaussian-blur), not a demonstration on fabricated content — `CENSOR_REGIONS` is
  empty for this piece on purpose, since nothing in it warrants censoring for any age group. A more
  mature story input would populate the same list through the same script.

### Changed
- `core-outputs/output-book/0-Title_Page/README.md` — documents the complete format-variant set from The
  Output Format Interviewer's 2026-09-04 list; only the separate "published, not rendered" gap remains.
- `agents/output-format-interviewer.md` — interview log updated with the full build and the two judgment
  calls made along the way (self-contained HTML instead of a new output type; censoring mechanism built
  with nothing flagged rather than fabricated content).

### Not done yet
- The interactive and puzzle HTML files were checked structurally (valid output, no unresolved template
  placeholders) but not opened in a live browser.
- The "published, not just rendered" gap (`SPEC.md`'s "Publishing" section) — explicitly out of scope for
  this pass, per the original request.

## 2026-09-06

### Added
- `core-outputs/output-book/0-Title_Page/src/generate_mobile.py` — the title page's mobile format
  variant, same reuse approach as `generate_web.py` (resamples `generate.py`'s shared composite).
  750x1159 — narrower than the web variant but at a 2x-equivalent pixel density (a common "mobile @2x"
  asset-width convention), so it stays crisp at typical mobile device pixel ratios.
- `render/mobile/title-page-mobile.png` — the rendered mobile variant.

### Changed
- `core-outputs/output-book/0-Title_Page/README.md`, `agents/output-format-interviewer.md` — document
  the mobile variant; remaining undone list narrowed to AI-accessibility, human-accessibility,
  animated/interactive, puzzle, age-censored, plus the "published, not rendered" gap.

## 2026-09-05

### Added
- `core-outputs/output-book/0-Title_Page/src/generate_web.py` — the title page's web format variant
  (`SPEC.md`'s "Format variants" section), built by The Exceptional Do-er per The Output Format
  Interviewer's 2026-09-04 round. Reuses `generate.py`'s composite and resamples it to 1000px wide
  rather than regenerating independently, to avoid visual drift between variants of the same piece.
- `render/web/title-page-web.png` — the rendered web variant, 1000x1545.

### Changed
- `core-outputs/output-book/0-Title_Page/src/generate.py` — refactored: composition extracted into
  `build_composite()` (shared with `generate_web.py`), archiving generalized into `archive_existing()`,
  output path moved to `render/print/` (was `render/`), matching the new per-variant subfolder
  convention.
- `render/title-page-print.png` and `render/ARCHIVE/` moved to `render/print/title-page-print.png` and
  `render/print/ARCHIVE/` (`git mv`, history preserved) to match.
- `core-outputs/output-book/0-Title_Page/README.md` — documents both variants and what's still only
  documented, not built (AI-accessibility, human-accessibility, animated/interactive, puzzle,
  age-censored, mobile — plus the still-open "published, not rendered" gap).
- `agents/output-format-interviewer.md` — interview log updated: web variant built, rest of the list
  still open.

## 2026-09-04

### Added
- `agents/output-format-interviewer.md` — The Output Format Interviewer: a new stage inserted between
  The Output Interviewer and The Exceptional Do-er. Given one already-decided output type, interviews
  the human on every distinct format/audience variant that type needs (accessibility, platform,
  interactivity, audience filtering — not a different technology, that's still Fan-out). Added after The
  Output Interviewer's own first interview round deferred exactly this question ("one render now, or
  several formats up front?") instead of resolving it.

### Changed
- `INTENT.md` — new addendum capturing the gap and the real interview run against the title page: a wide
  list of format/audience variants (AI accessibility, human accessibility, animated/interactive, puzzle,
  web-hosted, age-censored, mobile) plus output-type-level examples (3D model in TypeScript/WebGL,
  hacker-facing source+servers, text-to-speech audio), and a related but distinct gap — the pipeline
  stops at `render/`, not a genuinely published/reached location.
- `SPEC.md` — new "Format variants: one output type, multiple deliverable forms" section (the
  format/audience axis, distinct from Fan-out's output-type axis) and new "Publishing" section (render
  output vs. reached output); new open questions for both.
- `AGENTS.md` — asset chain now reads Input Creation Interviewer → Output Interviewer → **Output Format
  Interviewer** → Exceptional Do-er; six named agents, not five.
- `agents/output-interviewer.md` — handoff corrected: passes to The Output Format Interviewer, not
  straight to The Exceptional Do-er.
- `agents/exceptional-doer.md` — now also runs once per format variant of one asset, not just once per
  asset; new open question on whether it owns publishing too.

### Not done yet
- None of the newly identified format variants (beyond the existing print render) have actually been
  built, and the print render itself hasn't been moved into a `render/print/` subfolder or reached a
  published location — this round captured requirements, per the established interview-stage pattern,
  not production work.

## 2026-09-03

### Added
- `agents/input-creation-interviewer.md` — The Input Creation Interviewer, promoted from `IDEAS.md`'s
  Creation Interview entry: the first stage for a piece with no raw input.
- `agents/output-interviewer.md` — The Output Interviewer: the second stage for that same case, same
  interview pattern as The Storyized Interviewer but kept as its own named role (not folded in) and run
  against a design brief instead of raw input material.

### Changed
- `AGENTS.md` — documents two parallel entry chains converging on the same Do-er: The Storyized
  Interviewer for whole-book raw input, or The Input Creation Interviewer → The Output Interviewer for a
  single asset with no raw input of its own (proven producing the title page). The Exceptional Do-er
  runs at either granularity.
- `agents/storyized-interviewer.md` — scope clarified back to whole-book raw input, cross-referencing
  The Output Interviewer for the asset-granularity case.
- `agents/exceptional-doer.md` — updated to name both possible handoff sources.
- `IDEAS.md` — Creation Interview entry moved to Promoted.

## 2026-09-02

### Added
- `core-outputs/` (with `output-book/`) — the output-side counterpart to `core-inputs/`: generation
  code/scripts plus the rendered result, one folder per piece, folder names matching
  `core-inputs/input-book/` 1:1. First populated (reserved) for `0-Title_Page`.
- `core-inputs/input-book/0-Title_Page/design-brief.md` — the title page's settled design, standing in
  for a manuscript since front matter has no raw draft.

### Changed
- `SPEC.md`'s Layout section — documents `core-outputs/` alongside `core-inputs/`.
- `core-inputs/input-book/README.md`, `core-inputs/README.md` — corrected: generation code and rendered
  output belong on the output side (`core-outputs/`), not bundled into a front-matter input folder as
  first written; a front-matter folder holds a design brief instead of a manuscript.

## 2026-09-01

### Added
- `mediawiki-output/Infinity_0` — the first real output content: the book's title page (front matter),
  title "Infinity 0", author "Agent 0".

### Changed
- `mediawiki-output/Infinity_0_Series` — corrected: the page freed up by the earlier rename was for the
  title page (front matter), not a story; updated wording and status accordingly.

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
