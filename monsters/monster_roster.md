# Monster-Roster & KI-Verhalten (Bestiarium v0.1)

> **Design-Prinzip:** Schnelle Runden im 2-Spieler-Koop ohne Spielleiter.  
> Jeder Gegnertyp hat eine **feste Initiative (INIT: X)**, **statische Verteidigung (VT)** und ein einfaches, verständliches **3-Schritte-Verhalten** (Targeting / Action).  
> **Kartenformat:** **Tarot (70 × 120 mm)** mit Gutter-Fold Klapp-Druckbogen und zentriertem Deckrücken *»Bestiarium Imperialis«*.

---

## 🎲 Grundregeln für Monster-Aktivierung

1. **Aktivierungs-Reihenfolge (Initiative-Leiste):** Monster nutzen ihren festen Initiative-Wert (**`INIT: X`**) auf ihrer Monsterkarte. Ihr runder Holz-Marker (Ø 20 mm) wird beim Betreten eines Raumes direkt in die gelaserte **Initiative-Leiste** gesteckt (Helden würfeln `1d6 + GES`). Die Figuren aktivieren streng von links nach rechts entlang der Leiste.
2. **Kein Initiative-Wurf für Monster:** Der `INIT`-Wert ist statisch und unveränderlich.
3. **Monster-Angriff:** Wenn ein Monster angreift, würfelt ein Spieler **1d6 + Monster-Angriffsbonus** gegen den **VT-Wert des Helden** (Basis 4 + Rüstung/Schild). Bei Erfolg erleidet der Held den angegebenen Schaden abzüglich Rüstungsreduktion.
4. **Ziel-Priorität (Verhalten):**
   - **Primärziel:** Gemäß Kartentext (z. B. Skelette greifen Helden mit höchster Rüstung an; Worge flankieren auf den hintersten Helden; Ghouls stürmen auf den Helden mit den wenigsten LP).
   - **Gleichstand:** Nächstgelegenes Ziel wird gewählt.

---

## 📋 Monster-Profile (12 Gegnertypen — Kampagnen-Bestiarium)

### 1. Goblin-Späher (Goblin Scout) — Schwarm / Nahkampf
*Fliehende, feige Halsabschneider der Banden.*

| Eigenschaft | Wert |
|---|---|
| **Kategorie** | Standard (★☆☆) |
| **Lebenspunkte (LP)** | 3 |
| **Verteidigung (VT)** | 5 |
| **Bewegung** | 4 Felder |
| **Angriff** | 1d6 + 1 (Nahkampf) |
| **Schaden** | 1 |
| **Kopfgeld** | 1 Gold |

**Automatisches KI-Verhalten:**
1. **Rudel-Taktik:** Wenn ein befreundeter Goblin bereits an einen Helden angrenzt, bewege dich auf DIESEN Helden zu und greife an (erhält Vorteil).
2. **Angriff:** Greife den nächsten Helden an.
3. **Feigheit:** Wenn die LP des Goblins auf 1 fallen, zieht er sich mit voller Bewegung vom nächsten Helden zurück.

---

### 2. Goblin-Bogenschütze (Goblin Archer) — Fernkampf
*Schießt mit gezackten Knochenpfeilen aus dem Hinterhalt.*

| Eigenschaft | Wert |
|---|---|
| **Kategorie** | Standard (★☆☆) |
| **Lebenspunkte (LP)** | 2 |
| **Verteidigung (VT)** | 4 |
| **Bewegung** | 3 Felder |
| **Angriff** | 1d6 + 2 (Fernkampf, Reichweite 4) |
| **Schaden** | 1 |
| **Kopfgeld** | 1 Gold |

**Automatisches KI-Verhalten:**
1. **Abstand halten:** Steht ein Held direkt angrenzend, bewege dich 2 Felder weg (kein Gelegenheitsangriff) und schieße.
2. **Ziel:** Visiert den Helden mit den wenigsten LP in Sichtlinie an.
3. **Schuss:** Führe einen Fernkampfangriff aus.

---

### 3. Skelettkrieger (Skeleton Warrior) — Unbeugsamer Nahkämpfer
*Klappernde Gebeine mit rostigen Klingen, immun gegen Schmerz.*

| Eigenschaft | Wert |
|---|---|
| **Kategorie** | Standard (★★☆) |
| **Lebenspunkte (LP)** | 4 |
| **Verteidigung (VT)** | 6 |
| **Bewegung** | 3 Felder |
| **Angriff** | 1d6 + 2 (Nahkampf) |
| **Schaden** | 2 |
| **Kopfgeld** | 1 Gold |

**Sonderregel — Untot:** Immun gegen `Vergiftet` und `Brennend` (erleidet keinen Rundenstart-Schaden).  
**Automatisches KI-Verhalten:**
1. **Marsch:** Bewege dich auf kürzestem Weg auf den Helden mit der höchsten Rüstung zu (der Krieger sucht den stärksten Widerstand).
2. **Angriff:** Schlage mit dem Rostschwert zu (2 Schaden).
3. **Schildwall:** Wenn ein zweites Skelett angrenzt, erhalten beide +1 VT bis zur nächsten Runde.

---

### 4. Riesenspinne (Giant Spider) — Lauerjäger & Gift
*Lautlose Raubtiere in den staubigen Deckengewölben.*

| Eigenschaft | Wert |
|---|---|
| **Kategorie** | Standard (★★☆) |
| **Lebenspunkte (LP)** | 5 |
| **Verteidigung (VT)** | 5 |
| **Bewegung** | 4 Felder (klettert über Hindernisse) |
| **Angriff** | 1d6 + 2 (Nahkampf) |
| **Schaden** | 1 + Gift |
| **Kopfgeld** | 2 Gold |

**Sonderregel — Giftbiss:** Bei einem erfolgreichen Treffer muss der Held einen `ZÄH`-Wurf gegen SG 6 ablegen oder erhält den Zustand `Vergiftet` (-1 auf alle Würfe).  
**Automatisches KI-Verhalten:**
1. **Anspringen:** Bewege dich auf den Helden mit dem niedrigsten ZÄH-Wert zu (Magiegelehrte oder Goblin).
2. **Giftbiss:** Führe Nahkampfangriff aus.
3. **Netzwurf (einmalig bei Kampfbeginn):** Schleudert Netz auf bis zu 3 Felder – Ziel muss `GES (SG 6)` bestehen oder ist für 1 Runde `Verlangsamt` (halbe Bewegung).

---

### 5. Ödland-Worg (Wasteland Worg) — Schneller Flankierer
*Verwilderte Bestien aus dem Norden, getrieben von Blutdurst.*

| Eigenschaft | Wert |
|---|---|
| **Kategorie** | Elite (★★☆) |
| **Lebenspunkte (LP)** | 6 |
| **Verteidigung (VT)** | 5 |
| **Bewegung** | 5 Felder |
| **Angriff** | 1d6 + 3 (Nahkampf) |
| **Schaden** | 2 |
| **Kopfgeld** | 2 Gold |

**Sonderregel — Niederschlagen:** Bei einer gewürfelten 6 auf den Angriff wird der getroffene Held zu Boden geworfen (`Betäubt` / verliert nächsten Zug).  
**Automatisches KI-Verhalten:**
1. **Hinterhalt:** Umgeht den vordersten Tank, wenn möglich, und stürmt auf den hintersten Helden in Sichtlinie.
2. **Biss:** Greift mit 1d6 + 3 an.
3. **Rudeltrieb:** Wenn ein Verbündeter auf demselben Ziel steht: +1 Schaden.

---

### 6. Grabunhold / Gruftwächter (Crypt Guardian) — Mini-Boss
*Ein uralter, gepanzerter Hüne aus verfluchtem Erz und Moder.*

| Eigenschaft | Wert |
|---|---|
| **Kategorie** | Boss / Elite (★★★) |
| **Größe** | **Groß** — belegt **1 × 2 Felder** (siehe Regel unten) |
| **Lebenspunkte (LP)** | 14 |
| **Verteidigung (VT)** | 7 |
| **Bewegung** | 2 Felder |
| **Angriff** | 1d6 + 3 (Zweihand-Streitkolben) |
| **Schaden** | 3 |
| **Rüstung** | 1 (reduziert jeden erlittenen Schaden um 1) |
| **Kopfgeld** | 5 Gold + 1 garantierter Zug vom Ausrüstungsdeck |
| **Standee** | Breit: **60 × 45 mm** Plakette, Basis **60 × 20 mm** Schlitz (3 mm Sperrholz) |

**Sonderregeln:**
- **Zäh wie Granit:** Kann nicht betäubt oder weggestoßen werden.
- **Rundumschwung:** Einmal pro Runde, wenn 2 oder mehr Helden an ihn angrenzen, schlägt er im Kreis: Trifft alle angrenzenden Helden mit 2 Schaden!

**Automatisches KI-Verhalten:**
1. **Machtpräsenz:** Bewegt sich auf den Helden zu, der ihm in der letzten Runde den meisten Schaden zugefügt hat (oder auf den Berserker).
2. **Priorität Rundumschwung:** Wenn ≥ 2 Helden angrenzen, setzt er *Rundumschwung* ein.
3. **Zertrümmern:** Andernfalls führt er einen gezielten Keulenschlag (3 Schaden) gegen sein Primärziel aus.

---

### 7. Kultist des Schattens (Void Cultist) — Magie-Unterstützer
*Verblendete Fanatiker des Kaisertums, die dem Flüstern des Lich-Königs verfallen sind.*

| Eigenschaft | Wert |
|---|---|
| **Kategorie** | Standard (★☆☆) |
| **Lebenspunkte (LP)** | 3 |
| **Verteidigung (VT)** | 4 |
| **Bewegung** | 3 Felder |
| **Angriff** | 1d6 + 2 (Seelenschuss, Reichweite 3) |
| **Schaden** | 1 nekrotisch |
| **Kopfgeld** | 1 Gold |

**Sonderregel — Dunkles Ritual:** Angrenzende Untote erhalten +1 Schaden auf ihre Angriffe.  
**Automatisches KI-Verhalten:**
1. **Opferblut:** Wenn ein verbündeter Untoter in Sichtweite unter 2 LP fällt, heilt der Kultist diesen für 2 LP (und verliert selbst 1 LP).
2. **Abstand:** Weicht vor angrenzenden Helden zurück und visiert den nächsten Helden mit Seelenschuss an.
3. **Fluch:** Bei Volltreffer (6) erhält das Ziel den Zustand `Verlangsamt`.

---

### 8. Moor-Ghul (Carrion Ghoul) — Aasfresser & Krankheitsüberträger
*Verrottete, fiebrige Gestalten, die in den fauligen Gräbern des Moors hausen.*

| Eigenschaft | Wert |
|---|---|
| **Kategorie** | Standard (★★☆) |
| **Lebenspunkte (LP)** | 4 |
| **Verteidigung (VT)** | 5 |
| **Bewegung** | 5 Felder (sehr schnell) |
| **Angriff** | 1d6 + 2 (Zerfleischende Krallen) |
| **Schaden** | 1 + Seuche |
| **Kopfgeld** | 1 Gold |

**Sonderregel — Leichenfraß:** Steht der Ghul auf einem Feld eines besiegten Gegners oder Helden, regeneriert er am Rundenende **2 LP**.  
**Automatisches KI-Verhalten:**
1. **Blutgeruch:** Stürmt auf den Helden mit den wenigsten aktuellen LP zu.
2. **Zerfleischen:** Nahkampfangriff.
3. **Seuchenbiss:** Bei Erfolg muss der Held `ZÄH vs SG 6` bestehen oder wird `Vergiftet`.

---

### 9. Skelett-Scharfschütze (Bone Marksman) — Tödlicher Fernkämpfer
*Alte imperiale Schützen, deren Hände selbst im Tode nicht zittern.*

| Eigenschaft | Wert |
|---|---|
| **Kategorie** | Standard (★★☆) |
| **Lebenspunkte (LP)** | 3 |
| **Verteidigung (VT)** | 5 |
| **Bewegung** | 3 Felder |
| **Angriff** | 1d6 + 3 (Knochen-Langbogen, Reichweite 5) |
| **Schaden** | 2 |
| **Kopfgeld** | 2 Gold |

**Sonderregel — Geisterpfeil:** Ignoriert Deckung durch Säulen oder befreundete Figuren.  
**Automatisches KI-Verhalten:**
1. **Lauerstellung:** Bleibt nach Möglichkeit auf maximaler Distanz (5 Felder).
2. **Zielsucher:** Visiert ungeschützte Zauberer oder Waldläufer an (geringste Rüstung).
3. **Präzisionsschuss:** Greift mit 1d6 + 3 an.

---

### 10. Todesritter / Hügelfürst (Wight Champion) — Gepanzerte Elite
*Uralte Kriegsherren des Nordens, erweckt zu ewigem, hasserfülltem Dienst.*

| Eigenschaft | Wert |
|---|---|
| **Kategorie** | Elite (★★★) |
| **Lebenspunkte (LP)** | 8 |
| **Verteidigung (VT)** | 7 |
| **Rüstung** | 1 |
| **Bewegung** | 3 Felder |
| **Angriff** | 1d6 + 3 (Verfluchte Runenklinge) |
| **Schaden** | 2 |
| **Kopfgeld** | 3 Gold |

**Sonderregel — Grabeskälte:** Angrenzende Helden verlieren 1 Bewegung auf ihren Zug.  
**Automatisches KI-Verhalten:**
1. **Herausforderung:** Sucht gezielt den Nahkampf mit dem stärksten Krieger (Berserker / Kriegstänzerin).
2. **Runenschlag:** Nahkampfangriff mit 1d6 + 3. Bei Volltreffer (6) erleidet das Ziel zusätzlich 1 Erschöpfung!
3. **Schildblock:** 1× pro Runde pariert er den ersten erlittenen Treffer (-1 Schaden).

---

### 11. Der Blutgolem (Blood Golem) — Fleischgewordenes Nekromantie-Monstrum
*Eine gewaltige, pulsierende Monstrosität aus geronnenem Opferblut und gebrochenen Knochen.*

| Eigenschaft | Wert |
|---|---|
| **Kategorie** | Große Elite / Wächter (★★★) |
| **Größe** | **Groß** — belegt **1 × 2 Felder** (siehe Regel unten) |
| **Lebenspunkte (LP)** | 10 |
| **Verteidigung (VT)** | 6 |
| **Rüstung** | 0 (weiches, formloses Fleisch) |
| **Bewegung** | 3 Felder |
| **Angriff** | 1d6 + 3 (Blutfäuste / Tentakelkeule) |
| **Schaden** | 2 |
| **Kopfgeld** | 4 Gold |
| **Standee** | Breit: **60 × 45 mm** Plakette, Basis **60 × 20 mm** Schlitz (3 mm Sperrholz) |

**Sonderregel — Blutsauger (Vampirische Regeneration):** Jeder Schaden, den der Blutgolem an einem Helden verursacht, heilt ihn zeitgleich um genau diese Anzahl an Lebenspunkten!  
**Sonderregel — Unaufhaltsame Masse:** Kann nicht weggestoßen, betäubt oder verlangsamt werden.  
**Automatisches KI-Verhalten:**
1. **Blutdrang:** Zieht auf den Helden mit den meisten LP zu (um maximal viel Blut zu schöpfen).
2. **Zerschmettern:** Schlägt mit den Blutfäusten zu (2 Schaden, heilt sich selbst).
3. **Berstende Adern:** Fällt der Blutgolem auf 0 LP, explodiert er: Alle angrenzenden Figuren erleiden 2 Schaden (`GES vs SG 6` für halben Schaden).

---

### 12. Der Lich-König Malakor (The Lich-King) — KAMPAGNEN-ENDGEGNER
*Der uralte Herrscher des Nördlichen Ödlands, Beherrscher des Frosts und der Seelen.*

| Eigenschaft | Wert |
|---|---|
| **Kategorie** | Kampagnen-Boss (★★★★) |
| **Größe** | **Normal (1 × 1 Feld)** — schwebend, kein Breitenbonus; dafür **überhohe Standee-Silhouette** |
| **Lebenspunkte (LP)** | 18 |
| **Verteidigung (VT)** | 8 |
| **Rüstung** | 1 (Spektraler Schutzmantel) |
| **Bewegung** | 3 Felder (schwebend) |
| **Aktionen pro Runde** | **2 Aktionen** (aktiviert zweimal entlang der Initiative-Leiste!) |
| **Angriff 1** | 1d6 + 4 (Froststrahl des Todes, Reichweite 4, 3 Schaden) |
| **Angriff 2** | 1d6 + 3 (Seelenernter-Sense, Nahkampf, 3 Schaden + 1 Erschöpfung) |
| **Kopfgeld** | **Sieg über die Kampagne!** |
| **Standee** | Hoch: **30 × 80 mm** Plakette (deutlich überragt alle anderen Figuren), Basis **Ø 30 mm** Schlitz (3 mm Sperrholz) |

**Sonderregeln:**
- **Frosthauch-Aura:** Zu Rundenbeginn erleidet jeder Held im selben Raum 1 Frostschaden, es sei denn, er befindet sich in Deckung oder neben einer Feuerschale.
- **Totenbeschwörung (1× pro Runde):** Ruft mit einer Beschwörungs-Aktion **2 Skelettkrieger** aus dem gefrorenen Boden herbei!
- **Seelenkäfig:** Solange mindestens ein Skelett an Malakor angrenzt, kann ihm kein Nahkampfschaden zugefügt werden (Skelette werfen sich in den Hieb).

**Automatisches KI-Verhalten (2 Aktionen pro Runde):**
- **Aktion 1 (Fernkampf / Magie):** Wenn weniger als 2 Skelette im Raum sind $\rightarrow$ *Totenbeschwörung*. Andernfalls schleudert er einen *Froststrahl des Todes* auf den am weitesten entfernten Helden.
- **Aktion 2 (Vergeltung):** Greift mit der *Seelenernter-Sense* das Ziel mit den niedrigsten aktuellen LP an.

