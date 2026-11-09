import zipfile

def create_rich_gamebook_odt(output_path, svg1_path, svg2_path):
    with open(svg1_path, 'rb') as f:
        svg1_data = f.read()
    with open(svg2_path, 'rb') as f:
        svg2_data = f.read()

    manifest = """<?xml version="1.0" encoding="UTF-8"?>
<manifest:manifest xmlns:manifest="urn:oasis:names:tc:opendocument:xmlns:manifest:1.0" manifest:version="1.2">
  <manifest:file-entry manifest:full-path="/" manifest:version="1.2" manifest:media-type="application/vnd.oasis.opendocument.text"/>
  <manifest:file-entry manifest:full-path="content.xml" manifest:media-type="text/xml"/>
  <manifest:file-entry manifest:full-path="styles.xml" manifest:media-type="text/xml"/>
  <manifest:file-entry manifest:full-path="meta.xml" manifest:media-type="text/xml"/>
  <manifest:file-entry manifest:full-path="Pictures/map1.svg" manifest:media-type="image/svg+xml"/>
  <manifest:file-entry manifest:full-path="Pictures/map2.svg" manifest:media-type="image/svg+xml"/>
</manifest:manifest>"""

    meta = """<?xml version="1.0" encoding="UTF-8"?>
<office:document-meta xmlns:office="urn:oasis:names:tc:opendocument:xmlns:office:1.0" xmlns:meta="urn:oasis:names:tc:opendocument:xmlns:meta:1.0" office:version="1.2">
  <office:meta>
    <meta:generator>Agent_Bunny_GameBook_Engine</meta:generator>
    <meta:title>Szenario 01 - Die verfluchte Krypta von Dun-Karr</meta:title>
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

    content = """<?xml version="1.0" encoding="UTF-8"?>
<office:document-content xmlns:office="urn:oasis:names:tc:opendocument:xmlns:office:1.0" xmlns:style="urn:oasis:names:tc:opendocument:xmlns:style:1.0" xmlns:text="urn:oasis:names:tc:opendocument:xmlns:text:1.0" xmlns:draw="urn:oasis:names:tc:opendocument:xmlns:drawing:1.0" xmlns:svg="urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0" xmlns:fo="urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0" xmlns:xlink="http://www.w3.org/1999/xlink" office:version="1.2">
  <office:automatic-styles>
    <style:style style:name="P_Title" style:family="paragraph">
      <style:paragraph-properties fo:margin-top="0cm" fo:margin-bottom="0.3cm"/>
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
    <style:style style:name="P_Center" style:family="paragraph">
      <style:paragraph-properties fo:text-align="center"/>
    </style:style>
    <style:style style:name="P_PageBreak" style:family="paragraph">
      <style:paragraph-properties fo:break-before="page"/>
    </style:style>
    <style:style style:name="Frame_Map" style:family="graphic">
      <style:graphic-properties style:horizontal-pos="center" style:horizontal-rel="paragraph" style:vertical-pos="middle" style:vertical-rel="paragraph" fo:margin-top="0.2cm" fo:margin-bottom="0.2cm"/>
    </style:style>
  </office:automatic-styles>

  <office:body>
    <office:text>
      <!-- SEITE 1: TEXT TEIL 1 -->
      <text:p style:name="P_Title">Szenario 01 • Teil 1: Die Vorkammern</text:p>
      <text:p style:name="P_Flavor">„Klammer Grabesdunst schlägt euch entgegen. Das Flackern eurer Fackeln wirft tanzende Schatten an die feuchten Steinwände. Ihr betretet die uralte Vorkammer...“</text:p>
      
      <text:p style:name="P_H2">1. Dynamisches Raum-Setup (Begegnungsdeck)</text:p>
      <text:p>Dieses Gewölbe wird dynamisch durch das gemischte <text:span text:font-weight="bold">Begegnungsdeck (16 Karten)</text:span> bespielt!</text:p>
      <text:p>• <text:span text:font-weight="bold">Beim Betreten:</text:span> Deckt die oberste Karte des Begegnungsdecks auf.</text:p>
      <text:p>• <text:span text:font-weight="bold">[V] Vordere Zone:</text:span> Monster mit [V] auf die markierten Felder (z. B. A4, F4) stellen.</text:p>
      <text:p>• <text:span text:font-weight="bold">[H] Hintere Zone:</text:span> Fernkämpfer / Lauernde Monster mit [H] auf die hinteren Zonen (B5, E5) platzieren.</text:p>
      <text:p>• <text:span text:font-weight="bold">Sonderregeln:</text:span> Prüft, ob die Karte einen »Hinterhalt!« auslöst (Monster schlagen vor den Helden zu!).</text:p>
      
      <text:p style:name="P_H2">2. Interaktives Gelände auf dem Plan</text:p>
      <text:p>• <text:span text:font-weight="bold">2x Steinsäulen (B3, E3):</text:span> Blockieren Bewegung &amp; Sichtlinie. Bieten volle Deckung vor Pfeilen.</text:p>
      <text:p>• <text:span text:font-weight="bold">Schatztruhe (E4):</text:span> Knacken mit LIS (SG 5) oder Brechstange: Ziehe 1 Ausrüstungskarte!</text:p>
      <text:p>• <text:span text:font-weight="bold">Tor T1 (C6/D6):</text:span> Verdecktes Tür-Token. KRA (SG 6), LIS (SG 5) oder Schlüssel nötig. Führt zum Boss!</text:p>

      <text:p style:name="P_H2">3. Startpositionen der Helden</text:p>
      <text:p>Helden starten am Südrand: S1 (Berserker), S2 (Kriegstänzerin), S3 (Halsabschneider), S4 (Magierin).</text:p>

      <!-- SEITE 2: KAMPFPLAN 1 (180x180 mm SVG) -->
      <text:p style:name="P_PageBreak"/>
      <text:p style:name="P_H2">KAMPFPLAN 1: VORKAMMERN (6x6 FELDER, 30 mm RASTER)</text:p>
      <text:p style:name="P_Center">
        <draw:frame draw:style-name="Frame_Map" draw:name="Map1" text:anchor-type="paragraph" svg:width="18.0cm" svg:height="18.0cm">
          <draw:image xlink:href="Pictures/map1.svg" xlink:type="simple" xlink:show="embed" xlink:actuate="onLoad"/>
        </draw:frame>
      </text:p>

      <!-- SEITE 3: TEXT TEIL 2 (BOSS) -->
      <text:p style:name="P_PageBreak"/>
      <text:p style:name="P_Title">Die Grabkammer des Gruftwächters (Boss)</text:p>
      <text:p style:name="P_Flavor">„Das Steintor weicht krachend zurück. Vor euch erhebt sich ein gewaltiger Prunksarkophag. Kalter Grabeshauch erfüllt den Raum, als die uralte Prunkrüstung des Kriegsfürsten knarrend zum Leben erwacht...“</text:p>
      
      <text:p style:name="P_H2">1. Der Gruftwächter (Boss — 1x2 Felder)</text:p>
      <text:p><text:span text:font-weight="bold">👑 Grabunhold / Gruftwächter [Pos. C5–D5]:</text:span> LP 14 | VT 7 | RÜSTUNG 1 | BEW 3 | INI 3.</text:p>
      <text:p>• Streitkolben: Nahkampf, 3 Schaden.</text:p>
      <text:p>• Boss-Fähigkeit (Gruftbeben — unter 7 LP): Alle Helden GES (SG 6) oder Verlangsamt (2 BP zum Aufstehen). Ruft 1 Skelett-Verstärkung!</text:p>

      <text:p style:name="P_H2">2. Leibwache &amp; Gefahren</text:p>
      <text:p>• <text:span text:font-weight="bold">2x Skelett-Leibwache [B5, E5]:</text:span> LP 4 | VT 6 | BEW 3 | INI 2. Flankieren den Sarkophag.</text:p>
      <text:p>• <text:span text:font-weight="bold">Verborgene Stachelgrube (C3):</text:span> 2 Direktschaden &amp; Bewegung stoppt.</text:p>

      <text:p style:name="P_H2">3. Beute &amp; Belohnung</text:p>
      <text:p>• Prunksarkophag (C6/D6): 2 Ausrüstungskarten + 40 Goldmünzen + Quest-Relikt (Siegelring). 1 EP pro Held!</text:p>

      <!-- SEITE 4: KAMPFPLAN 2 (180x180 mm SVG) -->
      <text:p style:name="P_PageBreak"/>
      <text:p style:name="P_H2">KAMPFPLAN 2: BOSS-ARENA &amp; SARKOPHAG (6x6 FELDER, 30 mm RASTER)</text:p>
      <text:p style:name="P_Center">
        <draw:frame draw:style-name="Frame_Map" draw:name="Map2" text:anchor-type="paragraph" svg:width="18.0cm" svg:height="18.0cm">
          <draw:image xlink:href="Pictures/map2.svg" xlink:type="simple" xlink:show="embed" xlink:actuate="onLoad"/>
        </draw:frame>
      </text:p>

    </office:text>
  </office:body>
</office:document-content>"""

    with zipfile.ZipFile(output_path, 'w') as odt:
        odt.writestr('mimetype', 'application/vnd.oasis.opendocument.text', compress_type=zipfile.ZIP_STORED)
        odt.writestr('META-INF/manifest.xml', manifest, compress_type=zipfile.ZIP_DEFLATED)
        odt.writestr('meta.xml', meta, compress_type=zipfile.ZIP_DEFLATED)
        odt.writestr('styles.xml', styles, compress_type=zipfile.ZIP_DEFLATED)
        odt.writestr('Pictures/map1.svg', svg1_data, compress_type=zipfile.ZIP_DEFLATED)
        odt.writestr('Pictures/map2.svg', svg2_data, compress_type=zipfile.ZIP_DEFLATED)
        odt.writestr('content.xml', content, compress_type=zipfile.ZIP_DEFLATED)

if __name__ == '__main__':
    out_odt = r'c:\Users\christoph.willimzik\Agent_Bunny\RV_Quest\printables\gamebook_scenario_01.odt'
    svg1 = r'c:\Users\christoph.willimzik\Agent_Bunny\RV_Quest\printables\gamebook_map_room1_crypt.svg'
    svg2 = r'c:\Users\christoph.willimzik\Agent_Bunny\RV_Quest\printables\gamebook_map_boss_crypt.svg'
    create_rich_gamebook_odt(out_odt, svg1, svg2)
    print("Successfully generated rich ODT with embedded vector floor textures!")

