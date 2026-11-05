"""
Generates double-sided printable paper standees (A4 sheet, single standee SVG, HTML preview, and PDF).
Supports two paper standee styles:
1. Tent Fold (Tri-fold / A-frame with bottom glue tabs):
   - Standalone without plastic clips!
   - Base tab A (15mm) + Front panel (42mm) + Top fold line + Back panel (42mm, mirrored/flipped) + Base tab B (15mm).
   - Fold along dotted lines, glue tabs overlap on the bottom to form a rigid triangular base.
   - Fits standard 30x30mm dungeon grid field (base is 30mm wide x 15-20mm deep).

2. Straight Fold (Dual-sided for plastic / binder clips or slotted wooden/acrylic bases):
   - Front panel (30 x 42 mm) + Top fold line + Back panel (30 x 42 mm).
   - Folds in half back-to-back, fits straight into standard card / standee plastic bases or bulldog clips.
"""

import os
import sys
import base64
from pathlib import Path
from PIL import Image
import pymupdf

IMAGE_PATH = Path(r"C:\Users\christoph.willimzik\Agent_Bunny\RV_Quest\printables\art_assets\skeleton_warrior_woodcut_cropped_cropped.jpg")
OUTPUT_DIR = Path(r"C:\Users\christoph.willimzik\Agent_Bunny\RV_Quest\printables")

def build_paper_standees():
    print(f"Loading image from: {IMAGE_PATH}")
    with Image.open(IMAGE_PATH) as img:
        img_w, img_h = img.size
    
    with open(IMAGE_PATH, "rb") as f:
        img_b64 = base64.b64encode(f.read()).decode("ascii")

    # Standee specs (in mm):
    # Standee width: 30 mm
    # Standee height: 42 mm (RV_Quest standard figure height)
    # Art width: 28 mm, centered
    art_w_mm = 28.0
    scale = art_w_mm / img_w
    art_h_mm = img_h * scale
    
    # If height exceeds 38mm, clamp height
    if art_h_mm > 38.0:
        art_h_mm = 38.0
        art_w_mm = img_w * (art_h_mm / img_h)
        
    art_x = (30.0 - art_w_mm) / 2.0
    art_y = 42.0 - art_h_mm - 1.5 # 1.5mm from bottom fold

    # 1. Single Standee SVG: Tent Fold
    # Total height = 15 (tab 1) + 42 (front) + 42 (back) + 15 (tab 2) = 114 mm
    # Width = 30 mm (with 5mm margins around for crop marks -> 40 x 124 mm)
    tent_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
     viewBox="0 0 40 124" width="40mm" height="124mm">
  <defs>
    <style>
      .cut-line {{ stroke: #d32f2f; stroke-width: 0.3; fill: none; }}
      .fold-line {{ stroke: #1976d2; stroke-width: 0.3; stroke-dasharray: 1.5,1.0; fill: none; }}
      .tab-bg {{ fill: #f5eedb; stroke: #d32f2f; stroke-width: 0.3; }}
      .panel-bg {{ fill: #fcfcfb; }}
      .label-text {{ font-family: 'Cinzel', 'Palatino', serif; font-size: 2.2px; font-weight: bold; fill: #443; text-anchor: middle; }}
      .sub-text {{ font-family: sans-serif; font-size: 1.6px; fill: #776; text-anchor: middle; }}
      .ornament {{ stroke: #9e8a68; stroke-width: 0.25; fill: none; }}
    </style>
  </defs>

  <!-- Offset to (5, 5) -->
  <g transform="translate(5, 5)">
    <!-- Base Tab 1 (Bottom flap, 15mm) -->
    <path class="tab-bg" d="M 0,15 L 2,0 L 28,0 L 30,15 Z" />
    <text x="15" y="8" class="sub-text">▲ KLEBELASCHE A (Unten) ▲</text>

    <!-- Front Panel (30 x 42 mm, Y: 15 to 57) -->
    <rect x="0" y="15" width="30" height="42" class="panel-bg" stroke="#d32f2f" stroke-width="0.3"/>
    <!-- Subtle frame -->
    <rect x="1" y="16" width="28" height="40" rx="1.5" class="ornament" stroke-dasharray="2,0.8"/>
    <!-- Arch header banner -->
    <path d="M 2,21 Q 15,18 28,21" class="ornament"/>
    <text x="15" y="19" class="label-text">SKELETTKRIEGER</text>
    
    <!-- Artwork Front -->
    <image href="data:image/jpeg;base64,{img_b64}" xlink:href="data:image/jpeg;base64,{img_b64}"
           x="{art_x:.2f}" y="{15 + art_y:.2f}" width="{art_w_mm:.2f}" height="{art_h_mm:.2f}"/>

    <!-- Top Fold Line (between Front & Back, Y: 57) -->
    <line x1="0" y1="57" x2="30" y2="57" class="fold-line"/>
    <circle cx="15" cy="57" r="0.6" fill="#1976d2"/>

    <!-- Back Panel (30 x 42 mm, Y: 57 to 99, inverted/mirrored upside-down) -->
    <g transform="translate(15, 78) rotate(180) translate(-15, -21)">
      <rect x="0" y="0" width="30" height="42" class="panel-bg" stroke="#d32f2f" stroke-width="0.3"/>
      <rect x="1" y="1" width="28" height="40" rx="1.5" class="ornament" stroke-dasharray="2,0.8"/>
      <path d="M 2,6 Q 15,3 28,6" class="ornament"/>
      <text x="15" y="4" class="label-text">SKELETTKRIEGER</text>
      <!-- Horizontally mirrored artwork for back view -->
      <g transform="translate(15, {art_y + art_h_mm/2.0:.2f}) scale(-1, 1) translate(-15, -{art_y + art_h_mm/2.0:.2f})">
        <image href="data:image/jpeg;base64,{img_b64}" xlink:href="data:image/jpeg;base64,{img_b64}"
               x="{art_x:.2f}" y="{art_y:.2f}" width="{art_w_mm:.2f}" height="{art_h_mm:.2f}"/>
      </g>
    </g>

    <!-- Base Tab 2 (Bottom flap, 15mm, Y: 99 to 114) -->
    <path class="tab-bg" d="M 0,99 L 2,114 L 28,114 L 30,99 Z" />
    <text x="15" y="108" class="sub-text">▼ KLEBELASCHE B (Unten) ▼</text>

    <!-- Fold lines between tabs and panels -->
    <line x1="0" y1="15" x2="30" y2="15" class="fold-line"/>
    <line x1="0" y1="99" x2="30" y2="99" class="fold-line"/>
  </g>
</svg>"""

    tent_svg_path = OUTPUT_DIR / "skeleton_paper_standee_single.svg"
    with open(tent_svg_path, "w", encoding="utf-8") as f:
        f.write(tent_svg)
    print(f"Written single tent standee: {tent_svg_path}")

    # Now create the comprehensive A4 print sheet:
    # Contains:
    # - 4x Tent-Fold Standees (self-standing with glue tabs)
    # - 4x Straight-Fold Standees (for plastic / binder clips or slotted wooden bases)
    # - 8x Matching 30mm round paper base counters / status tokens (HP/Skulls)
    # - Alignment guides, fold lines (dashed blue), cut lines (red / black), clear assembly diagrams.

    def generate_tent_standee_group(idx, label="SKELETTKRIEGER"):
        return f"""
    <!-- Tent Standee #{idx} -->
    <g id="tent_standee_{idx}">
      <!-- Tab 1 -->
      <path class="tab-bg" d="M 0,15 L 2.5,0 L 27.5,0 L 30,15 Z" />
      <text x="15" y="8.5" class="sub-text">▲ KLEBELASCHE A ▲</text>

      <!-- Front Panel (30x42mm) -->
      <rect x="0" y="15" width="30" height="42" class="panel-bg" stroke="#222" stroke-width="0.35"/>
      <rect x="1" y="16" width="28" height="40" rx="1.5" class="ornament" stroke-dasharray="2,0.8"/>
      <path d="M 2,21 Q 15,18 28,21" class="ornament"/>
      <text x="15" y="19" class="label-text">{label}</text>
      
      <image href="data:image/jpeg;base64,{img_b64}" xlink:href="data:image/jpeg;base64,{img_b64}"
             x="{art_x:.2f}" y="{15 + art_y:.2f}" width="{art_w_mm:.2f}" height="{art_h_mm:.2f}"/>

      <!-- Stats pill -->
      <g transform="translate(15, 54)">
        <rect x="-11" y="-2" width="22" height="3.8" rx="1.9" fill="#2a1f18" stroke="#d4af37" stroke-width="0.25"/>
        <text x="0" y="0.8" font-family="'Cinzel', serif" font-size="2.0" font-weight="bold" fill="#f8dc88" text-anchor="middle">
          LP 2  ⚔ ATK 2
        </text>
      </g>

      <!-- Top Fold Line -->
      <line x1="-3" y1="57" x2="33" y2="57" class="fold-line"/>
      <polygon points="-2,56 -0.5,57 -2,58" fill="#1976d2"/>
      <polygon points="32,56 30.5,57 32,58" fill="#1976d2"/>

      <!-- Back Panel (upside down) -->
      <g transform="translate(15, 78) rotate(180) translate(-15, -21)">
        <rect x="0" y="0" width="30" height="42" class="panel-bg" stroke="#222" stroke-width="0.35"/>
        <rect x="1" y="1" width="28" height="40" rx="1.5" class="ornament" stroke-dasharray="2,0.8"/>
        <path d="M 2,6 Q 15,3 28,6" class="ornament"/>
        <text x="15" y="4" class="label-text">{label}</text>
        <g transform="translate(15, {art_y + art_h_mm/2.0:.2f}) scale(-1, 1) translate(-15, -{art_y + art_h_mm/2.0:.2f})">
          <image href="data:image/jpeg;base64,{img_b64}" xlink:href="data:image/jpeg;base64,{img_b64}"
                 x="{art_x:.2f}" y="{art_y:.2f}" width="{art_w_mm:.2f}" height="{art_h_mm:.2f}"/>
        </g>
        <!-- Stats pill on back too -->
        <g transform="translate(15, 39)">
          <rect x="-11" y="-2" width="22" height="3.8" rx="1.9" fill="#2a1f18" stroke="#d4af37" stroke-width="0.25"/>
          <text x="0" y="0.8" font-family="'Cinzel', serif" font-size="2.0" font-weight="bold" fill="#f8dc88" text-anchor="middle">
            LP 2  ⚔ ATK 2
          </text>
        </g>
      </g>

      <!-- Tab 2 -->
      <path class="tab-bg" d="M 0,99 L 2.5,114 L 27.5,114 L 30,99 Z" />
      <text x="15" y="108" class="sub-text">▼ KLEBELASCHE B ▼</text>

      <!-- Fold lines -->
      <line x1="-2" y1="15" x2="32" y2="15" class="fold-line"/>
      <line x1="-2" y1="99" x2="32" y2="99" class="fold-line"/>
    </g>
"""

    def generate_straight_standee_group(idx, label="SKELETTKRIEGER"):
        # Straight standee:
        # Height = 42mm (front) + 42mm (back) = 84mm
        # Top fold at Y = 42mm
        return f"""
    <!-- Straight Standee #{idx} (for Plastic / Binder Clips) -->
    <g id="straight_standee_{idx}">
      <!-- Front Panel (30x42mm) -->
      <rect x="0" y="0" width="30" height="42" class="panel-bg" stroke="#222" stroke-width="0.35"/>
      <rect x="1" y="1" width="28" height="40" rx="1.5" class="ornament" stroke-dasharray="2,0.8"/>
      <path d="M 2,6 Q 15,3 28,6" class="ornament"/>
      <text x="15" y="4" class="label-text">{label}</text>
      
      <image href="data:image/jpeg;base64,{img_b64}" xlink:href="data:image/jpeg;base64,{img_b64}"
             x="{art_x:.2f}" y="{art_y:.2f}" width="{art_w_mm:.2f}" height="{art_h_mm:.2f}"/>

      <g transform="translate(15, 39)">
        <rect x="-11" y="-2" width="22" height="3.8" rx="1.9" fill="#2a1f18" stroke="#d4af37" stroke-width="0.25"/>
        <text x="0" y="0.8" font-family="'Cinzel', serif" font-size="2.0" font-weight="bold" fill="#f8dc88" text-anchor="middle">
          LP 2  ⚔ ATK 2
        </text>
      </g>

      <!-- Top Fold Line -->
      <line x1="-3" y1="42" x2="33" y2="42" class="fold-line"/>
      <polygon points="-2,41 -0.5,42 -2,43" fill="#1976d2"/>
      <polygon points="32,41 30.5,42 32,43" fill="#1976d2"/>

      <!-- Back Panel (upside down, Y: 42 to 84) -->
      <g transform="translate(15, 63) rotate(180) translate(-15, -21)">
        <rect x="0" y="0" width="30" height="42" class="panel-bg" stroke="#222" stroke-width="0.35"/>
        <rect x="1" y="1" width="28" height="40" rx="1.5" class="ornament" stroke-dasharray="2,0.8"/>
        <path d="M 2,6 Q 15,3 28,6" class="ornament"/>
        <text x="15" y="4" class="label-text">{label}</text>
        <g transform="translate(15, {art_y + art_h_mm/2.0:.2f}) scale(-1, 1) translate(-15, -{art_y + art_h_mm/2.0:.2f})">
          <image href="data:image/jpeg;base64,{img_b64}" xlink:href="data:image/jpeg;base64,{img_b64}"
                 x="{art_x:.2f}" y="{art_y:.2f}" width="{art_w_mm:.2f}" height="{art_h_mm:.2f}"/>
        </g>
        <g transform="translate(15, 39)">
          <rect x="-11" y="-2" width="22" height="3.8" rx="1.9" fill="#2a1f18" stroke="#d4af37" stroke-width="0.25"/>
          <text x="0" y="0.8" font-family="'Cinzel', serif" font-size="2.0" font-weight="bold" fill="#f8dc88" text-anchor="middle">
            LP 2  ⚔ ATK 2
          </text>
        </g>
      </g>
    </g>
"""

    def generate_token(cx, cy, idx):
        # Round 30mm base token (matches 30x30mm dungeon grid)
        return f"""
      <!-- Base Token #{idx} (Ø 30mm) -->
      <g transform="translate({cx}, {cy})">
        <circle cx="0" cy="0" r="15" fill="#231b14" stroke="#d4af37" stroke-width="0.5"/>
        <circle cx="0" cy="0" r="13.5" fill="none" stroke="#7d6342" stroke-width="0.3" stroke-dasharray="1.5,1.0"/>
        <!-- Inner skull / crest icon -->
        <text x="0" y="-3.5" font-family="'Cinzel', serif" font-size="2.6" font-weight="bold" fill="#f8dc88" text-anchor="middle">💀 SKELETT</text>
        <text x="0" y="0.5" font-family="sans-serif" font-size="2.0" fill="#c4b29a" text-anchor="middle">#0{idx}</text>
        <rect x="-9" y="3.5" width="18" height="3.6" rx="1.8" fill="#581d1d" stroke="#d4af37" stroke-width="0.3"/>
        <text x="0" y="6.0" font-family="'Cinzel', serif" font-size="1.9" font-weight="bold" fill="#fff" text-anchor="middle">LP 2 · ATK 2</text>
        <circle cx="0" cy="0" r="15" fill="none" stroke="#222" stroke-width="0.25"/>
      </g>
"""

    sheet_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
     viewBox="0 0 210 297" width="210mm" height="297mm">
  <defs>
    <style>
      .cut-line {{ stroke: #222222; stroke-width: 0.35; fill: none; }}
      .fold-line {{ stroke: #1976d2; stroke-width: 0.35; stroke-dasharray: 2.0,1.2; fill: none; }}
      .tab-bg {{ fill: #f3edd9; stroke: #222222; stroke-width: 0.35; }}
      .panel-bg {{ fill: #fcfcfb; }}
      .title-text {{ font-family: 'Cinzel', 'Palatino', serif; font-size: 5.5px; font-weight: bold; fill: #1c150e; }}
      .subtitle-text {{ font-family: 'Palatino', 'Georgia', serif; font-size: 2.8px; font-style: italic; fill: #5c4e3e; }}
      .label-text {{ font-family: 'Cinzel', 'Palatino', serif; font-size: 2.2px; font-weight: bold; fill: #2a1f14; text-anchor: middle; }}
      .sub-text {{ font-family: sans-serif; font-size: 1.6px; fill: #665544; text-anchor: middle; }}
      .ornament {{ stroke: #a39070; stroke-width: 0.25; fill: none; }}
      .legend-text {{ font-family: sans-serif; font-size: 2.1px; fill: #332d26; }}
      .guide-box {{ fill: #f9f7f2; stroke: #d0c5b4; stroke-width: 0.4; }}
    </style>
  </defs>

  <!-- Page Background -->
  <rect width="210" height="297" fill="#ffffff" />

  <!-- Sheet Header -->
  <g transform="translate(14, 12)">
    <text x="0" y="0" class="title-text">VON HELDEN UND MONSTERN · DRUCKBOGEN</text>
    <text x="0" y="4.5" class="subtitle-text">Doppelseitige Papier-Standees (30 × 42 mm) · Skelettkrieger (Schergen / Untote)</text>
    <line x1="0" y1="6.8" x2="182" y2="6.8" stroke="#8a7356" stroke-width="0.5"/>
  </g>

  <!-- Legend & Instructions Box (Top Right, X: 110, Y: 22) -->
  <g transform="translate(138, 22)">
    <rect x="0" y="0" width="58" height="26" rx="2" class="guide-box"/>
    <text x="4" y="4.5" font-family="'Cinzel', serif" font-size="2.4px" font-weight="bold" fill="#2a1f14">ANLEITUNG & LEGENDE</text>
    
    <!-- Cut Line sample -->
    <line x1="4" y1="8.5" x2="12" y2="8.5" stroke="#222" stroke-width="0.4"/>
    <text x="14" y="9.3" class="legend-text">Durchgezogen: Schneidelinie</text>

    <!-- Fold Line sample -->
    <line x1="4" y1="13.5" x2="12" y2="13.5" stroke="#1976d2" stroke-width="0.4" stroke-dasharray="2.0,1.2"/>
    <text x="14" y="14.3" class="legend-text">Gestrichelt: Falzlinie (Rillen)</text>

    <!-- Base / Standee sizes -->
    <circle cx="8" cy="18.5" r="3" fill="#231b14" stroke="#d4af37" stroke-width="0.3"/>
    <text x="14" y="19.3" class="legend-text">Token: Ø 30 mm (Standard-Feld)</text>

    <text x="4" y="23.8" font-family="sans-serif" font-size="1.7px" fill="#7a6852">
      Empfehlung: 160–250 g/m² Papier/Karton
    </text>
  </g>

  <!-- Section 1 Header: 4x Tent-Fold Standees -->
  <g transform="translate(14, 25)">
    <rect x="0" y="0" width="118" height="6.5" rx="1.5" fill="#3b2d20"/>
    <text x="4" y="4.5" font-family="'Cinzel', serif" font-size="2.6px" font-weight="bold" fill="#f3d078">
      TYP A: SELBSTSTEHENDE DREIECKS-STANDEES (TENT-FOLD)
    </text>
    <text x="74" y="4.5" font-family="sans-serif" font-size="1.9px" fill="#e8dec8">
      4 Stück · Ohne Plastikfüße standfest
    </text>
  </g>

  <!-- 4 Tent Standees placed side by side -->
  <!-- X positions: 14, 52, 90, 128 (spacing = 38mm; 4 * 30 + 3 * 8 = 144 mm, leaves ample margins) -->
  <!-- Y position: 35. Height is 114 mm (15 tab + 42 front + 42 back + 15 tab) -> reaches Y = 149 -->
  <g transform="translate(14, 35)">{generate_tent_standee_group(1, "SKELETT 01")}</g>
  <g transform="translate(52, 35)">{generate_tent_standee_group(2, "SKELETT 02")}</g>
  <g transform="translate(90, 35)">{generate_tent_standee_group(3, "SKELETT 03")}</g>
  <g transform="translate(128, 35)">{generate_tent_standee_group(4, "SKELETT 04")}</g>

  <!-- Assembly Diagram for Tent-Fold (Right margin of Section 1, X: 168, Y: 60) -->
  <g transform="translate(168, 65)">
    <rect x="0" y="0" width="28" height="78" rx="2" class="guide-box"/>
    <text x="14" y="5.0" font-family="'Cinzel', serif" font-size="2.2px" font-weight="bold" fill="#2a1f14" text-anchor="middle">FALZ-SCHEMA</text>
    <text x="14" y="8.0" font-family="sans-serif" font-size="1.6px" fill="#665544" text-anchor="middle">Dreiecks-Standee</text>

    <!-- Mini Side-profile Diagram of Tent Fold -->
    <g transform="translate(14, 34) scale(0.48)">
      <!-- Peak -->
      <circle cx="0" cy="-35" r="2" fill="#1976d2"/>
      <line x1="0" y1="-35" x2="-18" y2="25" stroke="#222" stroke-width="1.8"/>
      <line x1="0" y1="-35" x2="18" y2="25" stroke="#222" stroke-width="1.8"/>
      <!-- Bottom overlapping glue tabs -->
      <line x1="-18" y1="25" x2="15" y2="25" stroke="#d32f2f" stroke-width="2.5" stroke-dasharray="4,2"/>
      <line x1="18" y1="27" x2="-15" y2="27" stroke="#1976d2" stroke-width="2.5"/>
      <text x="0" y="38" font-family="sans-serif" font-size="5px" font-weight="bold" fill="#443" text-anchor="middle">Bodenfläche</text>
      <text x="0" y="44" font-family="sans-serif" font-size="4px" fill="#776" text-anchor="middle">(Klebelaschen)</text>
    </g>

    <text x="14" y="58" font-family="sans-serif" font-size="1.7px" fill="#332" text-anchor="middle">1. Außen ausschneiden</text>
    <text x="14" y="62" font-family="sans-serif" font-size="1.7px" fill="#332" text-anchor="middle">2. An Linien rillen</text>
    <text x="14" y="66" font-family="sans-serif" font-size="1.7px" fill="#332" text-anchor="middle">3. Dach zusammenfalten</text>
    <text x="14" y="70" font-family="sans-serif" font-size="1.7px" fill="#332" text-anchor="middle">4. Laschen am Boden</text>
    <text x="14" y="73.5" font-family="sans-serif" font-size="1.7px" font-weight="bold" fill="#8d2b2b" text-anchor="middle">überlappend verkleben</text>
  </g>

  <!-- Section Divider -->
  <line x1="14" y1="156" x2="196" y2="156" stroke="#c0b39f" stroke-width="0.5"/>

  <!-- Section 2 Header: 4x Straight-Fold Standees -->
  <g transform="translate(14, 161)">
    <rect x="0" y="0" width="124" height="6.5" rx="1.5" fill="#2d3820"/>
    <text x="4" y="4.5" font-family="'Cinzel', serif" font-size="2.6px" font-weight="bold" fill="#b9e38d">
      TYP B: GERADE KLAPP-STANDEES (FÜR KARTENSTÄNDER / CLIPS)
    </text>
    <text x="84" y="4.5" font-family="sans-serif" font-size="1.9px" fill="#dce6d1">
      4 Stück · 30 × 42 mm
    </text>
  </g>

  <!-- 4 Straight Standees placed side by side -->
  <!-- X positions: 14, 52, 90, 128. Y: 171. Height = 84mm -> reaches Y = 255 -->
  <g transform="translate(14, 171)">{generate_straight_standee_group(5, "SKELETT 05")}</g>
  <g transform="translate(52, 171)">{generate_straight_standee_group(6, "SKELETT 06")}</g>
  <g transform="translate(90, 171)">{generate_straight_standee_group(7, "SKELETT 07")}</g>
  <g transform="translate(128, 171)">{generate_straight_standee_group(8, "SKELETT 08")}</g>

  <!-- Section 3: 8x Round Base Tokens (Ø 30 mm) -->
  <!-- Placed in column on right side: X = 178, Y = 178, 212, 246 (or arranged in 2 columns of 4) -->
  <g transform="translate(162, 161)">
    <rect x="0" y="0" width="34" height="6.5" rx="1.5" fill="#42241f"/>
    <text x="17" y="4.5" font-family="'Cinzel', serif" font-size="2.4px" font-weight="bold" fill="#f8dc88" text-anchor="middle">
      8× BASEN (Ø30)
    </text>
  </g>

  <!-- 8 round base counters (2 columns of 4, X: 169 and 189, Y: 184, 208, 232, 256) -->
  {generate_token(169, 182, 1)}
  {generate_token(193, 182, 2)}
  {generate_token(169, 206, 3)}
  {generate_token(193, 206, 4)}
  {generate_token(169, 230, 5)}
  {generate_token(193, 230, 6)}
  {generate_token(169, 254, 7)}
  {generate_token(193, 254, 8)}

  <!-- Footer Info -->
  <g transform="translate(14, 288)">
    <line x1="0" y1="0" x2="182" y2="0" stroke="#c0b39f" stroke-width="0.5"/>
    <text x="0" y="4" font-family="sans-serif" font-size="1.9px" fill="#776">
      Von Helden und Monstern · Tabletop Raster: 30 × 30 mm · Standee Maße: 30 mm B × 42 mm H · 100% maßstabsgetreu bei 100% Druckgröße
    </text>
  </g>
</svg>"""

    sheet_svg_path = OUTPUT_DIR / "standee_sheet_skeleton_a4.svg"
    with open(sheet_svg_path, "w", encoding="utf-8") as f:
        f.write(sheet_svg)
    print(f"Written A4 standee sheet SVG: {sheet_svg_path}")

    # Create HTML print wrapper
    html_content = f"""<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="utf-8">
<title>Skelettkrieger Standees - Von Helden und Monstern</title>
<style>
  @page {{
    size: A4 portrait;
    margin: 0;
  }}
  html, body {{
    margin: 0;
    padding: 0;
    width: 210mm;
    height: 297mm;
    background: #555;
    display: flex;
    justify-content: center;
    align-items: center;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  }}
  .page-container {{
    width: 210mm;
    height: 297mm;
    background: #ffffff;
    box-shadow: 0 8px 24px rgba(0,0,0,0.4);
    overflow: hidden;
  }}
  svg {{
    display: block;
    width: 210mm;
    height: 297mm;
  }}
  @media print {{
    body {{
      background: none;
    }}
    .page-container {{
      box-shadow: none;
    }}
  }}
</style>
</head>
<body>
  <div class="page-container">
{sheet_svg}
  </div>
</body>
</html>"""

    html_path = OUTPUT_DIR / "standee_sheet_skeleton_a4.html"
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Written A4 HTML wrapper: {html_path}")

    # Generate PDF using PyMuPDF
    pdf_path = OUTPUT_DIR / "standee_sheet_skeleton_a4.pdf"
    doc = pymupdf.open(str(sheet_svg_path))
    pdf_bytes = doc.convert_to_pdf()
    with open(pdf_path, "wb") as f:
        f.write(pdf_bytes)
    print(f"Written A4 PDF: {pdf_path}")

    # Render High-Res PNG Preview (300 DPI)
    pdf_doc = pymupdf.open(stream=pdf_bytes, filetype="pdf")
    page = pdf_doc[0]
    pix = page.get_pixmap(dpi=300)
    png_path = OUTPUT_DIR / "standee_sheet_skeleton_a4_300dpi.png"
    pix.save(str(png_path))
    print(f"Written 300 DPI preview PNG: {png_path}")

if __name__ == "__main__":
    build_paper_standees()
