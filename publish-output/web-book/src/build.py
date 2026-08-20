#!/usr/bin/env python3
"""Builds the book's webpage output (SPEC.md's "Webpage output" section):
a directory of self-contained HTML pages, one per input asset/story, that
a reader clicks through sequentially like flipping pages in a physical
book. Corrects the 2026-09-04 round's "web" answer, which had wrongly
built a resized static image instead -- see INTENT.md's 2026-09-08
addendum and README.md here.

Lives under publish-output/ (moved here 2026-09-09, INTENT.md's addendum
of that date) -- publish-output/ holds only final, ready-to-publish
deliverables; core-outputs/ keeps generation code and iteration history
"as already speced." web-book has no iteration history of its own (it's
a mechanical rebuild, not hand-tuned), so the whole folder -- source and
render together -- moved as one unit rather than splitting src/ back
into core-outputs/. Each source asset's own render/web/ PNG this script
reads *does* stay in core-outputs/ for now (undecided/deferred whether it
moves too -- see this project's memory, not this file).

Ordering source: core-inputs/input-book/*/priority.txt (the same
authoritative-order file SPEC.md's "book input structure" section already
established for stories, extended 2026-09-08 to front matter too).

Content source, for now: each asset's own already-rendered web-resolution
image (core-outputs/output-book/<N>-<Name>/render/web/*.png) -- works for
an image-only piece like the title page. A future prose story needs a
different content source; see README.md's "Open" section, not solved
here.

Usage: python3 build.py
Reads:  ../../../core-inputs/input-book/*/priority.txt
        ../../../core-outputs/output-book/<N>-<Name>/render/web/*.png
Writes: ../render/pages/index.html, page-<NNN>-<slug>.html
"""
import base64
import re
from dataclasses import dataclass
from pathlib import Path

SRC_DIR = Path(__file__).resolve().parent
WEB_BOOK_DIR = SRC_DIR.parent
PUBLISH_OUTPUT_DIR = WEB_BOOK_DIR.parent
REPO_ROOT = PUBLISH_OUTPUT_DIR.parent
INPUT_BOOK_DIR = REPO_ROOT / "core-inputs" / "input-book"
OUTPUT_BOOK_DIR = REPO_ROOT / "core-outputs" / "output-book"

PAGES_DIR = WEB_BOOK_DIR / "render" / "pages"

FOLDER_RE = re.compile(r"^(\d+)-(.+)$")


@dataclass
class Asset:
    folder_name: str
    priority: int
    title: str
    slug: str
    image_path: Path


def discover_assets() -> list[Asset]:
    assets = []
    for folder in sorted(INPUT_BOOK_DIR.iterdir()):
        if not folder.is_dir():
            continue
        match = FOLDER_RE.match(folder.name)
        if not match:
            continue
        priority_file = folder / "priority.txt"
        if not priority_file.exists():
            raise SystemExit(f"{folder} has no priority.txt -- every input-book asset needs one (SPEC.md)")
        priority = int(priority_file.read_text().strip())

        render_web_dir = OUTPUT_BOOK_DIR / folder.name / "render" / "web"
        images = sorted(render_web_dir.glob("*.png")) if render_web_dir.exists() else []
        if len(images) != 1:
            raise SystemExit(
                f"{folder.name}: expected exactly one PNG in {render_web_dir}, found {len(images)} "
                "-- a story's page needs a different content source than an embedded image; see "
                "web-book/README.md's Open section."
            )

        name = match.group(2)
        assets.append(Asset(
            folder_name=folder.name,
            priority=priority,
            title=name.replace("_", " "),
            slug=name.lower().replace("_", "-"),
            image_path=images[0],
        ))
    assets.sort(key=lambda a: a.priority)
    return assets


PAGE_TEMPLATE = """<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>Infinity 0 -- {title}</title>
<style>
  html, body {{ margin: 0; background: #111; color: #eee; font: 16px sans-serif; }}
  body {{ display: flex; flex-direction: column; align-items: center; padding: 24px 0 48px; }}
  img {{ max-width: min(92vw, 700px); height: auto; display: block; box-shadow: 0 0 24px rgba(0,0,0,.6); }}
  nav {{ margin-top: 20px; display: flex; gap: 24px; align-items: center; }}
  nav a {{ color: #6ee1ff; text-decoration: none; font-size: 15px; }}
  nav a:hover {{ text-decoration: underline; }}
  .counter {{ opacity: 0.6; font-size: 13px; }}
</style>
</head>
<body>
<img src="data:image/png;base64,{image_b64}" alt="{title}">
<nav>
  {prev_link}
  <span class="counter">Page {page_num} of {page_count}</span>
  {next_link}
</nav>
</body>
</html>
"""

INDEX_TEMPLATE = """<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>Infinity 0</title>
<style>
  html, body {{
    margin: 0; height: 100%; background: #111; color: #eee; font: 16px sans-serif;
    display: flex; align-items: center; justify-content: center; flex-direction: column;
  }}
  a {{ color: #6ee1ff; font-size: 20px; text-decoration: none; margin-top: 16px; }}
  a:hover {{ text-decoration: underline; }}
</style>
</head>
<body>
<h1>Infinity 0</h1>
<a href="{first_page}">Start reading &rarr;</a>
</body>
</html>
"""


def page_filename(index: int, asset: Asset) -> str:
    return f"page-{index:03d}-{asset.slug}.html"


def build() -> None:
    assets = discover_assets()
    if not assets:
        raise SystemExit(f"No assets found under {INPUT_BOOK_DIR}")

    PAGES_DIR.mkdir(parents=True, exist_ok=True)
    for existing in PAGES_DIR.glob("*.html"):
        existing.unlink()

    filenames = [page_filename(i, a) for i, a in enumerate(assets)]

    for i, asset in enumerate(assets):
        image_b64 = base64.b64encode(asset.image_path.read_bytes()).decode("ascii")
        prev_link = f'<a href="{filenames[i-1]}">&larr; Previous</a>' if i > 0 else ""
        next_link = f'<a href="{filenames[i+1]}">Next &rarr;</a>' if i < len(assets) - 1 else ""

        html = PAGE_TEMPLATE.format(
            title=asset.title,
            image_b64=image_b64,
            prev_link=prev_link,
            next_link=next_link,
            page_num=i + 1,
            page_count=len(assets),
        )
        (PAGES_DIR / filenames[i]).write_text(html)

    (PAGES_DIR / "index.html").write_text(INDEX_TEMPLATE.format(first_page=filenames[0]))

    print(f"Wrote {len(assets) + 1} pages to {PAGES_DIR} ({', '.join(a.title for a in assets)})")


if __name__ == "__main__":
    build()
