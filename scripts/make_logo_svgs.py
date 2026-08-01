#!/usr/bin/env python3
"""
make_logo_svgs.py — Generate self-contained SVG versions of both logo lockups.

Each SVG:
  - viewBox 0 0 1792 560 (matches HTML .poster dimensions)
  - Transparent background (for overlay on any color)
  - Embedded base64 PNG icon (transparent variant — works on any bg)
  - Vector <text> elements positioned to match the HTML lockup layout
  - Font-family chains: "Cormorant Garamond" / "Playfair Display" / "Tinos" /
    "Times New Roman" / serif for the wordmark; "Inter" / "Helvetica Neue" /
    "Arial" / sans-serif for subtitles. Browsers with Google Fonts loaded will
    use the actual fonts; otherwise fallbacks render close enough.

Outputs (both self-contained, ~500 KB each due to embedded PNG):
  /home/z/my-project/download/Well_Spring_Logo_Lockup.svg
  /home/z/my-project/download/Well_Spring_Logo_Lockup_Residential.svg

Also produces linked variants (icon referenced by relative URL — ~10 KB each,
requires the icon PNG to sit alongside the SVG):
  /home/z/my-project/download/Well_Spring_Logo_Lockup_Linked.svg
  /home/z/my-project/download/Well_Spring_Logo_Lockup_Residential_Linked.svg
"""
import base64
import os

DL = '/home/z/my-project/download'

# Layout constants (match logo_lockup.html / logo_lockup_residential.html)
VIEWBOX_W = 1792
VIEWBOX_H = 560
POSTER_PAD_LEFT = 64
POSTER_PAD_RIGHT = 80
ICON_SIZE = 420
GAP = 56

WORDMARK_X = POSTER_PAD_LEFT + ICON_SIZE + GAP  # = 540

# Vertical positions (baseline coordinates — text-anchor=start, dominant-baseline=alphabetic)
# Layout (top to bottom), all centered vertically in 560px viewport.
# Content block height ≈ 250px → starts at y≈155, ends at y≈405.
Y_MAIN = 240       # "Well Spring Intervention" 96px serif
Y_DIVIDER = 258    # top of divider (60x2)
Y_SUB = 295        # "LEVEL III RESIDENTIAL TREATMENT FACILITY · STAFF-SECURE" 20px
Y_SUB2 = 318       # "OUTPATIENT THERAPY · CASE MANAGEMENT · ..." 16px
Y_TAG = 348        # italic tagline 16px
Y_EMAIL = 385      # email 22px serif

# Colors
C_WALNUT = '#6b4d3f'
C_TERRACOTTA = '#ab5125'

def b64(path: str) -> str:
    with open(path, 'rb') as f:
        return base64.b64encode(f.read()).decode('ascii')

def make_svg(icon_src_abs: str, icon_src_rel: str, self_contained: bool) -> str:
    if self_contained:
        icon_data = f'data:image/png;base64,{b64(icon_src_abs)}'
    else:
        icon_data = icon_src_rel

    # Escape ampersands in text (we use &middot; in HTML; in SVG use the actual char)
    middot = '\u00b7'  # ·

    svg = f'''<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
     viewBox="0 0 {VIEWBOX_W} {VIEWBOX_H}" width="{VIEWBOX_W}" height="{VIEWBOX_H}" role="img"
     aria-label="Well Spring Intervention LLC — Level III Residential Treatment Facility, Staff-Secure">

  <!-- Background: transparent (overlay on any color) -->
  <rect x="0" y="0" width="{VIEWBOX_W}" height="{VIEWBOX_H}" fill="none"/>

  <!-- Icon (transparent PNG, 420x420, vertically centered) -->
  <image x="{POSTER_PAD_LEFT}" y="{(VIEWBOX_H - ICON_SIZE) // 2}"
         width="{ICON_SIZE}" height="{ICON_SIZE}"
         preserveAspectRatio="xMidYMid meet"
         xlink:href="{icon_data}"/>

  <!-- Wordmark block -->
  <g font-family="'Cormorant Garamond','Playfair Display','Tinos','Times New Roman',serif">

    <!-- Main: "Well Spring Intervention" — 96px, weight 600, walnut brown -->
    <text x="{WORDMARK_X}" y="{Y_MAIN}"
          font-size="96" font-weight="600" fill="{C_WALNUT}"
          letter-spacing="0.5" text-rendering="geometricPrecision">
      Well Spring <tspan fill="{C_TERRACOTTA}">Intervention</tspan>
    </text>

    <!-- Divider: 60x2 terracotta rule -->
    <rect x="{WORDMARK_X}" y="{Y_DIVIDER}" width="60" height="2" fill="{C_TERRACOTTA}"/>

    <!-- Subtitle 1: "LEVEL III RESIDENTIAL TREATMENT FACILITY · STAFF-SECURE" -->
    <text x="{WORDMARK_X}" y="{Y_SUB}"
          font-family="'Inter','Helvetica Neue','Arial',sans-serif"
          font-size="20" font-weight="500" fill="{C_WALNUT}"
          letter-spacing="5" opacity="0.78"
          text-rendering="geometricPrecision">
      LEVEL III RESIDENTIAL TREATMENT FACILITY {middot} STAFF-SECURE
    </text>

    <!-- Subtitle 2: services line -->
    <text x="{WORDMARK_X}" y="{Y_SUB2}"
          font-family="'Inter','Helvetica Neue','Arial',sans-serif"
          font-size="16" font-weight="500" fill="{C_WALNUT}"
          letter-spacing="3" opacity="0.62"
          text-rendering="geometricPrecision">
      OUTPATIENT THERAPY <tspan fill="{C_TERRACOTTA}" opacity="0.9"> {middot} </tspan> CASE MANAGEMENT <tspan fill="{C_TERRACOTTA}" opacity="0.9"> {middot} </tspan> PSYCHOSOCIAL REHABILITATION
    </text>

    <!-- Tagline (italic terracotta) -->
    <text x="{WORDMARK_X}" y="{Y_TAG}"
          font-family="'Inter','Helvetica Neue','Arial',sans-serif"
          font-size="16" font-weight="400" font-style="italic" fill="{C_TERRACOTTA}"
          letter-spacing="1"
          text-rendering="geometricPrecision">
      Empowerment {middot} Growth {middot} Freedom {middot} Health {middot} Wholeness {middot} Healing
    </text>

    <!-- Email -->
    <text x="{WORDMARK_X}" y="{Y_EMAIL}"
          font-size="22" font-weight="500" fill="{C_WALNUT}"
          letter-spacing="0.5"
          text-rendering="geometricPrecision">
      referral<tspan fill="{C_TERRACOTTA}">@</tspan>wellspringintervention.com
    </text>

  </g>

  <title>Well Spring Intervention LLC — Level III Residential Treatment Facility (Staff-Secure)</title>
  <desc>Horizontal logo lockup: transparent icon at left, wordmark with services descriptor, tagline, and referral email at right. Transparent background for overlay on any color.</desc>
</svg>
'''
    return svg

# Source PNGs (transparent variants)
SOURCES = [
    {
        'name': 'Well_Spring_Logo_Lockup',
        'icon_abs': f'{DL}/Well_Spring_Logo_Icon_Transparent.png',
        'icon_rel': 'Well_Spring_Logo_Icon_Transparent.png',
    },
    {
        'name': 'Well_Spring_Logo_Lockup_Residential',
        'icon_abs': f'{DL}/Well_Spring_Logo_Circular_Seal_Transparent.png',
        'icon_rel': 'Well_Spring_Logo_Circular_Seal_Transparent.png',
    },
]

for src in SOURCES:
    # Self-contained (embedded base64)
    svg_sc = make_svg(src['icon_abs'], src['icon_rel'], self_contained=True)
    out_sc = f'{DL}/{src["name"]}.svg'
    with open(out_sc, 'w', encoding='utf-8') as f:
        f.write(svg_sc)
    print(f'  -> {os.path.basename(out_sc)} ({os.path.getsize(out_sc) // 1024} KB, self-contained)')

    # Linked (relative URL — much smaller)
    svg_lk = make_svg(src['icon_abs'], src['icon_rel'], self_contained=False)
    out_lk = f'{DL}/{src["name"]}_Linked.svg'
    with open(out_lk, 'w', encoding='utf-8') as f:
        f.write(svg_lk)
    print(f'  -> {os.path.basename(out_lk)} ({os.path.getsize(out_lk)} bytes, linked)')

print('Done.')
