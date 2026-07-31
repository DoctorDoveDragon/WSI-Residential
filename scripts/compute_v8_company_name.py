"""Compute geometry for SOP-40:
1. Replace URL on top arc with company name "Well Spring Intervention LLC"
2. Add website URL "www.wellspringintervention.com" below the circle (outside it)
"""
import math

# Current canvas: 2600×2600, seal center (1300, 1300), outer hairline r=1225
# Outer circle bottom: y = 1300 + 1225 = 2525
# Canvas bottom: 2600
# Available space below circle: 2600 - 2525 = 75px (not enough for text)

# Plan: Enlarge canvas to 2600×2800 (add 200px at bottom)
# Seal center stays at (1300, 1300)
# New available space below outer circle: 2800 - 2525 = 275px

print("=== CANVAS ENLARGEMENT ===")
print(f"  Old: 2600×2600 (square)")
print(f"  New: 2600×2800 (added 200px at bottom)")
print(f"  Seal center stays at (1300, 1300)")
print(f"  Outer circle bottom y=2525, canvas bottom y=2800")
print(f"  Available space for URL: 275px")
print()

# === CHANGE 1: Company name on top arc ===
print("=== CHANGE 1: Company name on top arc ===")
print('  Old text: "www.wellspringintervention.com" (30 chars)')
print('  New text: "Well Spring Intervention LLC" (28 chars)')
print("  Same circle r=1100, same font 132px Playfair Display 900, same letter-spacing 28px")
print("  Same startOffset=25% (centered at 12:00)")
print()

# Verify new text fits — approximate width
text = "Well Spring Intervention LLC"
char_count = len(text)
font_px = 132
letter_spacing = 28
# Approximate char advance for Playfair Display 900: font_px * 0.55 + letter_spacing
char_advance = font_px * 0.55 + letter_spacing
text_width = char_count * char_advance
circumference = 2 * math.pi * 1100
arc_fraction = text_width / circumference
arc_degrees = arc_fraction * 360
print(f"  Approx text width: {text_width:.0f}px")
print(f"  Circle circumference (r=1100): {circumference:.0f}px")
print(f"  Arc fraction: {arc_fraction:.1%} = {arc_degrees:.1f}°")
print(f"  Centered at 12:00, spans from {12 - arc_degrees/2/30:.2f}:00 to {12 + arc_degrees/2/30:.2f}:00")
print(f"  Clears accent dots at 9:00 and 3:00 ✓")
print()

# === CHANGE 2: Website URL below the circle ===
print("=== CHANGE 2: Website URL below the circle ===")
print('  Text: "www.wellspringintervention.com"')
print("  Position: OUTSIDE outer hairline (r=1225), at bottom of canvas")
print()

# Available vertical space: y=2525 (outer circle bottom) to y=2800 (canvas bottom) = 275px
# Choose font size that fits with margins
# Use 90px (smaller than the 132px company name on top — it's secondary info)
url_font = 90
url_letter_spacing = 10
url_text = "www.wellspringintervention.com"
url_char_count = len(url_text)
url_char_advance = url_font * 0.55 + url_letter_spacing
url_text_width = url_char_count * url_char_advance
print(f"  Font: {url_font}px Playfair Display 700 (lighter weight than 900 on top)")
print(f"  Letter-spacing: {url_letter_spacing}px (tighter than 28px on top)")
print(f"  Approx text width: {url_text_width:.0f}px")
print(f"  Canvas width: 2600px, text centered at x=1300")
print(f"  Text spans x={1300 - url_text_width/2:.0f} to x={1300 + url_text_width/2:.0f}")
print(f"  Margin from canvas edges: {1300 - url_text_width/2:.0f}px left/right ✓")
print()

# Vertical position
# Cap height ≈ 0.7 * font_px = 63px
# Descender ≈ 0.25 * font_px = 22.5px
# Want: 60px margin from outer circle bottom (y=2525), centered in available space
url_cap_h = url_font * 0.7
url_desc = url_font * 0.25
url_baseline_y = 2525 + 60 + url_cap_h  # 2525 + 60 + 63 = 2648
# Or center in available space: midpoint of (2525, 2800) = 2662, baseline = 2662 + (cap_h - desc)/2 = 2662 + 20 = 2682
url_baseline_y = 2680  # nice round number, centered
url_cap_top_y = url_baseline_y - url_cap_h
url_desc_y = url_baseline_y + url_desc
print(f"  Baseline y: {url_baseline_y}")
print(f"  Cap top y:  {url_cap_top_y:.1f} ({url_cap_top_y - 2525:.1f}px below outer circle bottom) ✓")
print(f"  Descenders y: {url_desc_y:.1f} ({2800 - url_desc_y:.1f}px above canvas bottom) ✓")
print()

# Add flanking ornament to balance composition
print("  Flanking ornament (optional, for balance):")
print(f"    Two short rules at y={url_baseline_y - url_cap_h/2:.0f} (vertical center of text)")
print(f"    Left rule:  x=200 to x=400, stroke 4px walnut-brown opacity 0.5")
print(f"    Right rule: x=2200 to x=2400, stroke 4px walnut-brown opacity 0.5")
print(f"    Endpoint terracotta dots at (200, y) and (2400, y), r=8")
print()

# === HTML structure changes ===
print("=== HTML STRUCTURE CHANGES ===")
print("1. .poster width/height: 2600×2600 → 2600×2800")
print("2. .seal-svg: keep at 2600×2600 (top-aligned, covers seal area only)")
print("3. .icon-wrap: change from top:50%/left:50% to absolute top:1300/left:1300")
print("   (so icon stays centered on (1300,1300) matching seal SVGs)")
print("4. URL textPath content: 'www.wellspringintervention.com' → 'Well Spring Intervention LLC'")
print("5. Add new <div class='bottom-url'> with 'www.wellspringintervention.com' below circle")
