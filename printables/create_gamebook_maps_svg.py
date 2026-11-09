import xml.etree.ElementTree as ET

def generate_dungeon_grid_svg(page_type="room1"):
    # 6x6 grid = 180mm x 180mm
    # Let's use 720 x 720 px (120px per 30mm cell)
    width = 720
    height = 720
    cell = 120

    svg = []
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="180mm" height="180mm">')
    
    # Defs
    svg.append("""  <defs>
    <!-- Background stone base -->
    <radialGradient id="dungeonGlow" cx="50%" cy="50%" r="70%">
      <stop offset="0%" stop-color="#3a3731"/>
      <stop offset="70%" stop-color="#24211e"/>
      <stop offset="100%" stop-color="#12100e"/>
    </radialGradient>

    <!-- Slab Gradients -->
    <linearGradient id="slabGrad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#4e4942"/>
      <stop offset="50%" stop-color="#3d3933"/>
      <stop offset="100%" stop-color="#2a2723"/>
    </linearGradient>

    <linearGradient id="slabGrad2" x1="100%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#46423b"/>
      <stop offset="60%" stop-color="#38342f"/>
      <stop offset="100%" stop-color="#26231f"/>
    </linearGradient>

    <!-- Pillar 3D shading -->
    <radialGradient id="pillarGrad" cx="40%" cy="35%" r="60%">
      <stop offset="0%" stop-color="#8c857b"/>
      <stop offset="60%" stop-color="#544d44"/>
      <stop offset="100%" stop-color="#26221c"/>
    </radialGradient>

    <!-- Wood Chest Gradient -->
    <linearGradient id="woodGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#8a532d"/>
      <stop offset="50%" stop-color="#5c3418"/>
      <stop offset="100%" stop-color="#361c0a"/>
    </linearGradient>

    <!-- Gold Inlay / Rune Glow -->
    <radialGradient id="runeGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#d4af37" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#d4af37" stop-opacity="0"/>
    </radialGradient>

    <!-- Drop shadow for relief -->
    <filter id="shadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="2" dy="4" stdDeviation="3" flood-color="#000000" flood-opacity="0.75"/>
    </filter>
  </defs>""")

    # Background
    svg.append(f'  <rect x="0" y="0" width="{width}" height="{height}" fill="url(#dungeonGlow)"/>')

    # Flagstone Slabs on all 36 cells
    svg.append('  <!-- Floor Flagstones -->')
    svg.append('  <g filter="url(#shadow)">')
    for r in range(6):
        for c in range(6):
            x = c * cell
            y = r * cell
            grad = "url(#slabGrad1)" if (r + c) % 2 == 0 else "url(#slabGrad2)"
            # Subdivide each 30mm cell into 2-3 realistic flagstones
            if (r * 6 + c) % 3 == 0:
                svg.append(f'    <rect x="{x+4}" y="{y+4}" width="{cell*0.55-6}" height="{cell-8}" rx="2" fill="{grad}" stroke="#161412" stroke-width="1.5"/>')
                svg.append(f'    <rect x="{x+cell*0.55+2}" y="{y+4}" width="{cell*0.45-6}" height="{cell-8}" rx="2" fill="url(#slabGrad2)" stroke="#161412" stroke-width="1.5"/>')
            elif (r * 6 + c) % 3 == 1:
                svg.append(f'    <rect x="{x+4}" y="{y+4}" width="{cell-8}" height="{cell*0.48-6}" rx="2" fill="{grad}" stroke="#161412" stroke-width="1.5"/>')
                svg.append(f'    <rect x="{x+4}" y="{y+cell*0.48+2}" width="{cell-8}" height="{cell*0.52-6}" rx="2" fill="url(#slabGrad1)" stroke="#161412" stroke-width="1.5"/>')
            else:
                svg.append(f'    <rect x="{x+4}" y="{y+4}" width="{cell-8}" height="{cell-8}" rx="3" fill="{grad}" stroke="#161412" stroke-width="1.5"/>')
    svg.append('  </g>')

    # Grid overlay lines (subtle 30mm tactical grid)
    svg.append('  <!-- 30mm Grid Overlay -->')
    for i in range(1, 6):
        pos = i * cell
        svg.append(f'  <line x1="{pos}" y1="0" x2="{pos}" y2="{height}" stroke="#d4af37" stroke-width="0.8" stroke-dasharray="4,8" opacity="0.4"/>')
        svg.append(f'  <line x1="0" y1="{pos}" x2="{width}" y2="{pos}" stroke="#d4af37" stroke-width="0.8" stroke-dasharray="4,8" opacity="0.4"/>')
    
    # Outer Border
    svg.append(f'  <rect x="0" y="0" width="{width}" height="{height}" fill="none" stroke="#5a4934" stroke-width="6"/>')
    svg.append(f'  <rect x="3" y="3" width="{width-6}" height="{height-6}" fill="none" stroke="#12100e" stroke-width="2"/>')

    # Coordinates
    cols = ['A', 'B', 'C', 'D', 'E', 'F']
    for r in range(6):
        for c in range(6):
            coord = f"{cols[c]}{6-r}"
            x = c * cell + 8
            y = r * cell + 18
            svg.append(f'  <text x="{x}" y="{y}" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#8c7a62" opacity="0.65">{coord}</text>')

    if page_type == "room1":
        # Spawn Zones: [V] = Vordere Zone (Row 3, 4), [H] = Hintere Zone (Row 5, 6)
        # S1..S4 = Helden Startzone (Row 1 / y: 600..720)
        # Pillars at B3, E3 (r=3, c=1; r=3, c=4 -> row 3 in 0-indexed is line 3, which is 6-3 = Row 3)
        
        # Pillars
        for (pc, pr) in [(1, 3), (4, 3)]:
            px = pc * cell + cell // 2
            py = pr * cell + cell // 2
            svg.append(f'''  <!-- Pillar at col {pc}, row {pr} -->
  <g filter="url(#shadow)">
    <circle cx="{px}" cy="{py}" r="46" fill="#181512" stroke="#0a0908" stroke-width="2"/>
    <circle cx="{px}" cy="{py}" r="40" fill="url(#pillarGrad)" stroke="#3a342c" stroke-width="3"/>
    <circle cx="{px}" cy="{py}" r="26" fill="none" stroke="#26221c" stroke-width="2" stroke-dasharray="6,4"/>
    <circle cx="{px}" cy="{py}" r="14" fill="#332d26"/>
    <text x="{px}" y="{py+5}" font-family="Georgia, serif" font-size="12" font-weight="bold" fill="#d5c8b5" text-anchor="middle">SÄULE</text>
  </g>''')

        # Chest at E4 (c=4, r=2)
        cx = 4 * cell + 22
        cy = 2 * cell + 32
        svg.append(f'''  <!-- Chest at E4 -->
  <g filter="url(#shadow)">
    <rect x="{cx}" y="{cy}" width="76" height="56" rx="4" fill="url(#woodGrad)" stroke="#1a0d05" stroke-width="2"/>
    <!-- Iron bands -->
    <rect x="{cx+10}" y="{cy}" width="8" height="56" fill="#2d2d2d" stroke="#111" stroke-width="1"/>
    <rect x="{cx+58}" y="{cy}" width="8" height="56" fill="#2d2d2d" stroke="#111" stroke-width="1"/>
    <!-- Keyhole lock -->
    <rect x="{cx+32}" y="{cy+20}" width="12" height="16" rx="2" fill="#d4af37" stroke="#68551b" stroke-width="1"/>
    <circle cx="{cx+38}" cy="{cy+26}" r="2.5" fill="#111"/>
    <text x="{cx+38}" y="{cy+50}" font-family="Georgia, serif" font-size="10" font-weight="bold" fill="#faedcd" text-anchor="middle">TRUHE</text>
  </g>''')

        # Door Tor T1 at C6/D6 (r=0, c=2 & 3)
        svg.append('''  <!-- Door at C6-D6 -->
  <g filter="url(#shadow)">
    <rect x="244" y="4" width="232" height="28" rx="3" fill="#8a532d" stroke="#d4af37" stroke-width="2"/>
    <rect x="250" y="8" width="105" height="20" fill="#4a2a14" stroke="#1a0d05" stroke-width="1"/>
    <rect x="365" y="8" width="105" height="20" fill="#4a2a14" stroke="#1a0d05" stroke-width="1"/>
    <text x="360" y="23" font-family="Georgia, serif" font-size="13" font-weight="bold" fill="#f8e7b9" text-anchor="middle">TOR T1 (TÜR-TOKEN)</text>
  </g>''')

        # Encounter Spawn Zone Watermarks: [H] in Row 5 & 6, [V] in Row 3 & 4
        # [H] Hintere Zone
        for (hc, hr) in [(1, 1), (4, 1)]:
            hx = hc * cell + cell // 2
            hy = hr * cell + cell // 2
            svg.append(f'''  <rect x="{hc*cell+15}" y="{hr*cell+15}" width="90" height="90" rx="8" fill="none" stroke="#8c2d19" stroke-width="2" stroke-dasharray="6,6" opacity="0.45"/>
  <text x="{hx}" y="{hy+6}" font-family="Arial, sans-serif" font-size="16" font-weight="bold" fill="#b8332a" text-anchor="middle" opacity="0.6">[ H ]</text>
  <text x="{hx}" y="{hy+24}" font-family="Arial, sans-serif" font-size="9" fill="#b8332a" text-anchor="middle" opacity="0.6">Hintere Zone</text>''')

        # [V] Vordere Zone
        for (vc, vr) in [(0, 2), (5, 2)]:
            vx = vc * cell + cell // 2
            vy = vr * cell + cell // 2
            svg.append(f'''  <rect x="{vc*cell+15}" y="{vr*cell+15}" width="90" height="90" rx="8" fill="none" stroke="#d4821a" stroke-width="2" stroke-dasharray="6,6" opacity="0.45"/>
  <text x="{vx}" y="{vy+6}" font-family="Arial, sans-serif" font-size="16" font-weight="bold" fill="#d4821a" text-anchor="middle" opacity="0.6">[ V ]</text>
  <text x="{vx}" y="{vy+24}" font-family="Arial, sans-serif" font-size="9" fill="#d4821a" text-anchor="middle" opacity="0.6">Vordere Zone</text>''')

        # Start Zone S1..S4 at row 5 (which is 1 on board, y: 600..720)
        heroes = [('S1', 'Berserker', 0), ('S2', 'Kriegstänzerin', 1), ('S3', 'Schurke', 2), ('S4', 'Magierin', 3)]
        for (sid, hname, sc) in heroes:
            sx = sc * cell + cell // 2
            sy = 5 * cell + cell // 2
            svg.append(f'''  <rect x="{sc*cell+12}" y="{5*cell+12}" width="96" height="96" rx="6" fill="#1b4d3e" fill-opacity="0.2" stroke="#2e7559" stroke-width="1.8" stroke-dasharray="5,4"/>
  <text x="{sx}" y="{sy}" font-family="Georgia, serif" font-size="15" font-weight="bold" fill="#58b38f" text-anchor="middle">{sid}</text>
  <text x="{sx}" y="{sy+18}" font-family="Arial, sans-serif" font-size="8.5" fill="#88cca8" text-anchor="middle">Start</text>''')

    elif page_type == "boss":
        # Sarcophagus across C6-D6 (c=2 and c=3, r=0)
        sx = 2 * cell + 20
        sy = 15
        svg.append(f'''  <!-- Sarcophagus -->
  <g filter="url(#shadow)">
    <rect x="{sx}" y="{sy}" width="200" height="90" rx="6" fill="#595247" stroke="#1d1914" stroke-width="3"/>
    <rect x="{sx+10}" y="{sy+8}" width="180" height="74" rx="4" fill="#3b352d" stroke="#d4af37" stroke-width="1.5"/>
    <!-- Carved Knight Relief -->
    <ellipse cx="{sx+100}" cy="{sy+45}" rx="70" ry="24" fill="#29241e" stroke="#6b5e4f" stroke-width="1.5"/>
    <!-- Sword relief -->
    <line x1="{sx+50}" y1="{sy+45}" x2="{sx+150}" y2="{sy+45}" stroke="#d4af37" stroke-width="2"/>
    <line x1="{sx+70}" y1="{sy+35}" x2="{sx+70}" y2="{sy+55}" stroke="#d4af37" stroke-width="2"/>
    <text x="{sx+100}" y="{sy+80}" font-family="Georgia, serif" font-size="11" font-weight="bold" fill="#f8e7b9" text-anchor="middle">PRUNK-SARKOPHAG</text>
  </g>''')

        # Boss Standee Footprint at C5-D5 (c=2,3 r=1)
        bx = 2 * cell + 25
        by = 1 * cell + 20
        svg.append(f'''  <!-- Boss GW (1x2 fields) -->
  <g filter="url(#shadow)">
    <rect x="{bx}" y="{by}" width="190" height="80" rx="8" fill="#5c1d11" fill-opacity="0.35" stroke="#8c2d19" stroke-width="3"/>
    <text x="{bx+95}" y="{by+38}" font-family="Georgia, serif" font-size="16" font-weight="bold" fill="#d9534f" text-anchor="middle">👑 GRUFTWÄCHTER</text>
    <text x="{bx+95}" y="{by+58}" font-family="Arial, sans-serif" font-size="11" fill="#f2b2ad" text-anchor="middle">Boss-Standee (60 × 30 mm)</text>
  </g>''')

        # Minion Guards SK3, SK4 at B5 (c=1, r=1) and E5 (c=4, r=1)
        for (mc, mr, mlabel) in [(1, 1, 'SK3 (Leibwache)'), (4, 1, 'SK4 (Leibwache)')]:
            mx = mc * cell + cell // 2
            my = mr * cell + cell // 2
            svg.append(f'''  <rect x="{mc*cell+15}" y="{mr*cell+15}" width="90" height="90" rx="8" fill="#8c2d19" fill-opacity="0.25" stroke="#8c2d19" stroke-width="2" stroke-dasharray="6,4"/>
  <text x="{mx}" y="{my+5}" font-family="Georgia, serif" font-size="13" font-weight="bold" fill="#e07567" text-anchor="middle">{mlabel}</text>''')

        # Pillars at A3, F3 (c=0, r=3 and c=5, r=3)
        for (pc, pr) in [(0, 3), (5, 3)]:
            px = pc * cell + cell // 2
            py = pr * cell + cell // 2
            svg.append(f'''  <!-- Pillar -->
  <g filter="url(#shadow)">
    <circle cx="{px}" cy="{py}" r="46" fill="#181512" stroke="#0a0908" stroke-width="2"/>
    <circle cx="{px}" cy="{py}" r="40" fill="url(#pillarGrad)" stroke="#3a342c" stroke-width="3"/>
    <circle cx="{px}" cy="{py}" r="26" fill="none" stroke="#26221c" stroke-width="2" stroke-dasharray="6,4"/>
    <text x="{px}" y="{py+5}" font-family="Georgia, serif" font-size="12" font-weight="bold" fill="#d5c8b5" text-anchor="middle">SÄULE</text>
  </g>''')

        # Spike Pit Trap at C3 (c=2, r=3)
        tx = 2 * cell + 15
        ty = 3 * cell + 15
        svg.append(f'''  <!-- Trap at C3 -->
  <g filter="url(#shadow)">
    <rect x="{tx}" y="{ty}" width="90" height="90" rx="4" fill="#14110e" stroke="#8c2d19" stroke-width="2"/>
    <!-- Spikes inside pit -->
    <polygon points="{tx+15},{ty+75} {tx+25},{ty+25} {tx+35},{ty+75}" fill="#6b6459" stroke="#111"/>
    <polygon points="{tx+35},{ty+75} {tx+45},{ty+20} {tx+55},{ty+75}" fill="#8a8275" stroke="#111"/>
    <polygon points="{tx+55},{ty+75} {tx+65},{ty+25} {tx+75},{ty+75}" fill="#6b6459" stroke="#111"/>
    <text x="{tx+45}" y="{ty+84}" font-family="Arial, sans-serif" font-size="9" font-weight="bold" fill="#e07567" text-anchor="middle">⚠️ STACHELGRUBE</text>
  </g>''')

        # Entrance Zone at C1, D1 (c=2, 3, r=5)
        for (ec, elabel) in [(2, 'Eingang E1'), (3, 'Eingang E2')]:
            ex = ec * cell + cell // 2
            ey = 5 * cell + cell // 2
            svg.append(f'''  <rect x="{ec*cell+12}" y="{5*cell+12}" width="96" height="96" rx="6" fill="#1b4d3e" fill-opacity="0.25" stroke="#2e7559" stroke-width="2" stroke-dasharray="5,4"/>
  <text x="{ex}" y="{ey+6}" font-family="Georgia, serif" font-size="13" font-weight="bold" fill="#58b38f" text-anchor="middle">{elabel}</text>''')

    svg.append('</svg>')
    return '\n'.join(svg)

# Write SVGs
svg1 = generate_dungeon_grid_svg("room1")
with open(r"c:\Users\christoph.willimzik\Agent_Bunny\RV_Quest\printables\gamebook_map_room1_crypt.svg", "w", encoding="utf-8") as f:
    f.write(svg1)

svg2 = generate_dungeon_grid_svg("boss")
with open(r"c:\Users\christoph.willimzik\Agent_Bunny\RV_Quest\printables\gamebook_map_boss_crypt.svg", "w", encoding="utf-8") as f:
    f.write(svg2)

print("Generated gamebook SVGs successfully!")

