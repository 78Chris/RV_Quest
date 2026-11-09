# Richtlinien & Spezifikation: Game Book Druckvorlagen (A4 Duplex & Großdruck)

> **Status:** Aktiv & Verbindlich ab 05. November 2026  
> **Format:** A4-Bögen im Browser-Druck (HTML/CSS) -> Duplex -> Schnitt auf 210 × 210 mm Quadrat-Buch  
> **Bindung:** Wire-O Spiralbindung (Doppel-Drahtkamm)

---

## 1. Kern-Design-Regeln für das Game Book

### 🖨️ Druck- & Duplex-Pipeline (Browser-to-Print via Edge/Chrome)
- **Format:** `@page { size: 210mm 297mm; margin: 0; }` (Standard A4 Hochformat).
- **Duplex-Druck:** Immer vorbereitet für **beidseitigen Druck („An langer Kante spiegeln“)**.
  - **Ungerade Seiten (1, 3, 5...):** Linke Buchseite (Szenario-Text, Regeln, Encounter-Setup, Beute).
  - **Gerade Seiten (2, 4, 6...):** Rechte Buchseite (Taktischer 6×6 Kampfplan à 30 mm = 180 × 180 mm).
- **Aufgeschlagen am Tisch:** Links immer die lesbaren Werte & Story, rechts immer die Arena.
- **Schnittkante bei 210 mm:** 
  - Die oberen 210 × 210 mm bilden die quadratische Buchseite.
  - Bei genau 210 mm verläuft eine feine gestrichelte Schnittlinie (`border-top: 1px dashed #7a6a53`).
  - Der untere Streifen (87 mm) dient als Schnittabfall bzw. Druckhinweis.

---

## 2. Großdruck-Spezifikation (Große Schrift für optimale Lesbarkeit)

Für entspanntes Lesen am Spieltisch ohne Lesebrille/Lupe:
- **Fließtext & Regeln:** Mindestens **11 pt bis 12 pt** (starker Kontrast, z. B. `#111111` auf dezentem Pergament `#fcfaf5`).
- **Überschriften (H1):** **20 pt bis 22 pt** fett, zentriert oder markant linksbündig.
- **Abschnittstitel (H2):** **14 pt bis 15 pt** in kräftigem Akzent-Ton (`#5c1d11` / `#8c2d19`).
- **Stat-Blöcke & Zahlen:** 
  - Werte wie **LP**, **VT**, **Rüstung**, **Bewegung** in großen Badges (**12 pt fett**).
  - Klare Trennung durch Kacheln / Boxen mit solidem Rand.
- **Zeilenabstand:** Mindestens `line-height: 1.35 bis 1.4` für ermüdungsfreies Lesen bei Dämmerlicht/Kerzenschein im Camper.

---

## 3. Dynamische Begegnungskarten & Spielfeld-Layout

- **Keine festen Monster in Vorkammern:** Vorkammern nutzen immer das **16-Karten-Begegnungsdeck**.
- **Zonenausweisung auf dem 30 mm Raster:**
  - `[V]` = **Vordere Zone** (Nahkämpfer, Worge, Spinnenstürmer).
  - `[H]` = **Hintere Zone** (Bogenschützen, Spinnennester, lauernde Einheiten).
  - `S1..S4` = Feste Startfelder der 4 Helden am Südrand.
- **Feste Boss-Kammern (Teil 2):** Bleiben kuratierte Höhepunkte mit Boss-Stat-Block, Sonderfähigkeit (Phasenwechsel unter 50% LP) und fester Leibwache.

---

## 4. Grafiken & Midjourney-Asset-Pipeline (Austauschbarkeit)

Die Spielfelder und Dungeonelemente sind so modular aufgebaut, dass sie jederzeit durch **Midjourney-Grafiken** veredelt werden können:

### Modulare Bildelemente & Maße:
1. **Möbel & Objekte (Transparente PNGs / Freisteller):**
   - **Schatztruhe:** 1×1 Feld (30 × 30 mm -> 354 × 354 px bei 300 DPI).
   - **Steinsarkophag:** 1×2 Felder (60 × 30 mm -> 708 × 354 px bei 300 DPI).
   - **Rundsäulen:** 1×1 Feld (30 × 30 mm Kreis/Draufsicht).
   - **Fallen (Stachelgrube, Bärenfalle):** 1×1 Feld (30 × 30 mm).
2. **Kachel-Bodentexturen:**
   - Nahtlose Steinböden, Gruftfliesen oder Erdreich können als Hintergrund-Textur hinter das SVG-Gitter gelegt werden.
3. **Midjourney-Prompt-Stil für Top-Down Kacheln:**
   - `top-down battlemap token, medieval dungeon stone chest / sarcophagus / stone pillar, isolated on white background, sharp vector woodcut engraving style, highly detailed --no perspective, 3d`

