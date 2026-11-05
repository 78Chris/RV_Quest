"""
Laser Cut Standee & Base SVG Generator for "Von Helden und Monstern"
===================================================================
Production Rules & Constraints:
1. Raster Engraving Requirements for Woodcut Art:
   - Symmetrical arched plaque for 100% reversible (dual-sided) engraving in laser jigs.
   - High-key line art / dithered raster engraving (prevents deep charring/smoke pooling on birch plywood).
   - Centered illustrations with proper clipping path to prevent bleeding onto the cut border.
   - Snug Art Layout:
     * Minimal left and right white edges (< 1 mm margins).
     * Bottom almost flush with the base line (~0.5 - 1.0 mm above base).
     * Top has just a couple of mm under the arched dome.

2. Tabletop Grid Dimensions:
   - Grid field size: 30 mm x 30 mm (Standard Dungeon Square).
   - Standard Standee Width: 30 mm (Fills field width, fully stable).
   - Standard Base Diameter: 30 mm round (Matches field footprint).
   - Miniature Heights:
     * Small / Minion (Goblins, Spiders): 25 - 30 mm
     * Standard / Hero / Skeleton: 40 - 45 mm (Default: 42 mm)
     * Large / Boss (Ghouls, Malakor): 55 - 60 mm
   - Tenon (Zapfen) standard: 10.0 mm wide x 3.0 mm deep (Slot: 10.2 mm x 3.0 mm, 0.2mm kerf allowance).
"""

import os
import sys
import base64
from pathlib import Path
from PIL import Image
import numpy as np

# Global Tabletop Standards (Scale: 10 SVG units = 1.0 mm)
UNITS_PER_MM = 10.0

DEFAULT_GRID_SIZE_MM = 30.0
DEFAULT_STANDEE_WIDTH_MM = 30.0
DEFAULT_BASE_DIAMETER_MM = 30.0
DEFAULT_TENON_WIDTH_MM = 10.0
DEFAULT_WOOD_THICKNESS_MM = 3.0
DEFAULT_SLOT_KERF_ALLOWANCE_MM = 0.2  # 0.2mm extra length for smooth friction fit

CATEGORIES = {
    "small": {
        "width_mm": 30.0,
        "height_mm": 28.0,
        "base_dia_mm": 30.0,
        "tenon_w_mm": 10.0,
        "tenon_h_mm": 3.0,
    },
    "standard": {
        "width_mm": 30.0,
        "height_mm": 42.0,
        "base_dia_mm": 30.0,
        "tenon_w_mm": 10.0,
        "tenon_h_mm": 3.0,
    },
    "boss": {
        "width_mm": 30.0,
        "height_mm": 58.0,
        "base_dia_mm": 30.0,
        "tenon_w_mm": 14.0,
        "tenon_h_mm": 3.0,
    },
    "boss_large": {
        "width_mm": 60.0,
        "height_mm": 60.0,
        "base_dia_mm": 60.0,
        "tenon_w_mm": 16.0,
        "tenon_h_mm": 3.0,
    }
}


def crop_tight_bounds(
    image_path: str,
    output_cropped_path: str = None,
    threshold: int = 230,
    pad_side: int = 8,
    pad_bottom: int = 4,
    pad_top: int = 12
) -> str:
    """
    Detects the dark artwork bounding box, trims away excess white space,
    leaving minimal side margins, bottom almost flush, and snug headroom.
    """
    img = Image.open(image_path)
    arr = np.array(img.convert('L'))
    dark_pixels = np.where(arr < threshold)

    if len(dark_pixels[0]) == 0:
        return image_path

    min_y, max_y = int(np.min(dark_pixels[0])), int(np.max(dark_pixels[0]))
    min_x, max_x = int(np.min(dark_pixels[1])), int(np.max(dark_pixels[1]))

    crop_left = max(0, min_x - pad_side)
    crop_right = min(img.width, max_x + pad_side)
    crop_bottom = min(img.height, max_y + pad_bottom)
    crop_top = max(0, min_y - pad_top)

    cropped = img.crop((crop_left, crop_top, crop_right, crop_bottom))

    if not output_cropped_path:
        p = Path(image_path)
        output_cropped_path = str(p.parent / f"{p.stem}_tight{p.suffix}")

    cropped.save(output_cropped_path, quality=95)
    return output_cropped_path


def generate_standee_svg(
    image_path: str,
    output_svg_path: str,
    title: str = "Miniatur",
    category: str = "standard",
    auto_crop: bool = True
) -> str:
    """
    Generates a production-ready SVG containing:
    1. Symmetrical flippable standee plaque with embedded raster art and laser cut line (#ff0000).
    2. Matching 30mm round base with centered slot.
    3. Dashed 30mm grid boundary for visual verification.
    """
    cfg = CATEGORIES.get(category, CATEGORIES["standard"])
    w_mm = cfg["width_mm"]
    h_mm = cfg["height_mm"]
    base_dia_mm = cfg["base_dia_mm"]
    tenon_w_mm = cfg["tenon_w_mm"]
    tenon_h_mm = cfg["tenon_h_mm"]

    w_units = w_mm * UNITS_PER_MM
    h_units = h_mm * UNITS_PER_MM
    tenon_w_units = tenon_w_mm * UNITS_PER_MM
    tenon_h_units = tenon_h_mm * UNITS_PER_MM

    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image file not found: {image_path}")

    # Process image if auto_crop is requested
    final_img_path = image_path
    if auto_crop:
        p = Path(image_path)
        cropped_candidate = p.parent / f"{p.stem}_cropped{p.suffix}"
        if cropped_candidate.exists():
            final_img_path = str(cropped_candidate)
        else:
            final_img_path = crop_tight_bounds(image_path, str(cropped_candidate))

    # Read dimensions of the final image
    with Image.open(final_img_path) as img:
        img_orig_w, img_orig_h = img.size

    with open(final_img_path, "rb") as f:
        b64_data = base64.b64encode(f.read()).decode("ascii")

    # Symmetrical Tenon horizontal centering (exact symmetry for dual-sided jig flipping)
    tenon_left = (w_units - tenon_w_units) / 2.0
    tenon_right = tenon_left + tenon_w_units

    # Top corner radius (3mm = 30 units)
    corner_r = 30.0

    # Perfectly symmetrical cut path (Red line #ff0000, 1.5 pt stroke)
    cut_path = (
        f"M 0,{h_units} "
        f"L 0,{corner_r} "
        f"Q 0,0 {corner_r},0 "
        f"L {w_units - corner_r},0 "
        f"Q {w_units},0 {w_units},{corner_r} "
        f"L {w_units},{h_units} "
        f"L {tenon_right},{h_units} "
        f"L {tenon_right},{h_units + tenon_h_units} "
        f"L {tenon_left},{h_units + tenon_h_units} "
        f"L {tenon_left},{h_units} "
        f"Z"
    )

    # Base parameters
    base_dia_units = base_dia_mm * UNITS_PER_MM
    base_r_units = base_dia_units / 2.0
    slot_w_units = DEFAULT_WOOD_THICKNESS_MM * UNITS_PER_MM
    slot_l_units = (tenon_w_mm + DEFAULT_SLOT_KERF_ALLOWANCE_MM) * UNITS_PER_MM

    # Viewbox setup
    margin = 15.0
    spacing = 30.0
    total_w = int(margin + w_units + spacing + base_dia_units + margin)
    total_h = int(margin + max(h_units + tenon_h_units + 80, base_dia_units + 120))

    base_x_offset = int(margin + w_units + spacing)

    # Precise Image Placement (Snug fit requirements):
    # 1. Left/Right white margins reduced to a minimum (< 1mm, ~0.5mm)
    #    Target image display width: w_units - 10 (29.0 mm wide)
    # 2. Bottom almost flush with base: bottom edge touches Y = h_units - 6 (0.6mm from base)
    # 3. Top margin: a couple of mm under the arched dome.
    target_img_w = w_units - 10.0  # 290 units = 29 mm
    scale_factor = target_img_w / float(img_orig_w)
    target_img_h = img_orig_h * scale_factor

    # If scaled height is taller than plaque, constrain height to leave ~2mm at top
    max_img_h = h_units - 25.0  # Leaves 2.5 mm margin at top
    if target_img_h > max_img_h:
        target_img_h = max_img_h
        target_img_w = target_img_h * (img_orig_w / float(img_orig_h))

    # Center horizontally on plaque
    img_x = (w_units - target_img_w) / 2.0
    # Place flush with bottom (leaving 0.6mm gap above base cut line)
    img_y = h_units - target_img_h - 6.0

    svg_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" 
     xmlns:xlink="http://www.w3.org/1999/xlink"
     viewBox="0 0 {total_w} {total_h}" 
     width="{total_w / UNITS_PER_MM:.1f}mm" height="{total_h / UNITS_PER_MM:.1f}mm">

  <!-- ======================================================== -->
  <!-- 1. SYMMETRICAL STANDEE ({w_mm:.0f} mm W x {h_mm:.0f} mm H)               -->
  <!-- Layer 00 (Black / Image): LightBurn raster engrave        -->
  <!-- Layer 02 (Red #FF0000 / Line): LightBurn outer vector cut -->
  <!-- ======================================================== -->
  <g id="standee_plaque" transform="translate({margin}, {margin})">
    <!-- Centered Woodcut Illustration (High-Key Line Engrave) -->
    <!-- Direct presentation attributes and xlink for full LightBurn compatibility -->
    <image id="engrave_artwork"
           x="{img_x:.1f}" y="{img_y:.1f}" 
           width="{target_img_w:.1f}" height="{target_img_h:.1f}" 
           href="data:image/jpeg;base64,{b64_data}"
           xlink:href="data:image/jpeg;base64,{b64_data}" />

    <!-- Symmetrical Laser Cut Path (Red Line #FF0000) -->
    <path id="standee_cut" d="{cut_path}" 
          fill="none" stroke="#FF0000" stroke-width="1.0" />
  </g>

  <!-- ======================================================== -->
  <!-- 2. ROUND BASE ({base_dia_mm:.0f} mm Diameter - Fits 30mm Grid)           -->
  <!-- ======================================================== -->
  <g id="standee_base" transform="translate({base_x_offset}, {margin})">
    <!-- Reference: 30x30mm dungeon grid square (Blue #0000FF -> LightBurn Tool layer) -->
    <rect id="grid_guide" x="0" y="60" width="{base_dia_units}" height="{base_dia_units}" 
          fill="none" stroke="#0000FF" stroke-width="1.0" stroke-dasharray="10,10" />

    <!-- Base Outer Cut (Red Line #FF0000: {base_dia_mm:.0f} mm round) -->
    <circle id="base_cut" cx="{base_r_units}" cy="{60 + base_r_units}" r="{base_r_units}" 
            fill="none" stroke="#FF0000" stroke-width="1.0" />
    
    <!-- Centered Slot for 3mm wood ({DEFAULT_WOOD_THICKNESS_MM:.1f} mm x {tenon_w_mm + DEFAULT_SLOT_KERF_ALLOWANCE_MM:.1f} mm) -->
    <rect id="slot_cut" x="{base_r_units - slot_w_units / 2.0}" y="{60 + base_r_units - slot_l_units / 2.0}" 
          width="{slot_w_units}" height="{slot_l_units}" rx="1.5" 
          fill="none" stroke="#FF0000" stroke-width="1.0" />
  </g>
</svg>"""

    os.makedirs(os.path.dirname(os.path.abspath(output_svg_path)), exist_ok=True)
    with open(output_svg_path, "w", encoding="utf-8") as f:
        f.write(svg_content)

    print(f"Generated snug laser-ready standee SVG: {output_svg_path}")
    return output_svg_path


if __name__ == "__main__":
    base_dir = Path(__file__).resolve().parent
    img = base_dir / "skeleton_warrior_woodcut_cropped.jpg"
    if not img.exists():
        img = base_dir / "skeleton_warrior_woodcut.jpg"
    out_svg = base_dir / "skeleton_standee_laser_ready.svg"

    generate_standee_svg(
        image_path=str(img),
        output_svg_path=str(out_svg),
        title="Skelettkrieger",
        category="standard",
        auto_crop=True
    )
