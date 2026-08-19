"""A small, dependency-free "graphics plugin" for tracing an image's actual
bright structure, used to make the title page's wireframe match the real
galaxy photo instead of drawing an abstract shape unrelated to it.

No numpy/opencv/scipy is available in this environment (no pip either --
checked directly), so this is pure Python + Pillow: radial ray-marching
against real pixel brightness, not a real edge-detector, but genuinely
derived from the image rather than a fixed formula.
"""
import math

from PIL import Image, ImageFilter

ANALYSIS_WIDTH = 300


def _analysis_grayscale(fitted: Image.Image):
    """Downsample the (already canvas-fitted) source photo for fast pixel
    access. Returns (image, scale) where scale maps analysis-space
    coordinates back to the full canvas."""
    w, h = fitted.size
    analysis_height = max(1, int(ANALYSIS_WIDTH * h / w))
    small = fitted.convert("L").resize((ANALYSIS_WIDTH, analysis_height), Image.BILINEAR)
    scale = w / ANALYSIS_WIDTH
    return small, scale


def galaxy_centroid(fitted: Image.Image):
    """Brightness-weighted centroid, in full canvas coordinates -- the
    actual visual center of the galaxy in the photo, not a guessed point."""
    small, scale = _analysis_grayscale(fitted)
    w, h = small.size
    px = small.load()
    sx = sy = sw = 0.0
    for y in range(h):
        for x in range(w):
            v = px[x, y]
            if v > 40:  # ignore near-black background/noise floor
                sx += x * v
                sy += y * v
                sw += v
    if sw == 0:
        return w * scale / 2, h * scale / 2
    return (sx / sw) * scale, (sy / sw) * scale


def _peak_brightness(small: Image.Image) -> int:
    w, h = small.size
    px = small.load()
    peak = 0
    for y in range(h):
        for x in range(w):
            if px[x, y] > peak:
                peak = px[x, y]
    return peak


def _smooth_closed(points, passes: int = 2):
    """Light moving-average smoothing around the closed loop -- the analysis
    image is coarse enough that per-angle threshold crossings are a little
    jittery; this keeps the traced shape a clean contour instead of a
    single-pixel-jagged one, without hiding the real asymmetry."""
    pts = points
    for _ in range(passes):
        n = len(pts)
        pts = [
            (
                (pts[(i - 1) % n][0] + pts[i][0] + pts[(i + 1) % n][0]) / 3,
                (pts[(i - 1) % n][1] + pts[i][1] + pts[(i + 1) % n][1]) / 3,
            )
            for i in range(n)
        ]
    return pts


def radial_silhouette(fitted: Image.Image, center, level: float, n_angles: int = 240, gap_tolerance: int = 5):
    """For each of n_angles directions from center, ray-march outward in the
    actual photo and return the edge of the *contiguous* bright region at
    that brightness level -- stops at the first run of `gap_tolerance`
    consecutive below-threshold pixels, so an isolated bright star or noise
    pixel far down the ray doesn't drag the contour out to it. Traces the
    photo's real silhouette -- bigger toward a bright spiral arm, smaller
    toward empty sky -- rather than a circle or a noise-driven starburst.
    Returns points in full canvas coordinates, closed-loop order (by angle).
    """
    small, scale = _analysis_grayscale(fitted)
    w, h = small.size
    px = small.load()
    threshold = _peak_brightness(small) * level

    cx, cy = center[0] / scale, center[1] / scale
    max_r = max(w, h)
    points = []
    for i in range(n_angles):
        theta = 2 * math.pi * i / n_angles
        dx, dy = math.cos(theta), math.sin(theta)
        last_hit = 1.0
        miss_run = 0
        r = 1.0
        while r < max_r:
            x, y = int(cx + dx * r), int(cy + dy * r)
            if 0 <= x < w and 0 <= y < h and px[x, y] > threshold:
                last_hit = r
                miss_run = 0
            else:
                miss_run += 1
                if miss_run > gap_tolerance and last_hit > 1.0:
                    break
            r += 1.0
        points.append((cx + dx * last_hit, cy + dy * last_hit))

    return [(x * scale, y * scale) for x, y in _smooth_closed(points)]


def radial_segments(fitted: Image.Image, center, level: float, n_angles: int = 240,
                     gap_tolerance: int = 2, min_segment: float = 3):
    """Like radial_silhouette, but returns *every* contiguous bright segment
    along each ray, not just the first. A real galaxy photo has gaps
    between filaments/spiral-arm strands; each separate bright run along a
    ray becomes its own (inner_point, outer_point) segment. Drawing all of
    them gives a genuinely branching/filament-like structure derived purely
    from the photo's 2D brightness -- no randomness, no synthesized shape --
    per the 2026-08-19 "go back to 2d tracing" feedback.
    """
    small, scale = _analysis_grayscale(fitted)
    w, h = small.size
    px = small.load()
    threshold = _peak_brightness(small) * level

    cx, cy = center[0] / scale, center[1] / scale
    max_r = max(w, h)
    all_segments = []
    for i in range(n_angles):
        theta = 2 * math.pi * i / n_angles
        dx, dy = math.cos(theta), math.sin(theta)
        segments = []
        in_segment = False
        seg_start = last_bright_r = 0.0
        miss_run = 0
        r = 1.0
        while r < max_r:
            x, y = int(cx + dx * r), int(cy + dy * r)
            bright = 0 <= x < w and 0 <= y < h and px[x, y] > threshold
            if bright:
                if not in_segment:
                    in_segment = True
                    seg_start = r
                last_bright_r = r
                miss_run = 0
            elif in_segment:
                miss_run += 1
                if miss_run > gap_tolerance:
                    if last_bright_r - seg_start >= min_segment:
                        segments.append((seg_start, last_bright_r))
                    in_segment = False
            r += 1.0
        if in_segment and last_bright_r - seg_start >= min_segment:
            segments.append((seg_start, last_bright_r))

        for r0, r1 in segments:
            p0 = ((cx + dx * r0) * scale, (cy + dy * r0) * scale)
            p1 = ((cx + dx * r1) * scale, (cy + dy * r1) * scale)
            all_segments.append((p0, p1))
    return all_segments


def _zhang_suen_thin(grid, w, h):
    """Classic Zhang-Suen thinning: repeatedly strips foreground pixels that
    aren't needed to keep the shape's topology, until only a 1-pixel-wide
    skeleton remains. Reference: Zhang & Suen, 1984, "A fast parallel
    algorithm for thinning digital patterns"."""
    changed = True
    while changed:
        changed = False
        for step in (1, 2):
            to_clear = []
            for y in range(1, h - 1):
                row = grid[y]
                for x in range(1, w - 1):
                    if row[x] != 1:
                        continue
                    p2, p3, p4 = grid[y - 1][x], grid[y - 1][x + 1], grid[y][x + 1]
                    p5, p6, p7 = grid[y + 1][x + 1], grid[y + 1][x], grid[y + 1][x - 1]
                    p8, p9 = grid[y][x - 1], grid[y - 1][x - 1]
                    seq = (p2, p3, p4, p5, p6, p7, p8, p9)
                    b = sum(seq)
                    if b < 2 or b > 6:
                        continue
                    a = sum(1 for i in range(8) if seq[i] == 0 and seq[(i + 1) % 8] == 1)
                    if a != 1:
                        continue
                    if step == 1:
                        if p2 * p4 * p6 != 0 or p4 * p6 * p8 != 0:
                            continue
                    else:
                        if p2 * p4 * p8 != 0 or p2 * p6 * p8 != 0:
                            continue
                    to_clear.append((y, x))
            if to_clear:
                changed = True
                for y, x in to_clear:
                    grid[y][x] = 0
    return grid


def skeleton_segments(fitted: Image.Image, level: float, analysis_width: int = 220):
    """The galaxy's actual topological skeleton -- a real medial-axis trace
    of its bright structure via Zhang-Suen thinning, not lines cast out
    from one point (a fan of rays reads as "a rainbow", not a skeleton;
    see the 2026-08-19 feedback this replaces). Branches wherever the
    photo's own bright shape branches. Returns (p0, p1) line segments
    between adjacent skeleton pixels, in full canvas coordinates.
    """
    w0, h0 = fitted.size
    h = max(1, int(analysis_width * h0 / w0))
    # A slight blur before thresholding merges isolated noise/star pixels
    # into the smooth shapes around them instead of leaving them as
    # disconnected skeleton litter after thinning.
    small = fitted.convert("L").resize((analysis_width, h), Image.BILINEAR).filter(ImageFilter.GaussianBlur(2))
    scale = w0 / analysis_width
    px = small.load()
    threshold = _peak_brightness(small) * level

    grid = [[1 if px[x, y] > threshold else 0 for x in range(analysis_width)] for y in range(h)]
    _zhang_suen_thin(grid, analysis_width, h)

    segments = []
    forward_offsets = ((1, 0), (0, 1), (1, 1), (1, -1))
    for y in range(h):
        row = grid[y]
        for x in range(analysis_width):
            if row[x] != 1:
                continue
            for dx, dy in forward_offsets:
                nx, ny = x + dx, y + dy
                if 0 <= nx < analysis_width and 0 <= ny < h and grid[ny][nx] == 1:
                    segments.append(((x * scale, y * scale), (nx * scale, ny * scale)))
    return segments
