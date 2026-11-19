# RV_Quest Project Index & Context Map

> **TOKEN OPTIMIZATION RULE FOR AI AGENTS:**
> **DO NOT** read large files (>15 KB) like `PROJECT_CONTEXT.md` or any `.html` card sheets into memory completely.
> Instead, consult this index first, then read only specific targeted line ranges or use `tools/find_card.ps1`.

---

## 1. Project Directory Map

| Directory | What it contains | When to read |
| :--- | :--- | :--- |
| `rules/` | Core mechanics, combat, conditions, exploration. Small markdown files (<12 KB each). | Specific rule lookups. |
| `adventures/` | Scenario 01-05 gamebook guides and quest outlines. | Quest flow, scenario room descriptions. |
| `characters/` | Character roster (4 core classes) and starter cards/spells. | Class stats, starting decks, spells. |
| `monsters/` | Monster roster and stats (`monster_roster.md`). | Monster baseline stats, abilities. |
| `components/` | Item card lists (`card_list.md`) and encounters (`encounter_cards.md`). | Loot tables, equipment inventory. |
| `printables/` | Printable HTML decks (A4 gutterfold), Midjourney prompt batches, and specs. | **Caution:** Card sheets are 35-55 KB each. Do targeted reads only. |
| `tools/` | Automation scripts (card sheet generator, balance simulators, fast card finder). | Execution or inspection. |

---

## 2. Fast File Reference Guide

### Rules & Mechanics
- [core_rules.md](file:///c:/Users/christoph.willimzik/Agent_Bunny/RV_Quest/rules/core_rules.md): Turn structure, action economy, core checks.
- [combat.md](file:///c:/Users/christoph.willimzik/Agent_Bunny/RV_Quest/rules/combat.md): Attack/defense dice, line of sight, range, damage resolution.
- [conditions.md](file:///c:/Users/christoph.willimzik/Agent_Bunny/RV_Quest/rules/conditions.md): Poisoned, Stunned, Burning, Weakened, etc.
- [exploration.md](file:///c:/Users/christoph.willimzik/Agent_Bunny/RV_Quest/rules/exploration.md): Room discovery, doors, traps, resting.

### Cards, Equipment & Monsters
- [components/card_list.md](file:///c:/Users/christoph.willimzik/Agent_Bunny/RV_Quest/components/card_list.md): Master inventory of Weapons, Armor, Trinkets, Consumables.
- [characters/starter_cards_and_spells.md](file:///c:/Users/christoph.willimzik/Agent_Bunny/RV_Quest/characters/starter_cards_and_spells.md): Class starter cards and spell decks.
- [monsters/monster_roster.md](file:///c:/Users/christoph.willimzik/Agent_Bunny/RV_Quest/monsters/monster_roster.md): Goblin, Skeleton, Wight, Ghoul, Spider, Void Cultist, Bosses.

### Printables & HTML Sheets (Heavy Files - Use Targeted Reads)
- `printables/armor_cards_all_gutterfold_a4.html` (48 KB): All armor card templates + artwork bindings.
- `printables/monster_cards_all_gutterfold_a4.html` (50 KB): Monster tarot cards + stat blocks.
- `printables/boss_cards_a5_gutterfold.html` (53 KB): A5 boss sheets (Malakor, Blood Golem, Zombie Giant).
- `printables/MONSTER_CARDS_PRODUCTION_SPECS.md` (11 KB): Production layout specs, dimensions (70x120mm / A5), margins.
- `printables/BATCH_PERMUTATION_PROMPTS_*.md`: Midjourney prompts for each equipment/monster type.

---

## 3. Fast Card / Asset Search

To inspect or find cards without burning tokens reading full HTML sheets, run this PowerShell snippet from `RV_Quest/`:

```powershell
# Search for any card or monster by name across all printable decks:
Select-String -Path "printables\*.html" -Pattern "card-title.*Leather" -Context 0, 10
# Or use the quick helper:
powershell -File tools\find_card.ps1 -Name "Eisenpanzer"
```

