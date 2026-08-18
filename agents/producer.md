# Producer

## Responsibility

Take one input, one target output type, and the current spec, and generate that one output. This is
where the actual "turn input into output" transformation happens.

Per `SPEC.md`'s "Fan-out" section, one input can need several outputs of different types (e.g. a book
input producing LaTeX, webpage, and 3D-model outputs). Each output type gets its own Producer instance,
in its own context window — a Producer is scoped to one (input, output type) pair, never to "all of this
input's outputs."

## Consumes

- One input, as dispatched by the Orchestrator.
- The output type it's been dispatched to produce.
- The current spec (`SPEC.md`), and whatever type-specific sub-spec applies to its output type.

## Produces

- A candidate output of its assigned type, handed to the Validator (not written directly to `outputs/`
  — see Validator).

## Handoff

Not yet decided — see the "Handoff" open question in [`AGENTS.md`](../AGENTS.md).

## Open questions

- Does a Producer get the whole spec every run, or only the parts relevant to its input and output type?
- What does a Producer do if the spec doesn't cover its input or output type (undefined case) — fail,
  best-effort, escalate?
- Do sibling Producers for the same input (different output types) ever need to coordinate, or are they
  fully independent by design (`SPEC.md`'s fan-out open questions)?
