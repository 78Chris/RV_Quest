# Szenario-Leitfaden & Vorlage (Scenario Design Guide)

> **Zweck:** Standard-Leitfaden für die Erstellung aller Kampagnen- und Einzelszenarien für *Von Helden und Monstern — Abenteuer in der Alten Welt*.  
> **Konstruktions-Prinzip:** **Dynamische Erkundung** — kein Durchblättern oder Spoilern des Dungeons im Voraus. Räume, Türen und Begegnungen werden dynamisch im Spiel aufgedeckt.

---

## 📐 Das 4-Säulen-Prinzip für Szenarien

Jedes Szenario in *Von Helden und Monstern* besteht aus exakt vier strukturellen Zonen / Kammern:

1. **Kammer 1 (Einstiegs-Zone — 4×4 Kachel):**
   - Die Helden betreten das Gewölbe oder den Schauplatz.
   - **Keine Leerräume:** Sofortige erste dynamische Begegnung (**Ziehe 1 Karte vom Begegnungsdeck**) oder atmosphärische Startwachen.
   - Ausgang: Verdecktes Zufalls-Tür-Token.
2. **Kammer 2 (Taktischer Korridor / Flutkanal — 3×6 oder 6×4 Kachel):**
   - Dynamische Begegnung via Begegnungsdeck (`[V]` Front / `[H]` Fernkampf/Ecken).
   - Enthält interaktives Gelände oder erste Missions-Schlüssel/Hebel (z. B. Schleusenrad A, Einsturzgefahr).
3. **Kammer 3 (Große Vorkammer / Vorhof — 6×4 oder 6×6 Kachel):**
   - Höhere Gefahr: Dynamische Begegnung mit Chance auf **»Hinterhalt!«**-Karten.
   - Nebenquest / Beute-Fokus: Alchemistentisch, Sarkophag oder Schatztruhe mit optionalem SG-Check.
   - Zweiter Hebel / Haupttor-Zugang zur Bosskammer.
4. **Kammer 4 (Die Boss-Arena — Feste Inszenierung — 6×6 Kachel):**
   - **Einzige nicht-zufällige Kammer:** Handgefertigter, dramatischer Höhepunkt des Szenarios.
   - Elite- oder Bossgegner mit einzigartigen Boss-Fähigkeiten (Aura, Reaktionen, Herbeirufen).
   - Taktische Geländeelemente (Säulen als Deckung, dunkle Altäre zum Entweihen, Opfergruben).

---

## 🚪 Das Dynamische Tür- & Zonen-System

In Szenario-Beschreibungen werden Türen und Durchgänge **niemals starr vorgegeben**, sondern nutzen den **Tür-Token-Pool (20 × 20 mm Holz-Tokens)**:

- **Plättchen verdeckt mischen:**
  - 🪓 **Axt:** Morsch/Verklemmt (`KRA vs. SG 5–6`) — Berserker glänzt.
  - 🗝️ **Schlüssel:** Eisenschloss (`LIS vs. SG 5–6`) — Goblin glänzt.
  - ✨ **Rune:** Arkanes Siegel (`VER vs. SG 5–6`) — Magierin glänzt.
  - 👁️ **Auge:** Fallen-Tür (`GES vs. SG 5–6`) — Kriegstänzerin glänzt.
  - 🚪 **Offen:** Frei passierbar!
- **Aufdecken:** Erst wenn ein Held direkt an die geschlossene Tür herantritt, wird das Token umgedreht.

---

## 🎴 Die Dynamische Raum-Aufdeckung (Room Reveal)

Sobald eine Tür geöffnet oder eine Wegbarriere überwunden wird:
1. **Modulare Kachel anlegen:** Die Kachel laut Szenario-Lageplan an die offene Tür legen.
2. **Feste Möbel & Missions-Objekte aufstellen:** Hebel, Altäre, Kisten laut Kachelkoordinaten (z. B. `C4`, `A1`) platzieren.
3. **Begegnungskarte ziehen:**
   - In Kammer 1, 2 und 3 wird **1 Karte vom 16-Karten Begegnungsdeck** (`components/encounter_cards.md`) gezogen.
   - Monster aufstellen:
     - `[V]` = Vordere Hälfte / Nahkämpfer.
     - `[H]` = Hintere Hälfte / Scharfschützen / Nischen.
   - **»Hinterhalt!«:** Zieht ihr eine Hinterhalt-Karte, dürfen die Monster in der ersten Runde **vor** allen Helden zuschlagen!
4. **Raum-Initiative ermitteln:** Helden würfeln `1d6 + GES`, Monster nutzen ihren festen Initiative-Wert; Holz-Token auf die Initiative-Leiste legen.

---

## 📋 Markdown-Vorlage für Neue Szenarien (Template)

Kopiere diese Vorlage, wenn du Szenario 04, 05 oder Erweiterungen schreibst:

```markdown
# Szenario XX — [Titel des Szenarios]

> **Art:** [z. B. Festungssturm, Ritualabbruch, Katakomben]  
> **Dauer:** ca. 60–80 Minuten  
> **Schwierigkeit:** [Mittel / Gehoben / Tödlich]  
> **Sprache:** Deutsch  

---

## 📖 Einführung & Atmosphäre
[3–4 Absätze stimmungsvoller Flavour-Text: Warum sind die 4 Helden hier? Was steht auf dem Spiel?]

---

## 🗺️ Gelände & Modulare Kacheln (30 mm Grid)
[Übersichts-Diagramm der 4 modularen Zonen von Kammer 1 bis 4]

---

## ⚡ Szenario-Sonderregeln
[1–3 thematische Mechaniken: z. B. Einsturzgefahr, Flutendes Wasser, Kälte, Alarm-Glocken]

---

## 🧭 Die Kammern im Detail

### Kammer 1: [Name Startzone]
- **Kachel:** [z. B. 4×4 Kachel]
- **Startaufstellung:** 4 Helden auf A1–D1.
- **Aufstellung:** Ziehe sofort 1 Karte vom Begegnungsdeck!
- **Tür:** Verdecktes Tür-Token auf [Koordinate].

### Kammer 2: [Name Durchgangszone]
- **Kachel:** [z. B. 3×6 oder 6×4 Kachel]
- **Aufstellung:** Ziehe 1 Karte vom Begegnungsdeck!
- **Missions-Interaktion / Gelände:** [z. B. Hebel A, Truhe]
- **Tür:** Verdecktes Tür-Token auf [Koordinate].

### Kammer 3: [Name Große Vorkammer]
- **Kachel:** [z. B. 6×4 Kachel]
- **Aufstellung:** Ziehe 1 Karte vom Begegnungsdeck!
- **Missions-Interaktion / Hindernis:** [z. B. Hebel B, Alchemistentisch]
- **Zugang zu Kammer 4:** [z. B. Öffnet nach Hebel A+B]

### Kammer 4: [Name Boss-Arena] (Feste Inszenierung)
- **Kachel:** 6×6 Kachel
- **Atmosphäre:** [Beschreibung]
- **Feste Gegner-Aufstellung:** 
  - 1× Boss / Elite [Werte, LP, Spezialfähigkeiten]
  - Schergen / Leibwächter
- **Taktische Geländeelemente:** [Säulen, Altar, Gruben mit SG-Aktionen]

---

## 🏆 Siegbedingungen & Belohnungen
- **Sieg:** [z. B. Boss besiegt]
- **Kopfgeld:** [Goldbetrag]
- **Schattenbazar-Zugang & Loot:** [Ausrüstungskarten, Artefakte, Dokumente]
- **Überleitung zu Szenario XX:** [Ausblick auf das nächste Abenteuer]
```

