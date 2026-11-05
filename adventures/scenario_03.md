# Szenario 03 — Die versunkene Zisterne von Valdor

> **Art:** Unterirdischer Dungeon-Crawl mit Schleim-, Wasser- und Ritual-Mechanik  
> **Dauer:** ca. 60–80 Minuten  
> **Schwierigkeit:** Gehoben (für 4 Helden)  
> **Sprache:** Deutsch  

---

## 📖 Einführung & Atmosphäre

> *Die aus dem Nebelmoor gerettete kaiserliche Depesche hat die schreckliche Wahrheit enthüllt: Der Vormarsch der Untoten aus dem Norden ist kein zufälliges Erwachen alter Gräber — kaiserliche Ratsherren und abtrünnige Magier paktieren im Verborgenen mit dem uralten Lich-König!*  
>  
> *Unter den prunkvollen Straßen der Hauptstadt Valdor liegt ein jahrhundertealtes Netz aus Zisternen und Abwasserkanälen. Dort unten, wo das Wasser der Brunnen zusammenfließt, hat sich der **Kult des Schattens** eingenistet. Sie gießen nekrotisches Gift in die Wasserversorgung und bereiten ein finsteres Ritual vor, um das Tor für die Armeen des Todes aufzustoßen.*  
>  
> *Der Gestank von Fäulnis und saurem Alchemisten-Gebräu schlägt euch entgegen, als ihr die feuchten Steinstufen in die Tiefe hinabsteigt. Trübes, brackiges Wasser schwappt euch um die Schienbeine. Ihr müsst die Schleusentore schließen, das Ritual unterbrechen und den Zirkel auslöschen, bevor ganz Valdor dem Gift anheimfällt!*

---

## 🗺️ Gelände & Modulare Kacheln (30 mm Grid)

Das Szenario nutzt **4 modulare Platten (Steinseite / Kanäle)**:

```
               ┌─────────────────────────────────────┐
               │              KAMMER 4               │
               │   (6×6 Kachel: Das Ritualbecken)    │
               │     [ BOSS & RITUAL-ALTAR ]         │
               └──────────────────┬──────────────────┘
                                  │ [Verriegeltes Eisengitter-Schleusentor]
               ┌──────────────────┴──────────────────┐
               │              KAMMER 3               │
               │   (6×4 Kachel: Die giftige Rinne)   │
               │      [Schleusenhebel B & Beute]     │
               └──────────────────┬──────────────────┘
                                  │ [Schwere Eichentür]
               ┌──────────────────┴──────────────────┐
               │              KAMMER 2               │
               │  (3×6 Kachel: Der Überflutete Gang) │
               │      [Schleusenhebel A & Spinnen]   │
               └──────────────────┬──────────────────┘
                                  │ [Morsche Holztür]
               ┌──────────────────┴──────────────────┐
               │              KAMMER 1               │
               │   (4×4 Kachel: Einstiegsschacht)    │
               │            START-ZONE               │
               └─────────────────────────────────────┘
```

---

## 💧 Besondere Zisternen-Regeln

1. **Brackwasser & Fließendes Gift (Wasserfelder):**
   * Blau/Grün markierte Wasserfelder sind **Schwieriges Gelände** (kosten **2 Bewegungspunkte**).
   * Wer eine Runde im giftigen Brackwasser beendet, muss einen **ZÄH-Wurf vs. SG 5** ablegen oder erhält den Zustand `Vergiftet` (1 Schaden am Rundenende).
2. **Die Schleusenmechanik (Wasser senken):**
   * In Kammer 2 und Kammer 3 befindet sich jeweils ein **Schleusenrad (Hebel)**.
   * Ein Held auf dem Hebelfeld kann mit **1 Aktion (KRA vs. SG 5)** das Rad betätigen.
   * **Effekt:** Das Giftwasser in der jeweiligen Kammer fließt ab! Die Felder werden zu normalem Gelände und die Giftgefahr erlischt.
   * Werden **beide Hebel** umgelegt, öffnet sich automatisch das schwere Eisengitter zu Kammer 4 (dem Ritualbecken).
3. **Goblin-Vorteil (*Rohrkrabbler*):**
   * Der Goblin-Halsabschneider ignoriert auf schmalen Mauervorsprüngen und Rohren alle Bewegungsabzüge und darf Wasserfelder unbeschadet überspringen (`GES vs. SG 4`).

---

## 🧭 Die Kammern im Detail

### Kammer 1: Der Einstiegsschacht (Dynamische Einstiegs-Begegnung)
- **Kachel:** **4 × 4 Felder** (Feuchte Ziegelsteine, von der Decke tropfendes Abwasser).
- **Startaufstellung:** Die 4 Helden starten auf der südlichen Kante (Felder A1, B1, C1, D1) am Fuße der eisernen Steigeisenleiter.
- **Aufstellung via Begegnungsdeck:**
  - Kaum haben eure Stiefel das brackige Wasser berührt, hallt das Geräusch eurer Schritte durch das Gewölbe!
  - **Ziehe sofort 1 Karte vom Begegnungsdeck (`components/encounter_cards.md`)!**
  - Platziere die gezogenen Monster auf den nördlichen Feldern der Kachel (`[V]` = Reihe 2, `[H]` = Reihe 3/4 vor der Tür).
  - *Achtung bei »Hinterhalt!«:* Die Wachen der Zisterne haben euch gehört und greifen an, bevor ihr eure Waffen richtig gezogen habt!
- **Tür nach Norden (Übergang zu Kammer 2):**
  - **Verdecktes Tür-Token** auf Feld B4/C4 aus dem Zufallspool ziehen!
  - Mögliche Token:
    - 🪓 *Morsches Holz:* Durchbrechen (`KRA vs. SG 5`)
    - 🗝️ *Eisenschloss:* Schloss knacken (`LIS vs. SG 5`)
    - ✨ *Arkane Rune:* Magisches Siegel bannen (`VER vs. SG 5`)
    - 👁️ *Fallen-Auslöser:* Stolperdraht entschärfen (`GES vs. SG 5`)
    - 🚪 *Offen:* Ungesichert, sofort passierbar!
  - Sobald die Tür geöffnet wird, wird die 3×6-Kachel für Kammer 2 angelegt!

---

### Kammer 2: Der Überflutete Gang (Dynamische Begegnung)
- **Kachel:** **3 × 6 Felder** (Länglicher Kanal mit schmalem Steg und giftigem Tiefwasser).
- **Aufstellung via Begegnungsdeck:**
  - **Ziehe 1 Karte vom Begegnungsdeck (`components/encounter_cards.md`)!**
  - Platziere die gezogenen Monster: `[V]` = Vordere Hälfte (Felder A1–B3 im Wasser), `[H]` = Hintere Kante / Simse (Felder A4–B6).
  - *Hinterhalt-Regel:* Zieht ihr eine Karte mit **»Hinterhalt!«**, stürzen die Monster sofort von den feuchten Deckenrohren herab und schlagen in Runde 1 vor allen Helden zu!
- **Gelände & Schleusenmechanik:**
  - **Schleusenhebel A:** Befindet sich auf dem trockenen Mauervorsprung auf C5.
  - Ein Held auf dem Feld kann mit **1 Aktion (`KRA vs. SG 5`)** das Schleusenrad drehen $\rightarrow$ Das Brackwasser in Kammer 2 fließt ab, alle Wasserfelder werden zu normalem, sicherem Boden!
- **Tür nach Norden (Übergang zu Kammer 3):**
  - **Verdecktes Tür-Token** aus dem Vorrat ziehen und auf Feld B6 platzieren.
  - Tür öffnen (KRA / LIS / VER / GES nach Symbol) schaltet Kammer 3 frei!

---

### Kammer 3: Die giftige Rinne & das Labor (Dynamische Begegnung)
- **Kachel:** **6 × 4 Felder** (Breite Kammer mit Abflussgraben und Alchemisten-Bänken).
- **Aufstellung via Begegnungsdeck:**
  - **Ziehe 1 Karte vom Begegnungsdeck!**
  - Platziere Monster und eventuelle Raumelemente gemäß der Karte.
- **Feste Raumelemente der Zisterne:**
  - **Alchemistentisch (Feld D2–E2):** 
    - Mit **1 Aktion (`VER vs. SG 5`)** durchsuchbar.
    - Erfolg: Findet 1× `Heiltrank` (heilt 4 LP) oder 1× `Gegengift-Ampulle`.
  - **Schleusenhebel B (Feld A4):**
    - Mit **1 Aktion (`KRA vs. SG 5`)** betätigen $\rightarrow$ Entwässert Kammer 3!
- **Das Fallgitter zu Kammer 4 (Boss-Zugang):**
  - Massives Gusseisengitter mit mechanischem Sperrwerk.
  - **Öffnet sich automatisch**, sobald **Schleusenhebel A und B** betätigt wurden!
  - *Goblin-Alternative:* Der Goblin-Halsabschneider kann das Gestänge mit `LIS vs. SG 7` kurzzeitig überbrücken.

---

### Kammer 4: Das Ritualbecken des Seuchen-Zirkels (Feste Boss-Kammer)
- **Kachel:** **6 × 6 Felder** (Monumentales Zentralbecken mit giftigem Morast, Steinsäulen und dem Dunkelaltar).
- **Atmosphäre:**
  - Grüne, unheilvolle Flammen züngeln aus Opferschalen. In der Mitte steht der Kultführer, umgeben von schwappendem Nekrose-Schleim.
- **Feste Boss-Aufstellung (Szenario-Höhepunkt):**
  - **Boss: Meisterkultist Malakor / Schatten-Adept (Elite, 10 LP, VT 6):**
    - *Aura des Verfalls:* Alle Helden innerhalb von 2 Feldern erleiden zu Beginn ihres Zugs 1 Verfallsschaden (Rüstung schützt nicht!).
    - *Blutpfeil:* Fernkampfangriff (1d6 + 3, Reichweite 4, Schaden 2).
    - *Nekrotischer Pakt:* Opfert 2 LP, um sofort ein frisches Skelett aus dem Becken zu rufen.
  - **1× Skelett-Scharfschütze** (auf Erhöhung C2).
  - **2× Skelettkrieger** (Frontlinie vor dem Becken).
- **Taktische Geländeelemente:**
  - **2 Steinsäulen (B2 und E2):** Bieten volle Deckung vor Fernkampfangriffen (+2 VT gegen Fernkampf).
  - **Der Dunkelaltar (Feld C5–D5):** 
    - Ein Held mit hohem Verstand (Magierin) kann den Altar mit **1 Aktion (`VER vs. SG 6`)** weihen/zerstören.
    - Zerstörung bricht sofort die *Aura des Verfalls* des Bosses und fügt allen Untoten im Raum 2 direkten Schaden zu!

---

## 🏆 Siegbedingungen & Belohnung

### Sieg:
- Der Meisterkultist ist besiegt und die Zisterne vor dem Überlaufen gerettet.

### Niederlage:
- Alle 4 Helden sind bewusstlos / tot. (Die Helden können sich jedoch zurückziehen; die Seuche breitet sich in Valdor aus, was das nächste Szenario erschwert).

### Belohnungen & Rast-Phase:
1. **Kopfgeld:** Jeder Held erhält **6 Gold** (Kaiserliches Kopfgeld auf den Kult).
2. **Beutefund auf dem Altar:**
   - **Kaiserlicher Chiffren-Schlüssel:** Öffnet geheime Versorgungsräume in Szenario 04.
   - **1× Ziehung vom Ausrüstungsdeck (Loot)** für jeden Helden.
   - **Arkane Formelsammlung:** Magiegelehrte regeneriert sofort alle Erschöpfungspunkte und lernt eine optionale Meister-Rune.
3. **Übergang zu Szenario 04:**
   - Die Dokumente des Kultisten verweisen auf den geheimen Rückzugsort des Zirkels: **Die belagerte Felsen-Zitadelle von Mor-Goth** in den zerklüfteten Bergen.

