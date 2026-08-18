# SPEC

See [`INTENT.md`](INTENT.md) for why this exists, and [`AGENTS.md`](AGENTS.md) for the multi-agent
roles that operate against this contract.

## Core idea

A spec-driven architecture where the spec itself — along with everything derived from it — lives in
git. The system has an input side and an output side. The primary motivator: turn every input into an
output instantly.

"Spec-driven agentic coding" means the spec is the source of truth an agent works from to go from input
to output, rather than input being handled by ad hoc one-off logic per case.

## Layout

- `inputs/` — things that arrive and need to become an output.
- `outputs/` — what gets produced from an input.
- `mediawiki-input/`, `mediawiki-output/` — the first concrete case (below), as flat files in git.
- `SPEC.md` (this file) — the shared contract both sides work from.

`inputs/`/`outputs/` are the generic, git-native representation of the input/output side of the system.
`mediawiki-input/`/`mediawiki-output/` materialize that same split for the first concrete case — two
representations of the same abstract split, not competing designs.

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
in wikitext. The filename *is* the page title, no extension — except spaces become underscores, matching
MediaWiki's own URL convention (page "Infinity 0" → file `Infinity_0`). These directories are plain git
files, not a running wiki; importing them into a real MediaWiki instance is deliberately deferred — see
`LATER.md`.

## Open questions

- What counts as an "input" and "output" concretely beyond the wiki case (files? structured records?)?
- What does "instantly" require — synchronous generation, a watch/trigger loop, something else?
- Is the spec itself versioned/changed over time, and how do input/output pairs stay valid across spec
  revisions? (`CHANGELOG.md` is a first, lightweight step toward this.)
- When an output is a link rather than rendered content (the git-repo case), is the output-wiki *page*
  itself "the output" for traceability (`PRD.md` R8), or just an index — and does the linked external
  artifact need its own separate trace record?
- Is there always exactly one input wiki and one output wiki, or could there be many of either?

This doc will fill in further as those get answered.
