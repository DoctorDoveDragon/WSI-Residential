"""Compute optimal scale factor to fit house + logo inside the inner circle.

Current state (canvas 2600x2600, center (1300,1300)):
- Inner hairline circle: r=1040 (stroke 15px → visual inner edge ~1032.5)
- House wall corners at (761, 1915) etc., distance from center = sqrt(539^2 + 615^2) = 817.8
- Roof peak (1300, 645), distance = 655
- Logo display 1070x1220, content 1029x1180, 25px margins inside house

Goal: scale house + logo together (preserve their relative proportions) so the
house fills the inner circle with comfortable breathing room.

Constraints:
- Wall corners (top & bottom) must stay inside inner hairline r=1040 with >=30px clearance
- Roof peak must stay inside inner hairline with clearance
- House must not overlap URL text circle r=1100
- Heart lobes (logo content top y=712, dist=588 above center) must stay below wall tops
- Roof peak must stay "slightly above" heart lobes
"""
import math

CENTER = (1300, 1300)
INNER_R = 1040  # inner hairline radius
URL_R = 1100    # URL text circle radius

# Current house geometry (relative to center)
cur_wall_dx = 539       # |761 - 1300|
cur_corner_dy = 615     # |1915 - 1300| = |685 - 1300|
cur_peak_dy = 655       # |645 - 1300|
cur_corner_dist = math.sqrt(cur_wall_dx**2 + cur_corner_dy**2)
print(f"Current wall corner distance from center: {cur_corner_dist:.1f}")
print(f"Current roof peak distance from center:   {cur_peak_dy}")
print(f"Current clearance (corner to inner r={INNER_R}): {INNER_R - cur_corner_dist:.1f}px")
print(f"Current clearance (peak to inner r={INNER_R}):  {INNER_R - cur_peak_dy}px")
print()

# Heart lobes: top at y=712 (distance 588 above center)
cur_heart_top_dy = 588  # |712 - 1300|

# Test scale factors
print("Scale | Corner_r | Corner_clr | Peak_r | Peak_clr | Heart_clr_walltop | Heart_clr_peak | Logo_disp")
print("-" * 110)
for scale in [1.15, 1.18, 1.20, 1.22, 1.24, 1.26]:
    corner_dist = cur_corner_dist * scale
    corner_clr = INNER_R - corner_dist
    peak_dist = cur_peak_dy * scale
    peak_clr = INNER_R - peak_dist
    # Heart lobes top distance above center after scale
    heart_top_dy = cur_heart_top_dy * scale
    # Wall tops distance above center after scale
    wall_top_dy = cur_corner_dy * scale
    # Clearance: wall tops above heart lobes (positive = good, heart is below wall tops)
    heart_to_walltop = wall_top_dy - heart_top_dy  # how far wall top is above heart top
    # Roof peak above heart lobes
    heart_to_peak = peak_dist - heart_top_dy  # how far peak is above heart top
    logo_w = 1070 * scale
    logo_h = 1220 * scale
    print(f"  {scale:.2f} | {corner_dist:7.1f} | {corner_clr:9.1f} | {peak_dist:6.1f} | {peak_clr:7.1f} | {heart_to_walltop:17.1f} | {heart_to_peak:14.1f} | {logo_w:.0f}x{logo_h:.0f}")

print()
print("Target: corner clearance 35-60px (comfortable, not cramped)")
print("        heart_to_walltop > 15px (heart in body, not roof zone)")
print("        heart_to_peak > 50px (roof slightly above heart)")
print()

# Pick scale = 1.22 (corner clearance ~42px, well-balanced)
SCALE = 1.22
print(f"=== CHOSEN SCALE: {SCALE} ===")
print()
print("New house geometry (rounded to integers):")
new_wall_dx = round(cur_wall_dx * SCALE)
new_corner_dy = round(cur_corner_dy * SCALE)
new_peak_dy = round(cur_peak_dy * SCALE)
new_heart_top_dy = cur_heart_top_dy * SCALE

wall_x_left = CENTER[0] - new_wall_dx
wall_x_right = CENTER[0] + new_wall_dx
floor_y = CENTER[1] + new_corner_dy
wall_top_y = CENTER[1] - new_corner_dy
peak_y = CENTER[1] - new_peak_dy

print(f"  Walls: x={wall_x_left}, x={wall_x_right}  (width {2*new_wall_dx})")
print(f"  Floor: y={floor_y}")
print(f"  Wall tops: y={wall_top_y}")
print(f"  Roof peak: ({CENTER[0]}, {peak_y})  (rise {wall_top_y - peak_y}px above wall tops)")
print(f"  Roof angle: {math.degrees(math.atan((wall_top_y - peak_y) / new_wall_dx)):.2f}°")
print()
print("Verification:")
new_corner_dist = math.sqrt(new_wall_dx**2 + new_corner_dy**2)
print(f"  Wall corner distance from center: {new_corner_dist:.1f} (clearance {INNER_R - new_corner_dist:.1f}px from inner r={INNER_R})")
print(f"  Roof peak distance from center:   {new_peak_dy} (clearance {INNER_R - new_peak_dy}px from inner r={INNER_R})")
print(f"  Wall corner distance from URL circle r={URL_R}: {URL_R - new_corner_dist:.1f}px clearance")
print(f"  Heart lobes top y={CENTER[1] - new_heart_top_dy:.1f}, wall tops y={wall_top_y}")
print(f"    → wall tops are {wall_top_y - (CENTER[1] - new_heart_top_dy):.1f}px ABOVE heart lobes (heart in body ✓)")
print(f"  Heart lobes top y={CENTER[1] - new_heart_top_dy:.1f}, roof peak y={peak_y}")
print(f"    → roof peak is {(CENTER[1] - new_heart_top_dy) - peak_y:.1f}px ABOVE heart lobes (\"slightly above\" ✓)")
print()
print("New logo display size:")
print(f"  {round(1070*SCALE)}x{round(1220*SCALE)} (was 1070x1220)")
print(f"  Logo content: {round(1029*SCALE)}x{round(1180*SCALE)} (was 1029x1180)")
print()
print("Margins between logo content and house walls (should stay ~25-30px):")
logo_content_w = 1029 * SCALE
logo_content_h = 1180 * SCALE
margin_x = (2*new_wall_dx - logo_content_w) / 2
margin_y_top = (new_corner_dy - (1180*SCALE)/2) - (1180*SCALE)/2 + (1180*SCALE)  # simplified below
# Logo content centered at (1300,1300), spans (1300 - logo_content_w/2, 1300 - logo_content_h/2) to (1300 + logo_content_w/2, 1300 + logo_content_h/2)
content_left = CENTER[0] - logo_content_w/2
content_top = CENTER[1] - logo_content_h/2
content_bottom = CENTER[1] + logo_content_h/2
margin_left = content_left - wall_x_left
margin_right = wall_x_right - (CENTER[0] + logo_content_w/2)
margin_top = wall_top_y - content_top  # wall top above content top
margin_bottom = floor_y - content_bottom
print(f"  Left margin:   {margin_left:.1f}px")
print(f"  Right margin:  {margin_right:.1f}px")
print(f"  Top margin:    {margin_top:.1f}px (wall top to content top)")
print(f"  Bottom margin: {margin_bottom:.1f}px (floor to content bottom)")
print()
print("Recommended house stroke (scaled from 12.5px):")
print(f"  {round(12.5 * SCALE)}px (matches the 15px hairlines for visual consistency)")
