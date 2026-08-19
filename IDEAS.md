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

## Promoted

### A Creation Interview, for outputs authored with no raw input
*Added 2026-08-19, promoted 2026-08-19*

Promoted to **The Input Creation Interviewer** (`agents/input-creation-interviewer.md`), the first of a
three-stage chain for a piece with no raw input: Creation Interview (this role) → **The Output
Interviewer** (`agents/output-interviewer.md`, its own named role, not folded into The Storyized
Interviewer) → production (`The Exceptional Do-er`). See `AGENTS.md`'s "Named agents: the book-input
pipeline" section for the full chain (two entry chains converging on the same Do-er), and the title page
(`core-outputs/output-book/0-Title_Page/`) for the real trace this was derived from.

Still open, noted in the role docs rather than here: whether every front-matter piece follows the same
`core-inputs/`/`core-outputs/` split the title page landed on, whether asset-granularity interviews need
their own `<Piece>_Interview`-style log page, and whether a design brief stays revisable after handoff.

## Rejected

Nothing yet.
