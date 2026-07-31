#!/usr/bin/env python3
"""Compute the optimal icon size to fill the v4 house snugly.
v4 house: walls x=380/1520, floor y=1550, wall tops y=650, roof peak (950,350).
Icon content: 761×872 in 1024 frame (74.22% width, 85.16% height).
Content center offset: (+35, +31)px from frame center in 1024 frame.

Constraints (keep content inside house body, allow canopy in roof zone):
  - content_bottom ≤ floor - margin_bottom
  - content_left ≥ wall_left + margin_side
  - content_right ≤ wall_right - margin_side
  - content_top can extend into roof zone (canopy fills roof) but should
    stay below roof lines to avoid the roof cutting through the canopy
"""
import math

# v4 House geometry
WALL_L, WALL_R = 380, 1520
FLOOR_Y = 1550
WALL_TOP_Y = 650
PEAK = (950, 350)
CENTER = (950, 950)

# Icon content ratios (from PIL analysis)
CONTENT_W_RATIO = 761 / 1024   # 0.7422
CONTENT_H_RATIO = 872 / 1024   # 0.8516
# Content center offset in 1024 frame: (+35, +31)
OFFSET_X_1024 = 35
OFFSET_Y_1024 = 31

# Roof line equation: from (380, 650) to (950, 350)
# y = 650 - (300/570)*(x - 380) = 650 - 0.5263*(x-380)
def roof_y_at(x):
    return 650 - (300/570) * (x - 380)

print("=" * 70)
print("V4 HOUSE — ICON SIZE ANALYSIS")
print("=" * 70)
print(f"House body: x=[{WALL_L},{WALL_R}] (w={WALL_R-WALL_L}), y=[{WALL_TOP_Y},{FLOOR_Y}] (h={FLOOR_Y-WALL_TOP_Y})")
print(f"Roof peak: {PEAK}, roof rise = {WALL_TOP_Y - PEAK[1]}px")
print(f"Content aspect: {CONTENT_W_RATIO:.4f}w × {CONTENT_H_RATIO:.4f}h (taller than wide)")
print(f"House body aspect: {(WALL_R-WALL_L)/(FLOOR_Y-WALL_TOP_Y):.4f} (wider than tall)")

print("\n--- Option A: Fit to height (content_bottom = floor - 20px) ---")
margin_bot = 20
# content_bottom = CENTER_Y + CONTENT_H_RATIO * S / 2 = 950 + 0.4258*S
# ≤ FLOOR_Y - margin_bot = 1530
S_A = (1530 - 950) / (CONTENT_H_RATIO / 2)
print(f"  S = {S_A:.0f}px")
# Check width margin at this size
cw_A = CONTENT_W_RATIO * S_A
margin_side_A = (WALL_R - WALL_L - cw_A) / 2
print(f"  Content width = {cw_A:.0f}, side margin = {margin_side_A:.0f}px")
# Check content top
ct_A = 950 - CONTENT_H_RATIO * S_A / 2
print(f"  Content top = {ct_A:.0f} (roof peak={PEAK[1]}, wall_top={WALL_TOP_Y})")
# Check roof overlap at content left edge
cl_A = 950 - cw_A/2
roof_y_cl = roof_y_at(cl_A)
print(f"  Content left = {cl_A:.0f}, roof y at content left = {roof_y_cl:.0f}")
print(f"  Canopy spans y=[{ct_A:.0f}, ~{ct_A + 0.2*CONTENT_H_RATIO*S_A:.0f}]")
print(f"  Roof at content left ({roof_y_cl:.0f}) vs canopy bottom (~{ct_A + 0.2*CONTENT_H_RATIO*S_A:.0f}): {'OVERLAP' if roof_y_cl < ct_A + 0.2*CONTENT_H_RATIO*S_A else 'CLEAR'}")

print("\n--- Option B: Fit to width (content fills body width, 40px margin) ---")
margin_side = 40
cw_B = (WALL_R - WALL_L) - 2 * margin_side  # 1060
S_B = cw_B / CONTENT_W_RATIO
ch_B = CONTENT_H_RATIO * S_B
cb_B = 950 + ch_B / 2
ct_B = 950 - ch_B / 2
print(f"  S = {S_B:.0f}px")
print(f"  Content height = {ch_B:.0f}")
print(f"  Content bottom = {cb_B:.0f} (floor={FLOOR_Y}, margin={FLOOR_Y-cb_B:.0f}px)")
print(f"  Content top = {ct_B:.0f} (roof peak={PEAK[1]})")
print(f"  Content bottom {'OVERFLOWS floor' if cb_B > FLOOR_Y else 'OK'}")
print(f"  Content top {'ABOVE roof peak' if ct_B < PEAK[1] else 'below peak'}")

print("\n--- Option C: Compromise — maximize size, allow canopy in roof zone ---")
# Target: content_bottom = floor - 25px (snug bottom), check roof overlap
margin_bot_C = 25
S_C = (FLOOR_Y - margin_bot_C - 950) / (CONTENT_H_RATIO / 2)
cw_C = CONTENT_W_RATIO * S_C
ch_C = CONTENT_H_RATIO * S_C
margin_side_C = (WALL_R - WALL_L - cw_C) / 2
ct_C = 950 - ch_C / 2
cb_C = 950 + ch_C / 2
cl_C = 950 - cw_C / 2
cr_C = 950 + cw_C / 2
print(f"  S = {S_C:.0f}px")
print(f"  Content: {cw_C:.0f}w × {ch_C:.0f}h")
print(f"  Content spans: ({cl_C:.0f},{ct_C:.0f}) to ({cr_C:.0f},{cb_C:.0f})")
print(f"  Side margin = {margin_side_C:.0f}px")
print(f"  Bottom margin = {FLOOR_Y - cb_C:.0f}px")
print(f"  Content top = {ct_C:.0f} (peak={PEAK[1]}, {PEAK[1]-ct_C:.0f}px below peak)")
# Roof line check: does roof cross canopy?
# Canopy ≈ top 25% of content height
canopy_bottom = ct_C + 0.25 * ch_C
print(f"  Canopy spans y=[{ct_C:.0f}, ~{canopy_bottom:.0f}]")
# At content left edge, where is roof?
roof_y_cl = roof_y_at(cl_C)
print(f"  Roof y at content left (x={cl_C:.0f}): {roof_y_cl:.0f}")
print(f"  Canopy bottom at content left ~{canopy_bottom:.0f}")
print(f"  Roof {'CROSSES' if roof_y_cl < canopy_bottom else 'BELOW'} canopy at left edge")
# At x=700 (quarter point)
roof_y_700 = roof_y_at(700)
print(f"  Roof y at x=700: {roof_y_700:.0f}, canopy bottom ~{canopy_bottom:.0f}")

# Content shift at this size
scale_C = S_C / 1024
shift_x = OFFSET_X_1024 * scale_C
shift_y = OFFSET_Y_1024 * scale_C
print(f"\n  Scale = {scale_C:.4f}")
print(f"  Content shift: ({shift_x:.1f}, {shift_y:.1f})px → use ({round(shift_x)}, {round(shift_y)})")
print(f"  CSS transform: translate(calc(-50% - {round(shift_x)}px), calc(-50% - {round(shift_y)}px))")

# Verify all house vertices inside inner hairline r=860
print("\n--- House vertices inside inner hairline (r=860) ---")
for name, (x,y) in [("floor_L",(WALL_L,FLOOR_Y)),("floor_R",(WALL_R,FLOOR_Y)),
                     ("wallTL",(WALL_L,WALL_TOP_Y)),("wallTR",(WALL_R,WALL_TOP_Y)),
                     ("peak",PEAK)]:
    d = math.sqrt((x-950)**2+(y-950)**2)
    print(f"  {name} ({x},{y}): dist={d:.0f} {'✓' if d<=860 else '✗'}")
