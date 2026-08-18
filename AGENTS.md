# AGENTS

The multi-agent architecture for turning inputs into outputs against the shared spec. See
[`INTENT.md`](INTENT.md) for why this is split across roles instead of one agent, and
[`SPEC.md`](SPEC.md) for the input/output contract these roles operate on.

## Roles

- **Orchestrator** — watches `inputs/` for new/changed items, decides which are ready to process and
  which output type(s) each one needs, and dispatches one Producer per (input, output type) pair. Owns
  sequencing and concurrency; doesn't do transformation work itself.
- **Producer** — takes one input, one target output type, and the current spec, and generates that one
  output. Per `SPEC.md`'s "Fan-out" section, one input can need several Producers — one per output type
  (e.g. LaTeX, webpage, 3D model), each running in its own context window rather than one Producer
  juggling every output type for an input.
- **Validator** — checks a Producer's output against the spec before it's considered final (correctness,
  completeness, format). Rejects/bounces back to the Producer on mismatch rather than letting drift land
  in `outputs/`.

Three roles, not more, until real usage shows a gap — see the open questions below before adding a
fourth.

## Named agents: the book-input pipeline

The first real usage (the `Infinity 0` book input) surfaced exactly that gap: nothing above covers
*collecting* an input and interviewing the human for its output requirements before any Producer work
starts. Two named agents cover that pipeline:

- **The Storyized Interviewer** — runs the intake interview: collects the input, and asks the human
  which output types (`SPEC.md`'s "Fan-out") are needed and what each one requires. See
  `agents/storyized-interviewer.md`.
- **The Exceptional Do-er** — takes the Interviewer's completed input + requirements record and produces
  every output type it identified. See `agents/exceptional-doer.md`.
- **The Narrative Reviewer** — reviews scene-breakdown decisions (currently: for the 3D output) for
  narrative sense, alongside full human review, not in place of it. Unlike every other agent here, it's
  **stateful**: it accumulates memory about the user and past decisions and gets trained directly, which
  is why it lives in its own subfolder, `agents/narrative-reviewer/`, with a `memory/` of its own, rather
  than a single file like the other roles. See `agents/narrative-reviewer/README.md`.

Their relationship to Orchestrator/Producer/Validator above isn't decided yet — see each one's own open
questions. Treat them as the concrete, named agents for the book-input pipeline first, and fold that
back into the generic roles once it's clear whether they're the same thing or genuinely distinct.

## Scaffolding

- `agents/orchestrator.md`, `agents/producer.md`, `agents/validator.md` — one doc per generic role: its
  responsibilities, inputs it consumes, outputs it produces, and how it hands off to the next role.
- `agents/storyized-interviewer.md`, `agents/exceptional-doer.md` — the named book-input pipeline agents,
  same template.
- `agents/narrative-reviewer/` — the one stateful named agent, as a subfolder rather than a single file:
  `README.md` for its role definition, `memory/` for what it accumulates over time.

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
- Fan-out (`SPEC.md`): with one Producer per (input, output type) pair, does one Validator check all of
  an input's outputs, or does each output type get its own Validator too — and does the Orchestrator
  need to know an input is "done" only once every output type for it has passed validation?
