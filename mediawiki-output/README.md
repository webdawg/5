# mediawiki-output

The output wiki, per `SPEC.md`'s "First concrete case" — rendered output, or a link to the output when
the real result isn't wiki-content-shaped (e.g. a created git repo).

Each file here is one MediaWiki page, in wikitext. The filename *is* the page title, exactly — no
extension, no slugging. These are plain files in git for now, not a running wiki — importing them into a
real MediaWiki instance is deferred, see `LATER.md`.
