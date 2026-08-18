# INTENT

## Why this exists

Most agentic coding setups treat "spec" as a one-time prompt and "input/output" as whatever happens to
flow through a single agent in a single session. This project inverts that: the spec is the persistent,
versioned source of truth (committed to git, evolving over time), and the system's job is to take
whatever shows up in `inputs/` and turn it into the matching `outputs/` — driven by that spec, not by
one-off improvisation per input.

The motivating constraint is speed and consistency: an input should become an output *instantly* and
*the same way every time*, because the transformation logic lives in a spec that agents read and follow,
not in ad hoc reasoning that varies run to run.

## Why multi-agent

A single agent doing "read spec, read input, write output" doesn't scale past trivial cases — it has no
separation between deciding *what* an input needs, *doing* the transformation, and *checking* the result
matches spec. Splitting these into distinct agent roles (see [`AGENTS.md`](AGENTS.md)) means:

- Each agent has a narrow, verifiable job instead of one agent silently doing everything.
- Work can run concurrently across multiple inputs instead of serially.
- A validation role can catch spec drift before a bad output lands, rather than trusting the producing
  agent's own judgment of its own work.

## What "done" looks like

An input lands in `inputs/`, the right output appears in `outputs/` shortly after with no manual
intervention, and the mapping between them is traceable back to a specific version of the spec that
produced it.

## Non-goals (for now)

- Not trying to support arbitrary unstructured input formats before the input/output contract itself is
  defined (see `SPEC.md`'s open questions).
- Not building a generic multi-agent framework — the agent roles here are specific to the
  input-to-output pipeline, not a reusable product.
