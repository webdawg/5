#!/usr/bin/env python3
"""Generates the title page's puzzle format variant, per The Output
Format Interviewer's 2026-09-04 round (agents/output-format-interviewer.md,
SPEC.md's "Format variants" section) -- "a puzzle version."

Same self-contained-HTML approach and same reasoning as
generate_interactive.py (no web/JS stack decided for the project yet;
stays a single dependency-free file rather than reaching for a game
framework). A tap-to-swap tile puzzle: the mobile PNG is sliced into a
grid via CSS background-position (one embedded image, no server-side
image slicing needed), shuffled client-side, solved by tapping two tiles
to swap them until every tile is back in its original position.

The generated HTML file itself is fully deterministic (same bytes every
run, same embedded image); the shuffle is intentionally *not*
deterministic -- it re-shuffles with a fresh random order every time a
player loads the page, same as any real puzzle would.

Usage: python3 generate_puzzle.py
Reads:  ../render/mobile/title-page-mobile.png (must already exist -- run
        generate_mobile.py first)
Writes: ../render/puzzle/title-page-puzzle.html (archives the previous
        file first -- see generate.py's archive_existing())
"""
import base64

import generate

MOBILE_PNG = generate.RENDER_ROOT / "mobile" / "title-page-mobile.png"
RENDER_DIR = generate.RENDER_ROOT / "puzzle"
RENDER_NAME = "title-page-puzzle.html"

GRID_COLS = 4
GRID_ROWS = 5

HTML_TEMPLATE = """<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>Infinity 0 -- Title Page (puzzle)</title>
<style>
  html, body {{
    margin: 0; min-height: 100%; background: #111; color: #eee;
    font: 16px sans-serif; display: flex; flex-direction: column;
    align-items: center; padding: 24px 0;
  }}
  h1 {{ font-size: 16px; font-weight: normal; opacity: 0.8; margin: 0 0 12px; }}
  #board {{
    display: grid;
    grid-template-columns: repeat({cols}, {tile_w}px);
    grid-template-rows: repeat({rows}, {tile_h}px);
    gap: 2px; background: #000;
  }}
  .tile {{
    width: {tile_w}px; height: {tile_h}px; cursor: pointer;
    background-image: url(data:image/png;base64,{image_b64});
    background-size: {bg_w}px {bg_h}px;
    outline: 2px solid transparent;
  }}
  .tile.selected {{ outline: 2px solid #6ee1ff; }}
  #status {{ margin-top: 14px; opacity: 0.85; }}
  #status.won {{ color: #6ee1ff; }}
</style>
</head>
<body>
<h1>Tap two tiles to swap them. Solve the title page.</h1>
<div id="board"></div>
<div id="status">shuffling...</div>
<script>
(function () {{
  var cols = {cols}, rows = {rows}, n = cols * rows;
  var board = document.getElementById('board');
  var statusEl = document.getElementById('status');
  var order = [];      // order[slot] = which original tile index sits in this slot
  var selected = null;

  for (var i = 0; i < n; i++) order.push(i);
  // Fisher-Yates -- fresh shuffle every page load, on purpose (see
  // generate_puzzle.py's docstring).
  for (var i = n - 1; i > 0; i--) {{
    var j = Math.floor(Math.random() * (i + 1));
    var t = order[i]; order[i] = order[j]; order[j] = t;
  }}

  var tiles = [];
  for (var slot = 0; slot < n; slot++) {{
    var el = document.createElement('div');
    el.className = 'tile';
    el.dataset.slot = slot;
    board.appendChild(el);
    tiles.push(el);
  }}

  function bgPosition(tileIndex) {{
    var c = tileIndex % cols, r = Math.floor(tileIndex / cols);
    var px = cols === 1 ? 0 : (c / (cols - 1)) * 100;
    var py = rows === 1 ? 0 : (r / (rows - 1)) * 100;
    return px + '% ' + py + '%';
  }}

  function render() {{
    for (var slot = 0; slot < n; slot++) {{
      tiles[slot].style.backgroundPosition = bgPosition(order[slot]);
    }}
    var solved = order.every(function (v, i) {{ return v === i; }});
    statusEl.textContent = solved ? 'solved!' : (n + ' tiles -- ' + order.filter(function (v, i) {{ return v === i; }}).length + ' in place');
    statusEl.className = solved ? 'won' : '';
  }}

  board.addEventListener('click', function (e) {{
    var el = e.target.closest('.tile');
    if (!el) return;
    var slot = parseInt(el.dataset.slot, 10);
    if (selected === null) {{
      selected = slot;
      el.classList.add('selected');
      return;
    }}
    if (selected !== slot) {{
      var tmp = order[selected]; order[selected] = order[slot]; order[slot] = tmp;
    }}
    tiles[selected].classList.remove('selected');
    selected = null;
    render();
  }});

  render();
}})();
</script>
</body>
</html>
"""


def main() -> None:
    if not MOBILE_PNG.exists():
        raise SystemExit(f"{MOBILE_PNG} doesn't exist -- run generate_mobile.py first")

    from PIL import Image
    with Image.open(MOBILE_PNG) as im:
        bg_w, bg_h = im.size

    tile_w, tile_h = bg_w // GRID_COLS, bg_h // GRID_ROWS

    RENDER_DIR.mkdir(parents=True, exist_ok=True)
    generate.archive_existing(RENDER_DIR, RENDER_NAME)

    image_b64 = base64.b64encode(MOBILE_PNG.read_bytes()).decode("ascii")
    html = HTML_TEMPLATE.format(
        cols=GRID_COLS, rows=GRID_ROWS,
        tile_w=tile_w, tile_h=tile_h,
        bg_w=bg_w, bg_h=bg_h,
        image_b64=image_b64,
    )

    out_path = RENDER_DIR / RENDER_NAME
    out_path.write_text(html)
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
