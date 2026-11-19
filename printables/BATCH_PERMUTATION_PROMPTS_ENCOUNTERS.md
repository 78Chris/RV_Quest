# Midjourney Prompts: Begegnungskarten (Scenic & Atmospheric Dungeon)

> **Quelle:** `RV_Quest/components/encounter_cards.md` (Karten B01 bis B16)  
> **Kartenformat:** Mini-Euro (44 × 68 mm)  
> **Stil-Konsistenz:** Handkolorierter Holzschnitt (*Albrecht-Dürer-Engraving*) exakt im visuellen Stil der Farb-Monster (`MasterArtwork/Monsters/Color`), aber eingebettet in lebendige, stimmungsvolle Dungeon-Szenen (Gewölbegänge, Krypten, Säulen, Fackelschein).  
> **Anti-Glitches:**  
> - **Klare Trennung:** Menschen (Helden, Gefangene) werden explizit mit Rasse, Kleidung und Helm/Gesicht beschrieben.  
> - **Geringeres `--sw` (`--sw 90` statt 200):** Überträgt Farbpalette und Strichstärke, verhindert aber mutierte Monstergesichter auf menschlichen Figuren.  
> - **Konsistentes Stilisieren (`--s 60`):** Hält Midjourney nah am Motiv ohne kitschige 3D-Shader.  
> - **Gezielte Negativ-Prompts (`--no ...`):** Schließen unerwünschte Bildfehler, Mutationen und fehlende Raumelemente aus.

---

## 🎴 TEIL 1: Einzel-Prompts (Single Prompts)

### 👺 Gruppe A: Goblins & Plünderer

#### B01. Banden-Vorposten (Goblin Outpost)
```text
/imagine prompt: A dynamic dungeon encounter scene inside a torchlit stone dungeon room, in the foreground two snarling green-skinned goblin scouts crouching low behind a battered wooden crate barricade brandishing jagged shortswords, in the background a goblin archer drawing a notched bone arrow tight on a curved shortbow, mossy cobblestones, dramatic firelight on stone arches, bold thick clean black outlines, hand-colored woodcut illustration, flat vibrant comic cell shading, clean flat color fills, vintage retro fantasy palette, atmospheric dark medieval fantasy dungeon background, cinematic dungeon lighting, dynamic action composition, borderless, no frame, no text --ar 1:1 --sref https://s.mj.run/m5Zt1Ar1RQA https://s.mj.run/TIDIa4U9vJg --sw 90 --s 60 --c 15 --v 6.1 --no modern, photo, 3d render, extra limbs, human faces on goblins
```

#### B02. Hinterhalt aus den Schatten! (Goblin Ambush)
```text
/imagine prompt: A dynamic dungeon encounter scene in a dark gothic corridor, in the foreground the metal greave and boot of a heroic human knight tripping a taut mechanical wire trap triggering clattering skull chimes, while three vicious leaping green-skinned goblins erupt forward from shadowy stone archways with raised gleaming daggers, frantic action, bold thick clean black outlines, hand-colored woodcut illustration, flat vibrant comic cell shading, clean flat color fills, vintage retro fantasy palette, atmospheric dark medieval fantasy dungeon background, cinematic dungeon lighting, dynamic action composition, borderless, no frame, no text --ar 1:1 --sref https://s.mj.run/m5Zt1Ar1RQA https://s.mj.run/TIDIa4U9vJg --sw 90 --s 60 --c 15 --v 6.1 --no green skin on knight, monster knight, deformed faces, modern, photo, 3d render
```

#### B03. Plünderer-Nest (Scavenger Nest)
```text
/imagine prompt: A dynamic dungeon encounter scene inside a damp mossy stone cellar, three startled scavenger goblins with pointed ears and green skin caught red-handed rummaging frantically through an open iron-banded wooden treasure chest overflowing with gold coins, whirling around toward the viewer with panicked hisses and raised rusty iron cleavers, bold thick clean black outlines, hand-colored woodcut illustration, flat vibrant comic cell shading, clean flat color fills, vintage retro fantasy palette, atmospheric dark medieval fantasy dungeon background, cinematic dungeon lighting, dynamic action composition, borderless, no frame, no text --ar 1:1 --sref https://s.mj.run/m5Zt1Ar1RQA https://s.mj.run/TIDIa4U9vJg --sw 90 --s 60 --c 15 --v 6.1 --no modern, photo, 3d render, human face
```

#### B04. Wachposten mit Bluthund (Watchpost with Beast)
```text
/imagine prompt: A dynamic dungeon encounter scene inside a cavernous underground ruin, a massive ferocious wasteland worg beast with rough grey fur straining violently against an iron chain snarling with dripping white fangs beside a crackling campfire, as a cruel green-skinned goblin handler holding a wooden torch releases the spiked collar, bold thick clean black outlines, hand-colored woodcut illustration, flat vibrant comic cell shading, clean flat color fills, vintage retro fantasy palette, atmospheric dark medieval fantasy dungeon background, cinematic dungeon lighting, dynamic action composition, borderless, no frame, no text --ar 1:1 --sref https://s.mj.run/m5Zt1Ar1RQA https://s.mj.run/TIDIa4U9vJg --sw 90 --s 60 --c 15 --v 6.1 --no modern, photo, 3d render, extra heads, cute dog
```

---

### 💀 Gruppe B: Untote & Nekromantie

#### B05. Ruhelose Wache (Restless Sentinel Guard)
```text
/imagine prompt: A dynamic dungeon encounter scene inside an ancient gothic burial vault, two armored skeleton sentinels with bleached bones and rusty iron helmets locking their weathered wooden shields together into a tight defensive shield wall, bronze spearheads thrusting forward menacingly in formation, torches flickering on stone tombs, bold thick clean black outlines, hand-colored woodcut illustration, flat vibrant comic cell shading, clean flat color fills, vintage retro fantasy palette, atmospheric dark medieval fantasy dungeon background, cinematic dungeon lighting, dynamic action composition, borderless, no frame, no text --ar 1:1 --sref https://s.mj.run/m5Zt1Ar1RQA https://s.mj.run/TIDIa4U9vJg --sw 90 --s 60 --c 15 --v 6.1 --no flesh, skin, living humans, modern, photo, 3d render
```

#### B06. Erwachen der Ahnen (Awakening Ancestors)
```text
/imagine prompt: A dynamic dungeon encounter scene in an ancient stone crypt, a dark jagged open trench in the cracked floor stones from which three decrepit skeleton warriors are clawing their way upward, bony hands gripping rusty iron broadswords, ethereal pale blue ghost flame burning in their hollow eye sockets, dust rising, bold thick clean black outlines, hand-colored woodcut illustration, flat vibrant comic cell shading, clean flat color fills, vintage retro fantasy palette, atmospheric dark medieval fantasy dungeon background, cinematic dungeon lighting, dynamic action composition, borderless, no frame, no text --ar 1:1 --sref https://s.mj.run/m5Zt1Ar1RQA https://s.mj.run/TIDIa4U9vJg --sw 90 --s 60 --c 15 --v 6.1 --no flesh, skin, living humans, modern, photo, 3d render
```

#### B07. Die Gruft der Bogenschützen (Crypt of the Bone Archers)
```text
/imagine prompt: A dynamic dungeon encounter scene inside a shadowy ruined subterranean catacomb, two skeletal bone archers leaning out from behind massive gothic stone pillars loosing bone-tipped arrows from ancient recurve bows, in front an armored skeleton warrior advancing with a notched broadsword and shield, bold thick clean black outlines, hand-colored woodcut illustration, flat vibrant comic cell shading, clean flat color fills, vintage retro fantasy palette, atmospheric dark medieval fantasy dungeon background, cinematic dungeon lighting, dynamic action composition, borderless, no frame, no text --ar 1:1 --sref https://s.mj.run/m5Zt1Ar1RQA https://s.mj.run/TIDIa4U9vJg --sw 90 --s 60 --c 15 --v 6.1 --no flesh, skin, living humans, modern, photo, 3d render
```

#### B08. Schändlicher Schrein (Defiled Altar)
```text
/imagine prompt: A dynamic dungeon encounter scene inside a gloomy underground sanctum, an ornate dark basalt necromancy altar radiating swirling tendrils of vibrant purple magical smoke and dark runes, while two kneeling skeletal warriors in cracked armor absorb the necromantic energy as their bone fissures knit closed, bold thick clean black outlines, hand-colored woodcut illustration, flat vibrant comic cell shading, clean flat color fills, vintage retro fantasy palette, atmospheric dark medieval fantasy dungeon background, cinematic dungeon lighting, dynamic action composition, borderless, no frame, no text --ar 1:1 --sref https://s.mj.run/m5Zt1Ar1RQA https://s.mj.run/TIDIa4U9vJg --sw 90 --s 60 --c 15 --v 6.1 --no modern, photo, 3d render, living humans
```

#### B09. Grabkammer-Hinterhalt! (Crypt Sarcophagus Ambush)
```text
/imagine prompt: A dynamic dungeon encounter scene inside an ancient burial chamber, a massive carved stone sarcophagus lid violently shattering outward in stone shards and dust as a towering ancient crowned skeletal warrior king brandishing a glowing grave-sword bursts forward, alongside a snarling rabid wasteland beast leaping from the shadows, bold thick clean black outlines, hand-colored woodcut illustration, flat vibrant comic cell shading, clean flat color fills, vintage retro fantasy palette, atmospheric dark medieval fantasy dungeon background, cinematic dungeon lighting, dynamic action composition, borderless, no frame, no text --ar 1:1 --sref https://s.mj.run/m5Zt1Ar1RQA https://s.mj.run/TIDIa4U9vJg --sw 90 --s 60 --c 15 --v 6.1 --no modern, photo, 3d render, living humans
```

---

### 🕷️ Gruppe C: Bestien & Ungeziefer

#### B10. Spinnennest (Spider Nest)
```text
/imagine prompt: A dynamic dungeon encounter scene inside a cavernous stone vault completely draped in thick white spiderwebs and suspended egg sacs, a colossal hairy black giant spider rearing up on hind legs spraying thick sticky white web strands forward, acidic lime-green venom dripping from sharp fangs, multiple glowing red eyes, bold thick clean black outlines, hand-colored woodcut illustration, flat vibrant comic cell shading, clean flat color fills, vintage retro fantasy palette, atmospheric dark medieval fantasy dungeon background, cinematic dungeon lighting, dynamic action composition, borderless, no frame, no text --ar 1:1 --sref https://s.mj.run/m5Zt1Ar1RQA https://s.mj.run/TIDIa4U9vJg --sw 90 --s 60 --c 15 --v 6.1 --no human faces on spider, cute spider, modern, photo, 3d render
```

#### B11. Lauernde Brut (Lurking Brood)
```text
/imagine prompt: A dynamic dungeon encounter scene in a mossy archway, two sneering green-skinned goblin skirmishers with daggers taunting and gesturing forward, while directly above them in the shadows of the vaulted stone ceiling a colossal striped giant spider silently descends head-first on a thick silk thread, fangs spread, bold thick clean black outlines, hand-colored woodcut illustration, flat vibrant comic cell shading, clean flat color fills, vintage retro fantasy palette, atmospheric dark medieval fantasy dungeon background, cinematic dungeon lighting, dynamic action composition, borderless, no frame, no text --ar 1:1 --sref https://s.mj.run/m5Zt1Ar1RQA https://s.mj.run/TIDIa4U9vJg --sw 90 --s 60 --c 15 --v 6.1 --no modern, photo, 3d render, cute spider
```

#### B12. Worg-Bau (Worg Den)
```text
/imagine prompt: A dynamic dungeon encounter scene inside a subterranean cave den littered with gnawed bones, two ferocious starving wasteland worgs with scruffy grey fur and glowing amber eyes charging at full sprint directly toward the viewer, bared fangs dripping saliva, predatory snarling postures, bold thick clean black outlines, hand-colored woodcut illustration, flat vibrant comic cell shading, clean flat color fills, vintage retro fantasy palette, atmospheric dark medieval fantasy dungeon background, cinematic dungeon lighting, dynamic action composition, borderless, no frame, no text --ar 1:1 --sref https://s.mj.run/m5Zt1Ar1RQA https://s.mj.run/TIDIa4U9vJg --sw 90 --s 60 --c 15 --v 6.1 --no cute dog, puppy, modern, photo, 3d render
```

#### B13. Krabbelndes Grauen (Creeping Horror)
```text
/imagine prompt: A dynamic dungeon encounter scene in a gothic stone corridor, a terrifying monstrous hairy giant spider dropping legs-first through a jagged breach in the ceiling masonry, landing right above an armored skeleton warrior standing guard with a broadsword on the flagstones below, web strands trailing, bold thick clean black outlines, hand-colored woodcut illustration, flat vibrant comic cell shading, clean flat color fills, vintage retro fantasy palette, atmospheric dark medieval fantasy dungeon background, cinematic dungeon lighting, dynamic action composition, borderless, no frame, no text --ar 1:1 --sref https://s.mj.run/m5Zt1Ar1RQA https://s.mj.run/TIDIa4U9vJg --sw 90 --s 60 --c 15 --v 6.1 --no modern, photo, 3d render, human face
```

---

### 🏛️ Gruppe D: Besondere Ereignis-Räume

#### B14. Verlassene Schatzkammer (Abandoned Vault)
```text
/imagine prompt: A dynamic dungeon tension scene inside a quiet vaulted chamber, a handsome human rogue in leather gloves cautiously prying open the heavy iron lid of an antique treasure chest, as a lethal spring-loaded golden poison needle trap snaps out with flying mechanical cogs and green venom mist, dramatic torchlight, bold thick clean black outlines, hand-colored woodcut illustration, flat vibrant comic cell shading, clean flat color fills, vintage retro fantasy palette, atmospheric dark medieval fantasy dungeon background, cinematic dungeon lighting, dynamic action composition, borderless, no frame, no text --ar 1:1 --sref https://s.mj.run/m5Zt1Ar1RQA https://s.mj.run/TIDIa4U9vJg --sw 90 --s 60 --c 15 --v 6.1 --no monster rogue, green skin on human, goblin face, modern, photo, 3d render
```

#### B15. Heilige Quelle / Alchemisten-Ruine (Holy Font Ruin)
```text
/imagine prompt: A dynamic dungeon scene inside an abandoned underground temple sanctuary, an ancient stone font basin glowing with bright luminous cyan-blue holy water and sparkling mist, while an armored skeleton sentinel in tattered heraldic tabard steps forward raising a rusty halberd to guard the pool, bold thick clean black outlines, hand-colored woodcut illustration, flat vibrant comic cell shading, clean flat color fills, vintage retro fantasy palette, atmospheric dark medieval fantasy dungeon background, cinematic dungeon lighting, dynamic action composition, borderless, no frame, no text --ar 1:1 --sref https://s.mj.run/m5Zt1Ar1RQA https://s.mj.run/TIDIa4U9vJg --sw 90 --s 60 --c 15 --v 6.1 --no modern, photo, 3d render, living humans
```

#### B16. Der Kerker der Gefangenen (Dungeon Cells)
```text
/imagine prompt: A dynamic dungeon narrative scene in a damp subterranean cell corridor, two ugly green-skinned goblin guards jeering and banging spiked wooden cudgels against heavy iron dungeon cell bars, behind the rusty bars a frightened human merchant in a merchant vest reaching desperate open hands through the grate pleading for rescue, bold thick clean black outlines, hand-colored woodcut illustration, flat vibrant comic cell shading, clean flat color fills, vintage retro fantasy palette, atmospheric dark medieval fantasy dungeon background, cinematic dungeon lighting, dynamic action composition, borderless, no frame, no text --ar 1:1 --sref https://s.mj.run/m5Zt1Ar1RQA https://s.mj.run/TIDIa4U9vJg --sw 90 --s 60 --c 15 --v 6.1 --no monster prisoner, green skin on human prisoner, modern, photo, 3d render
```

---

## ⚡ TEIL 2: Batch- & Permutations-Prompts (Discord & Web)

### 👺 Batch 1: Goblins & Plünderer (B01 bis B04)
```text
/imagine prompt: A dynamic dungeon encounter scene {two snarling green-skinned goblin scouts crouching low behind a battered wooden crate barricade inside a torchlit stone dungeon room brandishing jagged shortswords while a goblin archer draws an arrow tight on his shortbow in the background, armored metal boot of a heroic human knight tripping a taut mechanical wire trap triggering clattering skull chimes as three vicious leaping green-skinned goblins lunge forward from shadow archways with gleaming daggers, three startled green-skinned scavenger goblins caught red-handed rummaging frantically through an open iron-banded loot chest inside a damp mossy dungeon cellar whirling around with panicked hisses and raised rusty cleavers, massive ferocious wasteland worg beast straining violently against an iron chain snarling with dripping white fangs beside a smoky campfire inside a cavernous stone ruin as a green-skinned goblin handler releases the spiked collar}, bold thick clean black outlines, hand-colored woodcut illustration, flat vibrant comic cell shading, clean flat color fills, vintage retro fantasy palette, atmospheric dark medieval fantasy dungeon background, cinematic dungeon lighting, dynamic action composition, borderless, no frame, no text --ar 1:1 --sref https://s.mj.run/m5Zt1Ar1RQA https://s.mj.run/TIDIa4U9vJg --sw 90 --s 60 --c 15 --v 6.1 --no monster knight, green skin on human, deformed faces, modern, photo, 3d render
```

### 💀 Batch 2: Untote & Nekromantie (B05 bis B09)
```text
/imagine prompt: A dynamic dungeon encounter scene {two armored skeleton sentinels with bleached bones and iron helmets locking weathered wooden shields together into a solid defensive shield wall with bronze spears thrusting forward in disciplined formation inside an ancient gothic burial vault, three decrepit skeleton warriors clawing their way out of a dark cracked earth trench in an ancient stone crypt floor grabbing old rusted swords with ethereal pale blue flames igniting in their hollow eye sockets, two skeletal bone archers leaning out from behind massive gothic stone pillars of an abandoned catacomb loosing bone-tipped arrows while an armored skeleton vanguard advances with broadsword, ornate dark basalt necromancy altar in a shadowy crypt radiating ethereal purple smoke coils that magically knit together the cracked bones of two kneeling skeletal champions, massive carved stone sarcophagus lid violently exploding outward in stone shards inside a dark subterranean tomb as an ancient crowned skeletal king brandishing a glowing grave-sword bursts forth while a rabid beast lunges alongside}, bold thick clean black outlines, hand-colored woodcut illustration, flat vibrant comic cell shading, clean flat color fills, vintage retro fantasy palette, atmospheric dark medieval fantasy dungeon background, cinematic dungeon lighting, dynamic action composition, borderless, no frame, no text --ar 1:1 --sref https://s.mj.run/m5Zt1Ar1RQA https://s.mj.run/TIDIa4U9vJg --sw 90 --s 60 --c 15 --v 6.1 --no flesh, skin, living humans, modern, photo, 3d render
```

### 🕷️ Batch 3: Bestien & Ungeziefer (B10 bis B13)
```text
/imagine prompt: A dynamic dungeon encounter scene {colossal hairy black giant spider in an ancient dungeon vault draped in webs rearing up and spraying thick sticky pale web strands forcefully forward as acidic emerald venom drips from its mandibles, two sneering green-skinned goblin skirmishers taunting the viewer in a mossy archway while a colossal striped giant spider descends silently on silk threads directly behind them, two ferocious starving wasteland worgs charging at full sprint through a bone-littered subterranean cave den with bared dripping fangs bristling scruffy fur and predatory glowing yellow eyes, terrifying giant spider dropping violently legs-first through a jagged ceiling fissure of a crumbling stone hall while an armored skeleton warrior blocks the corridor with a notched broadsword}, bold thick clean black outlines, hand-colored woodcut illustration, flat vibrant comic cell shading, clean flat color fills, vintage retro fantasy palette, atmospheric dark medieval fantasy dungeon background, cinematic dungeon lighting, dynamic action composition, borderless, no frame, no text --ar 1:1 --sref https://s.mj.run/m5Zt1Ar1RQA https://s.mj.run/TIDIa4U9vJg --sw 90 --s 60 --c 15 --v 6.1 --no human faces on monsters, cute animals, modern, photo, 3d render
```

### 🏛️ Batch 4: Besondere Ereignis-Räume (B14 bis B16)
```text
/imagine prompt: A dynamic dungeon scene {handsome human rogue in leather gloves cautiously prying open the heavy iron lid of an antique treasure chest inside a mysterious vaulted chamber as a lethal spring-loaded golden poison trap needle snaps out toward his fingers with flying cogs, armored skeleton sentinel stepping protectively in front of an ancient stone font basin glowing with bright luminous cyan-blue holy water inside an abandoned underground temple ruin raising a rusty halberd to forbid passage, two ugly green-skinned goblin guards jeering and banging spiked wooden cudgels against rusty dungeon cell bars in a damp underground prison while a frightened human merchant reaches desperate hands through the iron grate}, bold thick clean black outlines, hand-colored woodcut illustration, flat vibrant comic cell shading, clean flat color fills, vintage retro fantasy palette, atmospheric dark medieval fantasy dungeon background, cinematic dungeon lighting, dynamic action composition, borderless, no frame, no text --ar 1:1 --sref https://s.mj.run/m5Zt1Ar1RQA https://s.mj.run/TIDIa4U9vJg --sw 90 --s 60 --c 15 --v 6.1 --no monster human, green skin on human, goblin face on merchant, modern, photo, 3d render
```
