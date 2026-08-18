# Producer

## Responsibility

Take one input plus the current spec and generate the corresponding output. This is where the actual
"turn input into output" transformation happens.

## Consumes

- One input, as dispatched by the Orchestrator.
- The current spec (`SPEC.md`).

## Produces

- A candidate output, handed to the Validator (not written directly to `outputs/` — see Validator).

## Handoff

Not yet decided — see the "Handoff" open question in [`AGENTS.md`](../AGENTS.md).

## Open questions

- Does a Producer get the whole spec every run, or only the parts relevant to its input?
- What does a Producer do if the spec doesn't cover its input (undefined case) — fail, best-effort,
  escalate?
