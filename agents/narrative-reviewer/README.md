# The Narrative Reviewer

## Responsibility

Performs narrative review on scene-breakdown decisions for the 3D output (and potentially other outputs
later): checks that how a given input unit got split into scenes actually makes narrative sense, not
just that it's technically well-formed. Answers the "who/what performs the narrative review" open
question from `mediawiki-input/Infinity_0_Interview`.

Unlike every other agent in this repo, this one is **stateful**: it remembers the user and prior
decisions/feedback over time and gets trained directly, rather than being invoked fresh with no memory
each run. That's why it gets its own subfolder (`agents/narrative-reviewer/`) instead of a single file
like the other roles under `agents/`.

## Consumes

- A candidate scene-breakdown decision (how many scenes, what each one covers) from **The Exceptional
  Do-er**.
- Its own accumulated memory (see `memory/`) of prior reviews, feedback, and user preferences.

## Produces

- A narrative-review verdict on a scene-breakdown decision, informed by its accumulated memory.

Full human review still happens alongside this — this agent's review doesn't replace the user's own
sign-off, it runs together with it.

## Memory

`memory/` holds whatever this agent accumulates over time about the user and prior narrative-review
decisions. Format/contents not yet decided — the user intends to train it directly, so expect this to
fill in from actual use rather than being designed upfront.

## Handoff

Not yet decided — see the "Handoff" open question in [`AGENTS.md`](../../AGENTS.md). Runs alongside
human review, not as a gate that replaces it.

## Open questions

- What exactly goes in `memory/` — free-form notes, structured records, something else?
- How does "training" this agent actually work in practice — manual corrections logged to memory, a
  more formal feedback loop, something else?
- Does human review happen before, after, or genuinely together with this agent's review (same pass)?
- Relationship to the Validator role (`AGENTS.md`) — is this a specialized Validator, or a fully
  separate step in the pipeline?
