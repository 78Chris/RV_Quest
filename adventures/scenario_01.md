# Szenario 01 — Die verfluchte Krypta von Dun-Karr

> **Art:** Einführungs-Szenario / Tutorial  
> **Dauer:** ca. 45–60 Minuten  
> **Schwierigkeit:** Normal (für 4 Helden)  
> **Sprache:** Deutsch  

---

## 📖 Einführung & Atmosphäre

> *Am Rande des Nördlichen Ödlands gähnt der Eingang zu den Grabhügeln von Dun-Karr in der frostigen Erde. Alte Legenden besagen, dass hier ein korrumpierter Hauptmann des alten Kaiserreichs ruht — gebettet auf gestohlenem Gold und arkanen Relikten.*  
>  
> *Für den Nordland-Berserker ist es die Jagd nach einer legendären Schlachtklinge; die Elfische Kriegstänzerin spürt eine Entweihung uralter Wurzeln; die Magiegelehrte sucht nach arkanen Schriftrollen für die Akademie; und der Goblin-Halsabschneider hat schlichtweg von der prall gefüllten Schatztruhe des Fürsten gehört.*  
>  
> *Mit gezogenen Klingen und flackernder Fackel steigt ihr in das klamme Steingewölbe hinab...*

---

## 🗺️ Dungeon-Aufbau & Game Book Struktur

> **Hinweis zur Buchfassung:**  
> Für das physische Game Book (Wire-O Quadrat-Format 210 × 210 mm) liegen die druckfertigen Dokumente vor:  
> - 📄 Markdown-Buchvorlage: [`scenario_01_gamebook.md`](file:///c:/Users/christoph.willimzik/Agent_Bunny/RV_Quest/adventures/scenario_01_gamebook.md)  
> - 📄 LibreOffice Writer: [`printables/gamebook_scenario_01.odt`](file:///c:/Users/christoph.willimzik/Agent_Bunny/RV_Quest/printables/gamebook_scenario_01.odt)  
> - 📄 Word Document: [`printables/gamebook_scenario_01.docx`](file:///c:/Users/christoph.willimzik/Agent_Bunny/RV_Quest/printables/gamebook_scenario_01.docx)  
> Die Vorkammern werden dynamisch über das **16-Karten-Begegnungsdeck** mit Zonen `[V]` und `[H]` bestückt; Teil 2 ist die illustrierte Boss-Arena des Gruftwächters.

Der Dungeon besteht aus **4 zusammenhängenden Abschnitten**, die in der Buchform auf 2 übersichtliche Doppelseiten (Vorkammern & Grabkammer) verteilt sind.

```
                  ┌───────────────────────┐
                  │        RAUM 4         │
                  │  (6×6 Grabkammer)     │
                  │       [ BOSS ]        │
                  └───────────┬───────────┘
                              │ [Tür-Tor / Schloss / Rune]
                  ┌───────────┴───────────┐
                  │        RAUM 3         │
                  │ (6×6 Säulengewölbe)   │
                  │    [Encounter Deck]   │
                  └───────────┬───────────┘
                              │ [Tür-Token]
                  ┌───────────┴───────────┐
                  │        RAUM 2         │
                  │ (6×4 Vorkammer)       │
                  │    [Encounter Deck]   │
                  └───────────┬───────────┘
                              │ [Tür-Token]
                  ┌───────────┴───────────┐
                  │        RAUM 1         │
                  │ (4×4 Eingangshalle)   │
                  │      START-ZONE       │
                  └───────────────────────┘
```

---

## 🚪 Die Räume im Detail

### Raum 1: Die verfallene Eingangshalle (Startraum)
- **Größe & Kachel:** 4 × 4 Felder (Grid: A1 bis D4, kleines Nebengewölbe).
- **Startzone:** Die 4 Helden starten auf den Feldern A1, B1, C1, D1.
- **Inhalt & Entdeckung:**
  - Staubige Reliefs, feuchte Fliesen. Keine Gegner.
  - **Tutorial-Aktion:** Jeder Held kann seinen Zug nutzen, um sich mit Bewegung (3–4 Felder) und Aktionen vertraut zu machen.
  - **Tür zu Raum 2:** Am nördlichen Ende (Feld B4/C4). Liegt als verdecktes **Tür-Token** bereit (Empfehlung für den ersten Einstieg: 🪓 *Axt* oder 🗝️ *Schlüssel*).
- **Rundentrigger:** Sobald ein Held das Tür-Token löst, wird das Tile von Raum 2 angelegt und **1 Begegnungskarte** gezogen!

---

### Raum 2: Die Vorkammer der Krypta (Erste Begegnung)
- **Größe & Kachel:** **6 × 4 Felder** (24 Felder — mittlere Kammer mit Front- und Rücklinie).
- **Tür-Aufbau:** Beim Öffnen der Tür zu Raum 1 wird die Kachel angelegt.
- **Gegner-Aufstellung & Inhalt:**
  - **Ziehe 1 Karte vom Begegnungsdeck (`components/encounter_cards.md`)!**
  - *Tutorial-Empfehlung für den ersten Spieldurchlauf:* Karte `B01 (Banden-Vorposten)` oder `B05 (Ruhelose Wache)`.
  - Bei weiteren Durchläufen: Vollständig zufälliger Zug vom gemischten Stapel (hohe Wiederspielbarkeit!).
- **Initiative:** Alle Helden würfeln `1d6 + GES`, Monster nutzen ihren festen Wert. Plättchen in die **Initiative-Leiste** stecken!
- **Tür zu Raum 3:** Am Nordende liegt ein weiteres **verdecktes zufälliges Tür-Token**.

---

### Raum 3: Das finstere Säulengewölbe (Gefahr & Manövrieren)
- **Größe & Kachel:** **6 × 6 Felder** (36 Felder — große Haupthalle mit viel Manövrierraum).
- **Tür-Aufbau:** Held deckt das Tür-Token an Raum 2 auf und überwindet die entsprechende Herausforderung (Aufbrechen, Dietrich, Magiebannung oder Entschärfen).
- **Gegner-Aufstellung & Inhalt:**
  - **Ziehe 1 Karte vom Begegnungsdeck!** (Z. B. Spinnen, Untote oder ein Hinterhalt).
- **Atmosphäre & Gelände:**
  - **Knochenfeld / Schutt:** 2 markierte Reihen gelten als schwieriges Gelände (doppelte Bewegungskosten).
  - 2 massive Steinsäulen bieten Deckung für Fernkämpfer oder Schutz vor Anstürmen.
  - **Ereigniskarte:** Beim ersten Betreten dieses Raums wird am Rundenende zusätzlich **1 Ereigniskarte** gezogen!
- **Tür zu Raum 4 (Boss-Tor):**
  - Massive, runenversiegelte Eisentür: Benötigt einen in Raum 2/3 erbeuteten Gruftschlüssel ODER einen Dietrich-Wurf `LIS (SG 8)` ODER Runenbannung `VER (SG 8)`.

---

### Raum 4: Die Grabkammer des Gruftwächters (Große Boss-Begegnung)
- **Größe & Kacheln:** **Kombinierter Großsaal aus 2 Kacheln:** **6 × 6 + 6 × 4 Felder** (**60 Felder gesamt** = 18 × 30 cm Spielfläche ohne Trennwand).
  - Bietet reichlich Platz für epische Bewegungen, Distanzschüsse der Akademie-Magierin, Flankierungsangriffe der Kriegstänzerin und den wuchtigen Rundumschlag des Bosses!
- **Tür:** Verschlossenes Eisengitter. Benötigt einen Schlüssel (gefunden bei den Skeletten in Raum 3) ODER einen Dietrich-Wurf `LIS (SG 8)` des Goblins ODER Runenbannung `VER (SG 8)`.
- **Gegner-Aufstellung:**
  - **1× Grabunhold / Gruftwächter (Boss — ★★★)** (LP 14, VT 7, Rüstung 1, Streitkolben 3 Schaden)
  - **2× Skelettkrieger** (Leibwächter, LP 4, VT 6)
- **Boss-Mechanik — Gruftbeben:**
  - Fällt der Gruftwächter auf unter 7 LP, schlägt er mit dem Kolben auf den Boden: Alle Helden müssen `GES (SG 6)` bestehen oder werden 1 Runde lang `Verlangsamt`.
- **Der Sarkophag (Hauptschatz):**
  - Sobald der Gruftwächter besiegt ist, darf der Steinsarkophag geöffnet werden:
  - **Belohnung:** **2 Karten vom Ausrüstungsdeck** + **8 Gold** (zur Aufteilung).

---

## 🏆 Sieg- & Niederlage-Bedingungen

- **Sieg (Victory):**
  - Der Grabunhold in Raum 4 ist besiegt und mindestens 1 Held ist noch auf den Beinen.
- **Niederlage (Defeat):**
  - Alle 4 Helden sind zeitgleich bewusstlos (0 LP).

---

## 💰 Szenario-Abrechnung & Rast (Intermission)

1. **Pauschalbelohnung:** Jeder Held erhält **5 Gold**.
2. **Kopfgeld:**
   - 2 Goblin-Späher (je 1G) = 2G
   - 1 Goblin-Bogenschütze = 1G
   - 4 Skelettkrieger (je 1G) = 4G
   - 1 Riesenspinne = 2G
   - 1 Grabunhold (Boss) = 5G
   - *Gesamtes Kopfgeld: 14 Gold* (wird gleichmäßig unter den 4 Helden aufgeteilt: je 3–4 Gold).
3. **Schatz-Ausbeute:** Bis zu 3 gezogene Ausrüstungskarten aus Truhen & Boss.
4. **Marktauslage:** Decke **4 neue Karten vom Ausrüstungsdeck** auf. Die Helden können ihr Gold ausgeben, um sich für Szenario 02 auszustatten!
5. **Erholung:** Alle Helden regenerieren ihre Lebenspunkte (LP) und die Erschöpfungsleisten (Fatigue) vollständig auf das Maximum.
