# PRD

Product requirements for **5** — spec-driven agentic coding with dynamic inputs and outputs. Sits above
the other docs: [`INTENT.md`](INTENT.md) is the motivating *why*, [`SPEC.md`](SPEC.md) the technical
*how*, [`AGENTS.md`](AGENTS.md) the *who*, [`ROADMAP.md`](ROADMAP.md) the *when*. This file is the
*what and for whom* — the requirements those other docs are built to satisfy. Update it when a
requirement changes; it should stay short enough to read in one sitting.

## Problem

Agentic coding setups typically treat "spec" as a one-time prompt and treat inputs/outputs as whatever
happens to flow through a single agent in a single session — nothing persists, nothing is reproducible,
and nothing enforces that the same input produces the same kind of output twice. There's no durable,
versioned contract governing the transformation, and no separation between deciding what an input needs,
producing it, and checking the result is correct.

## Who this is for

Right now: a single builder (the repo owner) using this as their own spec-driven pipeline. No external
users, no multi-tenant concerns, no auth model — that's explicitly out of scope until real usage
justifies it (see Non-goals).

## Goals

1. **A durable, versioned spec.** The contract governing input→output transformation lives in git, not
   in an ephemeral chat session, so it can be inspected, diffed, and reasoned about over time.
2. **Deterministic-enough transformation.** The same input, run against the same spec version, produces
   the same class of output — not byte-identical necessarily, but not arbitrarily different either.
3. **Separation of concerns via multi-agent roles.** Deciding, producing, and validating are distinct
   responsibilities (`AGENTS.md`), so a bad output is caught before it lands rather than trusted on the
   producing agent's own say-so.
4. **Speed.** Once the pipeline exists, an input becomes an output with no manual, per-input
   intervention — "instantly," per `INTENT.md`.
5. **Traceability.** Any output can be traced back to the input and spec version that produced it.

## Requirements

Functional requirements, phased per `ROADMAP.md`:

| # | Requirement | Phase |
|---|---|---|
| R1 | Define what counts as an input/output (format, storage convention) | 0 |
| R2 | Define what "instantly" requires operationally | 0 |
| R3 | A single agent can take one input + the spec and produce a matching output, manually triggered | 1 |
| R4 | Orchestrator dispatches inputs to Producers without doing transformation itself | 2 |
| R5 | Validator checks a candidate output against the spec before it's final, and can reject it | 2 |
| R6 | Input arrival triggers processing with no manual invocation | 3 |
| R7 | Multiple inputs can be processed concurrently without cross-interference | 4 |
| R8 | Every output records which input and spec version produced it | 4 |

Non-functional:

- **Auditability** — every stage of a transformation (dispatch, production, validation) should be
  reconstructable after the fact, not just the final output.
- **Spec-first** — no agent role should encode transformation logic that isn't traceable back to
  something written in `SPEC.md`. If an agent has to improvise, that's a sign the spec is incomplete,
  not a sign to improvise more.

## Non-goals

See `INTENT.md`'s Non-goals for the canonical list. Restated here because they bound the requirements
above:

- Not supporting arbitrary unstructured input formats before R1 is answered.
- Not a general-purpose, reusable multi-agent framework — the roles in `AGENTS.md` are specific to this
  pipeline.
- Not (yet) multi-user, hosted, or exposed to anyone but the repo owner.

## Success criteria

- **Phase 1 done:** a human can drop a file in `inputs/` and get a spec-correct file in `outputs/` after
  one manual invocation.
- **Phase 3 done:** the same, with zero manual invocation.
- **Ongoing:** `SPEC.md`'s and `AGENTS.md`'s open-questions sections trend toward empty, not toward
  accumulating unanswered items.

## Open questions

Tracked in detail in `SPEC.md` and `AGENTS.md` rather than duplicated here. The one PRD-level question
not fully covered there: **what does a rejected/failed input look like to the person who dropped it in**
— silence, a log entry, something in `outputs/` indicating failure? Needs an answer before Phase 2's
Validator rejection path (R5) is meaningful.
