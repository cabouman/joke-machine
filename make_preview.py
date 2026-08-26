#!/usr/bin/env python3
"""Draw the logo and the link-preview card for the Joke Machine.

Writes two files:

    docs/preview.png   1200x630, the picture messaging apps show
    docs/favicon.png   512x512, the browser tab and home screen icon

Run it before build_site.py if you change the look.

    python3 make_preview.py
"""

import json
import pathlib

from PIL import Image, ImageDraw, ImageFont

HERE = pathlib.Path(__file__).parent
DATA = HERE / "jokes.json"
OUT = HERE / "docs"

GOLD = (207, 185, 145)
CREAM = (250, 248, 244)
INK = (27, 26, 23)
MUTED = (98, 88, 71)

FONT_BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
FONT_PLAIN = "/System/Library/Fonts/Supplemental/Arial.ttf"


def draw_face(img, cx, cy, r):
    """Draw a round smiling face centred at (cx, cy) with radius r."""
    d = ImageDraw.Draw(img)

    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=CREAM)

    # Eyes: two rounded rectangles, which read as friendlier than dots.
    eye_dx = r * 0.36
    eye_y = cy - r * 0.22
    eye_w = r * 0.115
    eye_h = r * 0.30
    for sx in (-1, 1):
        ex = cx + sx * eye_dx
        d.rounded_rectangle(
            [ex - eye_w, eye_y - eye_h / 2, ex + eye_w, eye_y + eye_h / 2],
            radius=eye_w,
            fill=INK,
        )

    # Smile: the lower part of a circle, drawn thick.
    mouth_r = r * 0.60
    d.arc(
        [cx - mouth_r, cy - mouth_r * 0.55, cx + mouth_r, cy + mouth_r * 1.15],
        start=25,
        end=155,
        fill=INK,
        width=int(r * 0.11),
    )

    # Cheeks.
    cheek_r = r * 0.13
    for sx in (-1, 1):
        px = cx + sx * r * 0.60
        py = cy + r * 0.22
        d.ellipse(
            [px - cheek_r, py - cheek_r * 0.72, px + cheek_r, py + cheek_r * 0.72],
            fill=(232, 168, 150),
        )


def centred(d, text, font, cx, y, fill):
    left, top, right, bottom = d.textbbox((0, 0), text, font=font)
    d.text((cx - (right - left) / 2 - left, y - top), text, font=font, fill=fill)
    return bottom - top


def make_preview(title, subtitle, site_url):
    W, H = 1200, 630
    img = Image.new("RGB", (W, H), GOLD)
    d = ImageDraw.Draw(img)

    draw_face(img, W // 2, 215, 130)

    f_title = ImageFont.truetype(FONT_BOLD, 82)
    f_sub = ImageFont.truetype(FONT_PLAIN, 34)
    f_url = ImageFont.truetype(FONT_PLAIN, 26)

    centred(d, title, f_title, W // 2, 388, INK)
    centred(d, subtitle, f_sub, W // 2, 492, MUTED)
    centred(d, site_url, f_url, W // 2, 556, MUTED)

    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / "preview.png"
    img.save(path)
    return path, img.size


def make_favicon():
    # Draw large and shrink, so the curves come out smooth.
    S = 1024
    img = Image.new("RGB", (S, S), GOLD)
    draw_face(img, S // 2, S // 2, int(S * 0.40))
    img = img.resize((512, 512), Image.LANCZOS)

    path = OUT / "favicon.png"
    img.save(path)
    return path, img.size


def main():
    data = json.loads(DATA.read_text(encoding="utf-8"))
    site = data["site_url"].replace("https://", "").rstrip("/")

    for path, size in (
        make_preview(data["title"], data["tagline_short"], site),
        make_favicon(),
    ):
        print(f"Wrote {path}  ({size[0]}x{size[1]})")


if __name__ == "__main__":
    main()
