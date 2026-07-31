"""Compute new geometry for SOP-39:
1. Raise roof peak to same distance from center as wall corners (r=998)
2. Add ceiling line connecting the two top corner vertices
3. Place "Residential" text in the bottom half inside the inner circle
"""
import math

CENTER = (1300, 1300)
INNER_R = 1040  # inner hairline radius
URL_R = 1100    # URL text circle radius

# Current house geometry (from SOP-38)
wall_x_left = 642
wall_x_right = 1958
floor_y = 2050
wall_top_y = 550
cur_peak_y = 501

# Wall corner distance from center
wall_dx = wall_x_right - CENTER[0]  # 658
corner_dy = floor_y - CENTER[1]     # 750
corner_dist = math.sqrt(wall_dx**2 + corner_dy**2)
print(f"Wall corner distance from center: {corner_dist:.1f}")
print(f"Current roof peak distance from center: {CENTER[1] - cur_peak_y}")
print()

# === CHANGE 1: Raise peak to same distance as wall corners ===
target_peak_dist = corner_dist  # 997.7
new_peak_y = CENTER[1] - round(target_peak_dist)
new_rise = wall_top_y - new_peak_y
new_angle = math.degrees(math.atan(new_rise / wall_dx))
print(f"=== CHANGE 1: Raise peak ===")
print(f"  New peak: ({CENTER[0]}, {new_peak_y})")
print(f"  New peak distance from center: {CENTER[1] - new_peak_y} (was {CENTER[1] - cur_peak_y})")
print(f"  Wall corner distance:          {corner_dist:.1f}")
print(f"  Match: {'YES' if abs((CENTER[1] - new_peak_y) - corner_dist) < 1 else 'NO'}")
print(f"  New roof rise: {new_rise}px above wall tops (was {wall_top_y - cur_peak_y}px)")
print(f"  New roof angle: {new_angle:.2f}° (was {math.degrees(math.atan((wall_top_y - cur_peak_y) / wall_dx)):.2f}°)")
print(f"  Peak clearance from inner hairline r={INNER_R}: {INNER_R - (CENTER[1] - new_peak_y)}px (was {INNER_R - (CENTER[1] - cur_peak_y)}px)")
print()

# Check roof doesn't overlap URL text
# URL text at 12:00: baseline y=200, ascenders to y=105, descenders to y=230
url_descender_y = CENTER[1] - URL_R + 32  # ~232
print(f"  URL text descenders at y≈{url_descender_y}")
print(f"  Roof peak at y={new_peak_y}")
print(f"  Gap (peak below URL descenders): {new_peak_y - url_descender_y}px ✓" if new_peak_y > url_descender_y else f"  OVERLAP!")
print()

# Check roof doesn't overlap heart canopy
# Heart lobes at y=583 (from SOP-38), wall tops at y=550
heart_top_y = 583
print(f"  Heart lobes top: y={heart_top_y}")
print(f"  Wall tops: y={wall_top_y} (heart is {wall_top_y - heart_top_y}px below wall tops — heart in body)")
print(f"  Ceiling line at y={wall_top_y} separates roof from body")
print(f"  Roof is entirely above y={wall_top_y}; heart is below — no overlap ✓")
print()

# === CHANGE 2: Ceiling line connecting top corner vertices ===
print(f"=== CHANGE 2: Ceiling line ===")
print(f"  Line from ({wall_x_left}, {wall_top_y}) to ({wall_x_right}, {wall_top_y})")
print(f"  Horizontal line at y={wall_top_y}, length {wall_x_right - wall_x_left}px")
print(f"  Stroke: 15px walnut-brown (matches house walls)")
print(f"  This creates a triangular attic (roof) above and rectangular body below")
print()

# === CHANGE 3: "Residential" text in bottom half inside the circle ===
print(f"=== CHANGE 3: 'Residential' text ===")
# Place on r=950 circle (inside inner hairline r=1040)
RES_R = 950
res_baseline_y = CENTER[1] + RES_R  # 2250 at 6:00
icon_bottom_y = 2044  # icon image bottom
inner_hairline_bottom_y = CENTER[1] + INNER_R  # 2340

# Try font sizes
print(f"  Target: text inside inner hairline (r<{INNER_R}), below icon (y>{icon_bottom_y})")
print(f"  Baseline at r={RES_R}, y={res_baseline_y} at 6:00")
print()
print(f"  Font | CapTop_y | CapTop_r | Icon_clr | Desc_y | Desc_r | IHairline_clr")
for font_px in [90, 100, 110, 120, 130]:
    cap_h = font_px * 0.7
    desc = font_px * 0.25
    cap_top_y = res_baseline_y - cap_h
    cap_top_r = RES_R - cap_h
    desc_y = res_baseline_y + desc
    desc_r = RES_R + desc
    icon_clr = cap_top_y - icon_bottom_y
    ih_clr = inner_hairline_bottom_y - desc_y
    print(f"  {font_px:3d}px | {cap_top_y:7.1f} | {cap_top_r:7.1f} | {icon_clr:7.1f} | {desc_y:5.1f} | {desc_r:5.1f} | {ih_clr:6.1f}")

print()
# Choose 110px — good balance: matches URL prominence, fits with clearance
CHOSEN_FONT = 110
cap_h = CHOSEN_FONT * 0.7
desc = CHOSEN_FONT * 0.25
print(f"=== CHOSEN: {CHOSEN_FONT}px font on r={RES_R} ===")
print(f"  Baseline: y={res_baseline_y} (r={RES_R})")
print(f"  Cap top:  y={res_baseline_y - cap_h:.1f} (r={RES_R - cap_h:.1f}) — {res_baseline_y - cap_h - icon_bottom_y:.1f}px below icon bottom ✓")
print(f"  Descenders: y={res_baseline_y + desc:.1f} (r={RES_R + desc:.1f}) — {inner_hairline_bottom_y - (res_baseline_y + desc):.1f}px above inner hairline ✓")
print(f"  Ornament at y=2400 (r=1100): {2400 - (res_baseline_y + desc):.1f}px below descenders ✓")
print()

# Text arc length
text = "Residential"
char_count = len(text)
letter_spacing = 22  # proportional to URL's 28px at 132px font
# Approximate char advance: font_px * 0.55 + letter_spacing
char_advance = CHOSEN_FONT * 0.55 + letter_spacing
text_width = char_count * char_advance
circumference = 2 * math.pi * RES_R
arc_fraction = text_width / circumference
arc_degrees = arc_fraction * 360
print(f"  Text: '{text}' ({char_count} chars)")
print(f"  Letter-spacing: {letter_spacing}px")
print(f"  Approx text width: {text_width:.0f}px")
print(f"  Circle circumference (r={RES_R}): {circumference:.0f}px")
print(f"  Arc fraction: {arc_fraction:.1%} = {arc_degrees:.1f}°")
print(f"  Centered at 6:00, spans from {6 - arc_degrees/2/15:.2f}:00 to {6 + arc_degrees/2/15:.2f}:00")
print(f"  Clears accent dots at 9:00 and 3:00 ✓")
print()

# SVG path for Residential text
# r=950 circle, center (1300,1300)
# 9:00 = (1300-950, 1300) = (350, 1300)
# 3:00 = (1300+950, 1300) = (2250, 1300)
# Path from 9:00 to 3:00 through 6:00 (sweep=0 in SVG screen coords)
print(f"=== SVG path for 'Residential' ===")
print(f'  <path id="residential-circle" d="M 350,1300 A 950,950 0 0,0 2250,1300" fill="none" />')
print(f"  startOffset=50%, text-anchor=middle → centered at 6:00")
print(f"  Text reads left-to-right (upright) at 6:00 ✓")
