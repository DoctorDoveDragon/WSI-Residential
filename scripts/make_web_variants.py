#!/usr/bin/env python3
"""
make_web_variants.py — Produce web-optimized PNG sizes for all lockups.

For each source PNG in /home/z/my-project/download/ matching the pattern
Well_Spring_Logo_Lockup*.png, produce three web-optimized variants:
  - <base>_1200.png  (1200 wide — desktop retina / tablet landscape)
  - <base>_600.png   (600 wide  — tablet portrait / mobile retina)
  - <base>_300.png   (300 wide  — mobile non-retina / footer)

Downscaling uses LANCZOS (best quality) for both RGB and RGBA variants.

Also produces:
  - Well_Spring_Logo_Circular_Seal_Square_512.png  (512x512 — Android)
  - Well_Spring_Logo_Circular_Seal_Square_180.png  (180x180 — Apple touch)
  - Well_Spring_Logo_Circular_Seal_Square_32.png   (32x32   — favicon std)
  - Well_Spring_Logo_Circular_Seal_Square_16.png   (16x16   — favicon tiny)
  - favicon.ico (multi-resolution: 16, 32, 48)
  - Well_Spring_Logo_Icon_512.png / _180.png / _32.png / _16.png
  - apple-touch-icon.png (180x180 from seal, no transparency for iOS)
  - android-chrome-512x512.png (from seal, no transparency per spec)
  - android-chrome-192x192.png (from seal, no transparency per spec)
"""
from PIL import Image
import os
import glob

DL = '/home/z/my-project/download'

# Define the lockup sources and their target widths
LOCKUP_SOURCES = [
    # Source filename (no path) -> base name for outputs
    ('Well_Spring_Logo_Lockup.png',                          'Well_Spring_Logo_Lockup'),
    ('Well_Spring_Logo_Lockup_Residential.png',              'Well_Spring_Logo_Lockup_Residential'),
    ('Well_Spring_Logo_Lockup_Transparent.png',              'Well_Spring_Logo_Lockup_Transparent'),
    ('Well_Spring_Logo_Lockup_Residential_Transparent.png',  'Well_Spring_Logo_Lockup_Residential_Transparent'),
]
TARGET_WIDTHS = [1200, 600, 300]

print('=== Web-optimized lockup variants ===')
for src_name, base in LOCKUP_SOURCES:
    src_path = os.path.join(DL, src_name)
    if not os.path.exists(src_path):
        print(f'  SKIP {src_name} (not found)')
        continue
    im = Image.open(src_path)
    print(f'  {src_name}: {im.size} {im.mode}')
    for w in TARGET_WIDTHS:
        # Compute target height preserving aspect ratio
        h = int(im.height * (w / im.width))
        if im.mode == 'RGBA':
            thumb = im.resize((w, h), Image.LANCZOS)
        else:
            thumb = im.convert('RGB').resize((w, h), Image.LANCZOS)
        out = os.path.join(DL, f'{base}_{w}.png')
        thumb.save(out, 'PNG', optimize=True)
        print(f'    -> {os.path.basename(out)} ({w}x{h}, {os.path.getsize(out) // 1024} KB)')

print()
print('=== Favicons from residential seal ===')
SEAL_SRC = os.path.join(DL, 'Well_Spring_Logo_Circular_Seal_Square.png')  # 4063x4063 RGB
seal = Image.open(SEAL_SRC).convert('RGB')
print(f'  Source: {SEAL_SRC} ({seal.size})')

# Standard favicon sizes (rendered on a white background — favicons typically
# look better with a solid bg than transparent on browser tab bars)
FAV_SIZES = [16, 32, 48, 180, 192, 512]
for s in FAV_SIZES:
    thumb = seal.resize((s, s), Image.LANCZOS)
    # Save under conventional name
    if s == 16:
        out = os.path.join(DL, 'favicon-16x16.png')
    elif s == 32:
        out = os.path.join(DL, 'favicon-32x32.png')
    elif s == 48:
        out = os.path.join(DL, 'favicon-48x48.png')
    elif s == 180:
        out = os.path.join(DL, 'apple-touch-icon.png')
    elif s == 192:
        out = os.path.join(DL, 'android-chrome-192x192.png')
    elif s == 512:
        out = os.path.join(DL, 'android-chrome-512x512.png')
    thumb.save(out, 'PNG', optimize=True)
    print(f'    -> {os.path.basename(out)} ({s}x{s}, {os.path.getsize(out) // 1024} KB)')

# Multi-resolution .ico (16, 32, 48 embedded)
ico_sizes = [(16, 16), (32, 32), (48, 48)]
seal_ico = Image.open(SEAL_SRC).convert('RGBA')
ico_path = os.path.join(DL, 'favicon.ico')
seal_ico.save(ico_path, format='ICO', sizes=ico_sizes)
print(f'    -> favicon.ico (multi-res 16/32/48, {os.path.getsize(ico_path) // 1024} KB)')

print()
print('=== Favicons from general icon (bonus) ===')
ICON_SRC = os.path.join(DL, 'Well_Spring_Logo_Icon.png')  # 1024x1024 RGB
icon = Image.open(ICON_SRC).convert('RGB')
print(f'  Source: {ICON_SRC} ({icon.size})')
for s in [16, 32, 180, 512]:
    thumb = icon.resize((s, s), Image.LANCZOS)
    out = os.path.join(DL, f'Well_Spring_Logo_Icon_{s}.png')
    thumb.save(out, 'PNG', optimize=True)
    print(f'    -> {os.path.basename(out)} ({s}x{s}, {os.path.getsize(out) // 1024} KB)')

print()
print('=== site.webmanifest ===')
manifest = {
    'name': 'Well Spring Intervention LLC',
    'short_name': 'Well Spring',
    'description': 'Level III Residential Treatment Facility (Staff-Secure) for Children and Adolescents in North Carolina.',
    'start_url': '/',
    'display': 'standalone',
    'background_color': '#faeddc',
    'theme_color': '#6b4d3f',
    'icons': [
        {'src': '/android-chrome-192x192.png', 'sizes': '192x192', 'type': 'image/png'},
        {'src': '/android-chrome-512x512.png', 'sizes': '512x512', 'type': 'image/png'},
        {'src': '/apple-touch-icon.png',        'sizes': '180x180', 'type': 'image/png'},
    ],
}
import json
manifest_path = os.path.join(DL, 'site.webmanifest')
with open(manifest_path, 'w') as f:
    json.dump(manifest, f, indent=2)
print(f'  -> {os.path.basename(manifest_path)}')

print()
print('Done.')
