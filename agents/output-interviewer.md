# The Output Interviewer

## Responsibility

Runs the output-requirements interview for a single asset that went through **The Input Creation
Interviewer** first (front matter, or anything else authored rather than collected — see
`agents/input-creation-interviewer.md`). Same underlying pattern as **The Storyized Interviewer**
(interview the human to determine output-type requirements before any production starts, per `SPEC.md`'s
"Fan-out" section) but run against a design brief instead of raw input material, and scoped to one asset
rather than a whole book input. Doesn't produce any rendered output itself — its job ends once
requirements are captured and handed off.

Named and kept as its own role (2026-08-19) rather than folded silently into The Storyized Interviewer,
even though the interview technique is the same — the human explicitly wanted the three-stage chain
(Creation Interview → Output Interview → Do-er) named symmetrically, one role per stage.

## Consumes

- The design brief handed off by The Input Creation Interviewer.
- The human's answers during the interview: what deliverable(s) are actually needed, where the produced
  material lives, and what the generation tooling itself needs to be.

## Produces

- A completed requirements record, folded into the asset's own docs rather than a separate page for the
  title page's run — see "Interview log" below — ready to hand to The Exceptional Do-er.

## Handoff

Always passes to **The Exceptional Do-er** next.

## Interview log — what this actually looked like (the title page, 2026-08-19)

Three questions were asked, against the settled design brief:

1. **Deliverable(s)** — one master high-res render now, or several formats/resolutions up front?
   Answered: high-res render first, everything else later.
2. **Where does the produced material live?** — `outputs/` was empty scaffolding with no convention
   decided. Answered: mirror the input side — `core-outputs/output-book/`, folder names matching
   `core-inputs/input-book/` 1:1, holding generation code/scripts *and* the rendered result (not just a
   link).
3. **Does the generation code need to be reusable/documented, or is a one-off script enough?** Answered:
   "we are building our tool for our outputs" — a real tool, not a throwaway script. Also reframed the
   interview itself: identifying *how many* output deliverables a piece actually needs (could be
   anywhere from one to several) is part of this stage, not assumed upfront — per `SPEC.md`'s "Fan-out"
   applying at asset granularity too, not just at the whole-book level.

No dedicated `<Piece>_Interview`-style wiki page was created for this — the raw exchange lives in
`prompt-log/` (automatic capture), and the settled answers are folded into
`core-outputs/output-book/0-Title_Page/README.md`'s "Tooling"/"Status" sections plus the design brief's
own "Iteration log", rather than a separate log page. Whether that's sufficient long-term, or an asset
the size of a whole output type eventually needs its own dedicated interview-log page the way The
Storyized Interviewer's `<Input>_Interview` convention does, is open.

## Activation

Conversational, same as every other role in this chain right now — no automatic trigger. See
`AGENTS.md`'s "Activation" note.

## Open questions

- Does an asset-granularity run need its own `<Piece>_Interview`-style page, or is folding the record
  into the asset's own README/design-brief sufficient? (Carried over from `storyized-interviewer.md`'s
  equivalent question before this role split off.)
- Is a requirements record for one asset ever revisited/extended later (e.g. a second deliverable format
  gets added after production already started on the first), the same way `storyized-interviewer.md`
  asks for whole-book inputs?
- Relationship to The Storyized Interviewer: same interview *pattern*, different scope and named
  separately — is that split worth keeping once more than one asset has gone through it, or should they
  fold back into one role with two entry points?
