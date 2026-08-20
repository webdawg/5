# SPEC

See [`INTENT.md`](INTENT.md) for why this exists, and [`AGENTS.md`](AGENTS.md) for the multi-agent
roles that operate against this contract.

## Core idea

A spec-driven architecture where the spec itself — along with everything derived from it — lives in
git. The system has an input side and an output side. The primary motivator: turn every input into an
output instantly. One input can fan out to *multiple* outputs, each a different type — see "Fan-out"
below.

"Spec-driven agentic coding" means the spec is the source of truth an agent works from to go from input
to output, rather than input being handled by ad hoc one-off logic per case.

## Layout

- `inputs/` — things that arrive and need to become an output.
- `outputs/` — what gets produced from an input.
- `mediawiki-input/`, `mediawiki-output/` — the first concrete case (below), as flat files in git.
- `core-inputs/`, `core-outputs/` — raw source content and produced material by type (below), e.g.
  `core-inputs/input-book/` and `core-outputs/output-book/`.
- `SPEC.md` (this file) — the shared contract both sides work from.

`inputs/`/`outputs/` are the generic, git-native representation of the input/output side of the system.
`mediawiki-input/`/`mediawiki-output/` materialize that same split for the first concrete case. Where a
`mediawiki-input/` page's content isn't itself wiki-content-shaped (e.g. a whole book manuscript),
`core-inputs/` holds the actual raw material and the wiki page points at it, and `core-outputs/` holds
what got produced from it (generation code/scripts plus the rendered result) the same way — the same
abstract input/output split, materialized on both sides, not competing designs.

## First concrete case: input wiki / output wiki

Per `INTENT.md`'s 2026-08-18 addenda:

- **Input wiki** (`mediawiki-input/`) — holds *things* (raw material/data) and *instructions* (what
  should happen to them). This is the input side: what an Orchestrator watches for new/changed content
  on.
- **Output wiki** (`mediawiki-output/`) — holds either the rendered result directly, when the output is
  representable as wiki content, **or** a link to the output when it isn't. Example: an input
  instructing "create a git repo" can't be stored *in* MediaWiki — the output wiki instead gets a page
  linking to the created repo.

This means "the output" is sometimes the artifact itself (rendered wiki content) and sometimes an index
entry pointing at an artifact that lives elsewhere entirely. Both count as valid outputs; which one
applies depends on whether the result fits as wiki content.

**Representation, for now:** each file in `mediawiki-input/`/`mediawiki-output/` is one MediaWiki page,
in MediaWiki wikitext syntax — never Markdown, no exceptions, including any README/documentation file
that lives inside those two directories. The filename *is* the page title, no extension — except spaces
become underscores, matching MediaWiki's own URL convention (page "Infinity 0" → file `Infinity_0`).
These directories are plain git files, not a running wiki; importing them into a real MediaWiki instance
is deliberately deferred — see `LATER.md`.

## Second concrete case: book input structure (`core-inputs/input-book/`)

Per `INTENT.md`'s 2026-08-30 addendum. `mediawiki-input/Infinity_0` is the status/instructions page for
the `Infinity 0` book input, but a 495+-page manuscript isn't itself wiki-content-shaped as a single
page — so the raw text lives in `core-inputs/input-book/` instead, one folder per story:

```
core-inputs/input-book/<N>-<Story_Title>/
├── priority.txt   — a single integer; the authoritative order (not the folder-name number)
└── manuscript.txt — the raw, unedited story text
```

- The folder-name number (`N`) is a rough, human-sortable display hint, not the source of truth.
- `priority.txt` is authoritative. Reordering a story means editing that file, not renaming the folder
  — so reordering never breaks anything that references the folder by name. If the two ever disagree,
  `priority.txt` wins.
- Story titles use underscores for spaces, matching `mediawiki-input/`'s filename convention.

See `core-inputs/README.md` and `core-inputs/input-book/README.md`. This also answers
`mediawiki-input/Infinity_0`'s open "granularity" question: one folder per story.

## Fan-out: one input, multiple output types

Per `INTENT.md`'s 2026-08-23 addendum: one input isn't limited to one output. It can fan out to several
outputs, each a distinct *type*, all existing at once rather than as alternatives to pick between.
Example: a book input could produce a LaTeX output (print typesetting), a webpage output (an interactive
version of the story), and a 3D model output (scene settings) — three outputs, three types, one input.

Each output type gets its own agent instance, with its own context window — not one agent carrying every
output type's context for a given input. Per `AGENTS.md`, this means "Producer" is really one Producer
per **(input, output type)** pair, not one Producer per input; see the Producer role and
`agents/producer.md` for how that's captured.

This also resolves the old "is there always exactly one input wiki and one output wiki" question below:
there's one input wiki, but potentially many *kinds* of output, of which `mediawiki-output/` (rendered
wiki content or a link) is just one type — not the whole output side.

## Format variants: one output type, multiple deliverable forms

Per `INTENT.md`'s 2026-09-04 addendum: fan-out (above) splits one input into multiple output *types*
(LaTeX, webpage, 3D model, audio, ...). Within a single output type there's a second, distinct axis —
multiple *format/audience variants* of that same conceptual deliverable can be needed at once, not
different technologies but different packagings of the same piece for different consumers. Surfaced
running this for real against the title page's print render: an AI-accessibility variant, a
human-accessibility variant, an animated/interactive variant, a puzzle variant, a standard web-hosted
variant, an age-censored variant, a mobile variant — alongside output-*type*-level examples raised in the
same round (a 3D model in TypeScript/WebGL, a source-code-and-servers output for technical/"hacker"
users, a text-to-speech audio output).

Deciding this axis is **The Output Format Interviewer**'s job (`AGENTS.md`,
`agents/output-format-interviewer.md`) — runs after an output type is already decided (by The Storyized
Interviewer or The Output Interviewer) and before The Exceptional Do-er, one interview per output type.

**Tooling convention (2026-09-04):** each format variant gets its own separate generation script, not one
shared parametrized pipeline — chosen to avoid one script accumulating every variant's special-casing.
Each variant's rendered result lives in its own subfolder under `render/` (e.g. `render/print/`,
`render/web/`), mirroring `render/ARCHIVE/`'s existing subfolder convention for prior versions.

## Publishing: render output isn't the same as a reached, final output

The same 2026-09-04 round surfaced a related but distinct gap: the pipeline as built stops at a
generation/render step (`core-outputs/<piece>/render/`), which is a work product, not a genuinely
*published*, externally-reachable final artifact. Even the completed title page print render doesn't yet
live anywhere a real consumer would reach it. Not yet resolved — see open questions below.

### Open questions (format variants / publishing)

- Is the full 2026-09-04 list of format/audience variants a universal checklist (every output type gets
  checked against all of them), or decided fresh per output type/asset by whoever runs The Output Format
  Interviewer?
- What does "published" concretely mean, and where does it live — the still-empty top-level `outputs/`,
  a `published/` subfolder alongside each piece's `render/`, something else? Blocked on Phase 0's
  still-open "what counts as output concretely" question below.
- Does every output type go through The Output Format Interviewer, or only ones where format/audience
  variation is plausible (e.g. does a 3D model plausibly need an "age-censored" variant, or is that
  variant type-specific)?
- Does The Output Format Interviewer also apply to the whole-book chain (after The Storyized Interviewer,
  before The Exceptional Do-er), or only the asset chain (after The Output Interviewer) it was scoped to
  when introduced? Not yet decided — see `agents/output-format-interviewer.md`.

### Open questions (fan-out)

- How is the set of output types for a given input decided — declared on the input itself, inferred by
  an Orchestrator, or fixed globally by the spec? First answer, for the book-input pipeline: interview
  the human. See **The Storyized Interviewer** in `AGENTS.md`/`agents/storyized-interviewer.md`.
- Do all output types for one input share a single spec version, or can each type progress against its
  own version independently?
- Where does a given output type's own format contract live — one shared `SPEC.md`, or a per-type
  sub-spec (the way `mediawiki-input/`/`mediawiki-output/`'s "Representation, for now" is effectively a
  sub-spec for the wiki type)?
- Do the different output-type agents for the same input ever need to share context (e.g. the LaTeX and
  webpage outputs of the same book staying consistent with each other), or are they meant to be fully
  independent by design?

## Open questions

- What counts as an "input" and "output" concretely beyond the wiki case (files? structured records?)?
- What does "instantly" require — synchronous generation, a watch/trigger loop, something else?
- Is the spec itself versioned/changed over time, and how do input/output pairs stay valid across spec
  revisions? (`CHANGELOG.md` is a first, lightweight step toward this.)
- When an output is a link rather than rendered content (the git-repo case), is the output-wiki *page*
  itself "the output" for traceability (`PRD.md` R8), or just an index — and does the linked external
  artifact need its own separate trace record?

This doc will fill in further as those get answered.
