#!/usr/bin/env python3
"""Render the conference's typographic sharing image (requires Pillow)."""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
SCALE = 2
BLUE = "#2c5697"
DARK = "#1b365d"
LIGHT = "#96c8e6"
WHITE = "#ffffff"

card = Image.new("RGB", (1200 * SCALE, 630 * SCALE), WHITE)
draw = ImageDraw.Draw(card)


def text(x, y, value, size, colour=DARK, weight=400):
    font = ImageFont.truetype(str(ROOT / "static/fonts/Rubik-Variable.ttf"), size * SCALE)
    font.set_variation_by_axes([weight])
    draw.text((x * SCALE, y * SCALE), value, font=font, fill=colour, anchor="lt")


text(64, 90, "Nordic", 30, BLUE)
text(64, 138, "Research Software Engineering", 64, weight=500)
text(64, 224, "Conference 2027", 32)
text(64, 334, "15–16 June 2027", 34, BLUE, 500)
text(64, 389, "Delta Centre, Tartu, Estonia", 26)

draw.line([(64 * SCALE, 552 * SCALE), (1140 * SCALE, 552 * SCALE)], fill=LIGHT, width=SCALE)
text(64, 564, "Organized by University of Tartu, Institute of Computer Science,", 19)
text(64, 591, "Nordic-RSE and ELIXIR Estonia", 19)

output = ROOT / "static/social-card.png"
card.resize((1200, 630), Image.Resampling.LANCZOS).save(output, optimize=True)
print(output)
