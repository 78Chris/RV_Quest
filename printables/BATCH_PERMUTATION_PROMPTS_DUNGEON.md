# Midjourney Permutation & Batch Prompts: Dungeon Battlemaps & Assets

> **Verwendung:** Kopiere jeden `/imagine`-Befehl als Ganzes in Discord.  
> Midjourney erkennt die `{..., ...}`-Permutationen automatisch, fragt nach Bestätigung (`Are you sure?`) und reiht alle Prompts nacheinander in deine Standard-Queue ein.
>
> **Neuer, erprobter Standard für Battlemap-Böden (Batch 1):**  
> - **Top-down 2D orthographic RPG battlemap (90° bird-eye view):** Garantiert strikt senkrechte Draufsicht ohne Fluchtpunkte oder Schrägen.
> - **Edge to edge filling:** Füllt die gesamte Fläche vollflächig ohne weiße Ränder oder Löcher.
> - **Kein `--sref`:** Verhindert, dass Ausrüstungs-Freisteller oder weiße Schnittmuster in die Bodentextur gemischt werden.
> - **Kein `--tile`:** Verhindert Tapeten-Ornamente und Verjüngungen.
> - **Seitenverhältnis `--ar 1:1`:** Quadratisches Kachel-Format (180 × 180 mm für 6×6 Felder à 30 mm, mit 15 mm Rand passend für A4-Seiten), flexibel drehbar und kombinierbar.

---

## 🪨 Batch 1: Alle 5 Szenario-Bodengrafiken (Battlemap Base Boards)
*Alle 5 Szenario-Hintergründe in 1 Befehl – quadratisch 1:1, vollflächig, 2D Top-Down, perfekt für 30×30 mm Gitter-Overlay:*
1. **Sz. 01 Krypta:** Dunkle Schiefer-Flagstones, flache Steinplatten, Chisel-Textur
2. **Sz. 02 Nebelmoor:** Feuchter Torfboden, dunkler Schlamm, flache stehende Wasserlachen
3. **Sz. 03 Zisternen:** Nasses Kanalisations-Klinkerpflaster mit Algenfilm und dunklem Petrol/Giftgrün
4. **Sz. 04 Zitadelle:** Massives Festungspflaster, Granitplatten mit feinen Ruß- und Brandspuren
5. **Sz. 05 Frost-Nekropole:** Pechschwarzer Obsidian-Boden mit zartem blauem Eisstaub und Frostadern

```text
/imagine prompt: Top-down 2D orthographic tabletop RPG battlemap of {an ancient crypt stone floor with flat weathered slate-grey flagstones and ancient chisel texture, a dark misty swamp marsh ground with damp brown peat bog soil wet mud patches and flat shallow stagnant water puddles, an underground sewer waterway floor with damp weathered brick pavers moss glaze and calm dark murky teal-green water pooling, a fortified citadel stone courtyard ground with heavy square granite paving slabs and dark scorched burn marks, a frozen necropolis hall floor with smooth flat polished black obsidian tiles covered by a delicate layer of frosty blue ice dusting and faint frost veins}, bird-eye view looking straight down 90 degrees, filling the entire frame edge to edge, medieval woodcut engraving style, Albrecht Dürer hand-colored print aesthetic, clean muted flat colors, atmospheric tabletop gaming surface --ar 1:1 --v 6.1 --no perspective, angle, 3d, tilt, side view, wall, white background, cutout, border, frame, furniture, tokens, people, trees, horizon, sky
```

---

## 🏛️ Batch 2: Alle 1×1 Quadratischen Dungeon-Tokens (Möbel & Deckung)
*7 freigestellte Objekte auf reinweißem Hintergrund (30×30 mm auf der Karte)*

```text
/imagine prompt: A single isolated top-down battlemap token of {a medieval reinforced wooden treasure chest iron bands and heavy brass padlock, a massive round ancient stone pillar carved dungeon column with weathered cracks and rune engravings, a jagged glacial ice pillar spike crystalline sharp translucent frost column, a heavy medieval defensive wooden barricade sharpened timber stakes bound with thick ropes, an iron-banded wooden barrel oozing dark flammable tar and burning pitch with vivid orange-yellow flames and sparks, an ornate bronze standing brazier tripod with roaring bright golden flames and glowing coals, a deep pit trap with sharp forged iron and bone spikes pointing upward}, bold clean black woodcut lineart, hatched engraving shading, hand-colored woodcut print, Albrecht Dürer vintage medieval engraving style, clean vibrant flat color fills, pure solid white background, clean cutout silhouette, no shadows on background --ar 1:1 --sref https://i.imgur.com/VzU1WIk.png https://i.imgur.com/m6GMSd5.png https://i.imgur.com/juHvFJo.png --sw 100 --c 20 --v 6.1 --no perspective, side view, 3d isometric, floor, ground, wall
```

---

## 🏛️ Batch 3: Alle 1×2 Rechteckigen Dungeon-Tokens (Große Möbel & Altäre)
*4 freigestellte Objekte auf reinweißem Hintergrund (60×30 mm auf der Karte)*

```text
/imagine prompt: A single isolated top-down battlemap token of {an ancient weathered stone sarcophagus sculpted knight effigy on lid chipped dark granite with gold inlays, an alchemist workbench cluttered with glass retorts dusty grimoires colorful bubbling phials and mortar, a sinister sacrificial blood altar black stone carved with glowing occult runes dried crimson blood stains, an imposing Gothic throne of the lich king carved from blackened bones and polished obsidian frost-encrusted seat}, bold clean black woodcut lineart, hatched engraving shading, hand-colored woodcut print, Albrecht Dürer vintage medieval engraving style, clean vibrant flat color fills, pure solid white background, clean cutout silhouette, no shadows on background --ar 2:1 --sref https://i.imgur.com/VzU1WIk.png https://i.imgur.com/m6GMSd5.png https://i.imgur.com/juHvFJo.png --sw 100 --c 20 --v 6.1 --no perspective, side view, 3d isometric, floor, ground, wall
```
