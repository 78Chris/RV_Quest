# RV Quest — Project Context & Session Log

> **Purpose:** This is the living document that tracks all key decisions, open questions, and progress across sessions.  
> When resuming, read this file first to get full context.

### Session 8 — 2026-11-04 (Campaign Monte Carlo Balancing & Dynamic Victory Tiers)
- **Multi-Scenario Simulator Built & Run (`balance_simulator_campaign.py`):**
  - Extended previous Scenario 01 simulator into a full 5-scenario Monte Carlo testing suite (50,000 runs total).
  - Modeled Encounter Deck draws, Door-Tokens, boss opening strikes, Predator Initiative (worgs/ghouls act first in round 1), and fatigue/rest mechanics.
- **Balancing Insights & Rule Formalization:**
  - *Scenario 01 (Tutorial):* Confirmed rock-solid at **99.7%** win rate.
  - *Aktionsökonomie Insight:* 4 heroes (5 attacks/round) naturally overpower standard minion counts unless attrition is preserved.
  - *Victory/Retreat Rule Adopted in `campaign_guide.md`:*
    - **Heroischer Sieg:** Main objective completed AND at most 1 hero K.O. (heroes make it home victorious with full bounty).
    - **Verwundeter Rückzug:** 2+ heroes K.O. forces an emergency evacuation; scenario must be retreated/re-attempted, triggering injury scar checks.
    - **Totalverlust:** All 4 heroes incapacitated (party loses loot, pays fee to be rescued).

---

## 🎮 Project Overview

| Field | Value |
|### Session 8 — 2026-11-04 (Campaign Monte Carlo Balancing & Dynamic Victory Tiers)
- **Multi-Scenario Simulator Built & Run (`balance_simulator_campaign.py`):**
  - Extended previous Scenario 01 simulator into a full 5-scenario Monte Carlo testing suite (50,000 runs total).
  - Modeled Encounter Deck draws, Door-Tokens, boss opening strikes, Predator Initiative (worgs/ghouls act first in round 1), and fatigue/rest mechanics.
- **Balancing Insights & Rule Formalization:**
  - *Scenario 01 (Tutorial):* Confirmed rock-solid at **99.7%** win rate.
  - *Aktionsökonomie Insight:* 4 heroes (5 attacks/round) naturally overpower standard minion counts unless attrition is preserved.
  - *Victory/Retreat Rule Adopted in `campaign_guide.md`:*
    - **Heroischer Sieg:** Main objective completed AND at most 1 hero K.O. (heroes make it home victorious with full bounty).
    - **Verwundeter Rückzug:** 2+ heroes K.O. forces an emergency evacuation; scenario must be retreated/re-attempted, triggering injury scar checks.
    - **Totalverlust:** All 4 heroes incapacitated (party loses loot, pays fee to be rescued).

---|### Session 8 — 2026-11-04 (Campaign Monte Carlo Balancing & Dynamic Victory Tiers)
- **Multi-Scenario Simulator Built & Run (`balance_simulator_campaign.py`):**
  - Extended previous Scenario 01 simulator into a full 5-scenario Monte Carlo testing suite (50,000 runs total).
  - Modeled Encounter Deck draws, Door-Tokens, boss opening strikes, Predator Initiative (worgs/ghouls act first in round 1), and fatigue/rest mechanics.
- **Balancing Insights & Rule Formalization:**
  - *Scenario 01 (Tutorial):* Confirmed rock-solid at **99.7%** win rate.
  - *Aktionsökonomie Insight:* 4 heroes (5 attacks/round) naturally overpower standard minion counts unless attrition is preserved.
  - *Victory/Retreat Rule Adopted in `campaign_guide.md`:*
    - **Heroischer Sieg:** Main objective completed AND at most 1 hero K.O. (heroes make it home victorious with full bounty).
    - **Verwundeter Rückzug:** 2+ heroes K.O. forces an emergency evacuation; scenario must be retreated/re-attempted, triggering injury scar checks.
    - **Totalverlust:** All 4 heroes incapacitated (party loses loot, pays fee to be rescued).

---|
| **Title** | **Von Helden und Monstern — Abenteuer in der Alten Welt** *(formerly RV Quest)* |
| Inspired By | HeroQuest, Gloomhaven, Dungeon Crawl Classics |
| Players | 2 players (controlling **all 4 heroes**, 2 heroes each) |
| Party Size | **Always 4 heroes** in every scenario |
| Dice | **Only d6** — no other dice |
| Production | Standard home printer + laser cutter |
| Play Style | Co-op dungeon crawl, scenario-based |
| Session Length | Target: 45–90 min per scenario |
| **Game Language** | **German** — all player-facing content in German |
| Design Doc Language | English — for the designer's convenience |

### Session 8 — 2026-11-04 (Campaign Monte Carlo Balancing & Dynamic Victory Tiers)
- **Multi-Scenario Simulator Built & Run (`balance_simulator_campaign.py`):**
  - Extended previous Scenario 01 simulator into a full 5-scenario Monte Carlo testing suite (50,000 runs total).
  - Modeled Encounter Deck draws, Door-Tokens, boss opening strikes, Predator Initiative (worgs/ghouls act first in round 1), and fatigue/rest mechanics.
- **Balancing Insights & Rule Formalization:**
  - *Scenario 01 (Tutorial):* Confirmed rock-solid at **99.7%** win rate.
  - *Aktionsökonomie Insight:* 4 heroes (5 attacks/round) naturally overpower standard minion counts unless attrition is preserved.
  - *Victory/Retreat Rule Adopted in `campaign_guide.md`:*
    - **Heroischer Sieg:** Main objective completed AND at most 1 hero K.O. (heroes make it home victorious with full bounty).
    - **Verwundeter Rückzug:** 2+ heroes K.O. forces an emergency evacuation; scenario must be retreated/re-attempted, triggering injury scar checks.
    - **Totalverlust:** All 4 heroes incapacitated (party loses loot, pays fee to be rescued).

---

## 📁 Folder Structure

```
RV_Quest/
├── PROJECT_CONTEXT.md       ← This file (living context & session log)
├── PLAN.md                  ← Project plan and phase tracker
├── OPEN_QUESTIONS.md        ← Master registry of open questions & design choices
├── rules/
│   ├── core_rules.md        ← Core mechanics (dice, actions, turns)
│   ├── combat.md            ← Combat system
│   ├── exploration.md       ← Movement, doors, traps, treasure
│   └── conditions.md        ← Status effects (burning, stunned, etc.)
├── characters/
│   ├── character_roster.md  ← All playable characters
│   └── character_sheets/    ← Individual character sheets (printable)
├── monsters/
│   ├── monster_roster.md    ← All monsters with stats and behaviour
│   └── monster_cards/       ← Individual monster stat cards (printable)
├── lore/
│   ├── world.md             ← Setting overview, tone, factions
│   └── bestiary_lore.md     ← Flavour text for monsters
├── adventures/
│   ├── adventure_guide.md   ← How to create an adventure/scenario
│   └── scenario_01.md       ← First scenario (tutorial)
├── components/
│   └── component_list.md    ← Full bill of materials for the game
└── printables/
    └── README.md            ← Notes on print/laser cut settings
```

### Session 8 — 2026-11-04 (Campaign Monte Carlo Balancing & Dynamic Victory Tiers)
- **Multi-Scenario Simulator Built & Run (`balance_simulator_campaign.py`):**
  - Extended previous Scenario 01 simulator into a full 5-scenario Monte Carlo testing suite (50,000 runs total).
  - Modeled Encounter Deck draws, Door-Tokens, boss opening strikes, Predator Initiative (worgs/ghouls act first in round 1), and fatigue/rest mechanics.
- **Balancing Insights & Rule Formalization:**
  - *Scenario 01 (Tutorial):* Confirmed rock-solid at **99.7%** win rate.
  - *Aktionsökonomie Insight:* 4 heroes (5 attacks/round) naturally overpower standard minion counts unless attrition is preserved.
  - *Victory/Retreat Rule Adopted in `campaign_guide.md`:*
    - **Heroischer Sieg:** Main objective completed AND at most 1 hero K.O. (heroes make it home victorious with full bounty).
    - **Verwundeter Rückzug:** 2+ heroes K.O. forces an emergency evacuation; scenario must be retreated/re-attempted, triggering injury scar checks.
    - **Totalverlust:** All 4 heroes incapacitated (party loses loot, pays fee to be rescued).

---

## 🧠 Key Decisions Made

### Language
- **All game-facing content in German** — rulebook, character sheets, monster cards, item cards, scenarios, flavour text
- Design documents (PROJECT_CONTEXT, PLAN, SCHEDULE, rule drafts) stay in **English** for the designer
- When writing game content, default to German unless asked otherwise

### World & Setting
- **Title:** *Von Helden und Monstern — Abenteuer in der Alten Welt*
- **World Name:** **Die Alte Welt** (One giant continent, medieval tech, sword & sorcery)
- **Three starting realms:**
  1. **Kaisertum Valdor** (central/east) — human imperial realms, feudal city-states, trade hubs, and seat of the *Kaiserliche Akademie für Arkane Künste*
  2. **Sylvanheim** (west/forest) — ancient elven realm, home of the Kriegstänzerinnen and the *Heiliger Hain* (sacred grove)
  3. **Nördliches Ödland** (north) — harsh Scandinavia-inspired wildlands, warrior clans, origin of the Berserker
- **Goblins & the Schattenbazar:**
  - Goblins have no realm of their own; it is simply their way of living embedded across all human, elven, and border towns.
  - They operate the **Schattenbazar** — an informal, pan-continental trade and information darknet for goods, contraband, poisons, and services.
  - Respected guilds form distinct spheres of power within the Schattenbazar.
- Extensible by design — more realms to be added over time with wife

### Characters (4 heroes)
1. **Nordland Berserker** — huge Viking/barbarian, melee tank, rage when wounded, hails from the Nördliches Ödland, travels south for glory after defeating all northern enemies
2. **Elfische Kriegstänzerin** — always female, trained to guard Heiliger Hain, 2 attacks/round, on her world-journey
3. **Goblin Halsabschneider** — goblin assassin/rogue, backstab, locks/traps, can cast random spells when **very drunk**
4. **Magiegelehrte der Kaiserlichen Akademie für Arkane Künste** — human female mage, glass cannon, arrogant academic snob

**Inter-character tensions (to be mechanised):**
- Kriegstänzerin ↔ Halsabschneider: deep mutual cultural contempt (she despises him; he finds this funny)
- Magiegelehrte ↔ Halsabschneider: drunk goblin magic is a personal insult to the Akademie
- Kriegstänzerin ↔ Magiegelehrte: wary mutual professional respect

### Proposed 5 Attributes (awaiting confirmation)
| Abbrev. | German | Governs |
|### Session 8 — 2026-11-04 (Campaign Monte Carlo Balancing & Dynamic Victory Tiers)
- **Multi-Scenario Simulator Built & Run (`balance_simulator_campaign.py`):**
  - Extended previous Scenario 01 simulator into a full 5-scenario Monte Carlo testing suite (50,000 runs total).
  - Modeled Encounter Deck draws, Door-Tokens, boss opening strikes, Predator Initiative (worgs/ghouls act first in round 1), and fatigue/rest mechanics.
- **Balancing Insights & Rule Formalization:**
  - *Scenario 01 (Tutorial):* Confirmed rock-solid at **99.7%** win rate.
  - *Aktionsökonomie Insight:* 4 heroes (5 attacks/round) naturally overpower standard minion counts unless attrition is preserved.
  - *Victory/Retreat Rule Adopted in `campaign_guide.md`:*
    - **Heroischer Sieg:** Main objective completed AND at most 1 hero K.O. (heroes make it home victorious with full bounty).
    - **Verwundeter Rückzug:** 2+ heroes K.O. forces an emergency evacuation; scenario must be retreated/re-attempted, triggering injury scar checks.
    - **Totalverlust:** All 4 heroes incapacitated (party loses loot, pays fee to be rescued).

---|### Session 8 — 2026-11-04 (Campaign Monte Carlo Balancing & Dynamic Victory Tiers)
- **Multi-Scenario Simulator Built & Run (`balance_simulator_campaign.py`):**
  - Extended previous Scenario 01 simulator into a full 5-scenario Monte Carlo testing suite (50,000 runs total).
  - Modeled Encounter Deck draws, Door-Tokens, boss opening strikes, Predator Initiative (worgs/ghouls act first in round 1), and fatigue/rest mechanics.
- **Balancing Insights & Rule Formalization:**
  - *Scenario 01 (Tutorial):* Confirmed rock-solid at **99.7%** win rate.
  - *Aktionsökonomie Insight:* 4 heroes (5 attacks/round) naturally overpower standard minion counts unless attrition is preserved.
  - *Victory/Retreat Rule Adopted in `campaign_guide.md`:*
    - **Heroischer Sieg:** Main objective completed AND at most 1 hero K.O. (heroes make it home victorious with full bounty).
    - **Verwundeter Rückzug:** 2+ heroes K.O. forces an emergency evacuation; scenario must be retreated/re-attempted, triggering injury scar checks.
    - **Totalverlust:** All 4 heroes incapacitated (party loses loot, pays fee to be rescued).

---|### Session 8 — 2026-11-04 (Campaign Monte Carlo Balancing & Dynamic Victory Tiers)
- **Multi-Scenario Simulator Built & Run (`balance_simulator_campaign.py`):**
  - Extended previous Scenario 01 simulator into a full 5-scenario Monte Carlo testing suite (50,000 runs total).
  - Modeled Encounter Deck draws, Door-Tokens, boss opening strikes, Predator Initiative (worgs/ghouls act first in round 1), and fatigue/rest mechanics.
- **Balancing Insights & Rule Formalization:**
  - *Scenario 01 (Tutorial):* Confirmed rock-solid at **99.7%** win rate.
  - *Aktionsökonomie Insight:* 4 heroes (5 attacks/round) naturally overpower standard minion counts unless attrition is preserved.
  - *Victory/Retreat Rule Adopted in `campaign_guide.md`:*
    - **Heroischer Sieg:** Main objective completed AND at most 1 hero K.O. (heroes make it home victorious with full bounty).
    - **Verwundeter Rückzug:** 2+ heroes K.O. forces an emergency evacuation; scenario must be retreated/re-attempted, triggering injury scar checks.
    - **Totalverlust:** All 4 heroes incapacitated (party loses loot, pays fee to be rescued).

---|
| KRA | Kraft | Melee power, damage |
| GES | Geschick | Speed, dodge, ranged, actions |
| ZÄH | Zähigkeit | HP, damage resistance |
| VER | Verstand | Magic, traps, item ID |
| LIS | List | Stealth, deception, locks |

### Characters
- Max **5 attributes** per character
- User has specific character and setting ideas (to be shared next session)

### Dice System
- **Only d6** — core mechanic: **roll 1 or 2 d6 + attribute modifier vs. target number**
- Simple and fast, minimal maths
### Artwork (Phase 7 — reminder)
- **Male characters** (Berserker, Halsabschneider) modelled after **the designer** — photos to be provided
- **Female characters** (Kriegstänzerin, Magiegelehrte) modelled after **his wife** — photos to be provided
- ⚠️ **Reminder:** Ask for photos when artwork phase begins


### Production Constraints
- Standard A4/Letter printer
- Laser cutter available → **standees, bases, tokens, storage box** (tiles eliminated — see Game Book decision)
- Keep component count manageable for RV storage
- Time budget: ~1 hour/day weekdays = ~40 hours total over 8 weeks

### Production Format — Game Book *(Decided Session 7 — 2026-11-04)*
- **Format:** **210 × 210 mm Square Wire-Bound Scenario Book** (all 5 scenarios in one bound book)
  - **Left page (210 × 210 mm):** Scenario briefing, special rules, win/loss conditions, monster stat reference, encounter tables
  - **Right page (210 × 210 mm):** Full-colour 180 × 180 mm battle map (6 × 6 fields of 30 mm grid, pre-printed terrain, obstacles, spawn markers)
  - **Table footprint open:** 420 × 210 mm (42 × 21 cm) — saves ~10 cm of depth on camper dinette tables!
  - **Home Printer Workflow (1-Cut Method):** Feed standard full-size A4 sheets (210 × 297 mm, 160–200g) into printer. Print content in top 210 × 210 mm zone. Make 1 single guillotine slice across the bottom at 210 mm.
  - **Margin Safety:** 210 mm paper width minus 180 mm grid = 15 mm white margins left and right. Far exceeds standard printer hardware margins (3–5 mm), guaranteeing zero clipped content even on basic home printers.

### Print Document Format *(Decided Session 7 — 2026-11-04)*
- **Format:** Word / LibreOffice Writer `.docx`
- **Workflow:** Automated generation of A4 `.docx` with pre-set page spreads; print in one pass using printer's native colour profiles
- **Key printer settings:** Paper Type = Heavy/Cardstock, Quality = High/Best, Background Graphics = On

### Session 7 — 2026-11-04 (Game Book Format & Print Pipeline Decisions)
- **Production Format Changed — Game Book (wire-bound A4 Scenario Book):**
  - Dropped: 10-piece modular laser-cut tile kit + physical furniture/obstacle tokens.
  - Adopted: All 5 scenarios printed in one spiral-bound A4 book. Left page = instructions, right page = full-colour battle map with 30 mm grid, pre-printed terrain and spawn markers.
  - Laser cutter retained for standees, bases, tokens, and storage box.
  - Rationale: Major production simplification (eliminates ~70% of fabrication work), eliminates tile slippage in RV, table footprint reduced to book + standees + card decks + dice.
- **Print Document Format — Word / LibreOffice `.docx`:**
  - Final print files generated as `.docx` documents with A4 page spreads.
  - Print directly from LibreOffice Writer / MS Word in one pass using native colour profiles.
  - Avoids washed-out PDFs from earlier pipeline (SVG → PyMuPDF or Chrome → PDF).
- **Card Packaging & Individual Gear Artworks (Decided Session 7 — 2026-11-04):**
  - **Individual Gear Artworks:** Midjourney will be used to generate dedicated woodcut vignettes for all 24 weapons, 12 armors/helmets/shields, and 18 potions/relics (54 cards total + starter gear).
  - **Card Tuck Boxes (Schachteln):** Separate custom tuck boxes designed for printing on heavy 250–300g cardstock (fold, crease, glue) for each deck:
    1. Ausrüstungsdeck (54 Karten, ~20 mm Fülltiefe)
    2. Ereignisdeck (18 Karten, ~8 mm Fülltiefe)
    3. Begegnungsdeck (16 Karten, ~7 mm Fülltiefe)
    4. Startausrüstung & Zauberkarten (18 Karten)
- **Art Style & Midjourney `--sref` Anchors Saved (`printables/ART_STYLE_GUIDE.md`):**
  - Permanent master Goblin style benchmark: `https://i.imgur.com/7GHh0Ju.png` (replaces temporary CDN link)
  - High-contrast, reduced linework, open white areas tuned specifically for laser engraving without soot/charring. Backup candidates also cataloged.
  - **Full B&W Standee Prompt Roster:** Complete copy-paste prompts for all 12 campaign monsters compiled in `printables/MONSTER_PROMPTS_BW.md` with dynamic combat fighting stances, borderless constraints, and uncropped feet.
- **Campaign Scenarios 04 & 05 Completed:**
  - `adventures/scenario_04.md`: "Die belagerte Felsen-Zitadelle" (Fortress defense, barricades, portcullis, Blood Golem 1×2 & Wight Champion boss).
  - `adventures/scenario_05.md`: "Das Totenreich des Lich-Königs" (Grand campaign finale: Malakor LP 18, 2 actions/round, frost aura, 3 braziers, soul cages, victory scoring & epilogue).
  - **Full Hybrid Architecture Harmonized:** All scenarios (01–05) now strictly follow the hybrid design: intermediate rooms draw dynamically from the Encounter Deck (`[A]`, `[B]`), all door thresholds use facedown Tür-Tokens from the 8-piece pool, and boss arenas remain cinematic set-pieces. All 5 campaign scenarios are complete!

### Session 6 — 2026-11-03 (Art Guidelines, Equipment Expansion & Status Effects To-Do)
- **Art Style Guide Updated (`printables/ART_STYLE_GUIDE.md`):**
  - Removed old "90% Freiraum" rule; introduced tight framing (subject filling 85–90% of frame with minimal margins).
  - Enforced 100% pure solid white background (`#FFFFFF`, zero parchment texture) for standees to prevent laser soot/charring.
- **Armory & Equipment Expanded (`components/card_list.md`):**
  - Expanded loot deck from 36 to **54 cards**.
  - Weapons expanded from 13 to **24** (added reach polearms, armor-piercing dwarven hammer, flail, parry dagger, repeating crossbow).
  - Armor/Shields/Helmets doubled from 6 to **12** (added Stadtgarde Eisenhelm, Hörnerhelm, Buckler, Stachelschild, Zwergen-Schuppenpanzer).
- **To-Do Added:**
  - Create dedicated `rules/conditions.md` detailing comprehensive status effect mechanics and tabletop handling (especially *Betäubt / Stunned* prone standee placement, duration, saves, and immunities).

### Session 8 — 2026-11-04 (Campaign Monte Carlo Balancing & Dynamic Victory Tiers)
- **Multi-Scenario Simulator Built & Run (`balance_simulator_campaign.py`):**
  - Extended previous Scenario 01 simulator into a full 5-scenario Monte Carlo testing suite (50,000 runs total).
  - Modeled Encounter Deck draws, Door-Tokens, boss opening strikes, Predator Initiative (worgs/ghouls act first in round 1), and fatigue/rest mechanics.
- **Balancing Insights & Rule Formalization:**
  - *Scenario 01 (Tutorial):* Confirmed rock-solid at **99.7%** win rate.
  - *Aktionsökonomie Insight:* 4 heroes (5 attacks/round) naturally overpower standard minion counts unless attrition is preserved.
  - *Victory/Retreat Rule Adopted in `campaign_guide.md`:*
    - **Heroischer Sieg:** Main objective completed AND at most 1 hero K.O. (heroes make it home victorious with full bounty).
    - **Verwundeter Rückzug:** 2+ heroes K.O. forces an emergency evacuation; scenario must be retreated/re-attempted, triggering injury scar checks.
    - **Totalverlust:** All 4 heroes incapacitated (party loses loot, pays fee to be rescued).

---
## ❓ Open Questions & Decisions Needed

### 1. World & Narrative Lore (Phase 1 / Lore)
- [ ] **World name:** (Placeholder: *Die Alte Welt*, *Aethelgard*, *Valenor*?)
- [ ] **Human realm name:** Where the Kaiserliche Akademie is located (e.g. *Kaisertum Valdor*, *Herzogtum Solenheim*?)
- [ ] **Elven realm name:** Home of Kriegstänzerinnen and the Heiliger Hain (e.g. *Silberwald*, *Sylvanheim*, *Ewiger Hain*?)
- [ ] **Goblin guild/shadow network name:** (e.g. *Die Schattengilde*, *Die Rostkrallen*, *Die Kriecher*?)
- [ ] **Campaign overarching threat / main villain:** (e.g. An awakening Lich-King, a corrupt Archmage, or a Demonic incursion from the northern waste?)

### 2. Character Progression (Phase 3)
- [ ] **Level-Up & Growth:** Do heroes gain XP/Levels with +1 stat / new talent card upgrades after X completed scenarios, or is progression purely equipment & gold based?

### 3. Production Specs (Phase 7)
- [x] **Card & Tile Dimensions:** 
  - Karten im atmosphärischen **Tarot-Format (70 × 120 mm)**. Artwork & Rückseiten schrittweise via KI-Bildgeneratoren generiert.
  - Dungeon-Tiles: 30 × 30 mm Gitterfelder (3 mm Birkensperrholz).
  - Holz-Standees: 3 mm Sperrholz mit Zapfenverbindung in Ø 30 mm runden Basen (Schergen-Basen beidseitig nummeriert 1–6). Bildmaße: Standard 30 × 40 mm (3:4 Verhältnis), Groß 60 × 80 mm, Fliegend/Schwebend 30 × 80 mm (doppelte Höhe für Schwebe-Effekt).

### Session 7 — 2026-11-04 (Game Book Format & Print Pipeline Decisions)
- **Production Format Changed — Game Book (wire-bound A4 Scenario Book):**
  - Dropped: 10-piece modular laser-cut tile kit + physical furniture/obstacle tokens.
  - Adopted: All 5 scenarios printed in one spiral-bound A4 book. Left page = instructions, right page = full-colour battle map with 30 mm grid, pre-printed terrain and spawn markers.
  - Laser cutter retained for standees, bases, tokens, and storage box.
  - Rationale: Major production simplification (eliminates ~70% of fabrication work), eliminates tile slippage in RV, table footprint reduced to book + standees + card decks + dice.
- **Print Document Format — Word / LibreOffice `.docx`:**
  - Final print files generated as `.docx` documents with A4 page spreads.
  - Print directly from LibreOffice Writer / MS Word in one pass using native colour profiles.
  - Avoids washed-out PDFs from earlier pipeline (SVG → PyMuPDF or Chrome → PDF).
- **Card Packaging & Individual Gear Artworks (Decided Session 7 — 2026-11-04):**
  - **Individual Gear Artworks:** Midjourney will be used to generate dedicated woodcut vignettes for all 24 weapons, 12 armors/helmets/shields, and 18 potions/relics (54 cards total + starter gear).
  - **Card Tuck Boxes (Schachteln):** Separate custom tuck boxes designed for printing on heavy 250–300g cardstock (fold, crease, glue) for each deck:
    1. Ausrüstungsdeck (54 Karten, ~20 mm Fülltiefe)
    2. Ereignisdeck (18 Karten, ~8 mm Fülltiefe)
    3. Begegnungsdeck (16 Karten, ~7 mm Fülltiefe)
    4. Startausrüstung & Zauberkarten (18 Karten)
- **Art Style & Midjourney `--sref` Anchors Saved (`printables/ART_STYLE_GUIDE.md`):**
  - Permanent master Goblin style benchmark: `https://i.imgur.com/7GHh0Ju.png` (replaces temporary CDN link)
  - High-contrast, reduced linework, open white areas tuned specifically for laser engraving without soot/charring. Backup candidates also cataloged.
  - **Full B&W Standee Prompt Roster:** Complete copy-paste prompts for all 12 campaign monsters compiled in `printables/MONSTER_PROMPTS_BW.md` with dynamic combat fighting stances, borderless constraints, and uncropped feet.
- **Campaign Scenarios 04 & 05 Completed:**
  - `adventures/scenario_04.md`: "Die belagerte Felsen-Zitadelle" (Fortress defense, barricades, portcullis, Blood Golem 1×2 & Wight Champion boss).
  - `adventures/scenario_05.md`: "Das Totenreich des Lich-Königs" (Grand campaign finale: Malakor LP 18, 2 actions/round, frost aura, 3 braziers, soul cages, victory scoring & epilogue).
  - **Full Hybrid Architecture Harmonized:** All scenarios (01–05) now strictly follow the hybrid design: intermediate rooms draw dynamically from the Encounter Deck (`[A]`, `[B]`), all door thresholds use facedown Tür-Tokens from the 8-piece pool, and boss arenas remain cinematic set-pieces. All 5 campaign scenarios are complete!

### Session 6 — 2026-11-03 (Art Guidelines, Equipment Expansion & Status Effects To-Do)
- **Art Style Guide Updated (`printables/ART_STYLE_GUIDE.md`):**
  - Removed old "90% Freiraum" rule; introduced tight framing (subject filling 85–90% of frame with minimal margins).
  - Enforced 100% pure solid white background (`#FFFFFF`, zero parchment texture) for standees to prevent laser soot/charring.
- **Armory & Equipment Expanded (`components/card_list.md`):**
  - Expanded loot deck from 36 to **54 cards**.
  - Weapons expanded from 13 to **24** (added reach polearms, armor-piercing dwarven hammer, flail, parry dagger, repeating crossbow).
  - Armor/Shields/Helmets doubled from 6 to **12** (added Stadtgarde Eisenhelm, Hörnerhelm, Buckler, Stachelschild, Zwergen-Schuppenpanzer).
- **To-Do Added:**
  - Create dedicated `rules/conditions.md` detailing comprehensive status effect mechanics and tabletop handling (especially *Betäubt / Stunned* prone standee placement, duration, saves, and immunities).

### Session 8 — 2026-11-04 (Campaign Monte Carlo Balancing & Dynamic Victory Tiers)
- **Multi-Scenario Simulator Built & Run (`balance_simulator_campaign.py`):**
  - Extended previous Scenario 01 simulator into a full 5-scenario Monte Carlo testing suite (50,000 runs total).
  - Modeled Encounter Deck draws, Door-Tokens, boss opening strikes, Predator Initiative (worgs/ghouls act first in round 1), and fatigue/rest mechanics.
- **Balancing Insights & Rule Formalization:**
  - *Scenario 01 (Tutorial):* Confirmed rock-solid at **99.7%** win rate.
  - *Aktionsökonomie Insight:* 4 heroes (5 attacks/round) naturally overpower standard minion counts unless attrition is preserved.
  - *Victory/Retreat Rule Adopted in `campaign_guide.md`:*
    - **Heroischer Sieg:** Main objective completed AND at most 1 hero K.O. (heroes make it home victorious with full bounty).
    - **Verwundeter Rückzug:** 2+ heroes K.O. forces an emergency evacuation; scenario must be retreated/re-attempted, triggering injury scar checks.
    - **Totalverlust:** All 4 heroes incapacitated (party loses loot, pays fee to be rescued).

---
### Equipment, Cards & Party Size
- **Party Composition:** Every scenario is played with **all 4 heroes** (in a 2-player game, each player controls 2 heroes). Balancing is calibrated for a full 4-hero party.
- **Physical Cards for Everything:**
  - **Startausrüstung:** Physical starting gear cards given to each hero at the beginning (differentiated by a starter icon).
  - **Equipped Slots & Carrying Limit per Hero:**
    - 1 Armor slot
    - 2 Hand slots (1 two-handed OR 2 one-handed OR 1 one-handed + 1 shield/torch)
    - 1 Accessory slot (ring/amulet)
    - 3 Backpack/inventory slots (consumables, extra weapons, relics). Maximum 7 cards per hero total.
- **Ausrüstungsdeck (Loot & Market):**
  - **Feasible Size:** **24–36 cards** (beyond starting gear). Printed across 3–4 standard A4 sheets (approx. 9 cards per sheet).
  - Gives strong variety (weapons, armor upgrades, shields, scrolls, consumables, magical trinkets) without card bloat in an RV box.
  - Used for hidden chest/elite loot and 4-card face-up market display between adventures.
- **Ereigniskarten-Deck (Event Deck):**
  - **Deck of ~18–24 event cards** drawn during Phase 4 (End of Round) or upon dungeon triggers (entering new rooms, opening sarcophagi, timers).
  - Delivers dynamic hazards, wandering patrols, beneficial boons, and atmosphere.

### Session 7 — 2026-11-04 (Game Book Format & Print Pipeline Decisions)
- **Production Format Changed — Game Book (wire-bound A4 Scenario Book):**
  - Dropped: 10-piece modular laser-cut tile kit + physical furniture/obstacle tokens.
  - Adopted: All 5 scenarios printed in one spiral-bound A4 book. Left page = instructions, right page = full-colour battle map with 30 mm grid, pre-printed terrain and spawn markers.
  - Laser cutter retained for standees, bases, tokens, and storage box.
  - Rationale: Major production simplification (eliminates ~70% of fabrication work), eliminates tile slippage in RV, table footprint reduced to book + standees + card decks + dice.
- **Print Document Format — Word / LibreOffice `.docx`:**
  - Final print files generated as `.docx` documents with A4 page spreads.
  - Print directly from LibreOffice Writer / MS Word in one pass using native colour profiles.
  - Avoids washed-out PDFs from earlier pipeline (SVG → PyMuPDF or Chrome → PDF).
- **Card Packaging & Individual Gear Artworks (Decided Session 7 — 2026-11-04):**
  - **Individual Gear Artworks:** Midjourney will be used to generate dedicated woodcut vignettes for all 24 weapons, 12 armors/helmets/shields, and 18 potions/relics (54 cards total + starter gear).
  - **Card Tuck Boxes (Schachteln):** Separate custom tuck boxes designed for printing on heavy 250–300g cardstock (fold, crease, glue) for each deck:
    1. Ausrüstungsdeck (54 Karten, ~20 mm Fülltiefe)
    2. Ereignisdeck (18 Karten, ~8 mm Fülltiefe)
    3. Begegnungsdeck (16 Karten, ~7 mm Fülltiefe)
    4. Startausrüstung & Zauberkarten (18 Karten)
- **Art Style & Midjourney `--sref` Anchors Saved (`printables/ART_STYLE_GUIDE.md`):**
  - Permanent master Goblin style benchmark: `https://i.imgur.com/7GHh0Ju.png` (replaces temporary CDN link)
  - High-contrast, reduced linework, open white areas tuned specifically for laser engraving without soot/charring. Backup candidates also cataloged.
  - **Full B&W Standee Prompt Roster:** Complete copy-paste prompts for all 12 campaign monsters compiled in `printables/MONSTER_PROMPTS_BW.md` with dynamic combat fighting stances, borderless constraints, and uncropped feet.
- **Campaign Scenarios 04 & 05 Completed:**
  - `adventures/scenario_04.md`: "Die belagerte Felsen-Zitadelle" (Fortress defense, barricades, portcullis, Blood Golem 1×2 & Wight Champion boss).
  - `adventures/scenario_05.md`: "Das Totenreich des Lich-Königs" (Grand campaign finale: Malakor LP 18, 2 actions/round, frost aura, 3 braziers, soul cages, victory scoring & epilogue).
  - **Full Hybrid Architecture Harmonized:** All scenarios (01–05) now strictly follow the hybrid design: intermediate rooms draw dynamically from the Encounter Deck (`[A]`, `[B]`), all door thresholds use facedown Tür-Tokens from the 8-piece pool, and boss arenas remain cinematic set-pieces. All 5 campaign scenarios are complete!

### Session 6 — 2026-11-03 (Art Guidelines, Equipment Expansion & Status Effects To-Do)
- **Art Style Guide Updated (`printables/ART_STYLE_GUIDE.md`):**
  - Removed old "90% Freiraum" rule; introduced tight framing (subject filling 85–90% of frame with minimal margins).
  - Enforced 100% pure solid white background (`#FFFFFF`, zero parchment texture) for standees to prevent laser soot/charring.
- **Armory & Equipment Expanded (`components/card_list.md`):**
  - Expanded loot deck from 36 to **54 cards**.
  - Weapons expanded from 13 to **24** (added reach polearms, armor-piercing dwarven hammer, flail, parry dagger, repeating crossbow).
  - Armor/Shields/Helmets doubled from 6 to **12** (added Stadtgarde Eisenhelm, Hörnerhelm, Buckler, Stachelschild, Zwergen-Schuppenpanzer).
- **To-Do Added:**
  - Create dedicated `rules/conditions.md` detailing comprehensive status effect mechanics and tabletop handling (especially *Betäubt / Stunned* prone standee placement, duration, saves, and immunities).

### Session 8 — 2026-11-04 (Campaign Monte Carlo Balancing & Dynamic Victory Tiers)
- **Multi-Scenario Simulator Built & Run (`balance_simulator_campaign.py`):**
  - Extended previous Scenario 01 simulator into a full 5-scenario Monte Carlo testing suite (50,000 runs total).
  - Modeled Encounter Deck draws, Door-Tokens, boss opening strikes, Predator Initiative (worgs/ghouls act first in round 1), and fatigue/rest mechanics.
- **Balancing Insights & Rule Formalization:**
  - *Scenario 01 (Tutorial):* Confirmed rock-solid at **99.7%** win rate.
  - *Aktionsökonomie Insight:* 4 heroes (5 attacks/round) naturally overpower standard minion counts unless attrition is preserved.
  - *Victory/Retreat Rule Adopted in `campaign_guide.md`:*
    - **Heroischer Sieg:** Main objective completed AND at most 1 hero K.O. (heroes make it home victorious with full bounty).
    - **Verwundeter Rückzug:** 2+ heroes K.O. forces an emergency evacuation; scenario must be retreated/re-attempted, triggering injury scar checks.
    - **Totalverlust:** All 4 heroes incapacitated (party loses loot, pays fee to be rescued).

---
## 📅 Session Log

### Session 1 — 2026-10-26
- Project initiated, folder structure + PLAN/SCHEDULE created
- Constraints: d6 only, max 5 attributes, 2-player co-op, RV-friendly, Christmas gift
- Core dice mechanic: roll 1 or 2 d6 + attribute modifier vs. target number
- Language rule: game content German, design docs English
- World established: one continent, three realms (Menschenreich, Elfenreich, Nördliches Ödland)
- Goblin culture: no homeland, embedded in criminal underworld economy of all realms
- 4 characters defined: Berserker, Kriegstänzerin, Halsabschneider, Magierin
- Proposed 5 attributes: KRA / GES / ZÄH / VER / LIS
- Files created: `lore/world.md`, `characters/character_roster.md`, `rules/combat.md`
- Added **Equipment Deck System**: Single unified deck for dungeon loot & market display, with static class starting gear.
- Added **Card Catalog** (`components/card_list.md`): 36 Equipment Cards & 18 Event Cards in Mini-Euro format.
- Added **Hero Starter Cards & Spells** (`characters/starter_cards_and_spells.md`): 12 Starter Cards, 6 Arcane Spells, and the 1d6 Drunk Goblin Magic table.
- Added **Monster Bestiary & AI** (`monsters/monster_roster.md`): 6 monster profiles with stats, abilities, bounties, and 3-step automated AI behavior.

### Session 3 — 2026-10-27 (Standees & Automated Balance Testing)
- **30 mm Standee Standard Confirmed:**
  - Plaque width: **30 mm** (fills the 30mm dungeon square for optimal stability).
  - Standee base: **Ø 30 mm round** (friction-fit 10.2 × 3.0 mm slot for 3 mm plywood).
  - Symmetry: 100% horizontal mirror symmetry with centered tenon tab allowing seamless dual-sided laser engraving via jig.
  - Image tight bounds: Auto-crop utility (`generate_standee.py`) trims margins to <1 mm side whitespace, ~0.6 mm flush base, and ~2.5 mm dome ceiling.
- **Micro-Testing Plan Defined:**
  - 5 fast, modular 5–10 minute playtest drills designed (Breach & Reveal, 3-Round White Room, Fatigue & Intoxication, Skill Check, Standee Ergonomics).
- **Automated Monte-Carlo Simulation Executed (`balance_simulator.py`):**
  - **10,000 full runs** of Scenario 01 ("Die verfluchte Krypta von Dun-Karr") simulated.
  - Overall Victory Rate: **100.00%** (ideal tutorial difficulty).
  - Surviving HP average: Berserker 7.12 / 12, Kriegstänzerin 7.04 / 10, Goblin 4.53 / 8, Magierin 4.53 / 8.
  - Confirmed: Armor reduction (-1 dmg) successfully prevents one-shot kills, while Berserker rage and tactical spell-use function as intended.

### Session 5 — 2026-10-29 (Monster HP Tracking, Large Monster Rules & Balance Verification)
- **3-Tier Monster HP Tracking System (`rules/combat.md` & `components/card_list.md`):**
  - **Minions (LP 2–6):** 25× Ø 10 mm laser-cut birch damage tokens directly on the board.
  - **Elites (LP 6–10):** 5× laminated Mini-Euro cards with LP track (❶–❿) + whiteboard marker.
  - **Bosses (LP 14+):** 2× laminated A6 reference cards (Grabunhold LP 1–14, Lich-König LP 1–18) + marker.
- **Large Monster Rules ("Groß" — 1×2 Tiles):**
  - Grabunhold & Blutgolem occupy 1×2 fields on the 30 mm grid.
  - Blocks narrow 1-tile passages, grants tactical melee positioning options, and both tiles count for adjacency & AoE damage.
  - Standee format: 60 × 45 mm plaque with 60 × 20 mm rectangular base.
  - Lich-König Malakor stays on 1×1 field for maneuverability, but receives an imposing tall standee (30 × 80 mm plaque, Ø 30 mm round base).
- **Automated Balance Re-Test (`balance_simulator.py`):**
  - Modeled 1×2 positional blocking (25% chance of melee path obstruction per round).
  - 10,000 runs comparison:
    - *Without Large Monster Rule:* 99.98% Win Rate (2 wipes in Room 4).
    - *With Large Monster Rule:* 99.75% Win Rate (25 wipes in Room 4).
  - Verdict: Perfect difficulty tuning for Scenario 01 (target was >= 90% win rate). The boss feels dangerous without feeling unfair.

### Session 7 — 2026-11-04 (Game Book Format & Print Pipeline Decisions)
- **Production Format Changed — Game Book (wire-bound A4 Scenario Book):**
  - Dropped: 10-piece modular laser-cut tile kit + physical furniture/obstacle tokens.
  - Adopted: All 5 scenarios printed in one spiral-bound A4 book. Left page = instructions, right page = full-colour battle map with 30 mm grid, pre-printed terrain and spawn markers.
  - Laser cutter retained for standees, bases, tokens, and storage box.
  - Rationale: Major production simplification (eliminates ~70% of fabrication work), eliminates tile slippage in RV, table footprint reduced to book + standees + card decks + dice.
- **Print Document Format — Word / LibreOffice `.docx`:**
  - Final print files generated as `.docx` documents with A4 page spreads.
  - Print directly from LibreOffice Writer / MS Word in one pass using native colour profiles.
  - Avoids washed-out PDFs from earlier pipeline (SVG → PyMuPDF or Chrome → PDF).
- **Card Packaging & Individual Gear Artworks (Decided Session 7 — 2026-11-04):**
  - **Individual Gear Artworks:** Midjourney will be used to generate dedicated woodcut vignettes for all 24 weapons, 12 armors/helmets/shields, and 18 potions/relics (54 cards total + starter gear).
  - **Card Tuck Boxes (Schachteln):** Separate custom tuck boxes designed for printing on heavy 250–300g cardstock (fold, crease, glue) for each deck:
    1. Ausrüstungsdeck (54 Karten, ~20 mm Fülltiefe)
    2. Ereignisdeck (18 Karten, ~8 mm Fülltiefe)
    3. Begegnungsdeck (16 Karten, ~7 mm Fülltiefe)
    4. Startausrüstung & Zauberkarten (18 Karten)
- **Art Style & Midjourney `--sref` Anchors Saved (`printables/ART_STYLE_GUIDE.md`):**
  - Permanent master Goblin style benchmark: `https://i.imgur.com/7GHh0Ju.png` (replaces temporary CDN link)
  - High-contrast, reduced linework, open white areas tuned specifically for laser engraving without soot/charring. Backup candidates also cataloged.
  - **Full B&W Standee Prompt Roster:** Complete copy-paste prompts for all 12 campaign monsters compiled in `printables/MONSTER_PROMPTS_BW.md` with dynamic combat fighting stances, borderless constraints, and uncropped feet.
- **Campaign Scenarios 04 & 05 Completed:**
  - `adventures/scenario_04.md`: "Die belagerte Felsen-Zitadelle" (Fortress defense, barricades, portcullis, Blood Golem 1×2 & Wight Champion boss).
  - `adventures/scenario_05.md`: "Das Totenreich des Lich-Königs" (Grand campaign finale: Malakor LP 18, 2 actions/round, frost aura, 3 braziers, soul cages, victory scoring & epilogue).
  - **Full Hybrid Architecture Harmonized:** All scenarios (01–05) now strictly follow the hybrid design: intermediate rooms draw dynamically from the Encounter Deck (`[A]`, `[B]`), all door thresholds use facedown Tür-Tokens from the 8-piece pool, and boss arenas remain cinematic set-pieces. All 5 campaign scenarios are complete!

### Session 6 — 2026-11-03 (Art Guidelines, Equipment Expansion & Status Effects To-Do)
- **Art Style Guide Updated (`printables/ART_STYLE_GUIDE.md`):**
  - Removed old "90% Freiraum" rule; introduced tight framing (subject filling 85–90% of frame with minimal margins).
  - Enforced 100% pure solid white background (`#FFFFFF`, zero parchment texture) for standees to prevent laser soot/charring.
- **Armory & Equipment Expanded (`components/card_list.md`):**
  - Expanded loot deck from 36 to **54 cards**.
  - Weapons expanded from 13 to **24** (added reach polearms, armor-piercing dwarven hammer, flail, parry dagger, repeating crossbow).
  - Armor/Shields/Helmets doubled from 6 to **12** (added Stadtgarde Eisenhelm, Hörnerhelm, Buckler, Stachelschild, Zwergen-Schuppenpanzer).
- **To-Do Added:**
  - Create dedicated `rules/conditions.md` detailing comprehensive status effect mechanics and tabletop handling (especially *Betäubt / Stunned* prone standee placement, duration, saves, and immunities).

### Session 8 — 2026-11-04 (Campaign Monte Carlo Balancing & Dynamic Victory Tiers)
- **Multi-Scenario Simulator Built & Run (`balance_simulator_campaign.py`):**
  - Extended previous Scenario 01 simulator into a full 5-scenario Monte Carlo testing suite (50,000 runs total).
  - Modeled Encounter Deck draws, Door-Tokens, boss opening strikes, Predator Initiative (worgs/ghouls act first in round 1), and fatigue/rest mechanics.
- **Balancing Insights & Rule Formalization:**
  - *Scenario 01 (Tutorial):* Confirmed rock-solid at **99.7%** win rate.
  - *Aktionsökonomie Insight:* 4 heroes (5 attacks/round) naturally overpower standard minion counts unless attrition is preserved.
  - *Victory/Retreat Rule Adopted in `campaign_guide.md`:*
    - **Heroischer Sieg:** Main objective completed AND at most 1 hero K.O. (heroes make it home victorious with full bounty).
    - **Verwundeter Rückzug:** 2+ heroes K.O. forces an emergency evacuation; scenario must be retreated/re-attempted, triggering injury scar checks.
    - **Totalverlust:** All 4 heroes incapacitated (party loses loot, pays fee to be rescued).

---



### Session 9 — 2026-11-09 (Monster Cards Specification, Tarot Gutter-Fold & Asset Correlation)
- **Asset Inventory & Correlation Formalized:**
  - Correlated all 5 generated card backs (`art_assets/MasterArtwork/Cards/Card Backs`) 1-to-1 with their respective decks:
    1. Grimoire with Horned Beast Skull $\rightarrow$ **Bestiarium Imperialis** (Monsterdeck)
    2. Wheel of Fortune $\rightarrow$ **Rad des Schicksals** (Ereignisdeck)
    3. Wizard Grimoire & Astrolabe $\rightarrow$ **Codex Arcanum** (Magiedeck)
    4. Dark Dungeon Doorway $\rightarrow$ **Die Tiefen Gewölbe** (Begegnungsdeck)
    5. Night Bazaar with Lanterns $\rightarrow$ **Der Schattenbazar** (Ausrüstungsdeck)
  - Correlated all 12 color monster illustrations (`art_assets/MasterArtwork/Monsters/Color`) 1-to-1 with the complete bestiary roster in `monsters/monster_roster.md`.
- **Monster Card Standards & Design Rules:**
  - **Standard Card Format:** **Tarot ($70 \times 120\text{ mm}$ / Aspect Ratio $7:12$)** unified across all decks.
  - **Initiative Clarification & Phase Cleanup:** Removed obsolete "Phase 3" reference from card headers. Monsters activate strictly along the physical wooden **Initiative-Leiste (Tracker-Schiene)** using their fixed **`INIT: X`** stat; higher initiative acts first.
  - **Header Structure:** Threat stars (`★★☆`), fixed `INIT: X` pill, monster name (13.5 pt Cinzel Bold), and role/subtype subtitle.
  - **Illustration Frame:** Height tuned to $32\text{ mm}$ (approx. 27% of card height) with gothic darkwood border and subtle vignette, keeping full silhouette (torso, skull, weapon, shield) in sharp view.
  - **3-Zeilen Lore-Kasten:** Established a dedicated italic flavor lore block (approx. 3 lines) directly under the illustration to deepen world immersion without compromising legibility.
  - **Combat Stat Ribbon:** 4 large, high-contrast chips (❤️ Leben, 🛡️ Abwehr/VT, 👟 Bewegung, ⚔️ Angriff/Schaden) using bold 10.5 pt Cinzel numbers and distinct red highlight for damage/life.
  - **Rules & Behavior Box:**
    - Header standardized strictly to **`⚔️ VERHALTEN`** (simplified from "autonomes KI-Verhalten").
    - Descriptions formatted with full, player-friendly mechanical clarity:
      - *Ziel & Marsch:* Prioritized target selection (e.g. highest armor, nearest hero on tie).
      - *Angriff:* Exact formula (e.g. $1\text{d}6 + 2$ vs VT) and net damage.
      - *Synergien / Taktik:* Clear conditions (e.g. Schildwall $+1\text{ VT}$ when adjacent to another skeleton).
      - *Sonderregeln:* Explicit condition immunities (e.g. `Untot` immune to Poisoned & Burning damage).
    - Footer: Deck name (`Bestiarium Imperialis`), Card ID (`#03 / 12`), and bounty (`💰 1 Gold`).
- **Card Back & Typography Overlay:**
  - Card back ivory banner position mathematically calibrated at $Y = 85.7\%$ of total card height.
  - Authentic Fraktur font `UnifrakturMaguntia` (*»Bestiarium Imperialis«*) centered directly on the Midjourney banner overlay.
- **Production Template (Printable Gutter-Fold):**
  - Created [`printables/monster_card_draft_skeleton.html`](file:///c:/Users/christoph.willimzik/Agent_Bunny/RV_Quest/printables/monster_card_draft_skeleton.html).
  - Configured as an ink-saving A4 sheet: pure white background outside cards ($0\%$ ink waste on margins).
  - Exact $70 \times 120\text{ mm}$ Front Face connected to $70 \times 120\text{ mm}$ Back Face along a central dashed fold line (`▼ FALZLINIE (GUTTER-FOLD) ▼`).
  - Hairline $0.2\text{ mm}$ cut marks (Schnittmarken) for clean guillotine/cutter trimming with zero duplex misregistration.
