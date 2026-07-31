#!/usr/bin/env python3
"""Verify the snug house geometry for the circular seal."""
import math

CENTER = (950, 950)
INNER_HAIRLINE_R = 860
URL_RING_R = 890
OUTER_HAIRLINE_R = 920

# Icon
ICON_SIZE = 920
icon_left = CENTER[0] - ICON_SIZE / 2   # 490
icon_right = CENTER[0] + ICON_SIZE / 2  # 1410
icon_top = CENTER[1] - ICON_SIZE / 2    # 490
icon_bottom = CENTER[1] + ICON_SIZE / 2 # 1410

# House
house_floor_y = 1460
house_wall_left_x = 450
house_wall_right_x = 1450
house_wall_top_y = 440
house_roof_peak = (950, 200)

# House vertices
vertices = {
    "floor_left":  (450, 1460),
    "floor_right": (1450, 1460),
    "wall_top_left":  (450, 440),
    "wall_top_right": (1450, 440),
    "roof_peak": (950, 200),
}

print("=" * 70)
print("SNUG HOUSE GEOMETRY VERIFICATION")
print("=" * 70)

print(f"\nCanvas: 1900×1900, center {CENTER}")
print(f"URL ring r={URL_RING_R}, outer hairline r={OUTER_HAIRLINE_R}, inner hairline r={INNER_HAIRLINE_R}")
print(f"Icon: {ICON_SIZE}×{ICON_SIZE}, spans ({icon_left},{icon_top}) to ({icon_right},{icon_bottom})")

print("\n--- 1. Icon-to-House clearance (snug check) ---")
clearances = {
    "left (icon_left to wall)":   icon_left - house_wall_left_x,
    "right (wall to icon_right)": house_wall_right_x - icon_right,
    "bottom (icon_bottom to floor)": house_floor_y - icon_bottom,
    "top (wall_top to icon_top)": icon_top - house_wall_top_y,
}
for label, val in clearances.items():
    status = "SNUG ✓" if 30 <= val <= 70 else ("TIGHT" if val < 30 else "LOOSE")
    print(f"  {label}: {val}px  {status}")

print("\n--- 2. House vertices inside inner hairline (r=860) ---")
for name, (x, y) in vertices.items():
    dx = x - CENTER[0]
    dy = y - CENTER[1]
    dist = math.sqrt(dx*dx + dy*dy)
    clearance = INNER_HAIRLINE_R - dist
    status = "INSIDE ✓" if dist <= INNER_HAIRLINE_R else "OUTSIDE ✗"
    print(f"  {name} ({x},{y}): dist={dist:.1f}, clearance to inner hairline={clearance:.1f}px  {status}")

print("\n--- 3. Roof diagonal midpoint check ---")
# Left roof: (450,440) to (950,200)
mid = ((450+950)/2, (440+200)/2)
dx, dy = mid[0]-CENTER[0], mid[1]-CENTER[1]
dist = math.sqrt(dx*dx + dy*dy)
print(f"  Left roof midpoint {mid}: dist={dist:.1f}, clearance={INNER_HAIRLINE_R-dist:.1f}px")

print("\n--- 4. Roof angle ---")
rise = house_wall_top_y - house_roof_peak[1]  # 440-200 = 240
run = house_roof_peak[0] - house_wall_left_x   # 950-450 = 500
angle = math.degrees(math.atan2(rise, run))
print(f"  Rise={rise}, Run={run}, Angle={angle:.1f}°  (classic house roof ~25-35°)")

print("\n--- 5. Stroke clearance (12.5px stroke, centered on path) ---")
stroke_half = 12.5 / 2  # 6.25
# Icon left to inner edge of wall stroke
icon_to_wall_stroke = icon_left - (house_wall_left_x + stroke_half)
print(f"  Icon left to inner edge of wall stroke: {icon_to_wall_stroke:.2f}px (need >0)")
# Wall stroke outer edge to canvas edge
wall_outer_to_canvas = house_wall_left_x - stroke_half
print(f"  Wall stroke outer edge to canvas left: {wall_outer_to_canvas:.2f}px")
# Floor stroke to canvas bottom
floor_outer_to_canvas = 1900 - house_floor_y - stroke_half
print(f"  Floor stroke outer edge to canvas bottom: {floor_outer_to_canvas:.2f}px")
# Roof peak stroke to canvas top
peak_outer_to_canvas = house_roof_peak[1] - stroke_half
print(f"  Roof peak stroke outer edge to canvas top: {peak_outer_to_canvas:.2f}px")

print("\n--- 6. Summary ---")
all_snug = all(30 <= v <= 70 for v in clearances.values())
all_inside = all(math.sqrt((x-CENTER[0])**2 + (y-CENTER[1])**2) <= INNER_HAIRLINE_R
                 for x, y in vertices.values())
print(f"  All clearances snug (30-70px): {'YES ✓' if all_snug else 'NO ✗'}")
print(f"  All house vertices inside inner hairline: {'YES ✓' if all_inside else 'NO ✗'}")
print(f"  Roof angle reasonable: {'YES ✓' if 20 <= angle <= 35 else 'NO ✗'}")
