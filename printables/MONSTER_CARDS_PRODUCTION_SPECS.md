# Bestiarium Imperialis — Monsterkarten Produktions-Spezifikation (v2.0)

> **Dokumenttyp:** Druck- & Layout-Referenz für die 8 Standard-Monsterkarten (Großformat-Tarot) sowie Konzeption der A5-Bosskarten  
> **Projekt:** RV_Quest — Bestiarium Imperialis (Oversized Tarot Gutter-Fold Edition)  
> **Master-Druckdatei:** [`monster_cards_all_gutterfold_a4.html`](monster_cards_all_gutterfold_a4.html)  
> **Einzeldraft-Referenz:** [`monster_card_draft_skeleton_oversized_140mm.html`](monster_card_draft_skeleton_oversized_140mm.html)

---

## 🎴 1. Grundformat & Bogenarchitektur

| Parameter | Spezifikation |
|---|---|
| **Karten-Endformat** | **Oversized Tarot: $81{,}67 \times 138\,\text{mm}$** (Exaktes $7:12$-Verhältnis) |
| **Druckbogen-Format** | **DIN A4 Portrait ($210 \times 297\,\text{mm}$)** |
| **Verfahren** | **Gutter-Fold (Falzverbund):** Vorder- und Rückseite nebeneinander ($163{,}34 \times 138\,\text{mm}$ Verbund) |
| **Nutzen pro Bogen** | **2 Kartenpaare pro A4-Bogen** (vertikal & horizontal zentriert) |
| **Bögen gesamt** | **4 A4-Bögen** für alle 8 Standard-Monsterkarten des Starter-Sets |
| **Außenraum** | **100 % Reinweiß (`#ffffff`)** — Null Tintenverschwendung außerhalb der Schnittmarken |

### Bogenplatzierung & Symmetrische Zentrierung (Kein Beschnitt oben/unten)
* **Kartenbreite Verbund:** $163{,}34\,\text{mm}$ (Vorderseite $0\text{--}81{,}67\,\text{mm}$, Rückseite $81{,}67\text{--}163{,}34\,\text{mm}$)
* **Horizontale Zentrierung:** $X_{\text{Links}} = 23{,}33\,\text{mm}$, $X_{\text{Falz}} = 105{,}00\,\text{mm}$ (exakte Bogenmitte), $X_{\text{Rechts}} = 186{,}67\,\text{mm}$
* **Oberer Sicherheitsrand:** $Y_{\text{Top-Margin}} = 8{,}5\,\text{mm}$ (garantiert kein Abschneiden auf gängigen Heimdruckern!)
* **Karte 1 (Obere Position):** $Y_{\text{Top}} = 8{,}5\,\text{mm}$, $Y_{\text{Bottom}} = 146{,}5\,\text{mm}$ (Höhe $138\,\text{mm}$)
* **Trennspalt (Schnittfuge):** $4{,}0\,\text{mm}$ ($Y = 146{,}5\text{--}150{,}5\,\text{mm}$)
* **Karte 2 (Untere Position):** $Y_{\text{Top}} = 150{,}5\,\text{mm}$, $Y_{\text{Bottom}} = 288{,}5\,\text{mm}$ (Höhe $138\,\text{mm}$)
* **Unterer Sicherheitsrand:** $Y_{\text{Bottom-Margin}} = 8{,}5\,\text{mm}$ ($297{,}0 - 288{,}5 = 8{,}5\,\text{mm}$ — exakt spiegelsymmetrisch)

### Durchgehende Lineal-Anlegekanten (Ruler Alignment Guides)
* **Vertikalschnitte & Falzrille:** Verlängerte Markierungslinien reichen bis an die äußeren Papierkanten oben ($Y = 0{,}5\text{--}7{,}5\,\text{mm}$) und unten ($Y = 289{,}5\text{--}296{,}5\,\text{mm}$). Ein 30-cm-Stahllineal kann so über den gesamten Bogen angelegt und millimetergenau arretiert werden.
* **Horizontalschnitte:** Schnittmarken reichen weit in den linken ($X = 1\text{--}20\,\text{mm}$) und rechten ($X = 190\text{--}209\,\text{mm}$) Bogenrand.
* **Falz-Führungshaarlinie:** Eine feine gestrichelte Mittellinie ($X = 105{,}0\,\text{mm}$, $0{,}14\,\text{px}$) führt das Falzbein fehlerfrei über die Bogenachse.

---

## 🖼️ 2. Artwork- & Inhaltsarchitektur

### Größeres Artwork ($56{,}5 \times 56{,}5\,\text{mm}$) + Integrierte Lore-Box
Durch die Vergrößerung der Kartenhöhe von $120\,\text{mm}$ auf $138\,\text{mm}$ und der Breite von $70\,\text{mm}$ auf $81{,}67\,\text{mm}$ profitieren Artwork und Lesbarkeit massiv:
* **+23 % mehr Bildfläche:** Die quadratischen 1:1 Midjourney-Artworks wachsen von $51 \times 51\,\text{mm}$ auf **$56{,}5 \times 56{,}5\,\text{mm}$** ($31{,}9\,\text{cm}^2$).
* **Wiedereinführung der 3-Zeilen Lore-Box:** Jede Standardkarte besitzt nun eine zentrierte, atmosphärische Zitat-Box auf Pergamentfond mit warmbraunem Akzentrahmen (`7.2pt` Alegreya Italic).
* **Entlastete Regelsektion:** Da die Kartenzeilen $11{,}7\,\text{mm}$ breiter sind, laufen Sonderregeln und KI-Verhalten in weniger Zeilen um. Kein Textüberlauf, keine Verkleinerung der Schriften.

---

## ✂️ 3. Fertigungs- & Versiegelungsanleitung (Gutter-Fold & Seal)

### Benötigtes Material & Werkzeug
* **Papier:** 180–200 g/m² ungestrichenes, mattes Papier / Feinkarton (z. B. *Clairefontaine DCP* oder *Mondi Color Copy*).
* **Kaschierkleber:** 3M Sprühkleber (z. B. *3M Display Mount* oder *3M Super 77*) oder permanenter Kleberoller (*Tesa Roller permanent*).
* **Versiegelung (Schutzschicht):** Mod Podge (vorzugsweise *Mod Podge Hard Coat* / Matt) oder transparentes Acryl-Matt-Fixativspray.
* **Werkzeuge:**
  * Feine Schaumstoffwalze (Lackierwalze / *Flock*-Schaum) und Farbwanne.
  * 30–40 cm Metall-Lineal mit Rutschhemmung.
  * Scharfes Skalpell / Rollschneider / Cuttermesser & Schneidematte.
  * Falzbein (*Bone Folder*) oder Andrückrolle (*Brayer*).

### Schritt-für-Schritt Fertigungsablauf

#### 1. Drucken
* [`monster_cards_all_gutterfold_a4.html`](monster_cards_all_gutterfold_a4.html) im Browser öffnen (`Strg + P`).
* Einstellungen: **Skalierung 100 % (Tatsächliche Größe)**, Ränder **Keine**, Hintergrundgrafiken **Aktiviert**.

#### 2. Schutz vor Tintenverlaufen (Nur bei Tintenstrahldruckern zwingend!)
* *Hintergrund:* Wasserbasierte Tinte verläuft beim direkten Überrollen mit feuchtem Kleber/Lack!
* Den gedruckten A4-Bogen vor der Weiterverarbeitung kurz und dünn mit einem **matten Acrylspray / Fixativ** einnebeln und 15 Minuten ablüften lassen. *(Bei Laserdruckern entfällt dieser Schritt).*

#### 3. Versiegelung mit der Schaumstoffwalze (Mod Podge)
* **Verdünnung:** Mod Podge in der Farbwanne mit ca. **10–15 % Wasser** auf Konsistenz von flüssiger Sahne bringen.
* **Auftrag:** Walze auf dem Abrollgitter fast trocken rollen (dünner Film, keine Tropfen). In langen, gleichmäßigen Zügen über den **gesamten ungeschnittenen A4-Bogen** rollen.
* **Tipping-Off (Bläschen entfernen):** Mit einem sauberen, trockenen Schaumpinsel ohne Druck einmal leicht über die nasse Fläche schweben, um Mikroluftbläschen sofort zu brechen.
* **Trocknung:** 30–45 Min. trocknen lassen, optional 2. dünne Schicht kreuzweise auftragen.

#### 4. Rillen & Gutter-Fold Verklebung (3M Kleber)
* **Rillen:** Stahllineal an den oberen und unteren Falzmarken (`X = 105 mm`) anlegen und mit dem Falzbein eine präzise Rille ziehen.
* **3M Kleberauftrag:**
  1. Den Bogen wenden und die Rückseite gleichmäßig einsprühen.
  2. **30–60 Sekunden ablüften lassen**, bis der Kleber klebrig-griffig (*tacky*), aber nicht mehr nass ist.
  3. Den Bogen entlang der Rille zusammenklappen.
  4. Mit Andrückrolle oder Falzbein von der Falzachse nach außen kräftig anpressen (aktiviert die Kontaktklebung).
  5. **15–20 Minuten ruhen lassen**, damit die Klingen beim Schneiden nicht verkleben.

#### 5. Endschnitt mit dem Stahllineal
* Zuerst die vertikalen Außenschnitte ($X = 23{,}33\,\text{mm}$ und $X = 186{,}67\,\text{mm}$) mithilfe der oberen und unteren Randmarken schneiden.
* Danach die horizontalen Querschnitte ($Y = 8{,}5\,\text{mm}$, $Y = 146{,}5\,\text{mm}$, $Y = 150{,}5\,\text{mm}$, $Y = 288{,}5\,\text{mm}$) abtrennen.
* *Ergebnis:* Ein verzugsfreier, extrem steifer Kartenkörper von **360–400 g/m²** mit 100 % passgenauer Vorder- und Rückseite.
* **Aushärtung vor dem Stapeln:** Mod Podge benötigt **48–72 Stunden** zur vollen Durchhärtung. Die Karten in den ersten zwei Tagen nicht unter Druck in einer Schachtel lagern, um Verkleben (*Blocking*) zu verhindern.

---

## 📋 4. Deck-Zusammenstellung (8 Standard-Karten auf 4 A4-Bögen)

Die großen Monster und Kampagnen-Bosse wurden in eigene **A5-Landscape-Dashboards** ausgelagert. Das Standard-Monsterdeck umfasst **8 taktische Karten** auf **4 Druckbögen**:

| Bogen | # | Monster-Name | Stufe | Typus & Rolle | LP | VT | Bew. | Init | Hauptangriff |
|---|---|---|---|---|---|---|---|---|---|
| **Bogen 1** | **01** | Goblin-Späher | ★☆☆ | Standard · Schwarm / Flanker | 3 | 5 | 4 | **5** | +1 Rostdolch (1 Schaden) |
| | **02** | Goblin-Schütze | ★☆☆ | Standard · Hinterhalt-Fernkampf | 2 | 4 | 3 | **6** | +2 Knochenpfeil (1 Schaden) |
| **Bogen 2** | **03** | Skelettkrieger | ★★☆ | Standard · Untoter Nahkämpfer | 4 | 6 | 3 | **3** | +2 Rostschwert (2 Schaden) |
| | **04** | Riesenspinne | ★★☆ | Standard · Lauerjäger & Gift | 5 | 5 | 4 | **6** | +2 Giftbiss (1 Schaden + Gift) |
| **Bogen 3** | **05** | Ödland-Worg | ★★☆ | Elite · Schneller Flankierer | 6 | 5 | 5 | **7** | +3 Reißbiss (2 Schaden) |
| | **06** | Schattenkultist | ★☆☆ | Standard · Magie-Unterstützer | 3 | 4 | 3 | **4** | +2 Seelenschuss (1 Schaden) |
| **Bogen 4** | **07** | Moor-Ghul | ★★☆ | Standard · Aasfresser & Seuche | 4 | 5 | 5 | **5** | +2 Krallen (1 Schaden + Seuche) |
| | **08** | Skelett-Schütze | ★★☆ | Standard · Geister-Fernkämpfer | 3 | 5 | 3 | **5** | +3 Geisterbogen (2 Schaden) |

---

## 🐉 5. Konzept: Große Monster & Boss-Karten (A5-Querformat Gutter-Fold)

### Ausgelagerte Kreaturen & Bosse
1. **Grabunhold / Gruftwächter** *(Szenario 1 Boss · Groß 1×2 Felder · 14 LP)*
2. **Der Blutgolem** *(Szenario 4 Belagerungs-Monster · Groß 1×2 Felder · 10 LP)*
3. **Todesritter von Mor-Goth** *(Szenario 4 Bergfried-Boss · Elite-Hügelfürst · 8 LP)*
4. **Lich-König Malakor** *(Szenario 5 Kampagnen-Endgegner · 2 Aktionen/Runde · 18 LP)*

### Gutter-Fold Bogenarchitektur für A5-Querformat (1 Boss pro A4-Bogen)
* **Problem von echtem DIN A5 ($210 \times 148{,}5\,\text{mm}$):** Zwei echte A5-Seiten füllen $210 \times 297\,\text{mm}$ zu 100 % aus. Drucker schneiden an allen vier Rändern 5–8 mm ab.
* **Die Produktionslösung (Oversized Mini-A5 Gutter-Fold):**
  * **Endformat gefaltet:** **$195 \times 138\,\text{mm}$** (oder $190 \times 135\,\text{mm}$)
  * **Ungefalteter Druckbogen:** $195\,\text{mm}$ Breite $\times 276\,\text{mm}$ Gesamthöhe auf A4 Portrait.
  * **Sicherheitsränder auf A4:**
    * Links & Rechts: je **$7{,}5\,\text{mm}$ Rand** ($210 - 195 = 15\,\text{mm}$)
    * Oben & Unten: je **$10{,}5\,\text{mm}$ Rand** ($297 - 276 = 21\,\text{mm}$)
  * **Falzachse:** Waagerechte Mittellinie bei **$Y = 148{,}5\,\text{mm}$** (exakte Bogenmitte).
  * **Falzprinzip:** Die Oberseite klappt nach unten um (Top-to-Bottom Fold).

### Layout-Vorschlag A5-Querformat

#### Vorderseite (Front Face — Das taktische Boss-Tableau)
* **Zweispaltiger Split-View:**
  * **Linke Spalte ($40\,\% \approx 78\,\text{mm}$):** Großes, monumentales Hochkant-Artwork ($72 \times 108\,\text{mm}$, Seitenverhältnis `2:3`), darunter ein graviertes Pergamentband mit 3-zeiligem Schreckens-Zitat und Standee-Footprint-Hinweis (`Größe: 1×2 Felder / 60×45mm Holzplakette`).
  * **Rechte Spalte ($60\,\% \approx 117\,\text{mm}$):**
    * *Kopfbereich:* Boss-Titel in Fraktur & Cinzel (`16pt`), Gefahrensterne (`★★★★`), Initiative-Pille & Phasen-Anzeige.
    * *Stat-Leiste (Großchips):* Leben-Track (mit Kästchen zum Abstreichen oder Marker-Ablage), Rüstung, Verteidigung, Bewegung.
    * *Passive Auren & Resistenzen:* z. B. Frosthauch, Unaufhaltsame Masse, Seelenkäfig.
    * *Phasen-Matrix / Schwellenwerte:* Was passiert bei 50 % LP (z. B. Malakors arktischer Wirbel / Blutgolem-Wut).

#### Rückseite (Back Face — Zwei Design-Optionen)
* **Option A: Solo/Koop KI-Entscheidungsbaum & Kampagnen-Setup (Empfohlen)**
  * Vollwertiger Ablaufbaum: D6-Reaktionstabelle für Solo-Runden (z. B. Wurf 1-2: Rundumschlag, 3-4: Fernkampf/Fluch, 5-6: Schergen rufen).
  * Lair Actions & Umgebungsgefahren zu Rundenbeginn.
  * Beute- & Belohnungstabelle bei Boss-Sieg.
* **Option B: Atmosphärischer Großformat-Buchrücken (*Grimoire Imperialis*)**
  * Querformatige Ausführung des Leder-Holzschnitt-Grimoires mit breiter Banderole, dunklen Eisenbeschlägen und mittigem Dämonenschädel-Relief.
