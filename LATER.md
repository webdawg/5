# LATER

Concretely-scoped work that's deliberately deferred — not because it's an unproven idea (that's
`IDEAS.md`) and not because it's next up in sequence (that's `ROADMAP.md`), but because the *what* is
already decided and it's just not time yet. Each entry should be specific enough to act on whenever it
does become time.

## Deferred

### Import `mediawiki-input/` and `mediawiki-output/` into real MediaWiki instances
*Added 2026-08-18*

`mediawiki-input/` and `mediawiki-output/` hold one file per MediaWiki page, in git, filename as the
literal page title, as the concrete first case from `SPEC.md`. For now that's as far as it goes — flat
wikitext files in a repo, not a running wiki. Standing up two actual MediaWiki instances and importing
these pages into them (via `importDump.php`, the API, or another route) is real work with its own
decisions (hosting, auth, one instance vs. two, how imports stay in sync with the git files afterward)
that isn't worth making until there's a reason to actually run the wikis rather than just author pages
for them.

**Done when:** revisit once Phase 1 (`ROADMAP.md`) actually needs a running wiki, not before.
