# AGENTS

The multi-agent architecture for turning inputs into outputs against the shared spec. See
[`INTENT.md`](INTENT.md) for why this is split across roles instead of one agent, and
[`SPEC.md`](SPEC.md) for the input/output contract these roles operate on.

## Roles

- **Orchestrator** — watches `inputs/` for new/changed items, decides which are ready to process, and
  dispatches each to a Producer. Owns sequencing and concurrency; doesn't do transformation work itself.
- **Producer** — takes one input plus the current spec and generates the corresponding output. This is
  where the actual "turn input into output" work happens.
- **Validator** — checks a Producer's output against the spec before it's considered final (correctness,
  completeness, format). Rejects/bounces back to the Producer on mismatch rather than letting drift land
  in `outputs/`.

Three roles, not more, until real usage shows a gap — see the open questions below before adding a
fourth.

## Scaffolding

- `agents/orchestrator.md`, `agents/producer.md`, `agents/validator.md` — one doc per role: its
  responsibilities, inputs it consumes, outputs it produces, and how it hands off to the next role.

No runtime/framework choice has been made yet (e.g. whether these are separate Claude Code agent
invocations, separate processes, or something else) — that's an open question below, not a decision
baked into this scaffolding.

## Open questions

- Runtime: are these three roles separate agent processes/invocations, or one process with three
  internal phases?
- Handoff: how does an Orchestrator hand an input to a Producer, and a Producer to a Validator — a
  file-based queue, a git commit per stage, something else?
- Failure: what happens when the Validator rejects an output — retry the same Producer, escalate to a
  human, drop the input?
- Concurrency: can multiple Producers run on different inputs at once, and if so, do they share any
  state that needs coordination?
- Traceability: how is "this output came from this input, this spec version, this agent run" recorded
  (git commit metadata, a log file, something else)?
- Self-validation: `INTENT.md`'s 2026-08-18 addendum means AI can control both the input and the output
  side (e.g. an AI-authored MediaWiki edit as the input). If AI can also produce the input, what keeps
  the Validator's check meaningful rather than the pipeline grading its own homework — does correctness
  need an external anchor (a real prior page state, a human-authored input) in that case, or does the
  spec itself have to be strict enough that it doesn't matter who authored the input?
