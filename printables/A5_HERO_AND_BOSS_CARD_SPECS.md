# A5 Hero & Boss Card Specification (Layout 1A & Back Design 2)

## 1. Physical Specifications
- **Format:** DIN A5 Landscape
- **Trim Size:** $210 \times 148\text{ mm}$ (approx. $8.27 \times 5.83\text{ inches}$)
- **Bleed Size (+3mm each side):** $216 \times 154\text{ mm}$
- **Print Resolution (300 DPI):**
  - Trim: $2480 \times 1748\text{ px}$
  - With bleed: $2551 \times 1819\text{ px}$

---

## 2. Front Face: Layout 1A ("Split View")

- **Left Column ($\approx 40\text{--}45\%$ width | $\approx 85\text{--}90\text{ mm}$ wide):**
  - **Artwork Area:** $85\text{ mm} \times 130\text{ mm}$
  - **Aspect Ratio:** **`2:3`** (Portrait)
  - **Midjourney Flag:** `--ar 2:3`
  - **Resolution @ 300 DPI:** $\approx 1000 \times 1500\text{ px}$ (upscaled: $2000 \times 3000\text{ px}$)
  - **Art Content:** Full-body standing hero/boss character in medieval woodcut style on parchment.
- **Right Column ($\approx 55\text{--}60\%$ width | $\approx 115\text{--}120\text{ mm}$ wide):**
  - Name, Archetype / Boss Title, Flavor quote.
  - Core Combat Attributes (Health / Wounds track, Movement, Defense / Armor, Stamina / Mana).
  - Signature Passives and Active Skills / Attacks.
  - Inventory / Equipment Slots (Hero) or Resistance / Threat levels (Boss).

---

## 3. Back Face: Design 2 ("Solo/Co-op AI, Lore & Setup")

### A. For Boss Cards
Designed for autonomous solo & co-op play without requiring a Game Master / Overlord:
1. **Boss Behavior & AI Matrix / Flowchart:**
   - **Targeting Priority:** Who does the boss attack? (e.g., *Lowest HP*, *Nearest Hero*, *Hero carrying relic*).
   - **Action Table (D6 / Token Draw / Health Threshold):**
     - Roll 1-2: Cleave / Melee Sweep + Push back.
     - Roll 3-4: Ranged Curse / Summon adds.
     - Roll 5-6: Devastating Ultimate Attack.
2. **Lair & Environmental Hazards:**
   - Special room rules, traps triggered at round start, or altar effects while the boss is alive.
3. **Minion Reinforcement Rules:**
   - When and where adds/skulls spawn (e.g., every 3 rounds or when bloodied).
4. **Loot & Victory Rewards:**
   - Gold, specific artifact card drop, and XP / story unlock on defeat.

### B. For Hero Cards
Designed for seamless onboarding, campaign tracking, and game table reference:
1. **Character Lore & Backstory:**
   - 1–2 paragraphs detailing origins, motivations, personal vendettas, and personality.
2. **Starting Loadout & Setup:**
   - Initial equipment cards (Weapons, Armor, Items).
   - Starting token counts (Gold, Rations, Stamina, Spell slots).
   - Starting room placement rules.
3. **Rules & Actions Cheat Sheet:**
   - Quick reference for standard turn actions (Move, Attack, Search, Rest, Interact).
   - Combat dice symbols and combat roll formulas.
   - Condition / Status effects summary (Poisoned, Stunned, Bleeding, Weakened).
4. **Downed / Dying State Summary:**
   - What happens when reaching 0 HP (bleed-out counter, revival cost, death check rules).

---

## 4. Midjourney Prompt Template (Front Artwork)
```text
[Character Name / Description], full body standing pose, dynamic heroic/menacing stance, medieval woodcut engraving style, intricate hatchwork, high contrast ink lines, aged parchment background, clean isolated character --ar 2:3 --v 6.1
```
