import zipfile

def create_gamebook_odt(output_path):
    # ODF namespace declarations
    # 30 mm = 3.0cm, 180 mm = 18.0cm
    manifest = """<?xml version="1.0" encoding="UTF-8"?>
<manifest:manifest xmlns:manifest="urn:oasis:names:tc:opendocument:xmlns:manifest:1.0" manifest:version="1.2">
  <manifest:file-entry manifest:full-path="/" manifest:version="1.2" manifest:media-type="application/vnd.oasis.opendocument.text"/>
  <manifest:file-entry manifest:full-path="content.xml" manifest:media-type="text/xml"/>
  <manifest:file-entry manifest:full-path="styles.xml" manifest:media-type="text/xml"/>
  <manifest:file-entry manifest:full-path="meta.xml" manifest:media-type="text/xml"/>
</manifest:manifest>"""

    meta = """<?xml version="1.0" encoding="UTF-8"?>
<office:document-meta xmlns:office="urn:oasis:names:tc:opendocument:xmlns:office:1.0" xmlns:meta="urn:oasis:names:tc:opendocument:xmlns:meta:1.0" office:version="1.2">
  <office:meta>
    <meta:generator>Agent_Bunny_GameBook_Engine</meta:generator>
    <meta:title>Szenario 01 - Die Krypta von Dun-Karr</meta:title>
  </office:meta>
</office:document-meta>"""

    styles = """<?xml version="1.0" encoding="UTF-8"?>
<office:document-styles xmlns:office="urn:oasis:names:tc:opendocument:xmlns:office:1.0" xmlns:style="urn:oasis:names:tc:opendocument:xmlns:style:1.0" xmlns:fo="urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0" office:version="1.2">
  <office:master-styles>
    <style:master-page style:name="Standard" style:page-layout-name="PM1"/>
  </office:master-styles>
  <office:automatic-styles>
    <style:page-layout style:name="PM1">
      <style:page-layout-properties fo:page-width="21.0cm" fo:page-height="29.7cm" fo:margin-top="1.5cm" fo:margin-bottom="1.5cm" fo:margin-left="1.5cm" fo:margin-right="1.5cm"/>
    </style:page-layout>
  </office:automatic-styles>
</office:document-styles>"""

    # Cells styling
    # Grid: 6 columns x 3.0cm = 18.0cm
    content = """<?xml version="1.0" encoding="UTF-8"?>
<office:document-content xmlns:office="urn:oasis:names:tc:opendocument:xmlns:office:1.0" xmlns:style="urn:oasis:names:tc:opendocument:xmlns:style:1.0" xmlns:text="urn:oasis:names:tc:opendocument:xmlns:text:1.0" xmlns:table="urn:oasis:names:tc:opendocument:xmlns:table:1.0" xmlns:fo="urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0" office:version="1.2">
  <office:automatic-styles>
    <style:style style:name="TableGrid" style:family="table">
      <style:table-properties table:align="center" style:width="18.0cm"/>
    </style:style>
    <style:style style:name="TableCol" style:family="table-column">
      <style:table-column-properties style:column-width="3.0cm"/>
    </style:style>
    <style:style style:name="TableRow" style:family="table-row">
      <style:table-row-properties style:row-height="3.0cm" style:min-row-height="3.0cm"/>
    </style:style>
    
    <!-- Cell Styles -->
    <style:style style:name="CellBase" style:family="table-cell">
      <style:table-cell-properties fo:background-color="#DFD3BD" fo:padding="0.1cm" fo:border="0.05cm solid #8A7660"/>
    </style:style>
    <style:style style:name="CellDoor" style:family="table-cell">
      <style:table-cell-properties fo:background-color="#D4A373" fo:padding="0.1cm" fo:border="0.08cm solid #5C1D11"/>
    </style:style>
    <style:style style:name="CellMonster" style:family="table-cell">
      <style:table-cell-properties fo:background-color="#F2D6D3" fo:padding="0.1cm" fo:border="0.06cm dashed #8C2D19"/>
    </style:style>
    <style:style style:name="CellPillar" style:family="table-cell">
      <style:table-cell-properties fo:background-color="#73695D" fo:padding="0.1cm" fo:border="0.08cm solid #3D2D1D"/>
    </style:style>
    <style:style style:name="CellStart" style:family="table-cell">
      <style:table-cell-properties fo:background-color="#D0E6DB" fo:padding="0.1cm" fo:border="0.06cm dashed #174231"/>
    </style:style>
    <style:style style:name="CellChest" style:family="table-cell">
      <style:table-cell-properties fo:background-color="#FAEDCD" fo:padding="0.1cm" fo:border="0.06cm solid #875817"/>
    </style:style>
    <style:style style:name="CellRubble" style:family="table-cell">
      <style:table-cell-properties fo:background-color="#C2B59B" fo:padding="0.1cm" fo:border="0.05cm solid #8A7660"/>
    </style:style>
    <style:style style:name="CellBoss" style:family="table-cell">
      <style:table-cell-properties fo:background-color="#F5C8C2" fo:padding="0.1cm" fo:border="0.08cm solid #5C1D11"/>
    </style:style>
    <style:style style:name="CellSarcophagus" style:family="table-cell">
      <style:table-cell-properties fo:background-color="#8D7B68" fo:padding="0.1cm" fo:border="0.08cm solid #2B1D0C"/>
    </style:style>

    <!-- Paragraph Styles -->
    <style:style style:name="P_Title" style:family="paragraph">
      <style:paragraph-properties fo:margin-top="0cm" fo:margin-bottom="0.4cm"/>
      <style:text-properties fo:font-size="18pt" fo:font-weight="bold" fo:color="#3D2D1D" style:font-name="Georgia"/>
    </style:style>
    <style:style style:name="P_H2" style:family="paragraph">
      <style:paragraph-properties fo:margin-top="0.3cm" fo:margin-bottom="0.15cm"/>
      <style:text-properties fo:font-size="12pt" fo:font-weight="bold" fo:color="#5C1D11" style:font-name="Georgia"/>
    </style:style>
    <style:style style:name="P_Flavor" style:family="paragraph">
      <style:paragraph-properties fo:margin-left="0.4cm" fo:margin-right="0.4cm" fo:margin-bottom="0.3cm"/>
      <style:text-properties fo:font-size="9pt" fo:font-style="italic" fo:color="#3D3124"/>
    </style:style>
    <style:style style:name="P_CellCoord" style:family="paragraph">
      <style:paragraph-properties fo:text-align="left" fo:margin-bottom="0.2cm"/>
      <style:text-properties fo:font-size="7pt" fo:color="#7A6A53"/>
    </style:style>
    <style:style style:name="P_CellText" style:family="paragraph">
      <style:paragraph-properties fo:text-align="center"/>
      <style:text-properties fo:font-size="9pt" fo:font-weight="bold"/>
    </style:style>
    <style:style style:name="P_PageBreak" style:family="paragraph">
      <style:paragraph-properties fo:break-before="page"/>
    </style:style>
  </office:automatic-styles>

  <office:body>
    <office:text>
      <!-- SEITE 1: TEXT TEIL 1 -->
      <text:p style:name="P_Title">Szenario 01: Die Krypta von Dun-Karr</text:p>
      <text:p style:name="P_Flavor">„Klammer Grabesdunst schlägt euch entgegen. Das Flackern eurer Fackeln wirft tanzende Schatten an die feuchten Steinwände. Vor euch liegen die Vorkammern des verfluchten Kriegsfürsten...“</text:p>
      
      <text:p style:name="P_H2">1. Missionsziel &amp; Vorstoß</text:p>
      <text:p>Kämpft euch durch die Vorhut und öffnet das Tor bei C6/D6, um in das innere Grabgewölbe vorzudringen.</text:p>
      
      <text:p style:name="P_H2">2. Wächter der Vorhalle</text:p>
      <text:p><text:span text:style-name="P_CellText">👺 Goblin-Späher (2x) [A4, F4]:</text:span> LP 3 | VT 5 | BEW 4 | INI 4. Nahkampf 1 Schaden. Feigheit: Weicht bei 1 LP 2 Felder zurück.</text:p>
      <text:p><text:span text:style-name="P_CellText">💀 Skelettkrieger (2x) [B5, E5]:</text:span> LP 4 | VT 6 | BEW 3 | INI 2. Nahkampf 2 Schaden. Hämmer/Keulen machen +1 Bonusschaden.</text:p>
      
      <text:p style:name="P_H2">3. Interaktionen &amp; Fallen</text:p>
      <text:p>• <text:span text:style-name="P_CellText">Alarmhorn (B4):</text:span> Bleibt der Goblin-Späher am Leben, stößt er ins Horn: In Raum 2 erwacht +1 Skelett!</text:p>
      <text:p>• <text:span text:style-name="P_CellText">Schatztruhe (E4):</text:span> LIS (SG 5): Ziehe 1 Karte vom Ausrüstungsdeck.</text:p>
      <text:p>• <text:span text:style-name="P_CellText">Tor T1 (C6/D6):</text:span> KRA (SG 6) oder LIS (SG 5) zum Öffnen.</text:p>

      <!-- SEITE 2: KAMPFPLAN 1 -->
      <text:p style:name="P_PageBreak"/>
      <text:p style:name="P_H2">KAMPFPLAN 1: VORKAMMERN (6x6 FELDER, 30 mm RASTER)</text:p>
      <table:table table:name="Grid1" table:style-name="TableGrid">
        <table:table-column table:style-name="TableCol" table:number-columns-repeated="6"/>
        
        <!-- Row 6 -->
        <table:table-row table:style-name="TableRow">
          <table:table-cell table:style-name="CellBase"><text:p style:name="P_CellCoord">A6</text:p></table:table-cell>
          <table:table-cell table:style-name="CellBase"><text:p style:name="P_CellCoord">B6</text:p></table:table-cell>
          <table:table-cell table:style-name="CellDoor"><text:p style:name="P_CellCoord">C6</text:p><text:p style:name="P_CellText">TOR T1</text:p></table:table-cell>
          <table:table-cell table:style-name="CellDoor"><text:p style:name="P_CellCoord">D6</text:p><text:p style:name="P_CellText">TOR T1</text:p></table:table-cell>
          <table:table-cell table:style-name="CellBase"><text:p style:name="P_CellCoord">E6</text:p></table:table-cell>
          <table:table-cell table:style-name="CellBase"><text:p style:name="P_CellCoord">F6</text:p></table:table-cell>
        </table:table-row>

        <!-- Row 5 -->
        <table:table-row table:style-name="TableRow">
          <table:table-cell table:style-name="CellBase"><text:p style:name="P_CellCoord">A5</text:p></table:table-cell>
          <table:table-cell table:style-name="CellMonster"><text:p style:name="P_CellCoord">B5</text:p><text:p style:name="P_CellText">💀 SK1</text:p></table:table-cell>
          <table:table-cell table:style-name="CellBase"><text:p style:name="P_CellCoord">C5</text:p></table:table-cell>
          <table:table-cell table:style-name="CellBase"><text:p style:name="P_CellCoord">D5</text:p></table:table-cell>
          <table:table-cell table:style-name="CellMonster"><text:p style:name="P_CellCoord">E5</text:p><text:p style:name="P_CellText">💀 SK2</text:p></table:table-cell>
          <table:table-cell table:style-name="CellBase"><text:p style:name="P_CellCoord">F5</text:p></table:table-cell>
        </table:table-row>

        <!-- Row 4 -->
        <table:table-row table:style-name="TableRow">
          <table:table-cell table:style-name="CellMonster"><text:p style:name="P_CellCoord">A4</text:p><text:p style:name="P_CellText">👺 G1</text:p></table:table-cell>
          <table:table-cell table:style-name="CellBase"><text:p style:name="P_CellCoord">B4</text:p><text:p style:name="P_CellText">📯 Horn</text:p></table:table-cell>
          <table:table-cell table:style-name="CellBase"><text:p style:name="P_CellCoord">C4</text:p></table:table-cell>
          <table:table-cell table:style-name="CellBase"><text:p style:name="P_CellCoord">D4</text:p></table:table-cell>
          <table:table-cell table:style-name="CellChest"><text:p style:name="P_CellCoord">E4</text:p><text:p style:name="P_CellText">📦 TRUHE</text:p></table:table-cell>
          <table:table-cell table:style-name="CellMonster"><text:p style:name="P_CellCoord">F4</text:p><text:p style:name="P_CellText">👺 G2</text:p></table:table-cell>
        </table:table-row>

        <!-- Row 3 -->
        <table:table-row table:style-name="TableRow">
          <table:table-cell table:style-name="CellBase"><text:p style:name="P_CellCoord">A3</text:p></table:table-cell>
          <table:table-cell table:style-name="CellPillar"><text:p style:name="P_CellCoord">B3</text:p><text:p style:name="P_CellText">SÄULE</text:p></table:table-cell>
          <table:table-cell table:style-name="CellBase"><text:p style:name="P_CellCoord">C3</text:p></table:table-cell>
          <table:table-cell table:style-name="CellBase"><text:p style:name="P_CellCoord">D3</text:p></table:table-cell>
          <table:table-cell table:style-name="CellPillar"><text:p style:name="P_CellCoord">E3</text:p><text:p style:name="P_CellText">SÄULE</text:p></table:table-cell>
          <table:table-cell table:style-name="CellBase"><text:p style:name="P_CellCoord">F3</text:p></table:table-cell>
        </table:table-row>

        <!-- Row 2 -->
        <table:table-row table:style-name="TableRow">
          <table:table-cell table:style-name="CellBase"><text:p style:name="P_CellCoord">A2</text:p></table:table-cell>
          <table:table-cell table:style-name="CellBase"><text:p style:name="P_CellCoord">B2</text:p></table:table-cell>
          <table:table-cell table:style-name="CellRubble"><text:p style:name="P_CellCoord">C2</text:p><text:p style:name="P_CellText">Geröll</text:p></table:table-cell>
          <table:table-cell table:style-name="CellRubble"><text:p style:name="P_CellCoord">D2</text:p><text:p style:name="P_CellText">Geröll</text:p></table:table-cell>
          <table:table-cell table:style-name="CellBase"><text:p style:name="P_CellCoord">E2</text:p></table:table-cell>
          <table:table-cell table:style-name="CellBase"><text:p style:name="P_CellCoord">F2</text:p></table:table-cell>
        </table:table-row>

        <!-- Row 1 -->
        <table:table-row table:style-name="TableRow">
          <table:table-cell table:style-name="CellStart"><text:p style:name="P_CellCoord">A1</text:p><text:p style:name="P_CellText">🛡️ S1</text:p></table:table-cell>
          <table:table-cell table:style-name="CellStart"><text:p style:name="P_CellCoord">B1</text:p><text:p style:name="P_CellText">🗡️ S2</text:p></table:table-cell>
          <table:table-cell table:style-name="CellStart"><text:p style:name="P_CellCoord">C1</text:p><text:p style:name="P_CellText">🗝️ S3</text:p></table:table-cell>
          <table:table-cell table:style-name="CellStart"><text:p style:name="P_CellCoord">D1</text:p><text:p style:name="P_CellText">📜 S4</text:p></table:table-cell>
          <table:table-cell table:style-name="CellBase"><text:p style:name="P_CellCoord">E1</text:p></table:table-cell>
          <table:table-cell table:style-name="CellBase"><text:p style:name="P_CellCoord">F1</text:p></table:table-cell>
        </table:table-row>
      </table:table>

      <!-- SEITE 3: TEXT TEIL 2 -->
      <text:p style:name="P_PageBreak"/>
      <text:p style:name="P_Title">Die Grabkammer des Gruftwächters (Boss)</text:p>
      <text:p style:name="P_Flavor">„Das Steintor weicht krachend zurück. Vor euch erhebt sich ein gewaltiger Sarkophag. Kalter Hauch erfüllt den Raum, als die uralte Rüstung des Kriegsfürsten knarrend zum Leben erwacht...“</text:p>
      
      <text:p style:name="P_H2">1. Der Gruftwächter (Boss)</text:p>
      <text:p><text:span text:style-name="P_CellText">👑 Grabunhold / Gruftwächter [C5-D5, 1x2]:</text:span> LP 14 | VT 7 | RÜSTUNG 1 | BEW 3 | INI 3.</text:p>
      <text:p>Angriff: Streitkolben (Nahkampf, 3 Schaden).</text:p>
      <text:p><text:span text:style-name="P_CellText">Boss-Fähigkeit (Gruftbeben — unter 7 LP):</text:span> Alle Helden GES (SG 6) oder Verlangsamt (2 BP zum Aufstehen). Ruft 1 Skelettkrieger als Verstärkung!</text:p>

      <text:p style:name="P_H2">2. Leibwache &amp; Beute</text:p>
      <text:p>• <text:span text:style-name="P_CellText">Skelett-Leibwache (2x) [B5, E5]:</text:span> LP 4 | VT 6 | BEW 3 | INI 2. Flankieren den Sarkophag.</text:p>
      <text:p>• <text:span text:style-name="P_CellText">Der Prunksarkophag:</text:span> 2 Ausrüstungskarten, 40 Goldmünzen &amp; Quest-Relikt (Siegelring). 1 EP pro Held!</text:p>

      <!-- SEITE 4: KAMPFPLAN 2 -->
      <text:p style:name="P_PageBreak"/>
      <text:p style:name="P_H2">KAMPFPLAN 2: BOSS-ARENA &amp; SARKOPHAG (6x6 FELDER, 30 mm RASTER)</text:p>
      <table:table table:name="Grid2" table:style-name="TableGrid">
        <table:table-column table:style-name="TableCol" table:number-columns-repeated="6"/>
        
        <!-- Row 6 -->
        <table:table-row table:style-name="TableRow">
          <table:table-cell table:style-name="CellBase"><text:p style:name="P_CellCoord">A6</text:p></table:table-cell>
          <table:table-cell table:style-name="CellBase"><text:p style:name="P_CellCoord">B6</text:p></table:table-cell>
          <table:table-cell table:style-name="CellSarcophagus"><text:p style:name="P_CellCoord">C6</text:p><text:p style:name="P_CellText">SARKOPHAG</text:p></table:table-cell>
          <table:table-cell table:style-name="CellSarcophagus"><text:p style:name="P_CellCoord">D6</text:p><text:p style:name="P_CellText">SARKOPHAG</text:p></table:table-cell>
          <table:table-cell table:style-name="CellBase"><text:p style:name="P_CellCoord">E6</text:p></table:table-cell>
          <table:table-cell table:style-name="CellBase"><text:p style:name="P_CellCoord">F6</text:p></table:table-cell>
        </table:table-row>

        <!-- Row 5 -->
        <table:table-row table:style-name="TableRow">
          <table:table-cell table:style-name="CellBase"><text:p style:name="P_CellCoord">A5</text:p></table:table-cell>
          <table:table-cell table:style-name="CellMonster"><text:p style:name="P_CellCoord">B5</text:p><text:p style:name="P_CellText">💀 SK3</text:p></table:table-cell>
          <table:table-cell table:style-name="CellBoss"><text:p style:name="P_CellCoord">C5</text:p><text:p style:name="P_CellText">GRUFTWÄCHTER</text:p></table:table-cell>
          <table:table-cell table:style-name="CellBoss"><text:p style:name="P_CellCoord">D5</text:p><text:p style:name="P_CellText">BOSS (1x2)</text:p></table:table-cell>
          <table:table-cell table:style-name="CellMonster"><text:p style:name="P_CellCoord">E5</text:p><text:p style:name="P_CellText">💀 SK4</text:p></table:table-cell>
          <table:table-cell table:style-name="CellBase"><text:p style:name="P_CellCoord">F5</text:p></table:table-cell>
        </table:table-row>

        <!-- Row 4 -->
        <table:table-row table:style-name="TableRow">
          <table:table-cell table:style-name="CellBase"><text:p style:name="P_CellCoord">A4</text:p></table:table-cell>
          <table:table-cell table:style-name="CellBase"><text:p style:name="P_CellCoord">B4</text:p></table:table-cell>
          <table:table-cell table:style-name="CellBase"><text:p style:name="P_CellCoord">C4</text:p></table:table-cell>
          <table:table-cell table:style-name="CellBase"><text:p style:name="P_CellCoord">D4</text:p></table:table-cell>
          <table:table-cell table:style-name="CellBase"><text:p style:name="P_CellCoord">E4</text:p></table:table-cell>
          <table:table-cell table:style-name="CellBase"><text:p style:name="P_CellCoord">F4</text:p></table:table-cell>
        </table:table-row>

        <!-- Row 3 -->
        <table:table-row table:style-name="TableRow">
          <table:table-cell table:style-name="CellPillar"><text:p style:name="P_CellCoord">A3</text:p><text:p style:name="P_CellText">SÄULE</text:p></table:table-cell>
          <table:table-cell table:style-name="CellBase"><text:p style:name="P_CellCoord">B3</text:p></table:table-cell>
          <table:table-cell table:style-name="CellMonster"><text:p style:name="P_CellCoord">C3</text:p><text:p style:name="P_CellText">⚠️ GRUBE</text:p></table:table-cell>
          <table:table-cell table:style-name="CellBase"><text:p style:name="P_CellCoord">D3</text:p></table:table-cell>
          <table:table-cell table:style-name="CellBase"><text:p style:name="P_CellCoord">E3</text:p></table:table-cell>
          <table:table-cell table:style-name="CellPillar"><text:p style:name="P_CellCoord">F3</text:p><text:p style:name="P_CellText">SÄULE</text:p></table:table-cell>
        </table:table-row>

        <!-- Row 2 -->
        <table:table-row table:style-name="TableRow">
          <table:table-cell table:style-name="CellBase"><text:p style:name="P_CellCoord">A2</text:p></table:table-cell>
          <table:table-cell table:style-name="CellBase"><text:p style:name="P_CellCoord">B2</text:p></table:table-cell>
          <table:table-cell table:style-name="CellBase"><text:p style:name="P_CellCoord">C2</text:p></table:table-cell>
          <table:table-cell table:style-name="CellBase"><text:p style:name="P_CellCoord">D2</text:p></table:table-cell>
          <table:table-cell table:style-name="CellBase"><text:p style:name="P_CellCoord">E2</text:p></table:table-cell>
          <table:table-cell table:style-name="CellBase"><text:p style:name="P_CellCoord">F2</text:p></table:table-cell>
        </table:table-row>

        <!-- Row 1 -->
        <table:table-row table:style-name="TableRow">
          <table:table-cell table:style-name="CellBase"><text:p style:name="P_CellCoord">A1</text:p></table:table-cell>
          <table:table-cell table:style-name="CellBase"><text:p style:name="P_CellCoord">B1</text:p></table:table-cell>
          <table:table-cell table:style-name="CellStart"><text:p style:name="P_CellCoord">C1</text:p><text:p style:name="P_CellText">Eingang E1</text:p></table:table-cell>
          <table:table-cell table:style-name="CellStart"><text:p style:name="P_CellCoord">D1</text:p><text:p style:name="P_CellText">Eingang E2</text:p></table:table-cell>
          <table:table-cell table:style-name="CellBase"><text:p style:name="P_CellCoord">E1</text:p></table:table-cell>
          <table:table-cell table:style-name="CellBase"><text:p style:name="P_CellCoord">F1</text:p></table:table-cell>
        </table:table-row>
      </table:table>

    </office:text>
  </office:body>
</office:document-content>"""

    with zipfile.ZipFile(output_path, 'w') as odt:
        # mimetype must be first and uncompressed
        odt.writestr('mimetype', 'application/vnd.oasis.opendocument.text', compress_type=zipfile.ZIP_STORED)
        odt.writestr('META-INF/manifest.xml', manifest, compress_type=zipfile.ZIP_DEFLATED)
        odt.writestr('meta.xml', meta, compress_type=zipfile.ZIP_DEFLATED)
        odt.writestr('styles.xml', styles, compress_type=zipfile.ZIP_DEFLATED)
        odt.writestr('content.xml', content, compress_type=zipfile.ZIP_DEFLATED)

if __name__ == '__main__':
    out_file = r'c:\Users\christoph.willimzik\Agent_Bunny\RV_Quest\printables\gamebook_scenario_01.odt'
    create_gamebook_odt(out_file)
    print("Successfully created ODT:", out_file)

