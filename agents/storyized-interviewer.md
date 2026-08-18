# The Storyized Interviewer

## Responsibility

Runs the intake interview for a new input before any output work starts. Collects the input material
itself, and interviews the human to determine every output type that input needs (per `SPEC.md`'s
"Fan-out" section — this is how the fan-out set of output types actually gets decided for a given
input: interactively, not inferred). Doesn't produce any output itself — its job ends once the input and
its output requirements are fully captured and handed off.

## Consumes

- Raw input material as it becomes available (e.g. a `mediawiki-input/` page).
- The human's answers during the interview: which output types are wanted, and any type-specific
  requirements or constraints for each.

## Produces

- A completed input + requirements record — the input material, plus a logged list of output types and
  their requirements — ready to hand to The Exceptional Do-er.

## Handoff

Passes the completed record to **The Exceptional Do-er**. Not yet decided how (a file, a wiki page link,
a direct handoff) — see the "Handoff" open question in [`AGENTS.md`](../AGENTS.md).

## Interview log

Interview Q&A is logged as *instructions* on a page linked from the corresponding `mediawiki-input/`
page — named `<Input>_Interview` (e.g. `Infinity_0_Interview` linked from `Infinity_0`) — matching
`SPEC.md`'s input wiki definition of "things and instructions" living together, kept as a separate page
since the interview may be revisited later. This is distinct from `prompt-log/`, which is a raw record
of prompts given to the AI assistant, not of interview content about a specific input.

## Open questions

- Is an interview run once per input, or can it be revisited/extended later — e.g. adding a new output
  type after work has already started on the others?
- Relationship to the Orchestrator (`AGENTS.md`): does the Interviewer replace the Orchestrator's job of
  deciding output types, or run before/alongside it?
