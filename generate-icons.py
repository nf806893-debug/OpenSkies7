#!/usr/bin/env python3
"""
generate-icons.py
Generates all required PWA + Apple Touch icons for the weather app.
Run once: python3 generate-icons.py
Requires: Pillow  (pip install pillow)
"""

import os
try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    print("Installing Pillow...")
    os.system("pip install pillow --break-system-packages -q")
    from PIL import Image, ImageDraw, ImageFont

SIZES = [152, 167, 180, 192, 512]
OUT_DIR = "icons"

os.makedirs(OUT_DIR, exist_ok=True)

for size in SIZES:
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Rounded rect background (iOS style)
    radius = size // 5
    draw.rounded_rectangle([0, 0, size - 1, size - 1], radius=radius,
                            fill=(30, 110, 200, 255))

    # Gradient-ish overlay: lighter blue at top
    for y in range(size // 2):
        alpha = int(60 * (1 - y / (size / 2)))
        draw.line([(radius if y < radius else 0, y),
                   (size - (radius if y < radius else 1), y)],
                  fill=(255, 255, 255, alpha))

    # Sun circle
    cx = size // 2
    cy = int(size * 0.42)
    r  = int(size * 0.22)
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(255, 220, 80, 255))

    # Cloud
    cloud_y = int(size * 0.55)
    cw = int(size * 0.52)
    ch = int(size * 0.18)
    cx2 = size // 2
    draw.ellipse([cx2 - cw // 2, cloud_y - ch // 2,
                  cx2 + cw // 2, cloud_y + ch // 2],
                 fill=(255, 255, 255, 230))
    draw.ellipse([cx2 - cw // 4, cloud_y - ch,
                  cx2 + cw // 4, cloud_y],
                 fill=(255, 255, 255, 230))
    draw.ellipse([cx2 + cw // 8, cloud_y - int(ch * 0.7),
                  cx2 + int(cw * 0.55), cloud_y + int(ch * 0.15)],
                 fill=(255, 255, 255, 230))

    img = img.convert("RGB")
    path = os.path.join(OUT_DIR, f"icon-{size}.png")
    img.save(path, "PNG", optimize=True)
    print(f"  ✓ {path}")

print("\nAll icons generated in ./icons/")
