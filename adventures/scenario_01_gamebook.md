# Szenario 01 (Game Book Edition) — Die verfluchte Krypta von Dun-Karr

> **Format:** 210 × 210 mm Quadrat-Buch (Wire-O Spiralbindung) / A4-Druckvorlage  
> **Druckdateien:** [`gamebook_scenario_01.docx`](file:///c:/Users/christoph.willimzik/Agent_Bunny/RV_Quest/printables/gamebook_scenario_01.docx) & [`gamebook_scenario_01.odt`](file:///c:/Users/christoph.willimzik/Agent_Bunny/RV_Quest/printables/gamebook_scenario_01.odt)  
> **Tischmaß geöffnet:** 420 × 210 mm (Optimiert für kompakte Wohnmobiltische)  
> **Raster:** 30 mm Gitter (für 30 mm Holz-Standees und nummerierte Basen)  
> **Dauer:** ca. 45–60 Minuten | **Helden:** 4 Helden (Stufe 1)  

---

## 📖 Kampagnen-Kontext & Einstieg

*Am Rande des Nördlichen Ödlands gähnt der Eingang zu den Grabhügeln von Dun-Karr in der frostigen Erde. Alte Legenden besagen, dass hier ein korrumpierter Hauptmann des alten Kaiserreichs ruht — gebettet auf gestohlenem Gold und arkanen Relikten.*  
*Mit gezogenen Klingen und flackernder Fackel steigt ihr in das klamme Steingewölbe hinab...*

---

# DOPPELSEITE 1: DIE VORKAMMERN DER KRYPTA
*(Abschnitt 1: Vorkammer & Dynamisches Raum-Setup)*

## Linke Seite: Szenario-Text, Regeln & Begegnungs-Mechanik

### 1.1 Dynamisches Setup über das Begegnungsdeck
Dieses Gewölbe wird dynamisch über das **16-Karten-Begegnungsdeck** (`components/encounter_cards.md`) bespielt. Dadurch bleibt jedes Abenteuer unvorhersehbar und wiederholbar:
- **Beim Betreten:** Die oberste Karte des gemischten Begegnungsdecks wird aufgedeckt.
- **Aufstellung Vordere Zone `[V]`:** Auf den markierten Feldern (z. B. `A4`, `F4`) erscheinen die Nahkämpfer / Stürmer der Karte.
- **Aufstellung Hintere Zone `[H]`:** Auf den hinteren Markierungen (z. B. `B5`, `E5`) positionieren sich Fernkämpfer oder lauernde Monster.
- **»Hinterhalt!«:** Weist die Karte die Eigenschaft *Hinterhalt!* auf, schlagen die Monster in Runde 1 vor allen Helden zu!
- *(Tutorial-Empfehlung für den allerersten Durchlauf: Karte B01 „Banden-Vorposten“ oder B05 „Ruhelose Wache“)*.

### 1.2 Interaktives Gelände & Markierungen auf der Karte
- **2× Steinsäulen (`B3`, `E3`):** Massiver Stein. Blockiert Bewegung und Sichtlinie. Gewährt Helden und Monstern volle Deckung vor Fernkampfangriffen.
- **Schatztruhe (`E4`):** Schloss knacken mit `LIS (SG 5)` oder mit Brechstange/Stärke öffnen: Ziehe 1 Karte vom **Ausrüstungsdeck**!
- **Tor T1 (`C6/D6`):** Verdecktes **Tür-Token**. Erfordert zum Durchschreiten in die Grabkammer:
  - 🪓 `KRA (SG 6)`: Eintreten der morschen Balken.
  - 🗝️ `LIS (SG 5)`: Schloss mit Diebeswerkzeug öffnen.
  - 🚪 `Offen`: Freier Durchgang ohne Probe.
- **Helden-Startzone (`S1`–`S4`):** Die Gruppe beginnt auf den Feldern A1 bis D1 am Südrand.

---

## Rechte Seite: Kampfplan 1 (6 × 6 Felder à 30 mm = 180 × 180 mm)
*Eingebettete Vektor-Grafik: [`gamebook_map_room1_crypt.svg`](file:///c:/Users/christoph.willimzik/Agent_Bunny/RV_Quest/printables/gamebook_map_room1_crypt.svg)*

```
        A         B         C         D         E         F
    ┌─────────┬─────────┬─────────┬─────────┬─────────┬─────────┐
  6 │         │         │ [ TOR T1-TÜRTOKEN ] │         │         │ 6
    ├─────────┼─────────┼─────────┼─────────┼─────────┼─────────┤
  5 │         │  [ H ]  │         │         │  [ H ]  │         │ 5  <- Hintere Zone [H]
    ├─────────┼─────────┼─────────┼─────────┼─────────┼─────────┤
  4 │  [ V ]  │         │         │         │ [TRUHE] │  [ V ]  │ 4  <- Vordere Zone [V] & Truhe
    ├─────────┼─────────┼─────────┼─────────┼─────────┼─────────┤
  3 │         │ [SÄULE] │         │         │ [SÄULE] │         │ 3  <- Deckungssäulen
    ├─────────┼─────────┼─────────┼─────────┼─────────┼─────────┤
  2 │         │         │ [Geröll]│ [Geröll]│         │         │ 2  <- Schutt (2 BP)
    ├─────────┼─────────┼─────────┼─────────┼─────────┼─────────┤
  1 │  [S1]   │  [S2]   │  [S3]   │  [S4]   │         │         │ 1  <- Helden-Startzone
    └─────────┴─────────┴─────────┴─────────┴─────────┴─────────┘
        A         B         C         D         E         F
```

---

# DOPPELSEITE 2: DIE GRABKAMMER DES GRUFTWÄCHTERS
*(Abschnitt 2: Kuratierter Bosskampf & Hauptbeute)*

## Linke Seite: Boss-Mechanik, Taktik & Kampagnen-Fortschritt

### 2.1 Einstieg & Atmosphäre
*Als das Steintor T1 weicht, erfüllt fauliger Grabeshauch den Raum. Auf einem erhöhten Steinsarkophag erwacht eine riesige, in uralte Prunkrüstung gehüllte Gestalt. Seine Augen glimmen im kalten Totenfeuer, als er eine schwere Kriegskeule hebt.*

### 2.2 Boss & Leibwache

#### 👑 Grabunhold / Gruftwächter (Großer Boss — 1×2 Felder, Position `C5–D5`)
*Der verfluchte Kommandant von Dun-Karr.*
- **LP:** 14 | **VT:** 7 | **Rüstung:** 1 (Zieht von jedem erlittenen Treffer 1 Schaden ab)
- **Bewegung:** 3 | **Initiative:** 3 | **Größe:** 1×2 Felder (Doppelstandee 60 × 30 mm)
- **Angriff:** *Verfluchter Streitkolben* (Nahkampf, 3 Schaden).
- **Boss-Fähigkeit — Gruftbeben (Unter 7 LP):**
  - Sobald der Gruftwächter auf unter 7 LP fällt, schlägt er wuchtig auf den Steinboden:
  - Alle Helden müssen eine Probe auf **GES (SG 6)** bestehen oder werden umgeworfen und erhalten den Zustand `Verlangsamt` (kostet 2 Bewegungspunkte zum Aufstehen).
  - Er ruft **1 Skelettkrieger** als Verstärkung bei `E1/E2` herbei!

#### 💀 Skelett-Leibwächter (2 Exemplare — Position `SK3` auf `B5`, `SK4` auf `E5`)
- **LP:** 4 | **VT:** 6 | **Bewegung:** 3 | **Initiative:** 2
- Flankieren den Sarkophag und greifen jeden Helden an, der dem Boss zu nahe kommt.

### 2.3 Belohnung & Kampagnen-Fortschritt
- **Der Prunksarkophag (`C6/D6`):**
  - Nach dem Fall des Gruftwächters geplündert:
  - **2 Karten vom Ausrüstungsdeck** ziehen.
  - **40 Goldmünzen** für die Heldengruppe.
  - **Quest-Relikt:** *Siegelring des alten Kaiserreichs* (Schlüssel-Gegenstand für Kampagnen-Szenario 02).
- **Erfahrung & Rast:** Jeder überlebende Held erhält **1 EP**. Volle Heilung aller LP bis zur nächsten Rast.

---

## Rechte Seite: Kampfplan 2 (6 × 6 Felder à 30 mm = 180 × 180 mm)
*Eingebettete Vektor-Grafik: [`gamebook_map_boss_crypt.svg`](file:///c:/Users/christoph.willimzik/Agent_Bunny/RV_Quest/printables/gamebook_map_boss_crypt.svg)*

```
        A         B         C         D         E         F
    ┌─────────┬─────────┬─────────┬─────────┬─────────┬─────────┐
  6 │         │         │ [───SARKOPHAG───] │         │         │ 6  <- Relief-Sarkophag
    ├─────────┼─────────┼─────────┼─────────┼─────────┼─────────┤
  5 │         │  [SK3]  │ [ GRUFTWÄCHTER  ] │  [SK4]  │         │ 5  <- Boss (1x2) & Leibwache
    ├─────────┼─────────┼─────────┼─────────┼─────────┼─────────┤
  4 │         │         │                 │         │         │ 4
    ├─────────┼─────────┼─────────┼─────────┼─────────┼─────────┤
  3 │ [SÄULE] │         │ [⚠️STACHELGRUBE] │         │ [SÄULE] │ 3  <- Deckungssäulen & Falle
    ├─────────┼─────────┼─────────┼─────────┼─────────┼─────────┤
  2 │         │         │                 │         │         │ 2
    ├─────────┼─────────┼─────────┼─────────┼─────────┼─────────┤
  1 │         │         │  [E1]   │  [E2]   │         │         │ 1  <- Einstiegszone von Tor T1
    └─────────┴─────────┴─────────┴─────────┴─────────┴─────────┘
        A         B         C         D         E         F
```
