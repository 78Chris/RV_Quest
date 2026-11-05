"""
Accurate Monte-Carlo Balance Simulator for "Von Helden und Monstern"
===================================================================
Simulates Scenario 01 ("Die verfluchte Krypta von Dun-Karr") across 10,000 runs
using the exact monster AI priority rules defined in `monster_roster.md`.

Targeting AI Rules:
- Skelettkrieger: Targets hero with HIGHEST armor/ZÄH (Nordland Berserker tank).
- Riesenspinne: Targets hero with lowest ZÄH (Magiegelehrte / Goblin).
- Grabunhold (Boss): Targets Berserker / highest damage dealer; uses Rundumschlag when >= 2 heroes adjacent.
- Goblin Passive: "Durchwuseln" + Meucheln from shadows.
- Berserker Rage: Triggers at <= 6 HP (+1 KRA, -1 ZÄH).
- Revive: Once per room, an ally can revive an incapacitated hero to 1 LP (per co-op core rules).

Large Monster Rule (v2 — added 2026-10-29):
- Große Monster (Grabunhold, Blutgolem) occupy a 1×2 tile footprint.
- Heroes must approach from the side; at most 3 heroes can be adjacent simultaneously
  (vs 4 for a normal 1×1 monster). This is modelled by giving each hero a `LARGE_BLOCK_CHANCE`
  probability of being unable to reach the monster in a given round due to positioning.
- Large monsters also cannot enter 1-tile corridors (not modelled — scenario maps handle this).
- Run with `large_monster_rules=True` (default) or `False` to compare impact.
"""

import random
from dataclasses import dataclass
from typing import List, Dict

def roll_d6() -> int:
    return random.randint(1, 6)

def roll_advantage(attr: int) -> tuple[int, bool]:
    d1, d2 = roll_d6(), roll_d6()
    chosen = max(d1, d2)
    return (chosen + attr), (chosen == 6)

def roll_standard(attr: int) -> tuple[int, bool]:
    d = roll_d6()
    return (d + attr), (d == 6)

@dataclass
class Hero:
    name: str
    max_hp: int
    current_hp: int
    kra: int
    ges: int
    zah: int
    ver: int
    lis: int
    vt: int
    armor_reduc: int
    weapon_dmg: int
    fatigue: int = 0
    max_fatigue: int = 5
    is_ko: bool = False

    def reset(self):
        self.current_hp = self.max_hp
        self.fatigue = 0
        self.is_ko = False

    def take_damage(self, raw_dmg: int):
        effective = max(1, raw_dmg - self.armor_reduc)
        self.current_hp -= effective
        if self.current_hp <= 0:
            self.current_hp = 0
            self.is_ko = True

@dataclass
class Monster:
    name: str
    max_hp: int
    current_hp: int
    vt: int
    atk_bonus: int
    dmg: int
    armor_reduc: int = 0
    monster_type: str = "skeleton"  # "skeleton", "spider", "boss", "large_boss"
    is_large: bool = False           # True = 1x2 tile footprint (Grabunhold, Blutgolem)
    is_dead: bool = False

    def take_damage(self, raw_dmg: int):
        effective = max(1, raw_dmg - self.armor_reduc)
        self.current_hp -= effective
        if self.current_hp <= 0:
            self.current_hp = 0
            self.is_dead = True

def select_target_for_monster(monster: Monster, alive_heroes: List[Hero]) -> Hero:
    if monster.monster_type == "skeleton":
        # Skelettkrieger KI: Seeks strongest resistance -> Highest armor / HP (Berserker)
        return max(alive_heroes, key=lambda h: (h.armor_reduc, h.current_hp))
    elif monster.monster_type == "spider":
        # Spider KI: Seeks weakest prey -> Lowest ZÄH / HP (Magie or Goblin)
        return min(alive_heroes, key=lambda h: (h.zah, h.current_hp))
    elif monster.monster_type == "boss":
        # Boss Grabunhold KI: Attacks Berserker / biggest threat
        berserker = [h for h in alive_heroes if "Berserker" in h.name]
        return berserker[0] if berserker else alive_heroes[0]
    return alive_heroes[0]

# Probability that a given hero is blocked from reaching a large monster in a round
# (models the 1x2 footprint: only ~3 of 4 heroes can be adjacent simultaneously).
# Set to 0.25 = one hero slot out of four is typically unavailable.
LARGE_BLOCK_CHANCE = 0.25

def simulate_room_combat(heroes: List[Hero], monsters: List[Monster],
                         large_monster_rules: bool = True) -> bool:
    round_limit = 20
    current_round = 0
    revive_used = False

    while current_round < round_limit:
        current_round += 1

        active_heroes = [h for h in heroes if not h.is_ko]
        active_monsters = [m for m in monsters if not m.is_dead]

        if not active_monsters:
            return True
        if not active_heroes:
            return False

        # --- HERO PHASE ---
        for hero in active_heroes:
            alive_m = [m for m in monsters if not m.is_dead]
            if not alive_m:
                break

            # Target priority for heroes: focus lowest HP monster to eliminate activations
            target = min(alive_m, key=lambda m: m.current_hp)

            # Large monster blocking: hero may be unable to reach the monster this round
            if large_monster_rules and target.is_large:
                if random.random() < LARGE_BLOCK_CHANCE:
                    continue  # Hero is positionally blocked — skips attack this round

            if "Berserker" in hero.name:
                kra_bonus = hero.kra + (1 if hero.current_hp <= hero.max_hp // 2 else 0)
                tot, crit = roll_standard(kra_bonus)
                if tot >= target.vt or crit:
                    dmg = hero.weapon_dmg + (1 if crit else 0)
                    target.take_damage(dmg)

            elif "Kriegstänzerin" in hero.name:
                # 2 attacks
                for _ in range(2):
                    alive_m = [m for m in monsters if not m.is_dead]
                    if not alive_m:
                        break
                    target = min(alive_m, key=lambda m: m.current_hp)
                    tot, crit = roll_standard(hero.ges)
                    if tot >= target.vt or crit:
                        dmg = hero.weapon_dmg + (1 if crit else 0)
                        target.take_damage(dmg)

            elif "Goblin" in hero.name:
                # Flanking advantage
                tot, crit = roll_advantage(hero.lis)
                if tot >= target.vt or crit:
                    dmg = hero.weapon_dmg + 1 + (1 if crit else 0)
                    target.take_damage(dmg)

            elif "Magiegelehrte" in hero.name:
                if hero.fatigue < hero.max_fatigue:
                    hero.fatigue += 1
                    tot, crit = roll_standard(hero.ver)
                    if tot >= target.vt or crit:
                        dmg = 3 + (1 if crit else 0)
                        target.take_damage(dmg)
                else:
                    tot, crit = roll_standard(hero.kra)
                    if tot >= target.vt or crit:
                        dmg = 1 + (1 if crit else 0)
                        target.take_damage(dmg)

        # --- MONSTER PHASE ---
        alive_monsters = [m for m in monsters if not m.is_dead]
        alive_heroes = [h for h in heroes if not h.is_ko]

        if not alive_heroes:
            return False

        for monster in alive_monsters:
            alive_heroes = [h for h in heroes if not h.is_ko]
            if not alive_heroes:
                break

            target_hero = select_target_for_monster(monster, alive_heroes)

            if monster.monster_type == "boss" and len(alive_heroes) >= 2:
                # Rundumschwung hits all heroes (large monster: adjacent to either tile)
                for h in alive_heroes:
                    tot, crit = roll_standard(monster.atk_bonus)
                    if tot >= h.vt or crit:
                        dmg = 2 + (1 if crit else 0)
                        h.take_damage(dmg)
            else:
                tot, crit = roll_standard(monster.atk_bonus)
                if tot >= target_hero.vt or crit:
                    dmg = monster.dmg + (1 if crit else 0)
                    target_hero.take_damage(dmg)

        # --- CO-OP REVIVE RULE (1 Action to revive KO ally to 1 HP) ---
        if not revive_used:
            ko_heroes = [h for h in heroes if h.is_ko]
            alive_heroes = [h for h in heroes if not h.is_ko]
            if ko_heroes and alive_heroes and len(alive_monsters) <= 1:
                ko_heroes[0].is_ko = False
                ko_heroes[0].current_hp = 1
                revive_used = True

    return any(not h.is_ko for h in heroes)


def run_comprehensive_simulation(num_runs: int = 10000,
                                 large_monster_rules: bool = True) -> Dict:
    victories = 0
    wipes_by_room = {2: 0, 3: 0, 4: 0}
    hero_ko_counts = {"Berserker": 0, "Kriegstänzerin": 0, "Goblin": 0, "Magiegelehrte": 0}
    hp_totals = {"Berserker": 0, "Kriegstänzerin": 0, "Goblin": 0, "Magiegelehrte": 0}

    for _ in range(num_runs):
        heroes = [
            Hero("Nordland Berserker", max_hp=12, current_hp=12, kra=3, ges=1, zah=3, ver=0, lis=1, vt=5, armor_reduc=1, weapon_dmg=3),
            Hero("Elfische Kriegstänzerin", max_hp=10, current_hp=10, kra=2, ges=3, zah=2, ver=1, lis=1, vt=6, armor_reduc=1, weapon_dmg=2),
            Hero("Goblin Halsabschneider", max_hp=8, current_hp=8, kra=1, ges=2, zah=1, ver=1, lis=3, vt=5, armor_reduc=1, weapon_dmg=1),
            Hero("Magiegelehrte", max_hp=8, current_hp=8, kra=0, ges=1, zah=1, ver=3, lis=2, vt=5, armor_reduc=1, weapon_dmg=1)
        ]

        # Room 1: Entrance (no combat)

        # Room 2: Vorkammer (2 Skeleton Warriors)
        m2 = [
            Monster("Skelett 1", 4, 4, vt=6, atk_bonus=2, dmg=2, monster_type="skeleton"),
            Monster("Skelett 2", 4, 4, vt=6, atk_bonus=2, dmg=2, monster_type="skeleton")
        ]
        if not simulate_room_combat(heroes, m2, large_monster_rules):
            wipes_by_room[2] += 1
            continue

        # Rest between R2 and R3
        for h in heroes:
            if "Berserker" in h.name:
                h.current_hp = min(h.max_hp, h.current_hp + 2)  # Trockenfleisch
            if "Magiegelehrte" in h.name:
                h.fatigue = max(0, h.fatigue - 2)

        # Room 3: Säulengewölbe (3 Skeleton Warriors + 1 Giant Spider)
        m3 = [
            Monster("Skelett 1", 4, 4, vt=6, atk_bonus=2, dmg=2, monster_type="skeleton"),
            Monster("Skelett 2", 4, 4, vt=6, atk_bonus=2, dmg=2, monster_type="skeleton"),
            Monster("Skelett 3", 4, 4, vt=6, atk_bonus=2, dmg=2, monster_type="skeleton"),
            Monster("Spinne", 5, 5, vt=5, atk_bonus=2, dmg=1, monster_type="spider")
        ]
        if not simulate_room_combat(heroes, m3, large_monster_rules):
            wipes_by_room[3] += 1
            continue

        # Rest before Boss: Potion used on lowest HP hero
        lowest = min(heroes, key=lambda h: h.current_hp)
        lowest.current_hp = min(lowest.max_hp, lowest.current_hp + 3)
        for h in heroes:
            if "Magiegelehrte" in h.name:
                h.fatigue = max(0, h.fatigue - 2)

        # Room 4: Boss Chamber — Grabunhold (GROSS: 1x2 tiles) + 2 Skeletons
        m4 = [
            Monster("Grabunhold (Boss)", 14, 14, vt=7, atk_bonus=3, dmg=3,
                    armor_reduc=1, monster_type="boss", is_large=True),
            Monster("Skelett 1", 4, 4, vt=6, atk_bonus=2, dmg=2, monster_type="skeleton"),
            Monster("Skelett 2", 4, 4, vt=6, atk_bonus=2, dmg=2, monster_type="skeleton")
        ]
        if not simulate_room_combat(heroes, m4, large_monster_rules):
            wipes_by_room[4] += 1
            continue

        # Track stats for victory run
        victories += 1
        for h in heroes:
            if "Berserker" in h.name: short_name = "Berserker"
            elif "Kriegstänzerin" in h.name: short_name = "Kriegstänzerin"
            elif "Goblin" in h.name: short_name = "Goblin"
            elif "Magiegelehrte" in h.name: short_name = "Magiegelehrte"
            else: short_name = h.name.split()[0]

            hp_totals[short_name] += h.current_hp
            if h.is_ko:
                hero_ko_counts[short_name] += 1

    return {
        "runs": num_runs,
        "large_monster_rules": large_monster_rules,
        "victories": victories,
        "win_rate": (victories / num_runs) * 100.0,
        "wipes_by_room": wipes_by_room,
        "avg_hp_end": {k: v / max(1, victories) for k, v in hp_totals.items()},
        "ko_rate_end": {k: (v / max(1, victories)) * 100.0 for k, v in hero_ko_counts.items()}
    }

def print_results(res: Dict) -> None:
    rule_label = "MIT Groß-Monster-Regel" if res["large_monster_rules"] else "OHNE Groß-Monster-Regel"
    print("=" * 65)
    print(f"MONTE-CARLO SIMULATION: SCENARIO 01 — {rule_label}")
    print(f"({res['runs']:,} Runs)")
    print("=" * 65)
    print(f"Gesamtsieg-Quote:          {res['win_rate']:.2f}%")
    print(f"TPK in Raum 2:             {res['wipes_by_room'][2]} ({res['wipes_by_room'][2]/res['runs']*100:.2f}%)")
    print(f"TPK in Raum 3:             {res['wipes_by_room'][3]} ({res['wipes_by_room'][3]/res['runs']*100:.2f}%)")
    print(f"TPK beim Boss (Raum 4):    {res['wipes_by_room'][4]} ({res['wipes_by_room'][4]/res['runs']*100:.2f}%)")
    print("\nDurchschnittliche verbleibende LP bei Sieg:")
    for hero, hp in res['avg_hp_end'].items():
        print(f"  - {hero:16s}: {hp:.2f} LP")
    print("\nK.O.-Quote am Ende des Bosskampfes:")
    for hero, ko in res['ko_rate_end'].items():
        print(f"  - {hero:16s}: {ko:.2f}%")
    print("=" * 65)

if __name__ == "__main__":
    NUM_RUNS = 10_000

    # Run 1: With large monster positional blocking (new rule)
    res_with = run_comprehensive_simulation(NUM_RUNS, large_monster_rules=True)
    print_results(res_with)

    # Run 2: Without large monster rule (baseline, matches old sim)
    res_without = run_comprehensive_simulation(NUM_RUNS, large_monster_rules=False)
    print_results(res_without)

    # Delta summary
    print()
    print("IMPACT DER GROß-MONSTER-REGEL (Delta):")
    delta_win = res_with["win_rate"] - res_without["win_rate"]
    delta_boss = res_with["wipes_by_room"][4] - res_without["wipes_by_room"][4]
    print(f"  Siegquote:        {res_without['win_rate']:.2f}% -> {res_with['win_rate']:.2f}%  ({delta_win:+.2f}%)")
    print(f"  Boss-Wipes (R4):  {res_without['wipes_by_room'][4]} -> {res_with['wipes_by_room'][4]}  ({delta_boss:+d})")
    print()
    if res_with["win_rate"] >= 90.0:
        print("[OK] Szenario 01 ist BALANCIERT mit Groß-Monster-Regel (Siegquote >= 90%).")
    elif res_with["win_rate"] >= 75.0:
        print("[!]  Szenario 01 ist HERAUSFORDERND mit Groß-Monster-Regel — prüfe, ob das gewünscht ist.")
    else:
        print("[!!] Szenario 01 ist ZU SCHWER mit Groß-Monster-Regel — Balancing anpassen!")
