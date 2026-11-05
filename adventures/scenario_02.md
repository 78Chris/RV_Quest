# Szenario 02 — Hinterhalt im Nebelmoor

> **Art:** Taktisches Wildnis- & Flucht-Szenario  
> **Dauer:** ca. 50–70 Minuten  
> **Schwierigkeit:** Mittel (für 4 Helden)  
> **Sprache:** Deutsch  

---

## 📖 Einführung & Atmosphäre

> *Nachdem ihr die verfluchte Krypta von Dun-Karr hinter euch gelassen habt, führt euch die gefundene Schriftrolle nach Süden — an die nebligen Grenzlande zwischen dem Nördlichen Ödland und den Ausläufern von Kaisertum Valdor.*  
>  
> *Dichter, faulig riechender Nebel kriecht über das Moor. Der morastige Boden saugt bei jedem Schritt an euren Stiefeln. Plötzlich zerschneidet ein heiseres, kehliges Heulen die Stille. Aus dem trüben Dunst leuchten gelbe Augen auf: Hungrige Moor-Ghule und räudige Ödland-Worge haben eure Fährte aufgenommen, während im Schatten feige Goblin-Plünderer darauf lauern, die Reste eurer Ausrüstung zusammenzuklauben.*  
>  
> *Hier gibt es keine schützenden Mauern — ihr müsst euch den Weg durch Morast, Nebel und Bestien bahnen, um den sicheren Karrenweg zu erreichen!*

---

## 🗺️ Gelände & Modulare Kacheln (30 mm Grid)

Das Szenario nutzt **4 modulare Platten (Erd-/Holzseite)**, die ein weitläufiges Moor bilden:

```
               ┌─────────────────────────────────────┐
               │              ZONE 4                 │
               │   (6×6 Kachel: Der alte Steg)       │
               │         [ ZIEL & BOSS ]             │
               └──────────────────┬──────────────────┘
                                  │ [Nebel-Barriere / Weidenverhau]
               ┌──────────────────┴──────────────────┐
               │              ZONE 3                 │
               │   (6×4 Kachel: Das Moor-Labyrinth)  │
               │         [Encounter Deck]            │
               └──────────────────┬──────────────────┘
                                  │ [Schilf-Durchgang]
               ┌──────────────────┴──────────────────┐
               │              ZONE 2                 │
               │   (6×6 Kachel: Versunkene Ruine)    │
               │         [Encounter Deck]            │
               └──────────────────┬──────────────────┘
                                  │ [Moorpfad-Trigger]
               ┌──────────────────┴──────────────────┐
               │              ZONE 1                 │
               │   (4×4 Kachel: Moorrand-Start)      │
               │            START-ZONE               │
               └─────────────────────────────────────┘
```

---

## 🌿 Besondere Geländeregeln des Nebelmoors

1. **Morast & Schlammlöcher (Schwieriges Gelände):**
   * Alle mit braunem Moorwasser/Schlamm markierten Felder kosten **2 Bewegungspunkte** pro Feld.
   * *Goblin-Vorteil:* Dank seiner Rassenfähigkeit *Durchwuseln* und seines geringen Gewichts darf der Goblin 1 Morastfeld pro Zug wie normales Gelände überqueren!
2. **Dichter Bodennebel (Sichtweiten-Begrenzung):**
   * Fernkampfangriffe und Zauber haben eine **maximale Sichtweite von 4 Feldern** (darüber hinaus verschluckt der Nebel alle Silhouetten).
3. **Leichenfraß der Moor-Ghule:**
   * Besiegte Worge oder Goblins hinterlassen ein **Beute-/Kadaver-Plättchen**. Steht ein Moor-Ghul am Rundenende auf einem solchen Feld, frisst er und heilt sofort **2 LP**!

---

## 🧭 Die Zonen im Detail

### Zone 1: Der Morastige Waldrand (Startzone)
- **Kachel:** **4 × 4 Felder** (Erd-/Moos-Design).
- **Startaufstellung:** Die 4 Helden starten auf der südlichen Kante (Felder A1, B1, C1, D1).
- **Lage:** Aus dem Nebel schälen sich die ersten fauligen Gestalten.
- **Trigger am Nordrand:**
  - Am Übergang zu Zone 2 liegt ein verdecktes **Weg-Token** (funktioniert wie ein Tür-Token, z. B. 🪓 *Verhau wegschlagen* oder 👁️ *Trittsteine finden / GES*).
  - Sobald gelöst, wird Zone 2 angelegt und die erste Begegnung aufgedeckt!

---

### Zone 2: Die versunkene Ruine (Dynamische Begegnung)
- **Kachel:** **6 × 6 Felder** mit moosbewachsenen Steinresten, Säulen und tiefen Moraststellen.
- **Aufstellung via Begegnungsdeck:**
  - **Ziehe 1 Karte vom Begegnungsdeck (`components/encounter_cards.md`)!**
  - Die Karte bestimmt die genaue Monster-Aufstellung (`[V]` = Vordere Zone / Schlamm, `[H]` = Hintere Ruinenmauer / Deckung), sowie zusätzliche Hindernisse oder Schätze.
  - *Moor-Sonderregel:* Handelt es sich um Goblins oder Worge, nutzen diese den dichten Nebel für ihren Jagdvorteil.
- **Gelände:**
  - 2 Steinsäulen bieten Schutz vor Fernkampfangriffen.
  - Morastfelder verlangsamen Figuren ohne *Durchwuseln*.

---

### Zone 3: Das Knochen-Dickicht (Dynamische Begegnung)
- **Kachel:** **6 × 4 Felder** (ein schmaler Schilfpfad zwischen unpassierbaren Tümpeln).
- **Hindernis am Eingang:** Klebriges Schilfdickicht (benötigt `KRA (SG 6)` zum Durchschlagen oder `GES (SG 6)` zum Durchschlüpfen).
- **Aufstellung via Begegnungsdeck:**
  - **Ziehe 1 Karte vom Begegnungsdeck!**
  - *Gefahr im Verzug:* Zieht ihr eine Karte mit **»Hinterhalt!«**, brechen die Monster direkt aus dem Schilf hervor und agieren in Runde 1 vor allen Helden!
- **Rundenende-Event:** Am Ende der ersten Runde in Zone 3 wird zusätzlich **1 Karte vom Ereigniskarten-Deck** gezogen.

---

### Zone 4: Der alte Holzsteg & Das Rudel-Alpha (Boss-Zone)
- **Kachel:** **6 × 6 Felder** (ein morscher Holzsteg über dunklem Moorwasser).
- **Barriere:** Ein verfilzter Weidenverhau versperrt den Steg (`Axt / KRA 8` oder Fackel/Feuerzauber).
- **Gegner-Aufstellung:**
  - **1× Ödland-Worg-Alphabestie (Elite-Boss ★★☆):**
    - **LP 12**, **VT 6**, **Bewegung 6**, **Angriff 1d6 + 3**, **Schaden 2 (Rudel-Bonus +1)**.
    - *Sonderregel — Kehlenbiss:* Trifft das Alpha-Tier einen betäubten oder verlangsamten Helden, verursacht es **3 Schaden**!
  - **2× Moor-Ghule** (hungrige Aasfresser, die das Rudel begleiten).
- **Morscher Steg (Gelände-Gefahr):**
  - Helden oder Monster, die auf markierten morschen Stegfeldern rennen (Doppelbewegung), müssen `GES (SG 6)` bestehen oder brechen ein (`1 Schaden` + Runde beendet).

---

## 🏆 Belohnungen & Szenario-Abschluss

Wenn alle Bestien in Zone 4 besiegt sind und mindestens ein Held das Nordufer erreicht:

1. **Gold:** Jeder Held erhält **6 Gold** (plus Kopfgeld für besiegte Monster).
2. **Beute des Rudels:** Die Überreste eines kaiserlichen Boten am Steg enthalten:
   - **1 garantierte gezogene Waffe** vom Ausrüstungsdeck.
   - **Kaiserliche Depesche:** Eine versiegelte Nachricht, die enthüllt, dass die Untoten im Kaisertum von den *versunkenen Zisternen der Hauptstadt Valdor* koordiniert werden (Überleitung zu **Szenario 03**!).
3. **Zwischenspiel im Schattenbazar:**
   - Helden dürfen zwischen Szenario 02 und 03 auf dem *Schattenbazar* einkaufen (4 offene Ausrüstungskarten).
   - Verbrauchte Heiltränke und Rationen können wieder aufgefüllt werden.
