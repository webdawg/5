# mediawiki-input

The input wiki, per `SPEC.md`'s "First concrete case" — things and instructions.

Each file here is one MediaWiki page, in wikitext. The filename *is* the page title, no extension —
except spaces become underscores, matching MediaWiki's own URL convention (page "Infinity 0" → file
`Infinity_0`). These are plain files in git for now, not a running wiki — importing them into a real
MediaWiki instance is deferred, see `LATER.md`.
