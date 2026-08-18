# 5

Spec driven agentic coding with dynamic inputs, and outputs.

## The idea

A spec-based architecture where everything — the spec itself, inputs, and outputs — is saved in git.
Each side of the system has inputs and outputs; the primary motivator is turning every input into an
output instantly.

## Documentation map

- [`INTENT.md`](INTENT.md) — why this exists and why it's multi-agent.
- [`SPEC.md`](SPEC.md) — the input/output contract and architecture, with open questions.
- [`AGENTS.md`](AGENTS.md) — the multi-agent roles (Orchestrator, Producer, Validator) and how they hand
  off work; per-role detail lives under [`agents/`](agents/).
- [`CLAUDE.md`](CLAUDE.md) — guidance for working in this repo with Claude Code.

`inputs/` and `outputs/` hold each side's data.

## License

[AGPL-3.0-or-later](LICENSE).
