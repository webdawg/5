"""A small custom font, built from scratch rather than vendored: a
monospace, uppercase-only 5x7 stencil/dot-matrix glyph set, drawn as
blocks rather than loaded from a font file. Per 2026-08-19 request --
"can we make our own font for this?" -- yes, this is it.

Monospace and all-caps aren't formatting choices applied on top of some
other font; they're structural. Every glyph occupies the same 5x7 cell,
so fixed-width is automatic, and only uppercase letters/digits/space are
defined at all, so there's no lowercase to accidentally fall back to.
"""
from PIL import Image, ImageDraw

_ROWS = 7
_COLS = 5

FONT_5x7 = {
    "0": [".###.", "#...#", "#..##", "#.#.#", "##..#", "#...#", ".###."],
    "1": ["..#..", ".##..", "..#..", "..#..", "..#..", "..#..", ".###."],
    "2": [".###.", "#...#", "....#", "...#.", "..#..", ".#...", "#####"],
    "3": [".###.", "#...#", "....#", "..##.", "....#", "#...#", ".###."],
    "4": ["...#.", "..##.", ".#.#.", "#..#.", "#####", "...#.", "...#."],
    "5": ["#####", "#....", "####.", "....#", "....#", "#...#", ".###."],
    "6": ["..##.", ".#...", "#....", "####.", "#...#", "#...#", ".###."],
    "7": ["#####", "....#", "...#.", "..#..", ".#...", ".#...", ".#..."],
    "8": [".###.", "#...#", "#...#", ".###.", "#...#", "#...#", ".###."],
    "9": [".###.", "#...#", "#...#", ".####", "....#", "...#.", ".##.."],
    "A": ["..#..", ".#.#.", "#...#", "#...#", "#####", "#...#", "#...#"],
    "B": ["####.", "#...#", "#...#", "####.", "#...#", "#...#", "####."],
    "C": [".###.", "#...#", "#....", "#....", "#....", "#...#", ".###."],
    "D": ["####.", "#...#", "#...#", "#...#", "#...#", "#...#", "####."],
    "E": ["#####", "#....", "#....", "####.", "#....", "#....", "#####"],
    "F": ["#####", "#....", "#....", "####.", "#....", "#....", "#...."],
    "G": [".###.", "#...#", "#....", "#.###", "#...#", "#...#", ".###."],
    "H": ["#...#", "#...#", "#...#", "#####", "#...#", "#...#", "#...#"],
    "I": [".###.", "..#..", "..#..", "..#..", "..#..", "..#..", ".###."],
    "J": ["..###", "...#.", "...#.", "...#.", "...#.", "#..#.", ".##.."],
    "K": ["#...#", "#..#.", "#.#..", "##...", "#.#..", "#..#.", "#...#"],
    "L": ["#....", "#....", "#....", "#....", "#....", "#....", "#####"],
    "M": ["#...#", "##.##", "#.#.#", "#...#", "#...#", "#...#", "#...#"],
    "N": ["#...#", "##..#", "#.#.#", "#..##", "#...#", "#...#", "#...#"],
    "O": [".###.", "#...#", "#...#", "#...#", "#...#", "#...#", ".###."],
    "P": ["####.", "#...#", "#...#", "####.", "#....", "#....", "#...."],
    "Q": [".###.", "#...#", "#...#", "#...#", "#.#.#", "#..#.", ".##.#"],
    "R": ["####.", "#...#", "#...#", "####.", "#.#..", "#..#.", "#...#"],
    "S": [".####", "#....", "#....", ".###.", "....#", "....#", "####."],
    "T": ["#####", "..#..", "..#..", "..#..", "..#..", "..#..", "..#.."],
    "U": ["#...#", "#...#", "#...#", "#...#", "#...#", "#...#", ".###."],
    "V": ["#...#", "#...#", "#...#", "#...#", "#...#", ".#.#.", "..#.."],
    "W": ["#...#", "#...#", "#...#", "#.#.#", "#.#.#", "#.#.#", ".#.#."],
    "X": ["#...#", "#...#", ".#.#.", "..#..", ".#.#.", "#...#", "#...#"],
    "Y": ["#...#", "#...#", ".#.#.", "..#..", "..#..", "..#..", "..#.."],
    "Z": ["#####", "....#", "...#.", "..#..", ".#...", "#....", "#####"],
    " ": [".....", ".....", ".....", ".....", ".....", ".....", "....."],
}

GLYPH_GAP_COLS = 1  # blank columns between glyphs, in cell units


def text_size(text: str, pixel_size: int) -> tuple:
    text = text.upper()
    advance = _COLS + GLYPH_GAP_COLS
    width = (len(text) * advance - GLYPH_GAP_COLS) * pixel_size if text else 0
    height = _ROWS * pixel_size
    return max(0, width), height


def render_text(text: str, pixel_size: int, color) -> Image.Image:
    """Renders uppercase, monospace, blocky stencil text onto its own
    transparent RGBA layer sized exactly to fit."""
    text = text.upper()
    width, height = text_size(text, pixel_size)
    layer = Image.new("RGBA", (max(1, width), max(1, height)), (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)
    advance = (_COLS + GLYPH_GAP_COLS) * pixel_size

    for i, ch in enumerate(text):
        glyph = FONT_5x7.get(ch, FONT_5x7[" "])
        ox = i * advance
        for row, bits in enumerate(glyph):
            for col, bit in enumerate(bits):
                if bit == "#":
                    x0 = ox + col * pixel_size
                    y0 = row * pixel_size
                    draw.rectangle([x0, y0, x0 + pixel_size - 1, y0 + pixel_size - 1], fill=color)
    return layer


def fit_pixel_size(text: str, target_width: int) -> int:
    """Largest integer pixel_size whose rendered width doesn't exceed
    target_width, so title text can be sized relative to the canvas
    instead of hardcoded."""
    advance_units = (_COLS + GLYPH_GAP_COLS) * len(text.upper()) - GLYPH_GAP_COLS
    if advance_units <= 0:
        return 1
    return max(1, target_width // advance_units)
