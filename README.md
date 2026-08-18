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
- [`CODEBOT.md`](CODEBOT.md) — general principles for any agent generating code/output here.
- [`CHANGELOG.md`](CHANGELOG.md) — dated record of notable spec/doc changes.
- [`CLAUDE.md`](CLAUDE.md) — guidance for working in this repo with Claude Code.

`inputs/` and `outputs/` hold each side's data. [`examples/`](examples/) has a hand-authored, illustrative
input→output walkthrough — concrete, since the real format is still open (`SPEC.md`). [`prompt-log/`](prompt-log/)
keeps a raw, verbatim record of prompts given to the assistant, separate from the curated docs above.

## License

[AGPL-3.0-or-later](LICENSE).
