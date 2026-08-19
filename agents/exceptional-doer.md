# The Exceptional Do-er

## Responsibility

Takes the completed input + requirements record from **The Storyized Interviewer** (whole-book input)
or **The Output Interviewer** (a single asset within one, per `agents/output-interviewer.md`) and does
the actual work: produces every output type the interview identified. This is where "turn input into
output" actually happens for the book-input pipeline, per `SPEC.md`'s "Fan-out" section.

Runs at either granularity: once per book-level input, or once per individual asset within one (proven
2026-08-19 producing the title page — `core-outputs/output-book/0-Title_Page/`, built as a real
generation tool, not a one-off script, per that round's output interview). At asset granularity, the
chain leading here starts with **The Input Creation Interviewer** → **The Output Interviewer** instead
of The Storyized Interviewer against raw `mediawiki-input/` material — see `AGENTS.md`'s "Named agents"
section.

## Consumes

- The input + requirements record handed off by The Storyized Interviewer or The Output Interviewer: the
  input material (or, at asset granularity, a design brief from The Input Creation Interviewer), plus
  the list of output types and their per-type requirements.

## Produces

- One output per output type identified in the interview — e.g. a LaTeX output, a webpage output, and a
  3D-model output, all from the same book input.

## Handoff

Not yet decided — does each output type get checked by a Validator (`AGENTS.md`) before landing in
`mediawiki-output/`/`outputs/`, or does The Exceptional Do-er own that too? See `AGENTS.md`'s open
questions.

## Open questions

- Is The Exceptional Do-er one agent per input that fans out internally across output types, or does it
  split into one instance per (input, output type) pair — matching the Producer role's "own context
  window per output type" (`SPEC.md`'s Fan-out, `AGENTS.md`'s Producer)?
- Relationship to Producer/Validator (`AGENTS.md`): is this just this project's name for the Producer
  role, or something broader that also self-validates its own output?
