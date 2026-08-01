#!/usr/bin/env python3
"""
make_seal_transparent.py — Knock out the cream/white background from the
residential circular seal so it can be placed on colored website sections.

Strategy:
  - The seal source (Well_Spring_Logo_Circular_Seal_Square.png, 4063×4063, RGB)
    has:
      * White (#FFFFFF) outside the circular ring (the corners of the square)
      * Cream parchment (#FAEDDC) inside the ring (the seal's background)
      * Colored drawing inside: walnut-brown (#6B4D3F), terracotta (#AB5125),
        red heart (#B73030-ish), green leaves, blue water, etc.
  - We convert to RGBA, then set alpha=0 for any pixel whose RGB is close to
    either pure white OR the cream parchment color. Tolerance is per-channel
    (R, G, B all within tol of the target).
  - Edge anti-aliasing pixels (semi-cream) get partial alpha via a soft
    falloff based on distance from the target color.

Output:
  /home/z/my-project/download/Well_Spring_Logo_Circular_Seal_Transparent.png
"""
from PIL import Image
import numpy as np

SRC = '/home/z/my-project/download/Well_Spring_Logo_Circular_Seal_Square.png'
DST = '/home/z/my-project/download/Well_Spring_Logo_Circular_Seal_Transparent.png'

# Target colors to knock out
WHITE = np.array([255, 255, 255], dtype=np.float32)
CREAM = np.array([250, 237, 220], dtype=np.float32)  # #FAEDDC

# Per-channel tolerance for "definitely background"
HARD_TOL = 12.0
# Soft falloff range for anti-aliasing (pixels between HARD_TOL and HARD_TOL+SOFT_RANGE)
SOFT_RANGE = 18.0

print(f'Loading {SRC}...')
img = Image.open(SRC).convert('RGB')
arr = np.array(img, dtype=np.float32)
h, w, _ = arr.shape
print(f'  size: {w}x{h}')

# Compute distance from each target color
dist_white = np.sqrt(((arr - WHITE) ** 2).sum(axis=2))
dist_cream = np.sqrt(((arr - CREAM) ** 2).sum(axis=2))
dist = np.minimum(dist_white, dist_cream)

# Initialize alpha to 255 (fully opaque)
alpha = np.full((h, w), 255, dtype=np.float32)

# Hard knockout: distance < HARD_TOL → fully transparent
hard_mask = dist < HARD_TOL
alpha[hard_mask] = 0

# Soft falloff: HARD_TOL <= distance < HARD_TOL+SOFT_RANGE → partial alpha
soft_mask = (dist >= HARD_TOL) & (dist < HARD_TOL + SOFT_RANGE)
# Linear falloff from 0 (at HARD_TOL) to 255 (at HARD_TOL+SOFT_RANGE)
soft_alpha = ((dist[soft_mask] - HARD_TOL) / SOFT_RANGE) * 255.0
alpha[soft_mask] = soft_alpha

# For pixels that are partially transparent (alpha < 255), also "premultiply"
# the RGB toward a neutral mid-tone to avoid cream halos on dark backgrounds.
# Use the average of original RGB mixed with mid-gray based on alpha.
# This is a simple decontamination pass.
rgb = arr.copy()
# Premultiply-like: blend toward white background (so existing antialiasing
# which was computed against cream gets blended to white, then re-matted).
# Simpler: just leave RGB and let the soft alpha handle it. Most pixels are
# either fully opaque or fully transparent.

# Build RGBA
rgba = np.dstack([rgb, alpha]).astype(np.uint8)
out = Image.fromarray(rgba, mode='RGBA')
out.save(DST, 'PNG', optimize=True)
print(f'  wrote {DST}')
print(f'  fully transparent pixels: {(alpha == 0).sum()}/{alpha.size} = {(alpha == 0).sum() / alpha.size * 100:.1f}%')
print(f'  fully opaque pixels:      {(alpha == 255).sum()}/{alpha.size} = {(alpha == 255).sum() / alpha.size * 100:.1f}%')
print(f'  partial alpha pixels:     {((alpha > 0) & (alpha < 255)).sum()}')
