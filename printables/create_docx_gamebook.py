import zipfile
import os

def create_gamebook_docx(output_path):
    # Dimensions: 
    # A4 Portrait: 11906 x 16838 dxa (210 x 297 mm)
    # Margins: 15 mm = 850 dxa
    # 6x6 table: 180 mm total = 10206 dxa. Each column: 1701 dxa (30 mm)
    # Row height: 1701 dxa (30 mm)

    content_types = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
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
</Relationships>"""

    styles = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:docDefaults>
    <w:rPrDefault>
      <w:rPr>
        <w:rFonts w:ascii="Georgia" w:hAnsi="Georgia" w:cs="Georgia"/>
        <w:sz w:val="18"/>
        <w:szCs w:val="18"/>
        <w:color w:val="1A1A1A"/>
      </w:rPr>
    </w:rPrDefault>
  </w:docDefaults>
</w:styles>"""

    def make_cell(text, coord="", bg=None, bold=False, color="1A1A1A", font_size=16):
        shd = f'<w:shd w:val="clear" w:color="auto" w:fill="{bg}"/>' if bg else '<w:shd w:val="clear" w:color="auto" w:fill="DFD3BD"/>'
        bold_tag = '<w:b/>' if bold else ''
        coord_p = f"""<w:p>
          <w:pPr><w:spacing w:before="20" w:after="0"/><w:jc w:val="left"/></w:pPr>
          <w:r><w:rPr><w:sz w:val="12"/><w:color w:val="7A6A53"/><w:rFonts w:ascii="Arial" w:hAnsi="Arial"/></w:rPr><w:t>{coord}</w:t></w:r>
        </w:p>""" if coord else ""
        
        main_p = f"""<w:p>
          <w:pPr><w:spacing w:before="60" w:after="40"/><w:jc w:val="center"/></w:pPr>
          <w:r><w:rPr>{bold_tag}<w:sz w:val="{font_size}"/><w:color w:val="{color}"/><w:rFonts w:ascii="Georgia" w:hAnsi="Georgia"/></w:rPr><w:t>{text}</w:t></w:r>
        </w:p>"""

        return f"""<w:tc>
          <w:tcPr>
            <w:tcW w:w="1701" w:type="dxa"/>
            {shd}
            <w:tcMar><w:top w:w="40" w:type="dxa"/><w:bottom w:w="40" w:type="dxa"/><w:left w:w="40" w:type="dxa"/><w:right w:w="40" w:type="dxa"/></w:tcMar>
            <w:vAlign w:val="center"/>
          </w:tcPr>
          {coord_p}
          {main_p}
        </w:tc>"""

    def make_table(grid_def):
        rows_xml = []
        for r_idx, row in enumerate(grid_def):
            cells_xml = []
            for c_idx, cell in enumerate(row):
                coord = f"{chr(65+c_idx)}{6-r_idx}"
                cells_xml.append(make_cell(cell.get('text', ''), coord, cell.get('bg'), cell.get('bold', False), cell.get('color', '1A1A1A'), cell.get('size', 16)))
            
            tr_xml = f"""<w:tr>
              <w:trPr>
                <w:trHeight w:val="1701" w:hRule="exact"/>
                <w:cantSplit/>
              </w:trPr>
              {''.join(cells_xml)}
            </w:tr>"""
            rows_xml.append(tr_xml)

        return f"""<w:tbl>
          <w:tblPr>
            <w:tblW w:w="10206" w:type="dxa"/>
            <w:jc w:val="center"/>
            <w:tblBorders>
              <w:top w:val="single" w:sz="16" w:space="0" w:color="3D2D1D"/>
              <w:left w:val="single" w:sz="16" w:space="0" w:color="3D2D1D"/>
              <w:bottom w:val="single" w:sz="16" w:space="0" w:color="3D2D1D"/>
              <w:right w:val="single" w:sz="16" w:space="0" w:color="3D2D1D"/>
              <w:insideH w:val="single" w:sz="6" w:space="0" w:color="8A7660"/>
              <w:insideV w:val="single" w:sz="6" w:space="0" w:color="8A7660"/>
            </w:tblBorders>
          </w:tblPr>
          {''.join(rows_xml)}
        </w:tbl>"""

    # Grid 1 Definition
    grid_1 = [
        # Row 6
        [{}, {}, {'text': 'TOR T1', 'bg': 'D4A373', 'bold': True, 'color': '5C1D11'}, {'text': 'TOR T1', 'bg': 'D4A373', 'bold': True, 'color': '5C1D11'}, {}, {}],
        # Row 5
        [{}, {'text': 'SK1', 'bg': 'F2D6D3', 'bold': True, 'color': '8C2D19'}, {}, {}, {'text': 'SK2', 'bg': 'F2D6D3', 'bold': True, 'color': '8C2D19'}, {}],
        # Row 4
        [{'text': 'G1', 'bg': 'F2D6D3', 'bold': True, 'color': '8C2D19'}, {'text': 'HORN', 'bg': 'E8DFCC', 'bold': True}, {}, {}, {'text': 'TRUHE', 'bg': 'FAEDCD', 'bold': True, 'color': '875817'}, {'text': 'G2', 'bg': 'F2D6D3', 'bold': True, 'color': '8C2D19'}],
        # Row 3
        [{}, {'text': 'SÄULE', 'bg': '73695D', 'bold': True, 'color': 'FBF7EE'}, {}, {}, {'text': 'SÄULE', 'bg': '73695D', 'bold': True, 'color': 'FBF7EE'}, {}],
        # Row 2
        [{}, {}, {'text': 'Geröll', 'bg': 'C2B59B'}, {'text': 'Geröll', 'bg': 'C2B59B'}, {}, {}],
        # Row 1
        [{'text': 'S1', 'bg': 'D0E6DB', 'bold': True, 'color': '174231'}, {'text': 'S2', 'bg': 'D0E6DB', 'bold': True, 'color': '174231'}, {'text': 'S3', 'bg': 'D0E6DB', 'bold': True, 'color': '174231'}, {'text': 'S4', 'bg': 'D0E6DB', 'bold': True, 'color': '174231'}, {}, {}]
    ]

    # Grid 2 Definition (Boss)
    grid_2 = [
        # Row 6
        [{}, {}, {'text': 'SARKOPHAG', 'bg': '8D7B68', 'bold': True, 'color': 'FBF7EE'}, {'text': 'SARKOPHAG', 'bg': '8D7B68', 'bold': True, 'color': 'FBF7EE'}, {}, {}],
        # Row 5
        [{}, {'text': 'SK3', 'bg': 'F2D6D3', 'bold': True, 'color': '8C2D19'}, {'text': 'GRUFTWÄCHTER', 'bg': 'F5C8C2', 'bold': True, 'color': '5C1D11'}, {'text': 'BOSS (1x2)', 'bg': 'F5C8C2', 'bold': True, 'color': '5C1D11'}, {'text': 'SK4', 'bg': 'F2D6D3', 'bold': True, 'color': '8C2D19'}, {}],
        # Row 4
        [{}, {}, {}, {}, {}, {}],
        # Row 3
        [{'text': 'SÄULE', 'bg': '73695D', 'bold': True, 'color': 'FBF7EE'}, {}, {'text': 'GRUBE', 'bg': 'D9534F', 'bold': True, 'color': 'FFFFFF'}, {}, {}, {'text': 'SÄULE', 'bg': '73695D', 'bold': True, 'color': 'FBF7EE'}],
        # Row 2
        [{}, {}, {}, {}, {}, {}],
        # Row 1
        [{}, {}, {'text': 'Eingang', 'bg': 'D0E6DB', 'bold': True, 'color': '174231'}, {'text': 'Eingang', 'bg': 'D0E6DB', 'bold': True, 'color': '174231'}, {}, {}]
    ]

    p_break = '<w:p><w:r><w:br w:type="page"/></w:r></w:p>'

    document_xml = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:body>
    <!-- SEITE 1: TEXT TEIL 1 -->
    <w:p>
      <w:pPr><w:spacing w:before="0" w:after="60"/></w:pPr>
      <w:r><w:rPr><w:b/><w:sz w:val="18"/><w:color w:val="8C2D19"/></w:rPr><w:t>SZENARIO 01 • TEIL 1 VON 2 • EINFÜHRUNGS-QUEST</w:t></w:r>
    </w:p>
    <w:p>
      <w:pPr><w:spacing w:before="0" w:after="140"/></w:pPr>
      <w:r><w:rPr><w:b/><w:sz w:val="34"/><w:color w:val="3D2D1D"/></w:rPr><w:t>Die Krypta von Dun-Karr</w:t></w:r>
    </w:p>
    <w:p>
      <w:pPr><w:spacing w:before="0" w:after="140"/><w:ind w:left="140" w:right="140"/></w:pPr>
      <w:r><w:rPr><w:i/><w:sz w:val="17"/><w:color w:val="3D3124"/></w:rPr><w:t>„Klammer Grabesdunst schlägt euch entgegen. Das Flackern eurer Fackeln wirft tanzende Schatten an die feuchten Steinwände. Vor euch liegen die Vorkammern des verfluchten Kriegsfürsten...“</w:t></w:r>
    </w:p>
    
    <w:p>
      <w:pPr><w:spacing w:before="120" w:after="60"/></w:pPr>
      <w:r><w:rPr><w:b/><w:sz w:val="22"/><w:color w:val="5C1D11"/></w:rPr><w:t>1. MISSIONSZIEL &amp; ABLAUF</w:t></w:r>
    </w:p>
    <w:p>
      <w:pPr><w:spacing w:before="0" w:after="100"/></w:pPr>
      <w:r><w:t>Kämpft euch durch die Vorhut und öffnet das Tor bei C6/D6, um in die Grabkammer vorzustoßen.</w:t></w:r>
    </w:p>

    <w:p>
      <w:pPr><w:spacing w:before="120" w:after="60"/></w:pPr>
      <w:r><w:rPr><w:b/><w:sz w:val="22"/><w:color w:val="5C1D11"/></w:rPr><w:t>2. WÄCHTER DER VORHALLE</w:t></w:r>
    </w:p>
    <w:p><w:r><w:rPr><w:b/><w:color w:val="8C2D19"/></w:rPr><w:t>Goblin-Späher (2x) [A4, F4]: </w:t></w:r><w:r><w:t>LP 3 | VT 5 | BEW 4 | INI 4. Nahkampf 1 Schaden. Feigheit: Weicht bei 1 LP 2 Felder zurück.</w:t></w:r></w:p>
    <w:p><w:r><w:rPr><w:b/><w:color w:val="8C2D19"/></w:rPr><w:t>Skelettkrieger (2x) [B5, E5]: </w:t></w:r><w:r><w:t>LP 4 | VT 6 | BEW 3 | INI 2. Nahkampf 2 Schaden. Hämmer/Keulen machen +1 Schaden.</w:t></w:r></w:p>

    <w:p>
      <w:pPr><w:spacing w:before="120" w:after="60"/></w:pPr>
      <w:r><w:rPr><w:b/><w:sz w:val="22"/><w:color w:val="5C1D11"/></w:rPr><w:t>3. INTERAKTIVE ELEMENTE</w:t></w:r>
    </w:p>
    <w:p><w:r><w:rPr><w:b/></w:rPr><w:t>• Alarmhorn (B4): </w:t></w:r><w:r><w:t>Stößt ein Goblin ins Horn, erwacht in Teil 2 ein weiteres Skelett!</w:t></w:r></w:p>
    <w:p><w:r><w:rPr><w:b/></w:rPr><w:t>• Truhe (E4): </w:t></w:r><w:r><w:t>LIS (SG 5): Ziehe 1 Karte vom Ausrüstungsdeck.</w:t></w:r></w:p>
    <w:p><w:r><w:rPr><w:b/></w:rPr><w:t>• Tor T1 (C6/D6): </w:t></w:r><w:r><w:t>KRA (SG 6) oder LIS (SG 5) zum Aufbrechen.</w:t></w:r></w:p>

    {p_break}

    <!-- SEITE 2: KARTE TEIL 1 -->
    <w:p>
      <w:pPr><w:spacing w:before="0" w:after="100"/><w:jc w:val="center"/></w:pPr>
      <w:r><w:rPr><w:b/><w:sz w:val="20"/><w:color w:val="5C1D11"/></w:rPr><w:t>KAMPFPLAN 1: VORKAMMERN VON DUN-KARR (6x6 FELDER, 30 mm RASTER)</w:t></w:r>
    </w:p>
    {make_table(grid_1)}

    {p_break}

    <!-- SEITE 3: TEXT TEIL 2 -->
    <w:p>
      <w:pPr><w:spacing w:before="0" w:after="60"/></w:pPr>
      <w:r><w:rPr><w:b/><w:sz w:val="18"/><w:color w:val="8C2D19"/></w:rPr><w:t>SZENARIO 01 • TEIL 2 VON 2 • BOSSKAMPF</w:t></w:r>
    </w:p>
    <w:p>
      <w:pPr><w:spacing w:before="0" w:after="140"/></w:pPr>
      <w:r><w:rPr><w:b/><w:sz w:val="34"/><w:color w:val="3D2D1D"/></w:rPr><w:t>Die Grabkammer des Gruftwächters</w:t></w:r>
    </w:p>
    <w:p>
      <w:pPr><w:spacing w:before="0" w:after="140"/><w:ind w:left="140" w:right="140"/></w:pPr>
      <w:r><w:rPr><w:i/><w:sz w:val="17"/><w:color w:val="3D3124"/></w:rPr><w:t>„Das Steintor weicht krachend zurück. Vor euch erhebt sich ein gewaltiger Sarkophag. Kalter Hauch erfüllt den Raum, als die uralte Rüstung des Kriegsfürsten knarrend zum Leben erwacht...“</w:t></w:r>
    </w:p>

    <w:p>
      <w:pPr><w:spacing w:before="120" w:after="60"/></w:pPr>
      <w:r><w:rPr><w:b/><w:sz w:val="22"/><w:color w:val="5C1D11"/></w:rPr><w:t>1. DER GRUFTWÄCHTER (BOSS)</w:t></w:r>
    </w:p>
    <w:p><w:r><w:rPr><w:b/><w:color w:val="8C2D19"/></w:rPr><w:t>Grabunhold / Gruftwächter [C5-D5, 1x2]: </w:t></w:r><w:r><w:t>LP 14 | VT 7 | RÜSTUNG 1 | BEW 3 | INI 3.</w:t></w:r></w:p>
    <w:p><w:r><w:t>Angriff: Streitkolben (Nahkampf, 3 Schaden).</w:t></w:r></w:p>
    <w:p><w:r><w:rPr><w:b/></w:rPr><w:t>Gruftbeben (unter 7 LP): </w:t></w:r><w:r><w:t>Alle Helden GES (SG 6) oder Verlangsamt (2 BP zum Aufstehen). Ruft 1 Skelett-Verstärkung!</w:t></w:r></w:p>

    <w:p>
      <w:pPr><w:spacing w:before="120" w:after="60"/></w:pPr>
      <w:r><w:rPr><w:b/><w:sz w:val="22"/><w:color w:val="5C1D11"/></w:rPr><w:t>2. BEUTE &amp; BELOHNUNG</w:t></w:r>
    </w:p>
    <w:p><w:r><w:t>• 2x Ausrüstungskarten vom Stapel.</w:t></w:r></w:p>
    <w:p><w:r><w:t>• 40 Goldmünzen &amp; Quest-Relikt: Siegelring des alten Kaiserreichs.</w:t></w:r></w:p>
    <w:p><w:r><w:t>• 1 Erfahrungspunkt (EP) für jeden überlebenden Helden.</w:t></w:r></w:p>

    {p_break}

    <!-- SEITE 4: KARTE TEIL 2 -->
    <w:p>
      <w:pPr><w:spacing w:before="0" w:after="100"/><w:jc w:val="center"/></w:pPr>
      <w:r><w:rPr><w:b/><w:sz w:val="20"/><w:color w:val="5C1D11"/></w:rPr><w:t>KAMPFPLAN 2: BOSS-ARENA &amp; SARKOPHAG (6x6 FELDER, 30 mm RASTER)</w:t></w:r>
    </w:p>
    {make_table(grid_2)}

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
        docx.writestr('word/document.xml', document_xml)

if __name__ == '__main__':
    out_file = r'c:\Users\christoph.willimzik\Agent_Bunny\RV_Quest\printables\gamebook_scenario_01.docx'
    create_gamebook_docx(out_file)
    print("Successfully created DOCX:", out_file)

