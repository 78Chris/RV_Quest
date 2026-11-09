# Leitfaden zur Bildgenerierung & Stil-Prompts (Art Style Guide)

> **Zweck:** Einheitliche visuelle Ästhetik für alle Tarot-Karten, Rückseiten und Holz-Standees für *Von Helden und Monstern — Abenteuer in der Alten Welt*.  
> **Werkzeug:** Kostenlose Bildgenerierungs-Tokens (z. B. Stable Diffusion, Midjourney, DALL-E, Ideogram, Flux).

---

## 🎨 1. Visuelle Stil-DNA & Zwei-Stufen-Workflow (Two-Tier Pipeline)

Für *Von Helden und Monstern* nutzen wir eine klare **Zwei-Stufen-Strategie (Two-Tier)**:
1. **Druck-Karten (Tarot 70 × 120 mm):** **Hohe Detailtiefe & Handkolorierter Holzschnitt** (Aquarell/Tusche auf Pergament). Volle Ausnutzung der hohen Druckauflösung (300+ DPI).
2. **Holz-Standees (30 × 40 mm Lasergravur):** **Reduzierte, linienbasierte Holzschnitt-Grafik** mit Fokus auf klaren Konturen und moderatem Schraffur-Abstand (wie bei `goblin_scout_woodcut.jpg` und `wasteland_worg_woodcut.jpg`). Verhindert das Zuschmieren/Verbrennen bei zu feinen Liniendichten (wie beim ursprünglichen `skeleton_warrior_woodcut_cropped.jpg`).

### Linienführung & Detaillierungsgrad nach Medium:
- **Für Lasergravur (Standees):** 
  - Moderate Linienstärke mit fühlbarem Abstand zwischen den Linien.
  - Keine winzigen Mikroschraffuren; saubere offene Weißflächen zwischen Konturen.
  - **Fokus & Bildfüllung:** Die Figur füllt den 3:4-Ausschnitt dominant und formatfüllend aus (~85% Bildhöhe), mit minimalen Randabständen (Tight Framing).
  - **Absolut reiner, solider weißer Hintergrund (#FFFFFF):** Null Pergamenttextur, null Rauschen, null Papierflecken oder Grauschattierungen im Hintergrund! Der Laser interpretiert jegliche Pergament- oder Graustufen als dunkle Brandpunkte auf dem Birkensperrholz. Standees müssen knallhartes Schwarz auf 100% reinem Weiß sein.
  - Referenz-Benchmarks: `goblin_scout_woodcut.jpg` & `wasteland_worg_woodcut.jpg`.
- **Für Kartendruck (Tarot):**
  - Feine, detailreiche Ätzung / Kupferstich-Linien.
  - Koloriert im Stil historischer handkolorierter Holzschnitte (Holzschnittkonturen mit transparenten Aquarell-Lavuren / Gouache auf Altpergament).
  - Ebenfalls formatfüllender Bildausschnitt mit minimalen Randzonen.
  - Referenz-Benchmark: `skeleton_warrior_woodcut_colored.jpg`.

---

## 📐 2. Bildformate & Seitenverhältnisse

| Verwendungszweck | Bildmaß (mm) | Seitenverhältnis (`--ar`) | Besonderheiten & Bildausschnitt |
|---|---|---|---|
| **Tarotkarten-Gesamtformat (Kanonisch)** | **70 × 120 mm** | **`7:12`** | Gesamte Karte (Seitenverhältnis für Vollbild-Hintergründe, Druckbögen und Kartenrückseiten). |
| **Tarotkarten-Artwork-Box (Gerahmtes Fenster)** | ca. 60 × 60 mm (obere 50% der Karte) | **`1:1`** | **Standard für alle Ausrüstungs-, Zauber- und Item-Illustrationen.** Passt perfekt in den quadratischen Zierrahmen der oberen Kartenhälfte. Erlaubt 45°-Diagonalen für Klingen und zentrierte Symmetrie für Rüstungen/Tränke. |
| **Tarotkarten-Vollbild / Rückseiten** | 70 × 120 mm | **`7:12`** | Kartendeck-Rückseite mit ornamentaler Holzschnitt-Bordüre und zentralem Siegel. |
| **Standard-Standee (1×1 Feld)** | 30 × 40 mm | `3:4` | **Formatfüllende Ganzkörper-Pose (Tight Framing):** Figur füllt ca. 85–90% der Bildhöhe aus. Minimale Ränder oben und seitlich (< 5–10% Randabstand), weißer/heller Hintergrund für Laserkontur. Keine riesigen Leerräume ringsum! |
| **Horizontale / Niedrige Monster (z. B. Worg, Spinne)** | 30 × 40 mm | `3:4` | **Frontalansicht / Vorderkörper-Fokus:** Formatfüllender Angriffs-Porträt-Close-Up („frontal view, charging forward“), füllt die gesamte Breite und Höhe des 3:4-Rahmens mit minimalem Rand. |
| **Großes Monster (1×2 oder 2×2)** | 60 × 80 mm | `3:4` | Gleiches Seitenverhältnis (3:4), wuchtige, raumfüllende Silhouette mit minimalem Randabstand. |
| **Fliegend / Schwebend (1×1 Feld)** | 30 × 80 mm | `3:8` oder `1:2` | Obere Hälfte: Kreatur/Geist (formatfüllend in der Breite); Untere Hälfte: Wolken/Wirbel/Flug-Abstand. |

---

## 📝 3. Generische Prompt-Schablonen

### A. Monster-Standees (Gravurfähig für Holz — Formatfüllend & Tight Framing)

> **Das Referenz-Archetyp-Gesetz (Tight Framing & Maximaler Bildfokus):**  
> Alle Standee-Grafiken für Monster und Helden müssen das Bildfeld **optimal und raumfüllend ausnutzen** (ohne unnötig große weiße/leere Ränder ringsum):
> 
> 1. **Knappe Ränder / Formatfüllende Pose (Tight Framing, ca. 85–90% Canvas-Füllung):**
>    - Das Monster / der Held steht **groß und dominant im Bild** und füllt mindestens 85% der vertikalen Bildhöhe aus.
>    - **Keine riesigen Freiräume oder breiten Leerränder:** Oben und zu den Seiten nur ein minimaler Randpuffer (ca. 5–10%), damit die Silhouette auf dem 30 × 40 mm Standee sofort ins Auge springt und nicht winzig wirkt.
> 2. **Absolut reiner, solider weißer Hintergrund (#FFFFFF — KEIN Pergament, KEINE Textur):**
>    - 100% reinweißer Hintergrund (#FFFFFF) ohne jegliche Textur.
>    - **Streng verboten:** Absolut kein Pergament, kein Pergamentpapier, keine Papierstruktur, keine Falten, Flecken, Graustufen oder Schattierungen im Hintergrund. Der Laser brennt jeden Grau- oder Pergamentton als dunkle Brandfläche in das Holz!
>    - Keine gemalten Himmels-Schraffuren, keine Wolken, keine Wände, Torbögen, Ruinen oder Decken im Hintergrund.
> 3. **Rudimentärer Boden (Nur knapp unter den Füßen):**
>    - Lediglich eine winzige, skizzenhafte Standfläche direkt an den Füßen am unteren Bildrand, die nicht breit nach außen ausfranst.
> 4. **Figur & Linienstärke:**
>    - Markante, dicke Holzschnitt-Konturen (Linocut / Woodblock).
>    - Moderate Schraffur ausschließlich auf dem Körper/Kleidung der Figur, um Plastizität zu erzeugen.
>    - Klare, lesbare Piktogramm-Wirkung aus Distanz.

> **Prompt-Schablone (Standees — Reines Weiß ohne Pergament & Formatfüllend):**  
> `authentic medieval woodblock print of a [MONSTER_NAME], in the exact rustic style of early woodcuts, tight framing, subject filling 85% of frame, minimal margins, large centered figure, bold thick black carved ink outlines, moderate hatching on body, isolated on pure solid white background, 100% clean white background, zero texture, zero parchment, pure white negative space, small sketchy patch of dirt directly under feet touching bottom edge, no wide margins, no empty borders, no walls, no arches, no sky hatching, no background scenery, high contrast monochrome pure black on pure white, no solid black blobs, no text --ar 3:4`

---

### B. Tarotkarten-Farbillustrationen (Handkolorierter Holzschnitt — Hohe Detailtiefe)

> **Basis-Prompt (Druck-Qualität mit feinen Details, Farbe & knappen Rändern):**  
> `hand-colored medieval woodcut etching of a [CHARACTER/MONSTER/ITEM], dark fantasy, tight framing, subject filling frame, minimal outer margins, highly detailed fine linework, antique hand-tinted watercolor washes, muted earth tones on aged parchment texture, deep charcoal ink contours, antique sepia, aged crimson, forest moss green, intricate gothic styling, dramatic lighting --ar 7:12`

**Beispiel Skelettkrieger (Farbig für Tarot-Karte):**
> `hand-colored medieval woodcut etching of an ancient armored skeleton warrior rising from a stone tomb, dark fantasy, tight framing filling canvas, minimal margins, highly detailed fine linework, antique hand-tinted watercolor washes, muted earth tones on aged parchment texture, weathered bronze armor, glowing hollow eye sockets, aged sepia, bone white, dried blood accents, ornate gothic style --ar 7:12`

---

### C. Niedrige / Horizontale Monster (z. B. Worg, Spinne – Frontalansicht)

> **Basis-Prompt:**  
> `medieval woodcut engraving of a snarling [MONSTER_NAME], dramatic frontal view charging directly towards the viewer, tight close-up framing filling entire canvas width and height, minimal margins, upper body and head focus, menacing posture, dark fantasy, intricate high detail linework, fine cross-hatching, balanced contrast, albrecht dürer style, clean white background, monochrome, no solid black fills, no wide borders --ar 3:4`

**Beispiel Ödland-Worg (Frontal):**
> `medieval woodcut engraving of a monstrous dire wasteland worg, dramatic frontal three-quarter view lunging forward, tight framing filling frame, minimal margins, snarling jaws with long fangs, textured thick fur, glowing feral eyes, dark fantasy, intricate high detail linework, fine cross-hatching, balanced contrast with clean white space, albrecht dürer style, isolated on pure white background, monochrome, no wide borders --ar 3:4`

---

### C. Fliegende / Schwebende Monster (Mit Schwebe-Effekt)

> **Basis-Prompt:**  
> `medieval woodcut engraving of a flying [CREATURE], airborne, hovering high in the air, tight framing, filling frame vertically with minimal side margins, swirling spectral mist and dark wind underneath the creature, leaving the lower half elevated, dark fantasy, heavy linework, detailed cross-hatching, full body, isolated on pure white background, high contrast, monochrome, no wide borders --ar 1:2`

---

### C. Tarotkarten-Illustrationen (Gegenstände, Waffen, Zauber)

> **Basis-Prompt (Artwork-Box im 1:1 Quadratrahmen):**  
> `vintage medieval woodcut etching of a [ITEM / SPELL], dark fantasy illustration, tight framing, subject filling frame, minimal margins, muted earth tones on aged parchment texture, deep charcoal ink outlines, warm sepia, deep crimson accents, occult and antique aesthetic, centered, clean borders, high detail --ar 1:1`

**Beispiel Barbarenaxt:**
> `vintage medieval woodcut etching of a massive double-bitted northern battle axe, notched iron blade with carved runes, leather wrapped grip, bone charms dangling, dark fantasy illustration, tight framing filling canvas, minimal margins, muted earth tones on aged parchment texture, deep charcoal ink outlines, warm sepia, dark crimson accents, centered, clean vignette --ar 1:1`

---

### D. Tarotkarten-Rückseite (Einheitliche Kartenrücken)

> **Deck-Rückseite Prompt:**  
> `symmetrical medieval tarot card back design, ornate gothic arch border, dark fantasy occult woodcut, ancient sundial and crossed d6 dice emblem in center, intricate knotwork, alchemical symbols, printed on aged parchment, monochrome black ink with subtle antique gold tint, highly detailed, perfect symmetry --ar 7:12`

---

## 🪵 4. Lasergravur-Optimierung für Standees

- **Absoluter Reinweiß-Hintergrund (#FFFFFF — Kein Pergament):** Monster für Standees müssen zwingend auf reinweißem Grund (#FFFFFF) ohne jegliche Pergament-, Papier- oder Schmutztextur stehen. LightBurn und Laser-Rastergravuren brennen jegliche Graustufe oder Pergamentmaserung unweigerlich als dunkle Brandpunkte/Schmauch ins Holz. Ein 100% reinweißer Hintergrund ermöglicht zudem der Lasersoftware das saubere automatische Generieren der Außen-Schnittlinie (Offset 1,5 mm).
- **Dithering / Jarvis:** Für die Gravur auf Birkensperrholz liefert *Jarvis* oder *Stucki* Dithering mit 300 DPI die saubersten Schattierungen bei Holzschnitt-Grafiken.
- **Nummerierung der Basen:** Basen werden beidseitig gelasert mit z. B. Ziffern `1`, `2`, `3` in einer rustikalen Serifenschrift (z. B. *Cinzel* oder *IM Fell DW Pica*), 180° gespiegelt oder zentriert auf beiden Seiten des Steckschlitzes.

---

## 🔗 5. Gespeicherte Midjourney Style References (`--sref`)

> **Verwendung:** Füge den gewünschten Link ans Ende deines Prompts mit `--sref <URL> --sw 100-200` an.  
> *Hinweis:* Midjourney-CDN-Links können nach einigen Wochen ablaufen. Lade deine finalen Favoriten zusätzlich auf Imgur hoch oder speichere sie lokal in `printables/art_assets/MasterArtwork/`.

| Motiv / Benchmark | Midjourney CDN URL (`--sref`) | Empfohlenes `--sw` | Verwendung & Stil-Charakter |
|---|---|---|---|
| **Kartenrücken Master Style Reference (Der Schattenbazar)** | `https://i.imgur.com/YYHCCVL.png` | `150` | Verbindliche Style-Reference für alle Kartenrücken (Bestiarium Imperialis, Rad des Schicksals, Codex Arcanum, Die Tiefen Gewölbe). |
| **Goblin Woodcut (Aktueller Favorit — Imgur Permanent)** | `https://i.imgur.com/7GHh0Ju.png` | `150–200` | Permanente Imgur-URL. Reduzierte Linienführung, große offene Weißflächen, ideal für Lasergravur ohne Rußbildung. Master-Referenz für alle 12 Monster. |
| **Ausrüstungskarten Master Style Reference (3 Bildquellen)** | `https://i.imgur.com/VzU1WIk.png https://i.imgur.com/m6GMSd5.png https://i.imgur.com/juHvFJo.png` | `200` | Verbindliche Style-References für alle 54 Ausrüstungskarten (Nahkampf, Fernkampf, Rüstungen, Verbrauchsgegenstände, Zubehör). |
| Goblin Woodcut (Midjourney CDN Backup) | `https://cdn.midjourney.com/9f1b9564-cf67-4c9f-9837-8be863d93c9a/0_3.png` | `150–200` | CDN-Original. |
| Goblin Scout (Alternative B&W 1) | `https://cdn.midjourney.com/635d2a1e-6416-469b-a1e8-79fcee4fdb32/0_2.png` | `150–200` | Kräftige Konturen, leicht dichtere Schraffur. |
| Goblin Scout (Alternative B&W 2) | `https://cdn.midjourney.com/979f7c9e-64ef-4ef9-a314-7beab625ee4c/0_2.png` | `150–200` | Klassischer Holzschnitt-Charakter. |
| Goblin Scout (Alternative B&W 3) | `https://cdn.midjourney.com/e286007c-3e72-4362-94dd-30cdc3c9437c/0_0.png` | `100–150` | Frühere Generation. |

---

## ⏳ 6. Token-Budget & Zeitplan bis Weihnachten (7 Wochen)

Mit typischen kostenlosen KI-Tiers (z. B. 15–20 freie Generationen pro Tag oder ca. 50–100 Fast-Credits pro Woche) ist das Projekt bis Weihnachten **sehr entspannt machbar**:

### Benötigte Kern-Artworks:
| Kategorie | Standee (Laser, Monochrom) | Tarot-Karte (Farbig, Detailliert) | Status / Aufwand |
|---|---|---|---|
| **4 Helden** | 4 Standees (30 × 40 mm) | 4 Charakter-Porträts (groß für A5-Querformat Dashboard) | 8 Bilder (nach Fotovorlagen) |
| **12 Monster** | 12 Standees (30 × 40 mm / 60 × 80 mm) | 12 Monster-Porträts für Begegnungskarten | 24 Bilder (Skelett, Goblin, Worg bereits teilfertig!) |
| **Kartenrückseiten** | — | 3 Rückseiten-Motive (Ausrüstung, Ereignis, Begegnung) | 3 Bilder |
| **Ausrüstungs-Archetypen** | — | 10–12 wiederverwendbare Vignetten (Schwert, Axt, Rüstung, Trank etc.) | 10–12 Bilder |
| **Summe:** | **16 Standees** | **~31 Farbillustrationen** | **~47 finale Bilder total** |

### Monster-Gesamtübersicht (12 Kampagnen-Gegner):
1. **Goblin-Späher** *(Standard 30×40 mm)* — *bereits vorhanden!*
2. **Goblin-Bogenschütze** *(Standard 30×40 mm)*
3. **Skelettkrieger** *(Standard 30×40 mm)* — *bereits vorhanden!*
4. **Skelett-Scharfschütze** *(Standard 30×40 mm)*
5. **Riesenspinne** *(Standard 30×40 mm, Frontalansicht)*
6. **Ödland-Worg** *(Standard 30×40 mm, Frontalansicht)* — *bereits vorhanden!*
7. **Moor-Ghul** *(Standard 30×40 mm)*
8. **Kultist des Schattens** *(Standard 30×40 mm)*
9. **Todesritter / Hügelfürst** *(Elite 30×40 mm)*
10. **Grabunhold / Gruftwächter** *(Mini-Boss 60×80 mm)*
11. **Blutgolem** *(Groß 60×80 mm)*
12. **Lich-König Malakor** *(Kampagnen-Endgegner 60×80 mm oder 30×80 mm Schwebend)*

### Empfohlener Zwei-Stufen-Workflow pro Motiv:
1. **Option A (Prompt-Paar):** 
   - Einmal generieren mit dem Standee-Prompt (`tight framing, subject filling 85% of frame, minimal margins, bold clean black outlines, woodblock print, plain light background`).
   - Einmal generieren mit dem Farb-Tarot-Prompt (`tight framing, minimal margins, hand-colored medieval woodcut etching, antique watercolor washes`).
2. **Option B (Token-sparend — Bild-zu-Bild / Inpainting):**
   - Zuerst das detaillierte Farb-Artwork für die Tarot-Karte generieren.
   - Mit Python / ImageMagick oder Inpainting automatisch Konturen extrahieren bzw. vereinfachen (`build_simplified_standee.py`), um die Lasergravur-Vorlage ohne zusätzlichen Tokenverbrauch abzuleiten.
3. **Puffer:** Bei ~5 finalen Bildern pro Woche (ca. 10–15 Prompts mit Auswählen/Nachjustieren) ist der gesamte Kunst-Bestand **bereits Ende November / Anfang Dezember komplett fertig**, sodass der gesamte Dezember für den Holzlaserschnitt, das Lackieren und das Drucken bleibt.

