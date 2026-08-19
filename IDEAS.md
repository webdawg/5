# IDEAS

A running backlog of ideas worth keeping visible, lower-ceremony than `INTENT.md`'s addenda — no
dated-entry/verbatim requirement, just capture the idea while it's fresh. When an idea proves out,
promote it into `INTENT.md`/`SPEC.md`/`AGENTS.md`/`ROADMAP.md` and move it to Promoted below with a
link, rather than deleting it. If an idea gets rejected, leave it under Rejected with a one-line reason
— this file is a permanent record like everything else in this repo, not a to-do list to clear out.

## Open ideas

### Chain wikis for multi-stage agentic production
*Added 2026-08-18*

Since a pipeline instance has an input wiki and an output wiki (`SPEC.md`'s "First concrete case"), one
instance's output wiki can be another instance's input wiki — the output of stage N becomes the input of
stage N+1. That turns a single input→output hop into an actual chain: a genuine multi-stage agentic
production line, not just one isolated transformation.

Open threads this raises, not yet answered anywhere else:

- Does each hop in the chain run against its own spec version, or one shared spec across the whole
  chain? `SPEC.md`'s spec-versioning open question gets more pointed once there's a chain to trace
  through, not just one hop.
- Traceability (`PRD.md` R8) would need to follow a chain of hops, not just one input→spec→output link.
- Does the Orchestrator at stage N+1 watch the same wiki instance that stage N is writing to, or is
  there an explicit handoff/signal between instances?

Not promoted to `ROADMAP.md` yet — Phase 1 (a single input wiki / output wiki pair) isn't built, so
chaining multiple instances together is out of scope until that's proven first.

### A Creation Interview, for outputs authored with no raw input
*Added 2026-08-19*

`The Storyized Interviewer` (`agents/storyized-interviewer.md`) interviews about output requirements
for a raw input that has already arrived. The title page (`mediawiki-output/Infinity_0`) exposed a case
that doesn't fit that shape at all: front matter has no "unedited draft" to interview about — it's
authored straight to output. A **Creation Interview** would be a second, distinct interview role/pattern
for exactly that case: inputs that start from nothing rather than from raw material.

Plan to derive it empirically rather than design it upfront: log the concrete actions/prompts taken
while actually building the title page next (reusing `prompt-log/`'s existing raw-capture convention),
then distill the recurring question/decision pattern out of that trace into a new
`agents/creation-interviewer.md` role doc, mirroring `storyized-interviewer.md`'s structure.

Open threads this raises, not yet answered anywhere else:

- Does this replace or sit alongside `The Storyized Interviewer` — is "creation vs. intake" a fork at
  the top of the pipeline, or a variant mode of the same role?
- Front matter isn't a "story" — does it get its own `core-inputs/` subdirectory (e.g.
  `core-inputs/front-matter/`), or does authored-not-raw content skip `core-inputs/` entirely and go
  straight to `mediawiki-output/` the way the title page already did?

Not promoted to `AGENTS.md`/`ROADMAP.md` yet — no real Creation Interview has been run yet to generalize
from.

## Promoted

Nothing yet.

## Rejected

Nothing yet.
