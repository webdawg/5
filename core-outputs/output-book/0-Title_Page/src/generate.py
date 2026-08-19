#!/usr/bin/env python3
"""Generates the Infinity 0 title page render from its design brief.

Layer order (back to front), per
core-inputs/input-book/0-Title_Page/design-brief.md:

  1. NASA Milky Way photo (public domain)          -- source-milky-way.jpg
  2. Futuristic wireframe map                        -- generated here,
     traced from the photo's actual brightness (see trace_galaxy.py)
  3. Crayon layer: a big X at the galactic center,    -- generated here
     a circle in the bottom-left corner with a kid-
     drawn stick figure ("earth"), and a bouncing
     line connecting the two. No signature.
  4. Title + author, with a radial-gradient fade      -- generated here
     lightening whatever sits directly behind them

No numpy/opencv/pip is available in this environment (checked and
confirmed missing -- see prompt-log/), so the wireframe tracing in
trace_galaxy.py is a small pure-Python/Pillow "graphics plugin" instead
of a dependency: it walks the photo's actual pixel brightness rather
than drawing an arbitrary shape unrelated to the image.

The crayon layer is procedurally generated rather than AI-generated --
no image-generation tool was available either.

Usage: python3 generate.py
Reads:  ../../../../core-inputs/input-book/0-Title_Page/source-milky-way.jpg
Writes: ../render/title-page-print.png (archives the previous render
        first -- see archive_existing_render())
"""
import math
import random
from pathlib import Path

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageOps

from trace_galaxy import galaxy_centroid, radial_silhouette, skeleton_segments
import blockfont

# 5.5in x 8.5in trade paperback trim (Infinity_0_Interview.md), at 300 DPI --
# print-resolution, per the "high-res render first" decision.
DPI = 300
CANVAS_SIZE = (int(5.5 * DPI), int(8.5 * DPI))  # (1650, 2550)

SRC_DIR = Path(__file__).resolve().parent
TITLE_PAGE_DIR = SRC_DIR.parent
INPUT_DIR = TITLE_PAGE_DIR.parent.parent.parent / "core-inputs" / "input-book" / "0-Title_Page"
RENDER_DIR = TITLE_PAGE_DIR / "render"
ARCHIVE_DIR = RENDER_DIR / "ARCHIVE"
RENDER_NAME = "title-page-print.png"

WIREFRAME_COLOR = (110, 225, 255)
CRAYON_COLOR = (225, 15, 15)  # bright red, per 2026-08-19 feedback


def fitted_source_photo() -> Image.Image:
    """The source photo cropped/scaled to exactly fill the canvas. Analysis
    (galaxy tracing) runs on a downsample of *this*, not the raw source, so
    traced points land in the same coordinate space as the final canvas."""
    src = Image.open(INPUT_DIR / "source-milky-way.jpg").convert("RGB")
    return ImageOps.fit(src, CANVAS_SIZE, centering=(0.5, 0.4))


BLACK_THRESHOLD = 35  # grayscale value below which a pixel counts as "black" background


def load_base_layer(fitted: Image.Image) -> Image.Image:
    """Per 2026-08-19 feedback: the photo's black background becomes white,
    then the whole photo is converted to black-and-white (grayscale) --
    applied only to this displayed layer, not to `fitted` itself, so the
    galaxy tracing (which needs the original brightness data) is unaffected."""
    luminance = fitted.convert("L")
    black_mask = luminance.point(lambda v: 255 if v < BLACK_THRESHOLD else 0)
    white_img = Image.new("RGB", fitted.size, (255, 255, 255))
    whitened = Image.composite(white_img, fitted, black_mask)
    return whitened.convert("L").convert("RGB")


def draw_wireframe(fitted: Image.Image, center) -> Image.Image:
    """Traces the photo's own brightness structure -- purely 2D tracing, no
    randomly-generated shapes. Two closed contour levels give the overall
    silhouette; skeleton_segments gives the actual topological skeleton of
    the bright structure (Zhang-Suen thinning, real medial axis, branching
    wherever the photo's own shape branches) -- not a fan of rays cast out
    from one point, which reads as "a rainbow", not a skeleton (see the
    2026-08-19 feedback this replaces)."""
    layer = Image.new("RGBA", CANVAS_SIZE, (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)

    for level, width in ((0.12, 2), (0.32, 3)):
        contour = radial_silhouette(fitted, center, level, n_angles=240)
        draw.line(contour + [contour[0]], fill=(*WIREFRAME_COLOR, 140), width=width, joint="curve")

    for p0, p1 in skeleton_segments(fitted, level=0.18):
        draw.line([p0, p1], fill=(*WIREFRAME_COLOR, 160), width=2)

    glow = layer.filter(ImageFilter.GaussianBlur(5))
    out = Image.alpha_composite(glow, layer)

    draw_out = ImageDraw.Draw(out)
    cx, cy = center
    tick = 16
    draw_out.line([(cx - tick, cy), (cx + tick, cy)], fill=(*WIREFRAME_COLOR, 200), width=2)
    draw_out.line([(cx, cy - tick), (cx, cy + tick)], fill=(*WIREFRAME_COLOR, 200), width=2)
    return out


RNG_SEED = 0  # deterministic render -- rerunning reproduces the same image


def _crayon_stroke(draw: ImageDraw.ImageDraw, points, color, base_width: int):
    """Thick crayon stroke with a soft outer pass, a solid core, and a light
    waxy grain pass -- per 2026-08-19 feedback that a flat smooth line lost
    too much crayon texture. The *path* stays smooth (no per-point jitter
    here); hand-drawn wobble belongs to the path itself, built by the
    caller via _wobble(), not to the stroke rendering."""
    draw.line(points, fill=(*color, 80), width=base_width + 10, joint="curve")
    draw.line(points, fill=(*color, 235), width=base_width, joint="curve")
    grain_rng = random.Random(RNG_SEED)
    for x, y in points[::3]:
        for _ in range(2):
            ox = x + grain_rng.uniform(-base_width * 0.6, base_width * 0.6)
            oy = y + grain_rng.uniform(-base_width * 0.6, base_width * 0.6)
            r = grain_rng.uniform(1, base_width * 0.25)
            draw.ellipse([ox - r, oy - r, ox + r, oy + r], fill=(*color, grain_rng.randint(40, 100)))


def _wobble(points, rng: random.Random, jitter: float):
    """Hand-drawn imperfection: every point nudged a little, independently
    -- per 2026-08-19 'the entire crayon section needs to look hand
    written' feedback. Straight lines and perfect curves read as
    typeset/vector, not drawn by a kid."""
    return [(x + rng.uniform(-jitter, jitter), y + rng.uniform(-jitter, jitter)) for x, y in points]


def _hand_drawn_circle(center, radius: float, rng: random.Random, n: int = 72, wobble: float = 0.0):
    """A real hand-drawn circle doesn't close perfectly -- the start and
    end don't quite meet, per 2026-08-19 feedback ('look up what that
    means'). Starts at a random angle, sweeps slightly more or less than a
    full turn, and each point's radius wobbles a little."""
    start_angle = rng.uniform(0, 2 * math.pi)
    sweep = 2 * math.pi * rng.uniform(0.94, 1.06)  # doesn't land exactly back on itself
    points = []
    for i in range(n + 1):
        theta = start_angle + sweep * i / n
        r = radius + rng.uniform(-wobble, wobble)
        points.append((center[0] + r * math.cos(theta), center[1] + r * math.sin(theta)))
    return points


def _jump_arc(start, end, rng: random.Random, bulge_fraction: float, n: int = 160, wobble: float = 6.0):
    """A single leaping arc from start to end -- shaped like an ellipse,
    bulging out past the busy map area into open space before landing --
    per 2026-08-19 'should look like it jumps off the map, like an
    ellipse' feedback (replaces the earlier multi-bounce path)."""
    sx, sy = start
    ex, ey = end
    mx, my = (sx + ex) / 2, (sy + ey) / 2
    length = math.hypot(ex - sx, ey - sy)
    ux, uy = (ex - sx) / length, (ey - sy) / length
    px, py = -uy, ux
    if px > 0:  # always bulge toward the left -- open space away from the busy map
        px, py = -px, -py
    bulge = length * bulge_fraction
    control = (mx + px * bulge, my + py * bulge)

    points = []
    for i in range(n + 1):
        t = i / n
        # Quadratic Bezier through start -> control -> end.
        x = (1 - t) ** 2 * sx + 2 * (1 - t) * t * control[0] + t ** 2 * ex
        y = (1 - t) ** 2 * sy + 2 * (1 - t) * t * control[1] + t ** 2 * ey
        points.append((x, y))
    return _wobble(points, rng, wobble)


def draw_crayon_layer(center) -> Image.Image:
    """A big X at the galactic center (where the child wants to go), a
    circle in the bottom-left corner with a kid-drawn stick figure
    ("earth"), and a single leaping arc connecting the two -- per
    2026-08-19 feedback. Every shape is hand-drawn-imperfect (wobbly paths,
    circles that don't quite close), not geometrically perfect. No
    wireframe-tracing (see
    core-inputs/input-book/0-Title_Page/future-ideas.md for that concept)
    and no signature/attribution note."""
    layer = Image.new("RGBA", CANVAS_SIZE, (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)
    rng = random.Random(RNG_SEED)
    cx, cy = center

    # The X, marking where the child wants to go -- small (no larger than
    # ~5% of the page), hand-drawn, circled -- per 2026-08-19 feedback
    # (a big X was the earlier, now-superseded, instruction).
    x_circle_r = CANVAS_SIZE[0] * 0.025  # 5% of page width, diameter
    x_size = x_circle_r * 0.6
    _crayon_stroke(draw, _wobble([(cx - x_size, cy - x_size), (cx + x_size, cy + x_size)], rng, 3), CRAYON_COLOR, base_width=6)
    _crayon_stroke(draw, _wobble([(cx + x_size, cy - x_size), (cx - x_size, cy + x_size)], rng, 3), CRAYON_COLOR, base_width=6)
    _crayon_stroke(draw, _hand_drawn_circle((cx, cy), x_circle_r, rng, n=48, wobble=x_circle_r * 0.05), CRAYON_COLOR, base_width=5)

    # "Earth": a circle in the bottom-left corner with a kid-drawn stick figure.
    earth_center = (CANVAS_SIZE[0] * 0.17, CANVAS_SIZE[1] * 0.88)
    earth_r = CANVAS_SIZE[0] * 0.095
    _crayon_stroke(draw, _hand_drawn_circle(earth_center, earth_r, rng, wobble=earth_r * 0.03), CRAYON_COLOR, base_width=12)

    ecx, ecy = earth_center
    head_r = earth_r * 0.26
    head_center = (ecx, ecy - earth_r * 0.4)
    _crayon_stroke(draw, _hand_drawn_circle(head_center, head_r, rng, n=32, wobble=head_r * 0.05), CRAYON_COLOR, base_width=7)

    body_top = (ecx, head_center[1] + head_r)
    body_bottom = (ecx, ecy + earth_r * 0.35)
    _crayon_stroke(draw, _wobble([body_top, body_bottom], rng, 4), CRAYON_COLOR, base_width=7)

    arm_y = body_top[1] + (body_bottom[1] - body_top[1]) * 0.3
    _crayon_stroke(draw, _wobble([(ecx, arm_y), (ecx - earth_r * 0.4, arm_y + earth_r * 0.15)], rng, 4), CRAYON_COLOR, base_width=7)
    _crayon_stroke(draw, _wobble([(ecx, arm_y), (ecx + earth_r * 0.4, arm_y + earth_r * 0.15)], rng, 4), CRAYON_COLOR, base_width=7)
    _crayon_stroke(draw, _wobble([body_bottom, (ecx - earth_r * 0.3, ecy + earth_r * 0.75)], rng, 4), CRAYON_COLOR, base_width=7)
    _crayon_stroke(draw, _wobble([body_bottom, (ecx + earth_r * 0.3, ecy + earth_r * 0.75)], rng, 4), CRAYON_COLOR, base_width=7)

    # A single leaping arc from earth to the X, ending in an arrow pointing
    # at it -- per 2026-08-19 feedback ("jumps off the map, like an
    # ellipse"; replaces the earlier multi-bounce path).
    jump_start_angle = math.atan2(cy - ecy, cx - ecx)
    jump_start = (ecx + earth_r * math.cos(jump_start_angle), ecy + earth_r * math.sin(jump_start_angle))
    jump_end_angle = math.atan2(ecy - cy, ecx - cx)
    jump_end = (cx + x_circle_r * 1.6 * math.cos(jump_end_angle), cy + x_circle_r * 1.6 * math.sin(jump_end_angle))
    arc_pts = _jump_arc(jump_start, jump_end, rng, bulge_fraction=1.3)
    _crayon_stroke(draw, arc_pts, CRAYON_COLOR, base_width=10)

    tip = arc_pts[-1]
    arrow_dir = math.atan2(tip[1] - arc_pts[-6][1], tip[0] - arc_pts[-6][0])
    arrow_len = x_circle_r * 0.9
    for spread in (0.5, -0.5):
        wing_angle = arrow_dir + math.pi + spread
        wing = (tip[0] + arrow_len * math.cos(wing_angle), tip[1] + arrow_len * math.sin(wing_angle))
        _crayon_stroke(draw, _wobble([tip, wing], rng, 3), CRAYON_COLOR, base_width=6)

    return layer


def apply_title_fade(composed: Image.Image, center, radius: int) -> Image.Image:
    """Soft radial gradient centered on the title: lightens whatever sits
    directly behind it, fading outward with no hard edge, so the title
    reads clearly without a separate plate or outline."""
    mask = Image.new("L", CANVAS_SIZE, 0)
    mdraw = ImageDraw.Draw(mask)
    for r in range(radius, 0, -4):
        opacity = int(200 * (1 - r / radius) ** 1.5)
        bbox = [center[0] - r, center[1] - r, center[0] + r, center[1] + r]
        mdraw.ellipse(bbox, fill=opacity)
    mask = mask.filter(ImageFilter.GaussianBlur(30))

    lightened = ImageEnhance.Brightness(composed.convert("RGB")).enhance(2.1)
    lightened = ImageEnhance.Contrast(lightened).enhance(0.7)
    return Image.composite(lightened.convert("RGBA"), composed, mask)


TITLE_COLOR = (15, 15, 15, 255)  # black -- reads against the now-light galactic center
TITLE_TARGET_WIDTH = int(CANVAS_SIZE[0] * 0.78)
TITLE_TOP_FRACTION = 0.125  # 2026-08-19: ~17.5% down, then moved up 5 points -- supersedes the earlier 15-20% range


def title_block_layout(title: str, author: str):
    """Custom monospace, all-caps, blocky stencil font (blockfont.py) --
    not a vendored typeface. See its module docstring. Positioned a fixed
    fraction down from the top of the page, per 2026-08-19 feedback (this
    still lands above the galactic center for a typical galaxy photo, but
    top-of-page is now the authoritative anchor, not the center)."""
    title_px = blockfont.fit_pixel_size(title.upper(), TITLE_TARGET_WIDTH)
    title_layer = blockfont.render_text(title.upper(), title_px, TITLE_COLOR)

    author_text = f"BY {author}".upper()
    author_px = max(1, title_px * 2 // 5)
    author_layer = blockfont.render_text(author_text, author_px, TITLE_COLOR)

    gap = author_px * 5
    top = int(CANVAS_SIZE[1] * TITLE_TOP_FRACTION)
    return title_layer, author_layer, gap, top


def draw_title_and_author(canvas: Image.Image, title_layer, author_layer, gap: int, top: float, center_x: float) -> None:
    tx = center_x - title_layer.width / 2
    canvas.alpha_composite(title_layer, (int(tx), int(top)))

    ax = center_x - author_layer.width / 2
    ay = top + title_layer.height + gap
    canvas.alpha_composite(author_layer, (int(ax), int(ay)))


def archive_existing_render() -> None:
    """Per the 2026-08-19 versioning instruction: before writing a new
    render, move whatever's currently there into ARCHIVE, versioned."""
    current = RENDER_DIR / RENDER_NAME
    if not current.exists():
        return
    ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)
    existing = list(ARCHIVE_DIR.glob("title-page-print-v*.png"))
    next_version = len(existing) + 1
    dest = ARCHIVE_DIR / f"title-page-print-v{next_version}.png"
    current.rename(dest)
    print(f"Archived previous render -> render/ARCHIVE/{dest.name}")


def main() -> None:
    RENDER_DIR.mkdir(parents=True, exist_ok=True)
    archive_existing_render()

    fitted = fitted_source_photo()
    center = galaxy_centroid(fitted)

    title_layer, author_layer, gap, top = title_block_layout("Infinity 0", "Agent 0")
    fade_center = (center[0], top + (title_layer.height + gap + author_layer.height) / 2)

    composed = load_base_layer(fitted).convert("RGBA")
    composed = Image.alpha_composite(composed, draw_wireframe(fitted, center))
    composed = Image.alpha_composite(composed, draw_crayon_layer(center))
    composed = apply_title_fade(composed, fade_center, radius=int(CANVAS_SIZE[0] * 0.32))

    draw_title_and_author(composed, title_layer, author_layer, gap, top, center[0])

    out_path = RENDER_DIR / RENDER_NAME
    composed.convert("RGB").save(out_path, dpi=(DPI, DPI))
    print(f"Wrote {out_path} ({CANVAS_SIZE[0]}x{CANVAS_SIZE[1]} @ {DPI} DPI)")


if __name__ == "__main__":
    main()
