# RV Quest — Project Plan

> Tracks phases and tasks. Update status as we go.  
> Status: ✅ Done | 🔄 In Progress | ⬜ Not Started | 🔒 Blocked

---

## 🗺️ Development Phases

The game is built **inside-out**: core mechanics first, then content, then production.  
Each phase should produce a playable or testable artifact before moving on.

---

### Phase 0 — Foundation ✅ Done
*Establish the project structure and constraints.*

- [x] Define constraints (d6 only, max 5 attributes, 2-player, printer+laser cutter)
- [x] Create folder structure
- [x] Create living context document (PROJECT_CONTEXT.md)
- [x] Create project plan (PLAN.md)

---

### Phase 1 — Core Rules ✅ Done
*The engine everything else runs on.*

- [x] Setting & Tone — world name, flavour, genre feel
- [x] Core Dice Mechanic — d6 only, 1d6 + attribute vs SG, advantage/disadvantage (2d6)
- [x] The 5 Attributes — KRA, GES, ZÄH, VER, LIS
- [x] Turn Structure — 4-phase rounds (Initiative, Hero turns, Monster turns, End of Round)
- [x] Action Economy — Movement (3-4 tiles) + 1 Action
- [x] Success / Failure — SG scale (4/6/8/10), Volltreffer on 6, no patzer
- [x] Conditions / Status Effects — baseline table (burning, poisoned, stunned, slowed, hidden) in `rules/core_rules.md`
- [ ] **To Do:** Create dedicated `rules/conditions.md` detailing comprehensive status effect rules, tabletop handling (prone standee placement for Betäubt), saving throws, and item/immunity interactions.

📄 Output: `rules/core_rules.md`

---

### Phase 2 — Combat System ✅ Done
*Derived from core rules.*

- [x] Attack resolution (1d6 + KRA/GES vs. target VT)
- [x] Defense / damage reduction (armour & shields)
- [x] Death / knock-out (0 LP unconscious, 1 action partner revive)
- [x] Equipment deck & item limits (36 loot cards, carry slots, starting cards)
- [x] Special abilities in combat (Berserker rage, Kriegstanz, Meucheln)

📄 Output: `rules/combat.md`, `components/card_list.md`

---

### Phase 3 — Characters ✅ Done
*Hero starter kits and arcane systems.*

- [x] 4 Hero archetypes defined with 5 attributes & lore
- [x] 12 Starting Equipment cards (3 per hero)
- [x] Magiegelehrte spell deck (6 spells + 5-box fatigue track)
- [x] Goblinzauber 1d6 chaotic drunk magic table

📄 Output: `characters/character_roster.md`, `characters/starter_cards_and_spells.md`

---

### Phase 4 — Monsters & Balance Testing ✅ Done
*Adversaries, automated AI, and Monte-Carlo validation.*

- [x] 12 Core monster profiles with VT, LP, and damage (`monsters/monster_roster.md`)
- [x] 3-step priority automated AI for solo/co-op play
- [x] Mini-boss & Boss mechanics (Grabunhold, Todesritter, Malakor)
- [x] **Monte-Carlo Combat Balance:** 10,000 automated runs verified (`balance_simulator.py`) — 100% tutorial win rate, zero instant-kills, balanced attrition.
- [x] **Micro-Testing Suite:** 5 rapid 5–10 min modular test drills defined.

📄 Output: `monsters/monster_roster.md`, `balance_simulator.py`

---

### Phase 5 — Adventures & Scenarios ✅ Done
- [x] Scenario 01: "Die verfluchte Krypta von Dun-Karr" (tutorial, 4 rooms, boss, rewards)
- [x] Scenario 02: "Hinterhalt im Nebelmoor" (tactical wilderness & swamp retreat)
- [x] Scenario 03: "Die versunkene Zisterne von Valdor" (underground canal, floodgate levers, cultist ritual)
- [x] Scenario 04: "Die belagerte Felsen-Zitadelle" (fortress defense, barricades, portcullis, Blood Golem & Wight Champion)
- [x] Scenario 05: "Das Totenreich des Lich-Königs" (grand campaign finale, Malakor boss, frost aura, braziers, soul cages & epilogue)
- [x] 5-Scenario Campaign Guide (`adventures/campaign_guide.md`) — Intermission, Schattenbazar, injuries & scoring


---

### Phase 5 — Exploration & The Map ✅ Done
*How scenarios are physically laid out and explored.*

- [x] Map tile system → **replaced by wire-bound A4 Game Book** *(Session 7 — 2026-11-04)*
- [x] Room / corridor rules & Line of Sight (LoS)
- [x] Doors (picking locks vs. kicking doors), traps, and secret passages
- [x] Treasure, chests, and sarcophagus loot mechanics
- [x] Fog of war & dynamic encounter cards per room
- [x] Room-based Initiative with physical wooden tracker track & tokens

📄 Output: `rules/exploration.md`

---

### Phase 6 — Adventure / Scenario Design ✅ Done
*How to structure dynamic, replayable scenarios.*

- [x] Scenario template & design guide (`adventures/adventure_guide.md`)
- [x] 16-Card dynamic encounter deck system (`components/encounter_cards.md`)
- [x] Dynamic door-token pool integration (Axt, Schlüssel, Rune, Auge, Offen)
- [x] Scenario 01: "Die verfluchte Krypta von Dun-Karr"
- [x] Scenario 02: "Hinterhalt im Nebelmoor"
- [x] Scenario 03: "Die versunkene Zisterne von Valdor"

📄 Output: `adventures/adventure_guide.md`, `components/encounter_cards.md`

---

### Phase 7 — Lore & World
*Can happen in parallel with any other phase.*

1. ⬜ World name and overview
2. ⬜ Key factions / powers
3. ⬜ Bestiary flavour text
4. ⬜ Scenario lore hooks

📄 Output: `lore/world.md` + `lore/bestiary_lore.md`

---

### Phase 8 — Components & Production
*Final phase — design everything for printing and cutting.*

> **Format Decision (Session 7):** Game Book (wire-bound A4). Print pipeline: Word/LibreOffice `.docx`.

1. ⬜ Component list (standees, tokens, card decks, storage box — tiles removed)
2. ⬜ Card templates (character, monster, item, event) → `.docx` layout
3. ⬜ Laser cut files (standees, bases, tokens, box insert)
4. ⬜ **Scenario Book layout** — A4 `.docx` with left-page instructions + right-page 30mm grid battle map (1 file per scenario, or combined master book)
5. ⬜ Scenario Book print test (Scenario 01, 2-page spread)

📄 Output: `components/component_list.md` + `printables/`

---

## 🎯 Suggested Discussion Order

```
Tone & Setting → Core Mechanic → Attributes → Turn Structure
    → Combat → Characters → Monsters → Exploration
        → Adventure Design → Lore → Production
```

> Start with **Phase 1 — Core Rules** in the next session.  
> First question to tackle: **What is the core d6 mechanic?**

---
