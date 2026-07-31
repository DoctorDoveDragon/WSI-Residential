#!/usr/bin/env python3
"""Crop the icon to its visible content bounding box (plus small margin).
This removes the asymmetric padding so the frame matches the content,
allowing it to be sized precisely to fill the house body."""
from PIL import Image
import numpy as np

src = "/home/z/my-project/download/Well_Spring_Logo_Icon.png"
dst = "/home/z/my-project/download/Well_Spring_Logo_Icon_Cropped.png"

im = Image.open(src).convert("RGB")
arr = np.array(im)
bg = arr[0, 0].astype(int)
diff = np.abs(arr.astype(int) - bg).max(axis=2)
mask = diff > 30

rows = np.any(mask, axis=1)
cols = np.any(mask, axis=0)
r = np.where(rows)[0]
c = np.where(cols)[0]

content_left, content_right = c[0], c[-1]
content_top, content_bottom = r[0], r[-1]
content_w = content_right - content_left + 1
content_h = content_bottom - content_top + 1

print(f"Original: {im.size}")
print(f"Content bbox: cols {content_left}-{content_right} ({content_w}px), rows {content_top}-{content_bottom} ({content_h}px)")
print(f"Content center: ({(content_left+content_right)//2}, {(content_top+content_bottom)//2})")

# Add 15px symmetric margin
margin = 15
crop_left = max(0, content_left - margin)
crop_top = max(0, content_top - margin)
crop_right = min(im.size[0], content_right + margin + 1)
crop_bottom = min(im.size[1], content_bottom + margin + 1)

cropped = im.crop((crop_left, crop_top, crop_right, crop_bottom))
cropped.save(dst)
print(f"\nCropped: {cropped.size} → {dst}")
print(f"Crop box: ({crop_left}, {crop_top}, {crop_right}, {crop_bottom})")

# Verify the cropped content fills the frame
arr2 = np.array(cropped)
bg2 = arr2[0, 0].astype(int)
diff2 = np.abs(arr2.astype(int) - bg2).max(axis=2)
mask2 = diff2 > 30
rows2 = np.any(mask2, axis=1)
cols2 = np.any(mask2, axis=0)
r2 = np.where(rows2)[0]
c2 = np.where(cols2)[0]
print(f"Cropped content: cols {c2[0]}-{c2[-1]} (of {cropped.size[0]}), rows {r2[0]}-{r2[-1]} (of {cropped.size[1]})")
print(f"Content fills {100*(c2[-1]-c2[0])/cropped.size[0]:.1f}% width, {100*(r2[-1]-r2[0])/cropped.size[1]:.1f}% height")
print(f"Padding: L={c2[0]}, R={cropped.size[0]-1-c2[-1]}, T={r2[0]}, B={cropped.size[1]-1-r2[-1]}")
