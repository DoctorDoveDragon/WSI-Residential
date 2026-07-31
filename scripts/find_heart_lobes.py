#!/usr/bin/env python3
"""Find the heart lobes (top of heart canopy) y-coordinate in the current seal PNG.
The heart is red (#ab5125 or similar). Find the topmost red pixels in the central column band."""
from PIL import Image
import numpy as np

# Load current seal
im = Image.open('/home/z/my-project/download/Well_Spring_Logo_Circular_Seal.png').convert('RGB')
arr = np.array(im)
H, W = arr.shape[:2]
print(f"Seal PNG: {W}×{H}")

# Scale: 2600px design → 4063px PNG
scale = W / 2600
print(f"Scale: {scale:.4f}")

# Center is (1300,1300) in design = (1300*scale, 1300*scale) in PNG
cx_png = int(1300 * scale)
cy_png = int(1300 * scale)

# The heart is red — look for red-dominant pixels (R > G+30 and R > B+30)
# in the central column band (x from 700 to 1900 in design = 1094 to 2969 in PNG)
x1 = int(700 * scale)
x2 = int(1900 * scale)
print(f"Searching for red heart pixels in x=[{x1},{x2}]")

# Sample a red pixel — the heart is approximately #ab5125 = (171, 81, 37)
# But it might be rendered slightly differently. Let's find all reddish pixels.
r, g, b = arr[:,:,0].astype(int), arr[:,:,1].astype(int), arr[:,:,2].astype(int)
# Red-dominant: R significantly > G and B
red_mask = (r > g + 20) & (r > b + 20) & (r > 100)

# Restrict to central column band and upper half (heart is in top portion of logo)
central_band = red_mask[:cy_png, x1:x2]
print(f"Red pixels in central band, upper half: {central_band.sum()}")

if central_band.sum() > 0:
    rows_with_red = np.where(np.any(central_band, axis=1))[0]
    topmost_red_y = rows_with_red[0]
    # Convert back to design coords
    topmost_red_y_design = topmost_red_y / scale
    print(f"Topmost red (heart lobe) pixel: PNG y={topmost_red_y}, design y={topmost_red_y_design:.1f}")
    
    # Find the leftmost and rightmost red at that y
    cols_with_red = np.where(central_band[topmost_red_y, :])[0]
    leftmost_x = (cols_with_red[0] + x1) / scale
    rightmost_x = (cols_with_red[-1] + x1) / scale
    print(f"  Heart at top: x={leftmost_x:.0f} to {rightmost_x:.0f} (width {rightmost_x-leftmost_x:.0f})")
    
    # Also find the widest part of the heart (scan down a bit)
    print(f"\nHeart shape scan (top 100px):")
    for offset in range(0, 100, 10):
        y = topmost_red_y + offset
        if y < central_band.shape[0]:
            cols = np.where(central_band[y, :])[0]
            if len(cols) > 0:
                lx = (cols[0] + x1) / scale
                rx = (cols[-1] + x1) / scale
                print(f"  y={y/scale:.0f} (design): x={lx:.0f} to {rx:.0f} (width {rx-lx:.0f})")
    
    # The heart LOBES are the two bumps at the top. Find the dip between them.
    # Scan the top 60px and find where the heart is widest (lobes) vs narrow (dip)
    print(f"\nLooking for heart lobe peaks (top 60px, 2px steps):")
    for offset in range(0, 60, 2):
        y = topmost_red_y + offset
        if y < central_band.shape[0]:
            cols = np.where(central_band[y, :])[0]
            if len(cols) > 0:
                lx = (cols[0] + x1) / scale
                rx = (cols[-1] + x1) / scale
                # Find gaps (dip between lobes)
                if len(cols) > 5:
                    diffs = np.diff(cols)
                    gaps = np.where(diffs > 10)[0]
                    gap_info = f", {len(gaps)} gap(s)" if len(gaps) > 0 else ""
                    if len(gaps) > 0:
                        gap_x = (cols[gaps[0]] + x1) / scale
                        gap_info += f" at x~{gap_x:.0f}"
                else:
                    gap_info = ""
                print(f"  y={y/scale:.0f}: x={lx:.0f}-{rx:.0f} (w={rx-lx:.0f}){gap_info}")

print(f"\n--- CURRENT ROOF GEOMETRY ---")
print(f"Wall tops: y=685 (design)")
print(f"Roof peak: y=485 (design)")
print(f"Roof rise: 200px")
print(f"House walls: x=761, x=1839")
print(f"Logo content top: y=710 (design)")

# The heart lobes are somewhere around y=710-760 (top of content is 710, heart is the topmost element)
# Let's find exactly
