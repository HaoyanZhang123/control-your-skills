# -*- coding: utf-8 -*-
"""生成 README 封面 assets/cover.png（1600×420）。

画面上只有品牌标记与仓库名，没有标语和说明文字。
需要 Pillow 与 Windows 自带字体（Arial Black / Segoe UI）。
"""
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

W, H = 1600, 420
BG = (251, 251, 247)
INK = (0, 63, 103)
SOFT = (86, 122, 148)
GRID = (234, 236, 232)
WHITE = (255, 255, 255)
FONTS = Path("C:/Windows/Fonts")

TITLE = "control-your-skills"


def font(name, size):
    try:
        return ImageFont.truetype(str(FONTS / name), size)
    except OSError:
        return ImageFont.load_default()


def fit(d, text, name, start, max_w):
    size = start
    while size > 16 and d.textlength(text, font=font(name, size)) > max_w:
        size -= 1
    return font(name, size), size


def grid_bg(d):
    for x in range(0, W, 34):
        d.line([(x, 0), (x, H)], fill=GRID, width=1)
    for y in range(0, H, 34):
        d.line([(0, y), (W, y)], fill=GRID, width=1)


def marker(d, x, y, size):
    d.rounded_rectangle([x, y, x + size, y + size], radius=int(size * 0.26), fill=INK)
    p = size * 0.28
    w = max(2, size // 12)
    d.line([(x + p, y + p), (x + size - p, y + size - p)], fill=WHITE, width=w)
    d.line([(x + size - p, y + p), (x + p, y + size - p)], fill=WHITE, width=w)


def build():
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)

    grid_bg(d)
    d.rectangle([0, 0, W, 5], fill=INK)

    for r in range(3):
        for c in range(7):
            cx, cy = 1245 + c * 30, 84 + r * 30
            d.ellipse([cx - 2.5, cy - 2.5, cx + 2.5, cy + 2.5], fill=(206, 224, 238))

    marker(d, 96, 54, 46)
    d.text((158, 64), "DSH / DEVELOPER TOOLKIT",
           font=font("segoeuib.ttf", 15), fill=SOFT)

    ft, ts = fit(d, TITLE, "ariblk.ttf", 132, 1300)
    ty = 132
    d.text((94, ty), TITLE, font=ft, fill=INK)

    underline_y = ty + int(ts * 1.2) + 26
    d.line([(96, underline_y), (96 + 300, underline_y)], fill=INK, width=11)

    return im


if __name__ == "__main__":
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).with_name("cover.png")
    out.parent.mkdir(parents=True, exist_ok=True)
    img = build()
    img.save(out, "PNG", optimize=True)
    print(f"wrote {out} ({out.stat().st_size} bytes, {img.width}x{img.height})")
