#!/usr/bin/env python3
"""Find the actual visible content bounding box in the icon PNG.
The icon has a warm cream background (#faeddc or similar). Find the bbox
of all pixels that differ from the background."""
from PIL import Image
import numpy as np

icon_path = "/home/z/my-project/download/Well_Spring_Logo_Icon.png"
im = Image.open(icon_path).convert("RGB")
arr = np.array(im)
print(f"Icon size: {im.size}")
print(f"Corner pixels (BG sample): TL={arr[0,0]}, TR={arr[0,-1]}, BL={arr[-1,0]}, BR={arr[-1,-1]}")

# Background reference: average of the 4 corners
bg = arr[0,0].astype(int)
print(f"BG reference (TL corner): {bg}")

# Chebyshev distance from BG for each pixel
diff = np.abs(arr.astype(int) - bg).max(axis=2)  # max channel diff
threshold = 30  # pixels that differ by >30 in any channel are "content"
mask = diff > threshold

# Find content bbox
rows = np.any(mask, axis=1)
cols = np.any(mask, axis=0)
rmin, rmax = np.where(rows)[0][[0, -1]]
cmin, cmax = np.where(cols)[0][[0, -1]]

print(f"\nContent bounding box (threshold={threshold}):")
print(f"  Rows: {rmin} to {rmax} (height {rmax-rmin+1}px)")
print(f"  Cols: {cmin} to {cmax} (width {cmax-cmin+1}px)")
print(f"  Content size: {cmax-cmin+1} × {rmax-rmin+1}")
print(f"  Padding: left={cmin}, right={im.size[0]-1-cmax}, top={rmin}, bottom={im.size[1]-1-rmax}")

content_w = cmax - cmin + 1
content_h = rmax - rmin + 1
frame_w, frame_h = im.size
print(f"\nContent fills {100*content_w/frame_w:.1f}% of frame width, {100*content_h/frame_h:.1f}% of frame height")

# Now compute: if icon is placed at 920×920 in the 1900×1900 seal (centered at 950,950),
# where does the actual CONTENT sit?
seal_center = (950, 950)
icon_size_in_seal = 920
scale = icon_size_in_seal / frame_w
content_w_seal = content_w * scale
content_h_seal = content_h * scale
# Content is centered in the icon frame, so in seal coords:
content_left = seal_center[0] - content_w_seal / 2
content_right = seal_center[0] + content_w_seal / 2
content_top = seal_center[1] - content_h_seal / 2
content_bottom = seal_center[1] + content_h_seal / 2

print(f"\n--- In seal coordinates (icon at 920×920, centered 950,950) ---")
print(f"  Content spans: ({content_left:.0f}, {content_top:.0f}) to ({content_right:.0f}, {content_bottom:.0f})")
print(f"  Content size in seal: {content_w_seal:.0f} × {content_h_seal:.0f}")

# House walls (current snug design)
house = {
    "wall_left": 450, "wall_right": 1450,
    "floor": 1460, "wall_top": 440, "roof_peak_y": 200
}
print(f"\n  House walls: x={house['wall_left']},{house['wall_right']}  floor y={house['floor']}  wall_top y={house['wall_top']}")

print(f"\n--- ACTUAL clearance: house to VISIBLE content ---")
print(f"  Left:   content_left={content_left:.0f} → wall={house['wall_left']}  → gap = {content_left - house['wall_left']:.0f}px")
print(f"  Right:  wall={house['wall_right']} → content_right={content_right:.0f}  → gap = {house['wall_right'] - content_right:.0f}px")
print(f"  Bottom: content_bottom={content_bottom:.0f} → floor={house['floor']}  → gap = {house['floor'] - content_bottom:.0f}px")
print(f"  Top:    wall_top={house['wall_top']} → content_top={content_top:.0f}  → gap = {content_top - house['wall_top']:.0f}px")

# What house would be truly snug to the visible content (with 30px margin)?
margin = 30
snug_walls = {
    "left":  content_left - margin,
    "right": content_right + margin,
    "floor": content_bottom + margin,
    "wall_top": content_top - margin,
}
print(f"\n--- To be TRULY snug (30px margin to visible content) ---")
print(f"  Walls: x={snug_walls['left']:.0f}, x={snug_walls['right']:.0f}")
print(f"  Floor: y={snug_walls['floor']:.0f}")
print(f"  Wall tops: y={snug_walls['wall_top']:.0f}")
# Verify these are inside inner hairline r=860
import math
for corner_name, (x, y) in [("wall_top_left", (snug_walls['left'], snug_walls['wall_top'])),
                              ("wall_top_right", (snug_walls['right'], snug_walls['wall_top'])),
                              ("floor_left", (snug_walls['left'], snug_walls['floor'])),
                              ("floor_right", (snug_walls['right'], snug_walls['floor']))]:
    d = math.sqrt((x-950)**2 + (y-950)**2)
    print(f"  {corner_name} ({x:.0f},{y:.0f}): dist={d:.1f}  {'INSIDE r=860 ✓' if d<=860 else 'OUTSIDE r=860 ✗'}")
