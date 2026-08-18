# ROADMAP

Phased plan derived from `SPEC.md`'s and `AGENTS.md`'s open questions. `INTENT.md` is the *why* and
doesn't change; this file is the *what's next* and should — check it at the start of a session, tick
items off as they land, add items as scope gets clearer. Phases are roughly sequential, not strict gates.

## Phase 0 — Define the contract

Answer `SPEC.md`'s open questions before building against assumptions:

- [ ] What counts as an input/output concretely (files, structured records, something else)
- [ ] What "instantly" requires (synchronous, watch/trigger loop, something else)
- [ ] What "each side" means (two processes, two machines, two roles in one pipeline)
- [ ] Whether/how the spec itself versions, and how existing input/output pairs stay valid across a
      spec revision

**Done when:** `SPEC.md`'s open questions section is empty.

## Phase 1 — Single-agent pipeline

One agent, manually triggered: read an input, read the spec, write the matching output. No
Orchestrator/Producer/Validator split yet — proves the core loop before splitting it into roles.

**Done when:** a human can drop a file in `inputs/` and get a spec-correct file in `outputs/` after
manually invoking the agent once.

## Phase 2 — Multi-agent split

Introduce the `AGENTS.md` roles (Orchestrator, Producer, Validator) and answer its open questions:

- [ ] Runtime: separate agent processes/invocations, or phases of one run
- [ ] Handoff mechanism between roles
- [ ] Failure/retry behavior on Validator rejection
- [ ] Traceability: input → spec version → output

**Done when:** the three roles run as genuinely separate steps with a defined handoff, not one agent
doing all three jobs inline.

## Phase 3 — Instant

Remove the manual trigger from Phase 1 — an input landing in `inputs/` (or wherever Phase 0 decides
inputs live) produces an output with no human kicking off the run.

**Done when:** dropping an input and seeing the output requires zero manual invocation.

## Phase 4 — Concurrency and scale

Multiple inputs in flight at once; spec revisions happening while outputs are still being produced
against an older version.

**Done when:** two inputs can be processed at the same time without one's Producer/Validator run
interfering with the other's, and it's possible to tell which spec version produced any given output.
