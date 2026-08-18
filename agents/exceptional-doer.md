# The Exceptional Do-er

## Responsibility

Takes the completed input + requirements record from **The Storyized Interviewer** and does the actual
work: produces every output type the interview identified. This is where "turn input into output"
actually happens for the book-input pipeline, per `SPEC.md`'s "Fan-out" section.

## Consumes

- The input + requirements record handed off by The Storyized Interviewer: the input material, plus the
  list of output types and their per-type requirements.

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
