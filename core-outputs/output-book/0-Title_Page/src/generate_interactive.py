#!/usr/bin/env python3
"""Generates the title page's animated/interactive format variant, per
The Output Format Interviewer's 2026-09-04 round
(agents/output-format-interviewer.md, SPEC.md's "Format variants"
section) -- "a moving animated version that users can move if they
want."

No web/JS technology stack has been decided for this project generally
(that's SPEC.md Fan-out territory -- a whole webpage *output type* -- not
this role's job, which is a format variant of the already-decided title
page image). To stay a variant rather than accidentally becoming a new
output type, this is a single self-contained HTML file: one PNG embedded
as a base64 data URI, vanilla CSS/JS only, no build step, no external
requests, no framework decision made on the project's behalf. If a real
interactive webpage output type gets scoped later, this can be superseded
by it -- see this file's "Open questions" cross-reference in
agents/output-format-interviewer.md.

"Animated": a slow, continuous ambient zoom/breathe on the artwork.
"Users can move it": click-and-drag panning, plus scroll-wheel/pinch
zoom, independent of the ambient animation.

Usage: python3 generate_interactive.py
Reads:  ../render/web/title-page-web.png (must already exist -- run
        generate_web.py first)
Writes: ../render/interactive/title-page-interactive.html (archives the
        previous file first -- see generate.py's archive_existing())
"""
import base64

import generate

WEB_PNG = generate.RENDER_ROOT / "web" / "title-page-web.png"
RENDER_DIR = generate.RENDER_ROOT / "interactive"
RENDER_NAME = "title-page-interactive.html"

HTML_TEMPLATE = """<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>Infinity 0 -- Title Page (interactive)</title>
<style>
  html, body {{ margin: 0; height: 100%; background: #111; overflow: hidden; }}
  #viewport {{
    width: 100%; height: 100%; overflow: hidden; cursor: grab;
    display: flex; align-items: center; justify-content: center;
  }}
  #viewport:active {{ cursor: grabbing; }}
  #pan {{ transform-origin: center center; will-change: transform; }}
  #art {{
    display: block; max-width: none;
    animation: breathe 6s ease-in-out infinite;
  }}
  @keyframes breathe {{
    0%, 100% {{ transform: scale(1); }}
    50% {{ transform: scale(1.03); }}
  }}
  #hint {{
    position: fixed; bottom: 12px; left: 50%; transform: translateX(-50%);
    color: #ddd; font: 13px sans-serif; opacity: 0.7; pointer-events: none;
  }}
</style>
</head>
<body>
<div id="viewport">
  <div id="pan"><img id="art" src="data:image/png;base64,{image_b64}" alt="Infinity 0 title page"></div>
</div>
<div id="hint">drag to move &middot; scroll/pinch to zoom</div>
<script>
(function () {{
  var pan = document.getElementById('pan');
  var viewport = document.getElementById('viewport');
  var x = 0, y = 0, scale = 1;
  var dragging = false, lastX = 0, lastY = 0;

  function apply() {{
    pan.style.transform = 'translate(' + x + 'px,' + y + 'px) scale(' + scale + ')';
  }}

  viewport.addEventListener('mousedown', function (e) {{
    dragging = true; lastX = e.clientX; lastY = e.clientY;
  }});
  window.addEventListener('mousemove', function (e) {{
    if (!dragging) return;
    x += e.clientX - lastX; y += e.clientY - lastY;
    lastX = e.clientX; lastY = e.clientY;
    apply();
  }});
  window.addEventListener('mouseup', function () {{ dragging = false; }});

  viewport.addEventListener('touchstart', function (e) {{
    if (e.touches.length !== 1) return;
    dragging = true; lastX = e.touches[0].clientX; lastY = e.touches[0].clientY;
  }}, {{ passive: true }});
  viewport.addEventListener('touchmove', function (e) {{
    if (!dragging || e.touches.length !== 1) return;
    x += e.touches[0].clientX - lastX; y += e.touches[0].clientY - lastY;
    lastX = e.touches[0].clientX; lastY = e.touches[0].clientY;
    apply();
  }}, {{ passive: true }});
  viewport.addEventListener('touchend', function () {{ dragging = false; }});

  viewport.addEventListener('wheel', function (e) {{
    e.preventDefault();
    scale = Math.min(3, Math.max(0.5, scale - e.deltaY * 0.001));
    apply();
  }}, {{ passive: false }});
}})();
</script>
</body>
</html>
"""


def main() -> None:
    if not WEB_PNG.exists():
        raise SystemExit(f"{WEB_PNG} doesn't exist -- run generate_web.py first")

    RENDER_DIR.mkdir(parents=True, exist_ok=True)
    generate.archive_existing(RENDER_DIR, RENDER_NAME)

    image_b64 = base64.b64encode(WEB_PNG.read_bytes()).decode("ascii")
    html = HTML_TEMPLATE.format(image_b64=image_b64)

    out_path = RENDER_DIR / RENDER_NAME
    out_path.write_text(html)
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
