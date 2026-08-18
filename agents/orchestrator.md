# Orchestrator

## Responsibility

Watch `inputs/` for new or changed items and decide which are ready to hand to a Producer. Owns
sequencing and concurrency across inputs; does not transform anything itself.

## Consumes

- `inputs/` — the raw arrivals.
- The current spec (`SPEC.md`) — to know what counts as a valid, ready-to-process input.

## Produces

- A dispatch: one input handed to one Producer run.

## Handoff

Not yet decided — see the "Handoff" open question in [`AGENTS.md`](../AGENTS.md).

## Open questions

- How does it detect a new input (poll, filesystem watch, git hook)?
- What makes an input "ready" vs. incomplete/still arriving?
