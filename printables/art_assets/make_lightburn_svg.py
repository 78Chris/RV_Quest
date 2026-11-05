import base64
from pathlib import Path
from PIL import Image

art_dir = Path(r"C:\Users\christoph.willimzik\Agent_Bunny\RV_Quest\printables\art_assets")
img_path = art_dir / "skeleton_warrior_woodcut_cropped.jpg"
out_svg_path = art_dir / "skeleton_standee_lightburn_ready.svg"

with Image.open(img_path) as img:
    orig_w, orig_h = img.size

# Units: 10 units = 1 mm
w_units = 300.0
h_units = 420.0
tenon_w = 100.0
tenon_h = 30.0
corner_r = 30.0

tenon_left = (w_units - tenon_w) / 2.0  # 100.0
tenon_right = tenon_left + tenon_w      # 200.0

target_img_w = 290.0
scale = target_img_w / orig_w
target_img_h = orig_h * scale
max_img_h = h_units - 25.0
if target_img_h > max_img_h:
    target_img_h = max_img_h
    target_img_w = target_img_h * (orig_w / orig_h)

img_x = (w_units - target_img_w) / 2.0
img_y = h_units - target_img_h - 6.0

# Base: 30 mm diameter, slot 3.0 mm x 10.2 mm
base_dia = 300.0
base_r = 150.0

margin = 15.0
spacing = 30.0
total_w = int(margin + w_units + spacing + base_dia + margin)
total_h = int(margin + max(h_units + tenon_h + 80, base_dia + 120))
base_x_offset = int(margin + w_units + spacing)

# Cut path for standee
cut_path_standee = (
    f"M 0,{h_units} "
    f"L 0,{corner_r} "
    f"Q 0,0 {corner_r},0 "
    f"L {w_units - corner_r},0 "
    f"Q {w_units},0 {w_units},{corner_r} "
    f"L {w_units},{h_units} "
    f"L {tenon_right},{h_units} "
    f"L {tenon_right},{h_units + tenon_h} "
    f"L {tenon_left},{h_units + tenon_h} "
    f"L {tenon_left},{h_units} "
    f"Z"
)

with open(img_path, "rb") as f:
    b64_img = base64.b64encode(f.read()).decode("ascii")

svg = f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg"
     xmlns:xlink="http://www.w3.org/1999/xlink"
     viewBox="0 0 {total_w} {total_h}"
     width="{total_w/10.0:.1f}mm" height="{total_h/10.0:.1f}mm">

  <!-- ========================================================= -->
  <!-- 1. STANDEE (30mm x 42mm with 10mm x 3mm Zapfen)           -->
  <!-- Layer 00 (Black / Image): Auto-recognized by LightBurn    -->
  <!-- Layer 02 (Red #FF0000 / Line): Auto-recognized as Cut     -->
  <!-- ========================================================= -->
  <g id="standee" transform="translate({margin}, {margin})">
    <!-- Engrave Image (Direct href & xlink:href without clip-path) -->
    <image id="engrave_artwork"
           x="{img_x:.1f}" y="{img_y:.1f}"
           width="{target_img_w:.1f}" height="{target_img_h:.1f}"
           href="data:image/jpeg;base64,{b64_img}"
           xlink:href="data:image/jpeg;base64,{b64_img}" />

    <!-- Outer Vector Cut (Red #FF0000, 0.1mm hairline) -->
    <path id="standee_cut"
          d="{cut_path_standee}"
          fill="none"
          stroke="#FF0000"
          stroke-width="1.0" />
  </g>

  <!-- ========================================================= -->
  <!-- 2. BASE (30mm Round Base with Centered 3mm x 10.2mm Slot) -->
  <!-- ========================================================= -->
  <g id="base" transform="translate({base_x_offset}, {margin})">
    <!-- Base Outer Cut (Red #FF0000) -->
    <circle id="base_cut"
            cx="150.0" cy="210.0" r="150.0"
            fill="none"
            stroke="#FF0000"
            stroke-width="1.0" />

    <!-- Tenon Slot Cut (Red #FF0000) -->
    <rect id="slot_cut"
          x="135.0" y="159.0"
          width="30.0" height="102.0" rx="1.5"
          fill="none"
          stroke="#FF0000"
          stroke-width="1.0" />

    <!-- Blue Guide Line (30x30mm Grid Reference: Blue #0000FF -> LightBurn Tool Layer) -->
    <rect id="grid_guide"
          x="0" y="60"
          width="300.0" height="300.0"
          fill="none"
          stroke="#0000FF"
          stroke-width="1.0"
          stroke-dasharray="10,10" />
  </g>
</svg>
"""

out_svg_path.write_text(svg, encoding="utf-8")
print(f"Generated {out_svg_path} successfully ({out_svg_path.stat().st_size} bytes)")
