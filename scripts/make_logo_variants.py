#!/usr/bin/env python3
"""
Create a transparent-background variant of the Well Spring logo icon
by chroma-keying the warm peachy-cream background to transparent.

The actual background color is approximately RGB(254, 245, 230) — a warm
cream parchment. We chroma-key pixels close to this reference, with edge
feathering for clean edges.
"""
from PIL import Image

ICON_PATH = '/home/z/my-project/download/Well_Spring_Logo_Icon.png'
TRANSPARENT_OUT = '/home/z/my-project/download/Well_Spring_Logo_Icon_Transparent.png'
DARKBG_OUT = '/home/z/my-project/download/Well_Spring_Logo_Icon_DarkBg.png'

# Actual background color (sampled from corners of v5c icon)
BG_REF = (254, 245, 230)

def main():
    print(f'Loading icon: {ICON_PATH}')
    img = Image.open(ICON_PATH).convert('RGBA')
    w, h = img.size
    print(f'  Size: {w}x{h}')
    print(f'  Background reference: {BG_REF}')

    pixels = img.load()
    # Tolerance: 25 = full transparency, 45 = full opacity (edge feather)
    FULL_TRANSP_TOL = 25
    FULL_OPAQUE_TOL = 50

    trans_count = 0
    feather_count = 0
    opaque_count = 0

    for y in range(h):
        for x in range(w):
            r, g, b, a = pixels[x, y]
            # Chebyshev distance from background reference
            dist = max(abs(r - BG_REF[0]), abs(g - BG_REF[1]), abs(b - BG_REF[2]))
            if dist <= FULL_TRANSP_TOL:
                pixels[x, y] = (r, g, b, 0)
                trans_count += 1
            elif dist <= FULL_OPAQUE_TOL:
                # Feather edge: linearly interpolate alpha
                t = (dist - FULL_TRANSP_TOL) / (FULL_OPAQUE_TOL - FULL_TRANSP_TOL)
                new_a = int(255 * t)
                pixels[x, y] = (r, g, b, new_a)
                feather_count += 1
            else:
                opaque_count += 1

    img.save(TRANSPARENT_OUT, 'PNG')
    total = w * h
    print(f'✓ Transparent icon saved: {TRANSPARENT_OUT}')
    print(f'  Background pixels (α=0): {trans_count:,} ({100*trans_count/total:.1f}%)')
    print(f'  Feathered pixels (0<α<255): {feather_count:,} ({100*feather_count/total:.1f}%)')
    print(f'  Opaque pixels (α=255): {opaque_count:,} ({100*opaque_count/total:.1f}%)')

    # --- Dark background variant ---
    # Composite transparent version onto a deep walnut #2a1810 background
    dark_bg = Image.new('RGBA', img.size, (42, 24, 16, 255))
    composited = Image.alpha_composite(dark_bg, img)
    composited.convert('RGB').save(DARKBG_OUT, 'PNG')
    print(f'✓ Dark-bg icon saved: {DARKBG_OUT}')

    print('Done.')

if __name__ == '__main__':
    main()
