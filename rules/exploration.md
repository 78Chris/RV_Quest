# Erkundung, Sichtlinien & Raum-Aufbau (Exploration Rules)

> **Zweck:** Regeln für Bewegung durch den Dungeon, das Entdecken neuer Räume, Türen, Fallen, Beute und die Initiative.  
> **Sprache:** Deutsch (spielerbezogene Regeln).

---

## 🚪 1. Türen, Sichtlinien & Raum-Entdeckung (Fog of War)

Dungeons in *Von Helden und Monstern* werden modular aufgebaut. Zu Beginn eines Abenteuers liegt **nur der Startraum** auf dem Tisch. Alle weiteren Räume, Gänge und Gewölbe sind verborgen.

### 🚪 Zufällige Tür-Eigenschaften: Das Tür-Token-System
Um vorhersehbare Dungeons zu verhindern und sicherzustellen, dass nicht jede Tür blind gepickt wird, werden Türen als **verdeckte Holz-Tokens** platziert:

- **Aufbau:** Bei Spielbeginn liegt an jedem Durchgang ein **verdecktes Tür-Plättchen (quadratisch 20 × 20 mm oder rund Ø 20 mm, 3 mm Sperrholz)**.
- **Entdeckung:** Sobald ein Held auf ein Feld **direkt orthogonal angrenzend** an die Tür zieht, wird das Token aufgedeckt.
- **Die 5 Tür-Kategorien:**

| Symbol auf Token | Tür-Art (Door State) | Herausforderung & Lösung | Wer glänzt |
|---|---|---|---|
| 🪓 **Axt** | **Morsch / Verklemmt**<br>Quellendes Holz, verrostete Angeln. Kein Schloss vorhanden. | Probe auf **Kraft (`KRA`) vs. SG 6** (Aufbrechen).<br>*Misserfolg:* Macht Lärm! Sofort 1 Ereigniskarte ziehen. | 🪓 **Berserker** |
| 🗝️ **Schlüssel** | **Solides Eisenschloss**<br>Schweres Kastenschloss, intakt. | Probe auf **List (`LIS`) vs. SG 6** (Schloss knacken).<br>*Gewürfelte »1«:* Dietrich bricht im Schloss ab, Tür muss eingetreten werden! | 🗝️ **Halsabschneider** |
| ✨ **Rune** | **Arkanes Siegel**<br>Schimmernde Glyphen sperren den Durchgang; Waffen prallen ab. | Probe auf **Verstand (`VER`) vs. SG 6** (Bannen / Entladen).<br>*Misserfolg:* Magische Entladung, 1 Erschöpfung. | 📜 **Magiegelehrte** |
| 👁️ **Auge** | **Fallen-Tür**<br>Drahtzug mit Giftpfeil oder Fallbeil. | Probe auf **Geschick (`GES`) vs. SG 6** (Entschärfen / Hechten).<br>*(Kriegstänzerin entdeckt dies durch Elfensinne automatisch).* | 🗡️ **Kriegstänzerin** |
| 🚪 **Offen** | **Angelehnt / Entriegelt**<br>Schwingt leise auf. | Keine Probe nötig! Bewegung kann einfach fortgesetzt werden. | 🏃 **Alle Helden** |

### Der Raum-Aufbau bei Entdeckung (Room Reveal)
Sobald die Tür überwunden oder geöffnet ist, geschieht Folgendes in genauer Reihenfolge:
1. **Kachel(n) anlegen:** Das entsprechende modulare Raum-Tile wird passend an die Türöffnung angelegt.
   - **Mehrteilige Räume (Kombinierte Großsäle):** Szenarien können zwei Kacheln zu einem einzigen großen Raum nahtlos aneinanderlegen (z. B. **6×6 + 6×4 = 60 Felder** oder **6×6 + 6×6 = 72 Felder** Boss-Kathedrale). Sie bilden ein zusammenhängendes Gewölbe ohne trennende Wand!
2. **Mobiliar & Hindernisse platzieren:** Etwaige Truhen, Sarkophage, Säulen oder Schutt lt. Szenarioplan aufstellen.
3. **Begegnung ermitteln (Encounter Card):**
   - Ist der Raum im Szenario als **Handlungsraum / Bossraum** definiert, gilt die feste Szenariovorgabe (z. B. *Der Grabunhold*).
   - In allen normalen Räumen wird **1 Begegnungskarte (Begegnungsdeck)** gezogen!
   - Die Karte nennt die Monster-Kombination (z. B. *2 Skelettkrieger + 1 Riesenspinne*) sowie deren Startpositionen im Raum.
4. **Initiative ermitteln:** Siehe Abschnitt 2.

---

## ⏱️ 2. Die Raum-Initiative & Die Initiative-Leiste (Holz-Tracker)

Kämpfe werden nicht starr Runde für Runde neu ausgewürfelt. Die Initiative wird **einmalig beim Betreten / Aufdecken eines neuen Raumes mit Monstern** ermittelt und bleibt für diesen Raum gültig!

### Die gelaserte Initiative-Leiste (Holz-Komponente)
- Auf dem Tisch liegt eine schmale, lasergeschnittene Schiene aus 3 mm Sperrholz (die **Initiative-Leiste**) mit 6–8 Aussparungen/Fächern.
- Jeder Held und jeder Monstertyp besitzt ein rundes **Holz-Initiative-Plättchen (Ø 20 mm)** mit eingraviertem Symbol:
  - 🪓 Berserker
  - 🗡️ Kriegstänzerin
  - 🗝️ Halsabschneider
  - 📜 Magiegelehrte
  - 💀 Skelette
  - 🕷️ Spinnen
  - 🐺 Worge / Biester
  - 👑 Boss / Anführer

### Ermittlung beim Raum-Betreten:
1. **Helden würfeln:** Jeder Held würfelt **1d6 + GES**.
2. **Monster-Initiative:** Monster haben einen festen Initiative-Wert auf ihrer Monsterkarte (z. B. Riesenspinne: 5, Skelettkrieger: 3, Goblin-Späher: 6). Sie müssen nicht würfeln!
3. **Plättchen einordnen:** Die runden Holz-Plättchen werden von **höchstem zu niedrigstem Gesamtwert** von links nach rechts in die Initiative-Leiste gesteckt.
   - *Gleichstand:* Helden gewinnen den Gleichstand immer gegen Monster. Bei Gleichstand unter Helden entscheidet die Gruppe.
4. **Ablauf:** Der Zug wandert nun fortlaufend entlang der Leiste. Hat das letzte Plättchen agiert, beginnt die nächste Runde wieder ganz links.

> **Hinterhalt (Ambush):**  
> Zieht die Gruppe beim Öffnen einer Tür eine Begegnungskarte mit dem Merkmal **»Hinterhalt!«** (oder scheitert der Goblin beim Entschärfen einer Türalarm-Falle), dürfen alle Monster in der ersten Runde **vor** allen Helden handeln!

---

## 🪤 3. Fallen & Geheimtüren

### Fallenarten
- **Mechanische Fallen** (Stachelgruben, Stolperdrähte, Giftpfeile):
  - Entdecken: Helden mit Blicklinie zum Feld würfeln auf **Verstand (`VER`) vs. SG 6** (Elfische Kriegstänzerin entdeckt Fallen durch *Elfensinne* automatisch auf 2 Felder Abstand).
  - Entschärfen: Erfordert Angrenzen und eine Probe auf **List (`LIS`) vs. SG 6** (Goblin hat Vorteil).
  - Auslösen: Betritt eine Figur ein Feld mit einer unentdeckten Falle, löst sie sofort aus (z. B. 2 Schaden, Gift oder Festhalten).
- **Arkane Siegel / Runenfallen:**
  - Können nur mit **Verstand (`VER`) vs. SG 6** (Magiegelehrte) gebannt oder entladen werden.

### Geheimtüren & Geheimgänge
- Eine Wand kann durchsucht werden (**Aktion: Durchsuchen**).
- Gelingt eine Probe auf **VER vs. SG 6**, wird ein verborgener Riss, Hebel oder Stein entdeckt und durch einen Mauerdurchbruch-Marker ersetzt.

---

## 💎 4. Beute, Schatztruhen & Sarkophage

In Räumen können Truhen, Urnen oder Sarkophage stehen. Ein Held auf einem angrenzenden Feld kann die **Aktion: Durchsuchen** nutzen.

1. **Verschlossene Truhe:**
   - Muss zuerst geknackt (`LIS` vs. SG 6) oder zerschlagen (`KRA` vs. SG 8, macht Lärm $\rightarrow$ Ereigniskarte) werden.
2. **Beute ziehen:**
   - **Normale Holzkiste:** Ziehe **1 Karte vom Ausrüstungsdeck** ODER nimm **1d6 Goldmünzen**.
   - **Verzierter Sarkophag / Eisentruhe (Elite-Beute):** Ziehe **2 Karten vom Ausrüstungsdeck** (wähle 1, lege die andere ab) UND erhalte **2d6 Gold**.
3. **Fallen-Gefahr:** Bei Sarkophagen oder alten Gräbern muss vor dem Ziehen 1d6 gewürfelt werden. Bei einer »1« löst ein Gasstoß oder ein Skelett-Greifarm aus (1 Schaden + Zustand *Vergiftet*).

---

## 🪨 5. Gelände & Sichtlinien

| Geländetyp | Bewegungskosten | Auswirkung |
|---|---|---|
| **Normaler Steinboden** | 1 Feld pro Bewegungspunkt | Keine Einschränkung. |
| **Schutt & Geröll** | **2 Bewegungspunkte** pro Feld | Verlangsamt. Sturmangriffe nicht möglich. |
| **Wasser / Schlamm** | **2 Bewegungspunkte** pro Feld | Fernkampfangriffe aus dem Schlamm haben Nachteil. |
| **Säule / Mauer** | Unpassierbar | Blockiert Bewegung und blockiert vollständige Sichtlinie (Deckung). |
| **Figuren (Helden/Monster)** | Blockieren | Man kann nicht durch gegnerische Felder ziehen (Ausnahme: Goblin *Durchwuseln* und Kriegstänzerin *Schattenschritt*). |

### Sichtlinie (Line of Sight - LoS)
- Eine Sichtlinie existiert, wenn eine gedachte gerade Linie vom Zentrum des Angreiferfeldes zum Zentrum des Zielfeldes gezogen werden kann, ohne eine feste Wand oder eine geschlossene Tür zu schneiden.
- Steht eine befreundete oder feindliche Figur direkt auf dieser Linie zwischen Fernkämpfer und Ziel, erhält das Ziel **Teildeckung** (+1 auf Verteidigung).
