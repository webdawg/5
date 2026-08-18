# Validator

## Responsibility

Check a Producer's candidate output against the spec before it's considered final. Catches spec drift
and incorrect/incomplete outputs before they land in `outputs/`.

## Consumes

- A candidate output from a Producer.
- The current spec (`SPEC.md`) — the source of truth for what "correct" means.

## Produces

- Either: the output committed to `outputs/`, or a rejection sent back to the Producer.

## Handoff

Not yet decided — see the "Handoff" and "Failure" open questions in [`AGENTS.md`](../AGENTS.md).

## Open questions

- Is validation fully automated, or does some class of output need human sign-off?
- On rejection, does the same Producer retry, or does the Orchestrator re-dispatch fresh?
- How many retries before an input is considered failed rather than retried indefinitely?
- Narrative review (`mediawiki-input/Infinity_0_Interview`): the 3D output's scene-breakdown decisions
  need a check that the breakdown makes narrative sense, not just a format/completeness check. Is that
  within this role's job, or a distinct review step outside Validator as currently scoped?
