import zipfile
import os

def create_rich_gamebook_docx(output_path, svg1_path, svg2_path):
    # Read SVGs
    with open(svg1_path, 'rb') as f:
        svg1_data = f.read()
    with open(svg2_path, 'rb') as f:
        svg2_data = f.read()

    # In Word OpenXML, vector graphics / SVGs can be embedded via drawingML or directly.
    # Alternatively, we can include the SVG and standard drawingML reference, or embed an SVG image part.
    # Word supports SVG as an image part with contentType image/svg+xml since Office 2016 / 365 / LibreOffice!

    content_types = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Default Extension="svg" ContentType="image/svg+xml"/>
  <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
  <Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>
</Types>"""

    rels = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
</Relationships>"""

    doc_rels = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" Target="media/map1.svg"/>
  <Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" Target="media/map2.svg"/>
</Relationships>"""

    styles = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:docDefaults>
    <w:rPrDefault>
      <w:rPr>
        <w:rFonts w:ascii="Georgia" w:hAnsi="Georgia" w:cs="Georgia"/>
        <w:sz w:val="19"/>
        <w:szCs w:val="19"/>
        <w:color w:val="1A1A1A"/>
      </w:rPr>
    </w:rPrDefault>
  </w:docDefaults>
</w:styles>"""

    # 180 mm = 6480000 EMUs (1 mm = 36000 EMUs)
    # 180 mm x 180 mm
    def make_svg_drawing(rel_id, title):
        return f"""<w:p>
      <w:pPr><w:jc w:val="center"/><w:spacing w:before="60" w:after="60"/></w:pPr>
      <w:r>
        <w:drawing>
          <wp:inline distT="0" distB="0" distL="0" distR="0" xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing">
            <wp:extent cx="6480000" cy="6480000"/>
            <wp:docPr id="1" name="{title}"/>
            <a:graphic xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">
              <a:graphicData uri="http://schemas.openxmlformats.org/drawingml/2006/picture">
                <pic:pic xmlns:pic="http://schemas.openxmlformats.org/drawingml/2006/picture">
                  <pic:nvPicPr>
                    <pic:cNvPr id="0" name="{title}"/>
                    <pic:cNvPicPr/>
                  </pic:nvPicPr>
                  <pic:blipFill>
                    <a:blip r:embed="{rel_id}" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"/>
                    <a:stretch><a:fillRect/></a:stretch>
                  </pic:blipFill>
                  <pic:spPr>
                    <a:xfrm><a:off x="0" y="0"/><a:ext cx="6480000" cy="6480000"/></a:xfrm>
                    <a:prstGeom prst="rect"><a:avLst/></a:prstGeom>
                  </pic:spPr>
                </pic:pic>
              </a:graphicData>
            </a:graphic>
          </wp:inline>
        </w:drawing>
      </w:r>
    </w:p>"""

    p_break = '<w:p><w:r><w:br w:type="page"/></w:r></w:p>'

    document_xml = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:body>
    <!-- ========================================== -->
    <!-- SEITE 1: TEXT DOPPELSEITE 1                -->
    <!-- ========================================== -->
    <w:p>
      <w:pPr><w:spacing w:before="0" w:after="40"/></w:pPr>
      <w:r><w:rPr><w:b/><w:sz w:val="17"/><w:color w:val="8C2D19"/></w:rPr><w:t>SZENARIO 01 • TEIL 1: DIE VORKAMMERN</w:t></w:r>
    </w:p>
    <w:p>
      <w:pPr><w:spacing w:before="0" w:after="120"/></w:pPr>
      <w:r><w:rPr><w:b/><w:sz w:val="32"/><w:color w:val="3D2D1D"/></w:rPr><w:t>Die verfluchte Krypta von Dun-Karr</w:t></w:r>
    </w:p>
    <w:p>
      <w:pPr><w:spacing w:before="0" w:after="120"/><w:ind w:left="120" w:right="120"/></w:pPr>
      <w:r><w:rPr><w:i/><w:sz w:val="17"/><w:color w:val="3D3124"/></w:rPr><w:t>„Klammer Grabesdunst schlägt euch entgegen. Das Flackern eurer Fackeln wirft tanzende Schatten an die feuchten Steinwände. Ihr betretet die uralte Vorkammer...“</w:t></w:r>
    </w:p>
    
    <w:p>
      <w:pPr><w:spacing w:before="100" w:after="40"/></w:pPr>
      <w:r><w:rPr><w:b/><w:sz w:val="21"/><w:color w:val="5C1D11"/></w:rPr><w:t>1. DYNAMISCHES RAUM-SETUP (BEGEGNUNGSDECK)</w:t></w:r>
    </w:p>
    <w:p><w:r><w:t>Dieses Gewölbe wird dynamisch durch das gemischte </w:t></w:r><w:r><w:rPr><w:b/></w:rPr><w:t>Begegnungsdeck (16 Karten)</w:t></w:r><w:r><w:t> bespielt!</w:t></w:r></w:p>
    <w:p><w:r><w:rPr><w:b/><w:color w:val="8C2D19"/></w:rPr><w:t>• Beim Betreten: </w:t></w:r><w:r><w:t>Deckt die oberste Karte des Begegnungsdecks auf.</w:t></w:r></w:p>
    <w:p><w:r><w:rPr><w:b/><w:color w:val="8C2D19"/></w:rPr><w:t>• [V] Vordere Zone: </w:t></w:r><w:r><w:t>Monster mit [V] auf die markierten Felder (z. B. A4, F4) stellen.</w:t></w:r></w:p>
    <w:p><w:r><w:rPr><w:b/><w:color w:val="8C2D19"/></w:rPr><w:t>• [H] Hintere Zone: </w:t></w:r><w:r><w:t>Fernkämpfer / Lauernde Monster mit [H] auf die hinteren Zonen (B5, E5) platzieren.</w:t></w:r></w:p>
    <w:p><w:r><w:rPr><w:b/><w:color w:val="8C2D19"/></w:rPr><w:t>• Sonderregeln der Karte: </w:t></w:r><w:r><w:t>Prüft, ob die Karte einen »Hinterhalt!« auslöst (Monster agieren vor den Helden!).</w:t></w:r></w:p>
    <w:p><w:r><w:rPr><w:i/><w:sz w:val="16"/><w:color w:val="555555"/></w:rPr><w:t>(Tutorial-Empfehlung für den ersten Durchlauf: Karte B01 „Banden-Vorposten“ oder B05 „Ruhelose Wache“)</w:t></w:r></w:p>

    <w:p>
      <w:pPr><w:spacing w:before="100" w:after="40"/></w:pPr>
      <w:r><w:rPr><w:b/><w:sz w:val="21"/><w:color w:val="5C1D11"/></w:rPr><w:t>2. INTERAKTIVES GELÄNDE AUF DEM PLAN</w:t></w:r>
    </w:p>
    <w:p><w:r><w:rPr><w:b/></w:rPr><w:t>• 2x Steinsäulen (B3, E3): </w:t></w:r><w:r><w:t>Blockieren Bewegung &amp; Sichtlinie. Bieten volle Deckung vor Pfeilen.</w:t></w:r></w:p>
    <w:p><w:r><w:rPr><w:b/></w:rPr><w:t>• Schatztruhe (E4): </w:t></w:r><w:r><w:t>Knacken mit LIS (SG 5) oder Brechstange: Ziehe 1 Ausrüstungskarte!</w:t></w:r></w:p>
    <w:p><w:r><w:rPr><w:b/></w:rPr><w:t>• Tor T1 (C6/D6): </w:t></w:r><w:r><w:t>Zufälliges Tür-Token liegt verdeckt. KRA (SG 6), LIS (SG 5) oder Schlüssel nötig. Führt zur Boss-Grabkammer!</w:t></w:r></w:p>

    <w:p>
      <w:pPr><w:spacing w:before="100" w:after="40"/></w:pPr>
      <w:r><w:rPr><w:b/><w:sz w:val="21"/><w:color w:val="5C1D11"/></w:rPr><w:t>3. STARTPOSITIONEN DER HELDEN</w:t></w:r>
    </w:p>
    <w:p><w:r><w:t>Die Helden starten am Südrand: S1 (Berserker), S2 (Kriegstänzerin), S3 (Halsabschneider), S4 (Magierin).</w:t></w:r></w:p>

    {p_break}

    <!-- ========================================== -->
    <!-- SEITE 2: RECHTS (KAMPFPLAN 1 MIT TEXTUR)   -->
    <!-- ========================================== -->
    <w:p>
      <w:pPr><w:spacing w:before="0" w:after="60"/><w:jc w:val="center"/></w:pPr>
      <w:r><w:rPr><w:b/><w:sz w:val="21"/><w:color w:val="5C1D11"/></w:rPr><w:t>KAMPFPLAN 1: VORKAMMERN (6x6 FELDER, 30 mm RASTER)</w:t></w:r>
    </w:p>
    {make_svg_drawing("rId2", "Kampfplan 1 Krypta")}

    {p_break}

    <!-- ========================================== -->
    <!-- SEITE 3: TEXT DOPPELSEITE 2 (BOSS)         -->
    <!-- ========================================== -->
    <w:p>
      <w:pPr><w:spacing w:before="0" w:after="40"/></w:pPr>
      <w:r><w:rPr><w:b/><w:sz w:val="17"/><w:color w:val="8C2D19"/></w:rPr><w:t>SZENARIO 01 • TEIL 2: DAS TOTENREICH DES FÜRSTEN</w:t></w:r>
    </w:p>
    <w:p>
      <w:pPr><w:spacing w:before="0" w:after="120"/></w:pPr>
      <w:r><w:rPr><w:b/><w:sz w:val="32"/><w:color w:val="3D2D1D"/></w:rPr><w:t>Die Grabkammer des Gruftwächters</w:t></w:r>
    </w:p>
    <w:p>
      <w:pPr><w:spacing w:before="0" w:after="120"/><w:ind w:left="120" w:right="120"/></w:pPr>
      <w:r><w:rPr><w:i/><w:sz w:val="17"/><w:color w:val="3D3124"/></w:rPr><w:t>„Das Steintor weicht krachend zurück. Vor euch erhebt sich ein gewaltiger Prunksarkophag. Kalter Grabeshauch erfüllt den Raum, als die uralte Prunkrüstung des Kriegsfürsten knarrend zum Leben erwacht...“</w:t></w:r>
    </w:p>

    <w:p>
      <w:pPr><w:spacing w:before="100" w:after="40"/></w:pPr>
      <w:r><w:rPr><w:b/><w:sz w:val="21"/><w:color w:val="5C1D11"/></w:rPr><w:t>1. DER GRUFTWÄCHTER (BOSS — 1x2 FELDER)</w:t></w:r>
    </w:p>
    <w:p><w:r><w:rPr><w:b/><w:color w:val="8C2D19"/></w:rPr><w:t>👑 Grabunhold / Gruftwächter [Pos. C5–D5]:</w:t></w:r></w:p>
    <w:p><w:r><w:rPr><w:b/></w:rPr><w:t>LP: 14 | VT: 7 | RÜSTUNG: 1 | BEWEGUNG: 3 | INI: 3</w:t></w:r></w:p>
    <w:p><w:r><w:t>• </w:t></w:r><w:r><w:rPr><w:b/></w:rPr><w:t>Streitkolben: </w:t></w:r><w:r><w:t>Nahkampf, 3 Schaden.</w:t></w:r></w:p>
    <w:p><w:r><w:t>• </w:t></w:r><w:r><w:rPr><w:b/></w:rPr><w:t>Boss-Fähigkeit (Gruftbeben — unter 7 LP): </w:t></w:r><w:r><w:t>Schlägt auf den Steinboden. Alle Helden müssen GES (SG 6) bestehen oder werden Verlangsamt (kostet 2 BP zum Aufstehen). Ruft 1 Skelettkrieger als Verstärkung!</w:t></w:r></w:p>

    <w:p>
      <w:pPr><w:spacing w:before="100" w:after="40"/></w:pPr>
      <w:r><w:rPr><w:b/><w:sz w:val="21"/><w:color w:val="5C1D11"/></w:rPr><w:t>2. LEIBWACHE &amp; GEFAHREN</w:t></w:r>
    </w:p>
    <w:p><w:r><w:rPr><w:b/><w:color w:val="8C2D19"/></w:rPr><w:t>• 2x Skelett-Leibwache [B5, E5]: </w:t></w:r><w:r><w:t>LP 4 | VT 6 | BEW 3 | INI 2. Flankieren den Sarkophag.</w:t></w:r></w:p>
    <w:p><w:r><w:rPr><w:b/><w:color w:val="8C2D19"/></w:rPr><w:t>• Verborgene Stachelgrube (C3): </w:t></w:r><w:r><w:t>Betritt ein Held das Feld, erleidet er 2 Direktschaden und stoppt die Bewegung.</w:t></w:r></w:p>

    <w:p>
      <w:pPr><w:spacing w:before="100" w:after="40"/></w:pPr>
      <w:r><w:rPr><w:b/><w:sz w:val="21"/><w:color w:val="5C1D11"/></w:rPr><w:t>3. BEUTE &amp; KAMPAGNEN-FORTSCHRITT</w:t></w:r>
    </w:p>
    <w:p><w:r><w:t>• </w:t></w:r><w:r><w:rPr><w:b/></w:rPr><w:t>Prunksarkophag (C6/D6): </w:t></w:r><w:r><w:t>2x Ausrüstungskarten + 40 Goldmünzen.</w:t></w:r></w:p>
    <w:p><w:r><w:t>• </w:t></w:r><w:r><w:rPr><w:b/></w:rPr><w:t>Quest-Relikt: </w:t></w:r><w:r><w:t>Siegelring des alten Kaiserreichs (Startgegenstand für Szenario 02).</w:t></w:r></w:p>
    <w:p><w:r><w:t>• </w:t></w:r><w:r><w:rPr><w:b/></w:rPr><w:t>Erfahrung: </w:t></w:r><w:r><w:t>Jeder überlebende Held erhält 1 EP.</w:t></w:r></w:p>

    {p_break}

    <!-- ========================================== -->
    <!-- SEITE 4: RECHTS (BOSS-ARENA MIT TEXTUR)    -->
    <!-- ========================================== -->
    <w:p>
      <w:pPr><w:spacing w:before="0" w:after="60"/><w:jc w:val="center"/></w:pPr>
      <w:r><w:rPr><w:b/><w:sz w:val="21"/><w:color w:val="5C1D11"/></w:rPr><w:t>KAMPFPLAN 2: BOSS-ARENA &amp; SARKOPHAG (6x6 FELDER, 30 mm RASTER)</w:t></w:r>
    </w:p>
    {make_svg_drawing("rId3", "Kampfplan 2 Boss Arena")}

    <!-- SEKTIONS-EIGENSCHAFTEN (A4 Portrait, 15 mm Rand) -->
    <w:sectPr>
      <w:pgSz w:w="11906" w:h="16838"/>
      <w:pgMar w:top="850" w:right="850" w:bottom="850" w:left="850"/>
    </w:sectPr>
  </w:body>
</w:document>"""

    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as docx:
        docx.writestr('[Content_Types].xml', content_types)
        docx.writestr('_rels/.rels', rels)
        docx.writestr('word/_rels/document.xml.rels', doc_rels)
        docx.writestr('word/styles.xml', styles)
        docx.writestr('word/media/map1.svg', svg1_data)
        docx.writestr('word/media/map2.svg', svg2_data)
        docx.writestr('word/document.xml', document_xml)

if __name__ == '__main__':
    out_docx = r'c:\Users\christoph.willimzik\Agent_Bunny\RV_Quest\printables\gamebook_scenario_01.docx'
    svg1 = r'c:\Users\christoph.willimzik\Agent_Bunny\RV_Quest\printables\gamebook_map_room1_crypt.svg'
    svg2 = r'c:\Users\christoph.willimzik\Agent_Bunny\RV_Quest\printables\gamebook_map_boss_crypt.svg'
    create_rich_gamebook_docx(out_docx, svg1, svg2)
    print("Successfully generated rich DOCX with embedded vector floor textures!")

