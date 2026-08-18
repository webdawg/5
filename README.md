# 5

Spec driven agentic coding with dynamic inputs, and outputs.

## The idea

A spec-based architecture where everything — the spec itself, inputs, and outputs — is saved in git.
Each side of the system has inputs and outputs; the primary motivator is turning every input into an
output instantly.

## Documentation map

- [`PRD.md`](PRD.md) — product requirements: problem, goals, requirements, success criteria.
- [`INTENT.md`](INTENT.md) — why this exists and why it's multi-agent.
- [`SPEC.md`](SPEC.md) — the input/output contract and architecture, with open questions.
- [`AGENTS.md`](AGENTS.md) — the multi-agent roles (Orchestrator, Producer, Validator) and how they hand
  off work; per-role detail lives under [`agents/`](agents/).
- [`ROADMAP.md`](ROADMAP.md) — phased plan, derived from the open questions in the docs above.
- [`IDEAS.md`](IDEAS.md) — low-ceremony backlog of ideas not yet vetted or promoted into the docs above.
- [`LATER.md`](LATER.md) — concretely-scoped work deliberately deferred to a later time.
- [`CODEBOT.md`](CODEBOT.md) — general principles for any agent generating code/output here.
- [`CHANGELOG.md`](CHANGELOG.md) — dated record of notable spec/doc changes.
- [`CLAUDE.md`](CLAUDE.md) — guidance for working in this repo with Claude Code.

`inputs/` and `outputs/` hold each side's data. [`mediawiki-input/`](mediawiki-input/) and
[`mediawiki-output/`](mediawiki-output/) are the first concrete case (`SPEC.md`) — one file per MediaWiki
page, filename as the page title; importing them into real MediaWiki instances is deferred, see
`LATER.md`. [`core-inputs/`](core-inputs/) is the second concrete case — raw source content by input
type (e.g. `core-inputs/input-book/`), for material too large to be a single wiki page.
[`examples/`](examples/) has a hand-authored, illustrative input→output walkthrough — concrete, since
the real format is still open (`SPEC.md`). [`prompt-log/`](prompt-log/) keeps a raw, verbatim record of
prompts given to the assistant, separate from the curated docs above.

## License

[AGPL-3.0-or-later](LICENSE).
