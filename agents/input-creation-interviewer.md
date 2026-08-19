# The Input Creation Interviewer

## Responsibility

Runs first, and only for a piece with no raw input to begin with — front matter, or anything else
authored directly rather than edited from arriving raw material (per `IDEAS.md`'s "A Creation Interview"
entry, derived from actually doing this for the book's title page, 2026-08-19). Interviews the human to
determine the content/design itself: what the piece actually depicts or contains, and why — not which
output types or formats it needs, that's the next stage. Doesn't produce any rendered output itself, and
doesn't decide output-type requirements either — its job ends once the design is fully captured and
handed off.

Unlike The Storyized Interviewer's single intake pass, this interview runs in open-ended rounds: propose
a direction, render or describe it, take feedback, adjust — repeated as many times as needed, not a
fixed one-pass questionnaire. The title page went through 17+ rounds this way.

## Consumes

- The human's answers during the interview: what the piece should depict/contain, revised and
  re-revised across rounds as decisions firm up or change.

## Produces

- A design brief (e.g. `design-brief.md`, in the piece's `core-inputs/` folder) — this piece's stand-in
  for a manuscript, since there's no raw draft. Kept current through every round via its own "Iteration
  log" section, not just written once at the end.
- A `future-ideas.md` (or similar) alongside it for concepts that were part of the brief at some point
  and got superseded — kept rather than deleted, in case worth revisiting later.

## Handoff

Always passes the completed design brief to **The Output Interviewer** next — never straight to
**The Exceptional Do-er**, even for a simple piece. Keeps the three-stage chain consistent: Creation
Interview (this role) → The Output Interviewer → production (Do-er). See the 2026-08-19 decision in
`AGENTS.md`.

## Interview log

No dedicated interview-log page for this role (unlike The Storyized Interviewer's `<Input>_Interview`
wiki page) — the raw exchange is captured automatically by `prompt-log/`'s `SessionEnd` hook, and the
curated, current state of decisions lives in the design brief itself (its "Iteration log" section notes
what changed and why at each round, referencing prompt-log/ for the verbatim exchange where needed).

## Activation

Conversational — a human tells the assistant to start ("let's work on the title page next"), same as
every other role in this pipeline right now. No automatic trigger decides when a piece needs this role
versus going straight to The Storyized Interviewer (the whole-book-input chain); see `AGENTS.md`'s
"Activation" note and `ROADMAP.md` Phase 3 for when automatic triggering becomes in-scope generally.

## Open questions

- Front matter isn't a "story" — resolved for the title page: it gets a slot in `core-inputs/input-book/`
  alongside stories, holding a design brief instead of a manuscript, with its produced-material
  counterpart in `core-outputs/output-book/` (generation code + rendered result). Whether every
  front-matter piece follows this same pattern, or this was specific to the title page, is still open.
- How is it decided a given piece needs this role at all, rather than starting straight with The
  Storyized Interviewer? Right now: whenever there's no raw input to interview about — decided by
  whoever starts the work, not inferred.
- Is a round ever truly "done," or does a design brief stay revisable indefinitely even after handoff to
  The Output Interviewer / production has started? Not yet tested — the title page hadn't reached that
  point as of 2026-08-19.
