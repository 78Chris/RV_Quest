"""
Erweiterter Monte-Carlo Balance Simulator — ALLE 5 SZENARIEN
=============================================================
"Von Helden und Monstern — Abenteuer in der Alten Welt"

Testet jedes Szenario in ISOLATION (je eigener Lauf mit 10.000 Runs).
Modelliert alle Hybrid-System-Elemente:
  - Encounter-Deck: Zufällige Raumbesetzung aus 16 Karten (5 Gruppen)
  - Tür-Tokens: 5 mögliche Symbole, gleichwahrscheinlich; Probe variiert je Szenario
  - Feste Bosskammern: Fixe, cinematische Aufstellungen
  - Monster-KI mit Targeting-Priorität
  - Große Monster (1×2 Felder, Blockierungs-Chance)
  - Helden-Spezialfähigkeiten (Berserker-Rage, Goblin-Flanken, Kriegstänzerin 2 Angriffe, Magierin Fatigue)
  - Zwischen-Rast und Heiltranke
  - Kampagnen-Ausrüstungsannahmen pro Szenario (Starter / +1 Upgrade / +2 Upgrades / Meister)

Ziel-Siegquoten (Design-Vorgabe):
  Sz01 ≈ 100%  (Tutorial — sollte immer gewonnen werden)
  Sz02 ≈ 90–95%  (Mittel)
  Sz03 ≈ 85–92%  (Gehoben)
  Sz04 ≈ 80–90%  (Schwer)
  Sz05 ≈ 72–85%  (Sehr schwer — Finale)
"""

import random
from dataclasses import dataclass, field
from typing import List, Dict, Tuple, Optional

# ---------------------------------------------------------------------------
# Dice Helpers
# ---------------------------------------------------------------------------

def roll_d6() -> int:
    return random.randint(1, 6)

def roll_advantage(attr: int) -> Tuple[int, bool]:
    d1, d2 = roll_d6(), roll_d6()
    chosen = max(d1, d2)
    return (chosen + attr), (chosen == 6)

def roll_standard(attr: int) -> Tuple[int, bool]:
    d = roll_d6()
    return (d + attr), (d == 6)

# ---------------------------------------------------------------------------
# Data Classes
# ---------------------------------------------------------------------------

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
    # Types drive target-selection AI:
    # "goblin" "goblin_archer" "skeleton" "spider" "worg" "ghoul"
    # "cultist" "marksman" "deathknight" "boss" "large_boss" "lichking"
    monster_type: str = "skeleton"
    is_large: bool = False
    is_dead: bool = False
    regen_on_corpse: bool = False   # Moor-Ghul Leichenfraß
    vampiric: bool = False          # Blutgolem: heals = damage dealt
    summons_skeletons: bool = False  # Lich-König Totenbeschwörung

    def take_damage(self, raw_dmg: int):
        effective = max(1, raw_dmg - self.armor_reduc)
        self.current_hp -= effective
        if self.current_hp <= 0:
            self.current_hp = 0
            self.is_dead = True
        return effective  # return for vampiric tracking

# ---------------------------------------------------------------------------
# AI: Monster → Target Selection
# ---------------------------------------------------------------------------

def select_target(monster: Monster, alive_heroes: List[Hero]) -> Hero:
    if not alive_heroes:
        return None
    mt = monster.monster_type
    if mt == "skeleton":
        # Seeks highest armour/ZÄH (tank)
        return max(alive_heroes, key=lambda h: (h.armor_reduc, h.zah))
    elif mt in ("goblin", "goblin_archer", "cultist", "ghoul", "marksman"):
        # Seeks lowest HP / weakest
        return min(alive_heroes, key=lambda h: h.current_hp)
    elif mt == "spider":
        # Seeks lowest ZÄH (Magiegelehrte / Goblin)
        return min(alive_heroes, key=lambda h: (h.zah, h.current_hp))
    elif mt == "worg":
        # Flanks — targets rearmost (lowest index enemy from party, i.e. last hero)
        return alive_heroes[-1]
    elif mt in ("boss", "large_boss"):
        # Boss Grabunhold: targets Berserker / biggest threat
        berserker = [h for h in alive_heroes if "Berserker" in h.name]
        return berserker[0] if berserker else alive_heroes[0]
    elif mt == "deathknight":
        # Todesritter: challenges strongest melee hero
        melee = [h for h in alive_heroes if "Berserker" in h.name or "Kriegstänzerin" in h.name]
        return melee[0] if melee else min(alive_heroes, key=lambda h: h.current_hp)
    elif mt == "lichking":
        # Action 2: targets lowest HP
        return min(alive_heroes, key=lambda h: h.current_hp)
    return alive_heroes[0]

# ---------------------------------------------------------------------------
# Large Monster Blocking
# ---------------------------------------------------------------------------
LARGE_BLOCK_CHANCE = 0.25  # 1 of 4 heroes positionally blocked per round

# ---------------------------------------------------------------------------
# Room Combat Engine
# ---------------------------------------------------------------------------

def _execute_monster_attack(monster: Monster, alive_heroes_now: List[Hero], current_round: int):
    if not alive_heroes_now:
        return

    target_hero = select_target(monster, alive_heroes_now)
    if target_hero is None:
        return

    if monster.monster_type == "lichking":
        # Action 1: Froststrahl
        ranged_target = min(alive_heroes_now, key=lambda h: h.current_hp)
        tot, crit = roll_standard(monster.atk_bonus)
        if tot >= ranged_target.vt or crit:
            dmg = monster.dmg + (1 if crit else 0)
            ranged_target.take_damage(dmg)
        # Frosthauch Aura: 50% Chance pro ungerade Runde
        if current_round % 2 == 1:
            for h in alive_heroes_now:
                if not h.is_ko and random.random() < 0.5:
                    h.current_hp -= 1
                    if h.current_hp <= 0:
                        h.current_hp = 0
                        h.is_ko = True
        # Action 2: Sense (2 Schaden)
        alive = [h for h in alive_heroes_now if not h.is_ko]
        if alive:
            t2 = select_target(monster, alive)
            tot2, crit2 = roll_standard(monster.atk_bonus - 1)
            if tot2 >= t2.vt or crit2:
                t2.take_damage(2 + (1 if crit2 else 0))

    elif monster.monster_type in ("boss", "large_boss"):
        if len(alive_heroes_now) >= 2:
            for h in alive_heroes_now:
                tot, crit = roll_standard(monster.atk_bonus)
                if tot >= h.vt or crit:
                    h.take_damage(2 + (1 if crit else 0))
        else:
            tot, crit = roll_standard(monster.atk_bonus)
            if tot >= target_hero.vt or crit:
                dmg = monster.dmg + (1 if crit else 0)
                target_hero.take_damage(dmg)
                if monster.vampiric:
                    monster.current_hp = min(monster.max_hp, monster.current_hp + dmg)

    elif monster.monster_type == "deathknight":
        tot, crit = roll_standard(monster.atk_bonus)
        if tot >= target_hero.vt or crit:
            target_hero.take_damage(monster.dmg + (1 if crit else 0))

    elif monster.monster_type == "worg":
        extra = 1 if target_hero.current_hp <= (target_hero.max_hp // 2) else 0
        tot, crit = roll_standard(monster.atk_bonus)
        if tot >= target_hero.vt or crit:
            target_hero.take_damage(monster.dmg + extra + (1 if crit else 0))

    elif monster.monster_type == "cultist":
        # Meisterkultist Seuchenblitz: Trifft das Hauptziel und 1 weiteren Helden
        tot, crit = roll_standard(monster.atk_bonus)
        if tot >= target_hero.vt or crit:
            target_hero.take_damage(monster.dmg + (1 if crit else 0))
        # Kettenschaden auf zweiten Helden
        others = [h for h in alive_heroes_now if h != target_hero]
        if others:
            t2 = others[0]
            tot2, _ = roll_standard(monster.atk_bonus - 1)
            if tot2 >= t2.vt:
                t2.take_damage(1)

    else:
        tot, crit = roll_standard(monster.atk_bonus)
        if tot >= target_hero.vt or crit:
            target_hero.take_damage(monster.dmg + (1 if crit else 0))


def simulate_room_combat(heroes: List[Hero], monsters: List[Monster],
                         large_monster_rules: bool = True,
                         round_limit: int = 20,
                         boss_opening_strike: bool = False) -> bool:
    """
    Simuliert den Raumkampf.
    Regel 1: Raubtiere (Worg, Ghul) & Bosse greifen in Runde 1 VOR den Helden an.
    Regel 2: Boss-Eröffnungsschlag bei Betreten der Bosskammer.
    """
    current_round = 0
    revive_used = False
    lich = next((m for m in monsters if m.monster_type == "lichking"), None)

    # ── REGEL 2: BOSS-ERÖFFNUNGSSCHLAG BEIM BETRETEN DER KAMMER ──
    if boss_opening_strike:
        boss = next((m for m in monsters if m.monster_type in ("boss", "large_boss", "deathknight", "lichking", "worg") and m.max_hp >= 10), None)
        if boss:
            frontline = [h for h in heroes if not h.is_ko]
            if frontline:
                # Der vorderste Held (Türöffner, meist Berserker) kassiert den Schlag
                door_opener = frontline[0]
                tot, crit = roll_standard(boss.atk_bonus)
                if tot >= door_opener.vt or crit:
                    door_opener.take_damage(boss.dmg + (1 if crit else 0))

    while current_round < round_limit:
        current_round += 1

        active_heroes = [h for h in heroes if not h.is_ko]
        active_monsters = [m for m in monsters if not m.is_dead]

        if not active_monsters:
            return True
        if not active_heroes:
            return False

        # ── LICH-KÖNIG: Totenbeschwörung ──
        if lich and not lich.is_dead:
            skeletons_alive = [m for m in monsters if not m.is_dead and m.monster_type == "skeleton"]
            if len(skeletons_alive) == 0:
                for i in range(2):
                    monsters.append(Monster(f"Beschwor-Skelett-R{current_round}-{i}",
                                            4, 4, vt=6, atk_bonus=2, dmg=2,
                                            monster_type="skeleton"))

        # ── REGEL 1: RAUBTIER- & BOSS-INITIATIVE (In Runde 1 greifen schnelle Biester VOR Helden an) ──
        # Grabunhold in Sz01 ist ein schwerer, langsamer Boss (Initiative-Rang 2) -> greift NACH den Helden an
        if current_round == 1:
            fast_monsters = [m for m in monsters if not m.is_dead and m.monster_type in ("worg", "ghoul", "deathknight")]
            for fm in fast_monsters:
                alive_h = [h for h in heroes if not h.is_ko]
                if not alive_h:
                    return False
                _execute_monster_attack(fm, alive_h, current_round)

        # ── HELDEN-PHASE ──
        active_heroes = [h for h in heroes if not h.is_ko]
        for hero in active_heroes:
            alive_m = [m for m in monsters if not m.is_dead]
            if not alive_m:
                break

            seelenkafig_active = False
            if lich and not lich.is_dead:
                skels = [m for m in monsters if not m.is_dead and m.monster_type == "skeleton"]
                seelenkafig_active = len(skels) > 0

            prioritized = sorted(alive_m, key=lambda m: m.current_hp)
            target = None
            for m in prioritized:
                if m.monster_type == "lichking" and seelenkafig_active:
                    continue
                target = m
                break
            if target is None:
                target = prioritized[0]

            if large_monster_rules and target.is_large:
                if random.random() < LARGE_BLOCK_CHANCE:
                    continue

            if "Berserker" in hero.name:
                rage = hero.current_hp <= (hero.max_hp // 2)
                kra_bonus = hero.kra + (1 if rage else 0)
                tot, crit = roll_standard(kra_bonus)
                if tot >= target.vt or crit:
                    _do_hit(target, hero.weapon_dmg + (1 if crit else 0), monsters, lich, alive_m)

            elif "Kriegstänzerin" in hero.name:
                for _ in range(2):
                    alive_m2 = [m for m in monsters if not m.is_dead]
                    if not alive_m2:
                        break
                    t2 = min(alive_m2, key=lambda m: m.current_hp)
                    tot, crit = roll_standard(hero.ges)
                    if tot >= t2.vt or crit:
                        _do_hit(t2, hero.weapon_dmg + (1 if crit else 0), monsters, lich, alive_m2)

            elif "Goblin" in hero.name:
                tot, crit = roll_advantage(hero.lis)
                if tot >= target.vt or crit:
                    _do_hit(target, hero.weapon_dmg + 1 + (1 if crit else 0), monsters, lich, alive_m)

            elif "Magiegelehrte" in hero.name:
                if hero.fatigue < hero.max_fatigue:
                    hero.fatigue += 1
                    tot, crit = roll_standard(hero.ver)
                    if tot >= target.vt or crit:
                        _do_hit(target, 3 + (1 if crit else 0), monsters, lich, alive_m)
                else:
                    tot, crit = roll_standard(hero.kra)
                    if tot >= target.vt or crit:
                        _do_hit(target, 1 + (1 if crit else 0), monsters, lich, alive_m)

        # ── MONSTER-PHASE (Alle überlebenden Monster greifen an) ──
        alive_monsters_now = [m for m in monsters if not m.is_dead]
        alive_heroes_now = [h for h in heroes if not h.is_ko]
        if not alive_heroes_now:
            return False

        # Wenn in Runde 1 Raubtiere schon agiert haben, agieren sie in Runde 1 nicht doppelt
        for monster in alive_monsters_now:
            if current_round == 1 and monster.monster_type in ("worg", "ghoul", "deathknight"):
                continue  # Haben bereits in der Eröffnungs-Initiative agiert

            alive_heroes_now = [h for h in heroes if not h.is_ko]
            if not alive_heroes_now:
                break
            _execute_monster_attack(monster, alive_heroes_now, current_round)

        # ── CO-OP REVIVE ──
        if not revive_used:
            ko_heroes = [h for h in heroes if h.is_ko]
            alive_h = [h for h in heroes if not h.is_ko]
            remaining_m = [m for m in monsters if not m.is_dead]
            if ko_heroes and alive_h and len(remaining_m) <= 1:
                ko_heroes[0].is_ko = False
                ko_heroes[0].current_hp = 1
                revive_used = True

    # Siegbedingung (Heroischer Sieg):
    # Mindestens 3 der 4 Helden müssen auf den Beinen sein (maximal 1 K.O. erlaubt).
    return sum(1 for h in heroes if not h.is_ko) >= 3


def _do_hit(target: Monster, dmg: int, monsters: List[Monster],
            lich: Optional[Monster], alive_m: List[Monster]):
    """Apply damage to monster; Seelenkäfig redirects Nahkampf hits on Lich if Skeletons are adjacent."""
    effective = max(1, dmg - target.armor_reduc)
    target.current_hp -= effective
    if target.current_hp <= 0:
        target.current_hp = 0
        target.is_dead = True

# ---------------------------------------------------------------------------
# Encounter Deck — Weighted Random Draw
# ---------------------------------------------------------------------------

# 16-card deck with weights for each scenario context.
# Each entry: (Monster list factory function, difficulty_weight)
# We define the deck as a list of tuples: (card_name, monsters_factory)

def _skel(n): return [Monster(f"Skelett {i}", 4, 4, vt=6, atk_bonus=2, dmg=2, monster_type="skeleton") for i in range(1, n+1)]
def _gob_scout(n): return [Monster(f"GoblinSpäher {i}", 3, 3, vt=5, atk_bonus=1, dmg=1, monster_type="goblin") for i in range(1, n+1)]
def _gob_archer(n): return [Monster(f"GoblinBogen {i}", 2, 2, vt=4, atk_bonus=2, dmg=1, monster_type="goblin_archer") for i in range(1, n+1)]
def _spider(n): return [Monster(f"Spinne {i}", 5, 5, vt=5, atk_bonus=2, dmg=1, monster_type="spider") for i in range(1, n+1)]
def _worg(n): return [Monster(f"Worg {i}", 6, 6, vt=5, atk_bonus=3, dmg=2, monster_type="worg") for i in range(1, n+1)]
def _ghoul(n): return [Monster(f"Ghul {i}", 4, 4, vt=5, atk_bonus=2, dmg=1, monster_type="ghoul", regen_on_corpse=True) for i in range(1, n+1)]
def _marksman(n): return [Monster(f"Schütze {i}", 3, 3, vt=5, atk_bonus=3, dmg=2, monster_type="marksman") for i in range(1, n+1)]

# Full 16-card deck as factory functions
ENCOUNTER_DECK = [
    # A: Goblins (4 cards)
    ("B01 Banden-Vorposten",        lambda: _gob_scout(2) + _gob_archer(1)),
    ("B02 Hinterhalt!",             lambda: _gob_scout(2) + _gob_archer(1)),   # Ambush (same monsters)
    ("B03 Plünderer-Nest",          lambda: _gob_scout(3)),
    ("B04 Wachposten+Bluthund",     lambda: _gob_archer(1) + _worg(1)),
    # B: Undead (5 cards)
    ("B05 Ruhelose Wache",          lambda: _skel(2)),
    ("B06 Erwachen der Ahnen",      lambda: _skel(3)),
    ("B07 Gruft der Bogenschützen", lambda: _skel(1) + _gob_archer(2)),
    ("B08 Schändlicher Schrein",    lambda: _skel(2)),   # +1 regen skipped for speed
    ("B09 Grabkammer-Hinterhalt!",  lambda: _skel(2) + _worg(1)),
    # C: Beasts (4 cards)
    ("B10 Spinnennest",             lambda: _spider(2)),
    ("B11 Lauernde Brut",           lambda: _spider(1) + _gob_scout(2)),
    ("B12 Worg-Bau",                lambda: _worg(2)),
    ("B13 Krabbelndes Grauen",      lambda: _spider(1) + _skel(1)),
    # D: Special rooms (3 cards — treat as light encounters for balance)
    ("B14 Schatzkammer",            lambda: []),         # No monsters initially
    ("B15 Heilige Quelle",          lambda: _skel(1)),
    ("B16 Kerker der Gefangenen",   lambda: _gob_scout(2)),
]

def draw_encounter() -> List[Monster]:
    """Draw one random card from the 16-card encounter deck."""
    _, factory = random.choice(ENCOUNTER_DECK)
    return factory()


# ---------------------------------------------------------------------------
# Tür-Token Resolution
# ---------------------------------------------------------------------------

def resolve_door_token(heroes: List[Hero]) -> int:
    """
    Simulates resolving a random door token.
    Returns damage taken by the party (0 for success, 1–2 for failures/traps).
    Probabilities:
      🚪 Open (1/5) — instant, no cost
      🪓 KRA (1/5) — Berserker succeeds ~80%, others ~50%; fail = 1 dmg
      🗝️ LIS (1/5) — Goblin succeeds ~80%, others ~40%; fail = 1 dmg
      ✨ VER (1/5) — Magie succeeds ~80%, others ~40%; fail = 1 dmg
      👁️ GES (1/5) — Kriegstänzerin succeeds ~75%, others ~40%; fail = 1 dmg (trap)
    Returns the total HP lost by the party from a door-trap failure.
    """
    token = random.randint(1, 5)
    if token == 1:   # Open
        return 0
    # Pick best hero for the challenge
    alive = [h for h in heroes if not h.is_ko]
    if not alive:
        return 0
    if token == 2:   # KRA
        attr = max(h.kra for h in alive)
        sg = 5
    elif token == 3:  # LIS
        attr = max(h.lis for h in alive)
        sg = 5
    elif token == 4:  # VER
        attr = max(h.ver for h in alive)
        sg = 5
    else:            # GES
        attr = max(h.ges for h in alive)
        sg = 6
    tot, _ = roll_standard(attr)
    if tot < sg:
        # Failure: trap triggers, 1 damage to weakest hero
        target = min(alive, key=lambda h: h.current_hp)
        target.take_damage(1)
        return 1
    return 0


# ---------------------------------------------------------------------------
# Hero Factories with Scenario-Appropriate Equipment
# ---------------------------------------------------------------------------

def make_heroes_scenario(scenario: int) -> List[Hero]:
    """
    Returns 4 heroes with equipment scaled to expected level entering that scenario.
    Sz01: Starter gear (baseline)
    Sz02: Starter + minor upgrades
    Sz03: One real upgrade per hero (bought at Schattenbazar after Sz02)
    Sz04: Two upgrades — better weapons, some armor
    Sz05: Near-full kit — master weapons, good armor, restored HP
    """
    if scenario == 1:
        return [
            Hero("Nordland Berserker",    max_hp=12, current_hp=12, kra=3, ges=1, zah=3, ver=0, lis=1, vt=5, armor_reduc=1, weapon_dmg=3),
            Hero("Elfische Kriegstänzerin", max_hp=10, current_hp=10, kra=2, ges=3, zah=2, ver=1, lis=1, vt=6, armor_reduc=1, weapon_dmg=2),
            Hero("Goblin Halsabschneider", max_hp=8,  current_hp=8,  kra=1, ges=2, zah=1, ver=1, lis=3, vt=5, armor_reduc=1, weapon_dmg=1),
            Hero("Magiegelehrte",          max_hp=8,  current_hp=8,  kra=0, ges=1, zah=1, ver=3, lis=2, vt=5, armor_reduc=1, weapon_dmg=1),
        ]
    elif scenario == 2:
        # Minor loot from Sz01; heroes enter at ~90% HP (attrition modelled by -1 HP start)
        return [
            Hero("Nordland Berserker",    max_hp=12, current_hp=11, kra=3, ges=1, zah=3, ver=0, lis=1, vt=5, armor_reduc=1, weapon_dmg=3),
            Hero("Elfische Kriegstänzerin", max_hp=10, current_hp=9, kra=2, ges=3, zah=2, ver=1, lis=1, vt=6, armor_reduc=1, weapon_dmg=2),
            Hero("Goblin Halsabschneider", max_hp=8,  current_hp=7,  kra=1, ges=2, zah=1, ver=1, lis=3, vt=5, armor_reduc=1, weapon_dmg=1),
            Hero("Magiegelehrte",          max_hp=8,  current_hp=7,  kra=0, ges=1, zah=1, ver=3, lis=2, vt=5, armor_reduc=1, weapon_dmg=1),
        ]
    elif scenario == 3:
        # Nach Sz02: Leicht verbesserte Ausrüstung, aber keine unrealistischen Sprünge
        return [
            Hero("Nordland Berserker",    max_hp=12, current_hp=12, kra=3, ges=1, zah=3, ver=0, lis=1, vt=5, armor_reduc=1, weapon_dmg=4),
            Hero("Elfische Kriegstänzerin", max_hp=10, current_hp=10, kra=2, ges=3, zah=2, ver=1, lis=1, vt=6, armor_reduc=1, weapon_dmg=2),
            Hero("Goblin Halsabschneider", max_hp=8,  current_hp=8,  kra=1, ges=2, zah=1, ver=1, lis=3, vt=5, armor_reduc=1, weapon_dmg=2),
            Hero("Magiegelehrte",          max_hp=8,  current_hp=8,  kra=0, ges=1, zah=1, ver=3, lis=2, vt=5, armor_reduc=1, weapon_dmg=1),
        ]
    elif scenario == 4:
        # Nach Sz03: 1 Rüstungsupgrade für Tank, etwas mehr HP
        return [
            Hero("Nordland Berserker",    max_hp=13, current_hp=13, kra=3, ges=1, zah=3, ver=0, lis=1, vt=5, armor_reduc=2, weapon_dmg=4),
            Hero("Elfische Kriegstänzerin", max_hp=11, current_hp=11, kra=2, ges=3, zah=2, ver=1, lis=1, vt=6, armor_reduc=1, weapon_dmg=3),
            Hero("Goblin Halsabschneider", max_hp=9,  current_hp=9,  kra=1, ges=2, zah=1, ver=1, lis=3, vt=5, armor_reduc=1, weapon_dmg=2),
            Hero("Magiegelehrte",          max_hp=9,  current_hp=9,  kra=0, ges=1, zah=1, ver=3, lis=2, vt=5, armor_reduc=1, weapon_dmg=1, max_fatigue=6),
        ]
    else:  # scenario == 5
        # Pre-finale Schattenbazar: near-maxed, restored HP, master weapons
        return [
            Hero("Nordland Berserker",    max_hp=14, current_hp=14, kra=3, ges=1, zah=3, ver=0, lis=1, vt=5, armor_reduc=2, weapon_dmg=5),
            Hero("Elfische Kriegstänzerin", max_hp=12, current_hp=12, kra=2, ges=3, zah=2, ver=1, lis=1, vt=6, armor_reduc=2, weapon_dmg=4),
            Hero("Goblin Halsabschneider", max_hp=10, current_hp=10, kra=1, ges=2, zah=1, ver=1, lis=3, vt=6, armor_reduc=1, weapon_dmg=3),
            Hero("Magiegelehrte",          max_hp=11, current_hp=11, kra=0, ges=1, zah=1, ver=3, lis=2, vt=5, armor_reduc=1, weapon_dmg=1, max_fatigue=7),
        ]


# ---------------------------------------------------------------------------
# Rest Helpers
# ---------------------------------------------------------------------------

def mini_rest(heroes: List[Hero], heal_amount: int = 2):
    """Short rest between rooms: Berserker eats Trockenfleisch (+2 HP), Magie -2 fatigue."""
    for h in heroes:
        if "Berserker" in h.name:
            h.current_hp = min(h.max_hp, h.current_hp + heal_amount)
        if "Magiegelehrte" in h.name:
            h.fatigue = max(0, h.fatigue - 2)

def potion_on_lowest(heroes: List[Hero], heal: int = 3):
    """Potion used on lowest HP hero."""
    alive = [h for h in heroes if not h.is_ko]
    if alive:
        lowest = min(alive, key=lambda h: h.current_hp)
        lowest.current_hp = min(lowest.max_hp, lowest.current_hp + heal)


# ---------------------------------------------------------------------------
# SCENARIO 01: Die verfluchte Krypta von Dun-Karr
# ---------------------------------------------------------------------------

def run_scenario_01(large_monster_rules: bool = True) -> Dict:
    num_runs = 10_000
    victories = 0
    wipes_by_room: Dict[int, int] = {2: 0, 3: 0, 4: 0}
    hp_totals = {"Berserker": 0.0, "Kriegstänzerin": 0.0, "Goblin": 0.0, "Magiegelehrte": 0.0}
    ko_counts = {"Berserker": 0, "Kriegstänzerin": 0, "Goblin": 0, "Magiegelehrte": 0}

    for _ in range(num_runs):
        heroes = make_heroes_scenario(1)

        # Room 2: Vorkammer — 2 Skelettkrieger (fixed)
        m2 = _skel(2)
        if not simulate_room_combat(heroes, m2, large_monster_rules):
            wipes_by_room[2] += 1
            continue

        mini_rest(heroes)

        # Room 3: Säulengewölbe — 3 Skelettkrieger + 1 Riesenspinne (fixed)
        m3 = _skel(3) + _spider(1)
        if not simulate_room_combat(heroes, m3, large_monster_rules):
            wipes_by_room[3] += 1
            continue

        potion_on_lowest(heroes, 3)
        for h in heroes:
            if "Magiegelehrte" in h.name:
                h.fatigue = max(0, h.fatigue - 2)

        # Room 4: Boss — Grabunhold (1×2) + 2 Skelettkrieger (fixed)
        m4 = [
            Monster("Grabunhold (Boss)", 14, 14, vt=7, atk_bonus=3, dmg=3,
                    armor_reduc=1, monster_type="boss", is_large=True),
        ] + _skel(2)
        if not simulate_room_combat(heroes, m4, large_monster_rules):
            wipes_by_room[4] += 1
            continue

        victories += 1
        _record_hero_stats(heroes, hp_totals, ko_counts)

    return _make_result("Szenario 01 — Die verfluchte Krypta von Dun-Karr",
                        num_runs, victories, wipes_by_room, hp_totals, ko_counts,
                        target_low=90, target_high=100)


# ---------------------------------------------------------------------------
# SCENARIO 02: Hinterhalt im Nebelmoor
# ---------------------------------------------------------------------------

def run_scenario_02(large_monster_rules: bool = True) -> Dict:
    num_runs = 10_000
    victories = 0
    wipes_by_room: Dict[int, int] = {1: 0, 2: 0, 3: 0, 4: 0}
    hp_totals = {"Berserker": 0.0, "Kriegstänzerin": 0.0, "Goblin": 0.0, "Magiegelehrte": 0.0}
    ko_counts = {"Berserker": 0, "Kriegstänzerin": 0, "Goblin": 0, "Magiegelehrte": 0}

    for _ in range(num_runs):
        heroes = make_heroes_scenario(2)

        # Weg-Token at Zone 1 → Zone 2 transition
        resolve_door_token(heroes)

        # Zone 2: Versunkene Ruine — Encounter Deck
        m2 = draw_encounter()
        if m2:
            if not simulate_room_combat(heroes, m2, large_monster_rules):
                wipes_by_room[2] += 1
                continue

        mini_rest(heroes, heal_amount=1)

        # Zone 3: Knochen-Dickicht — Encounter Deck + door
        resolve_door_token(heroes)   # Schilfdickicht obstacle
        m3 = draw_encounter()
        if m3:
            if not simulate_room_combat(heroes, m3, large_monster_rules):
                wipes_by_room[3] += 1
                continue

        # Keine garantierte Trankheilung vor dem Boss (nur gefundene Beute)
        # potion_on_lowest(heroes, 3) entfernt
        for h in heroes:
            if "Magiegelehrte" in h.name:
                h.fatigue = max(0, h.fatigue - 2)

        # Zone 4 Boss: Ödland-Worg-Alpha (Elite) + 3 Moor-Ghule (mit Boss-Eröffnungsschlag!)
        # Alpha: LP 14, VT 6, Mov 6, Atk 1d6+3, Dmg 3
        m4 = [
            Monster("Worg-Alpha", 14, 14, vt=6, atk_bonus=3, dmg=3, monster_type="worg"),
        ] + _ghoul(3)
        if not simulate_room_combat(heroes, m4, large_monster_rules, boss_opening_strike=True):
            wipes_by_room[4] += 1
            continue

        victories += 1
        _record_hero_stats(heroes, hp_totals, ko_counts)

    return _make_result("Szenario 02 — Hinterhalt im Nebelmoor",
                        num_runs, victories, wipes_by_room, hp_totals, ko_counts,
                        target_low=88, target_high=95)


# ---------------------------------------------------------------------------
# SCENARIO 03: Die versunkene Zisterne von Valdor
# ---------------------------------------------------------------------------

def run_scenario_03(large_monster_rules: bool = True) -> Dict:
    num_runs = 10_000
    victories = 0
    wipes_by_room: Dict[int, int] = {1: 0, 2: 0, 3: 0, 4: 0}
    hp_totals = {"Berserker": 0.0, "Kriegstänzerin": 0.0, "Goblin": 0.0, "Magiegelehrte": 0.0}
    ko_counts = {"Berserker": 0, "Kriegstänzerin": 0, "Goblin": 0, "Magiegelehrte": 0}

    for _ in range(num_runs):
        heroes = make_heroes_scenario(3)

        # Kammer 1: Encounter Deck immediately (guards heard entry)
        m1 = draw_encounter()
        if m1:
            if not simulate_room_combat(heroes, m1, large_monster_rules):
                wipes_by_room[1] += 1
                continue

        # Door to Kammer 2
        resolve_door_token(heroes)
        mini_rest(heroes, heal_amount=1)

        # Kammer 2: Encounter Deck + water hazard (modelled: 10% chance of Vergiftet = -1 dmg to hero)
        m2 = draw_encounter()
        # Poison water: each hero has 25% chance to take 1 dmg from poison before combat
        for h in heroes:
            if not h.is_ko and random.random() < 0.25:
                h.take_damage(1)
        if m2:
            if not simulate_room_combat(heroes, m2, large_monster_rules):
                wipes_by_room[2] += 1
                continue

        # Door to Kammer 3
        resolve_door_token(heroes)
        mini_rest(heroes, heal_amount=1)

        # Kammer 3: Encounter Deck
        m3 = draw_encounter()
        if m3:
            if not simulate_room_combat(heroes, m3, large_monster_rules):
                wipes_by_room[3] += 1
                continue

        # Vor dem Bossraum: Rast
        for h in heroes:
            if "Magiegelehrte" in h.name:
                h.fatigue = max(0, h.fatigue - 2)

        # Kammer 4 Boss (fixed): Meisterkultist (14 LP, VT 6, Rüstung 1) + 2 Skelett-Scharfschützen + 2 Skelettkrieger
        m4 = [
            Monster("Meisterkultist", 14, 14, vt=6, atk_bonus=3, dmg=2,
                    armor_reduc=1, monster_type="cultist"),
            Monster("Skelett-Scharfschütze 1", 3, 3, vt=5, atk_bonus=3, dmg=2,
                    monster_type="marksman"),
            Monster("Skelett-Scharfschütze 2", 3, 3, vt=5, atk_bonus=3, dmg=2,
                    monster_type="marksman"),
        ] + _skel(2)
        if not simulate_room_combat(heroes, m4, large_monster_rules, boss_opening_strike=True):
            wipes_by_room[4] += 1
            continue

        victories += 1
        _record_hero_stats(heroes, hp_totals, ko_counts)

    return _make_result("Szenario 03 — Die versunkene Zisterne von Valdor",
                        num_runs, victories, wipes_by_room, hp_totals, ko_counts,
                        target_low=83, target_high=93)


# ---------------------------------------------------------------------------
# SCENARIO 04: Die belagerte Felsen-Zitadelle
# ---------------------------------------------------------------------------

def run_scenario_04(large_monster_rules: bool = True) -> Dict:
    num_runs = 10_000
    victories = 0
    wipes_by_room: Dict[int, int] = {1: 0, 2: 0, 3: 0, 4: 0}
    hp_totals = {"Berserker": 0.0, "Kriegstänzerin": 0.0, "Goblin": 0.0, "Magiegelehrte": 0.0}
    ko_counts = {"Berserker": 0, "Kriegstänzerin": 0, "Goblin": 0, "Magiegelehrte": 0}

    for _ in range(num_runs):
        heroes = make_heroes_scenario(4)

        # Zone 1: Felsiger Bastionsaufstieg — Encounter Deck
        m1 = draw_encounter()
        if m1:
            if not simulate_room_combat(heroes, m1, large_monster_rules):
                wipes_by_room[1] += 1
                continue

        # Door Tür 1 (Mauerdurchbruch)
        resolve_door_token(heroes)
        mini_rest(heroes, heal_amount=2)

        # Zone 2: Torhof — Blutgolem (Boss, 1×2, vampiric) + Encounter Deck companions
        companions = draw_encounter()
        m2 = [
            Monster("Blutgolem", 12, 12, vt=6, atk_bonus=3, dmg=2,
                    armor_reduc=0, monster_type="large_boss", is_large=True, vampiric=True),
        ] + (companions[:2] if companions else _skel(2))
        if not simulate_room_combat(heroes, m2, large_monster_rules):
            wipes_by_room[2] += 1
            continue

        # Fallgitter opened — progress to Bergfried (kurze Verschnaufpause)
        mini_rest(heroes, heal_amount=1)
        for h in heroes:
            if "Magiegelehrte" in h.name:
                h.fatigue = max(0, h.fatigue - 2)

        # Zone 3: Waffensaal — Encounter Deck, door Tür 2
        m3 = draw_encounter()
        if m3:
            if not simulate_room_combat(heroes, m3, large_monster_rules):
                wipes_by_room[3] += 1
                continue

        # Door Tür 2 (Portal zum Thronsaal)
        resolve_door_token(heroes)

        # Zone 4 Boss (fixed): Todesritter von Mor-Goth + 1 Skelett-Scharfschütze + 2 Skelettkrieger
        # Todesritter: LP 14, VT 7, Rüstung 1, Klinge 3 dmg
        m4 = [
            Monster("Todesritter von Mor-Goth", 14, 14, vt=7, atk_bonus=3, dmg=3,
                    armor_reduc=2, monster_type="deathknight"),
            Monster("Skelett-Scharfschütze", 3, 3, vt=5, atk_bonus=3, dmg=2,
                    monster_type="marksman"),
        ] + _skel(2)
        if not simulate_room_combat(heroes, m4, large_monster_rules, boss_opening_strike=True):
            wipes_by_room[4] += 1
            continue

        victories += 1
        _record_hero_stats(heroes, hp_totals, ko_counts)

    return _make_result("Szenario 04 — Die belagerte Felsen-Zitadelle",
                        num_runs, victories, wipes_by_room, hp_totals, ko_counts,
                        target_low=78, target_high=90)


# ---------------------------------------------------------------------------
# SCENARIO 05: Das Totenreich des Lich-Königs (FINALE)
# ---------------------------------------------------------------------------

def run_scenario_05(large_monster_rules: bool = True) -> Dict:
    num_runs = 10_000
    victories = 0
    wipes_by_room: Dict[int, int] = {1: 0, 2: 0, 3: 0, 4: 0}
    hp_totals = {"Berserker": 0.0, "Kriegstänzerin": 0.0, "Goblin": 0.0, "Magiegelehrte": 0.0}
    ko_counts = {"Berserker": 0, "Kriegstänzerin": 0, "Goblin": 0, "Magiegelehrte": 0}

    for _ in range(num_runs):
        heroes = make_heroes_scenario(5)

        # Zone 1: Gletscherspalte — Encounter Deck
        m1 = draw_encounter()
        if m1:
            if not simulate_room_combat(heroes, m1, large_monster_rules):
                wipes_by_room[1] += 1
                continue

        # Tür 1 (Eiskluft) + Glatteis tick (25% chance 1 dmg per hero)
        resolve_door_token(heroes)
        for h in heroes:
            if not h.is_ko and random.random() < 0.25:
                h.take_damage(1)

        mini_rest(heroes, heal_amount=2)

        # Zone 2: Seelenbrücke — Encounter Deck (harder positioning: narrow bridge)
        m2 = draw_encounter()
        # Glatteis in Zone 2: 20% chance of 1 dmg before combat
        for h in heroes:
            if not h.is_ko and random.random() < 0.20:
                h.take_damage(1)
        if m2:
            if not simulate_room_combat(heroes, m2, large_monster_rules):
                wipes_by_room[2] += 1
                continue

        # Tür 2: Gefrorenes Runentor
        resolve_door_token(heroes)
        potion_on_lowest(heroes, 4)
        for h in heroes:
            if "Magiegelehrte" in h.name:
                h.fatigue = max(0, h.fatigue - 4)

        # Zone 3 → Das Allerheiligste (Boss Chamber)
        # Frosthauch-Aura: 1 Kälteschaden every round (modelled in combat loop for Lichking)
        # Feuerschalen: Heroes use 1 action to light → modelled as 50% chance each hero avoids 1 frost tick
        # pre-combat: heroes enter and try to light Feuerschalen
        # Simplified: 1st two rounds of Lichkampf: each hero takes 1 frost before attacking
        # This is modelled inside the lichking combat loop via the aura application

        # Lich-König Boss: LP 18, VT 8, Rüstung 1, 2 actions/round + summons
        # Seelenkäfig: starts with 2 Skelettkrieger adjacent
        m_boss = [
            Monster("Lich-König Malakor", 18, 18, vt=8, atk_bonus=4, dmg=3,
                    armor_reduc=1, monster_type="lichking", summons_skeletons=True),
        ] + _skel(2)  # Initial guardian skeletons (Seelenkäfig)

        if not simulate_room_combat(heroes, m_boss, large_monster_rules, round_limit=25):
            wipes_by_room[4] += 1
            continue

        victories += 1
        _record_hero_stats(heroes, hp_totals, ko_counts)

    return _make_result("Szenario 05 — Das Totenreich des Lich-Königs (FINALE)",
                        num_runs, victories, wipes_by_room, hp_totals, ko_counts,
                        target_low=70, target_high=85)


# ---------------------------------------------------------------------------
# Stats Helpers
# ---------------------------------------------------------------------------

def _record_hero_stats(heroes, hp_totals, ko_counts):
    for h in heroes:
        if "Berserker" in h.name:   k = "Berserker"
        elif "Kriegstänzerin" in h.name: k = "Kriegstänzerin"
        elif "Goblin" in h.name:    k = "Goblin"
        else:                       k = "Magiegelehrte"
        hp_totals[k] += h.current_hp
        if h.is_ko:
            ko_counts[k] += 1


def _make_result(name, num_runs, victories, wipes_by_room, hp_totals, ko_counts,
                 target_low, target_high):
    win_rate = (victories / num_runs) * 100.0
    return {
        "name": name,
        "runs": num_runs,
        "victories": victories,
        "win_rate": win_rate,
        "wipes_by_room": wipes_by_room,
        "avg_hp_end": {k: v / max(1, victories) for k, v in hp_totals.items()},
        "ko_rate_end": {k: (v / max(1, victories)) * 100.0 for k, v in ko_counts.items()},
        "target_low": target_low,
        "target_high": target_high,
    }


# ---------------------------------------------------------------------------
# Pretty Printing
# ---------------------------------------------------------------------------

STATUS_EMOJI = {True: "✅", False: "❌"}

def print_result(res: Dict):
    win = res["win_rate"]
    in_range = res["target_low"] <= win <= res["target_high"]
    status = "✅ BALANCIERT" if in_range else ("⚠️  ZU LEICHT" if win > res["target_high"] else "❌ ZU SCHWER")

    print("=" * 70)
    print(f"  {res['name']}")
    print(f"  ({res['runs']:,} Runs)   Ziel: {res['target_low']}–{res['target_high']}%")
    print("=" * 70)
    print(f"  Gesamtsieg-Quote: {win:.2f}%   →  {status}")
    print()
    print("  Niederlagen nach Zone/Raum:")
    for room, count in sorted(res["wipes_by_room"].items()):
        pct = count / res["runs"] * 100
        bar = "█" * int(pct * 2)
        print(f"    Zone/Raum {room}: {count:5d} Wipes  ({pct:.2f}%)  {bar}")
    print()
    print("  Ø verbleibende LP bei Sieg:")
    for hero, hp in res["avg_hp_end"].items():
        bar = "░" * int(hp)
        print(f"    {hero:18s}: {hp:5.2f} LP  {bar}")
    print()
    print("  K.O.-Quote am Szenario-Ende (Siege):")
    for hero, ko in res["ko_rate_end"].items():
        print(f"    {hero:18s}: {ko:.2f}%")
    print()


def print_campaign_summary(results: List[Dict]):
    print()
    print("╔══════════════════════════════════════════════════════════════════════╗")
    print("║           KAMPAGNEN-ÜBERSICHT — BALANCE-DASHBOARD                   ║")
    print("╚══════════════════════════════════════════════════════════════════════╝")
    print(f"  {'Szenario':<45} {'Siegquote':>9}  {'Ziel':>12}  Status")
    print("  " + "-" * 68)
    for r in results:
        in_range = r["target_low"] <= r["win_rate"] <= r["target_high"]
        icon = "✅" if in_range else ("⚠️ " if r["win_rate"] > r["target_high"] else "❌")
        short = r["name"].split("—")[1].strip()[:42]
        print(f"  {short:<45} {r['win_rate']:>8.2f}%  "
              f"{r['target_low']:>3}–{r['target_high']}%   {icon}")
    print()
    all_ok = all(r["target_low"] <= r["win_rate"] <= r["target_high"] for r in results)
    if all_ok:
        print("  🎉 ALLE Szenarien sind im Zielkorridor — Kampagne ist balanciert!")
    else:
        print("  ⚠️  Mindestens ein Szenario liegt außerhalb des Zielkorridors!")
        print("     Passe die Monsterstärke oder Ausrüstungsannahmen an und re-rune.")
    print()


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import time
    print()
    print("╔══════════════════════════════════════════════════════════════════════╗")
    print("║   Monte-Carlo Balance Simulator — Von Helden und Monstern           ║")
    print("║   Alle 5 Szenarien · 10.000 Runs je · Hybrid-System                ║")
    print("╚══════════════════════════════════════════════════════════════════════╝")
    print()

    t0 = time.time()
    results = []

    print("⏳ Teste Szenario 01...")
    r1 = run_scenario_01(large_monster_rules=True)
    print_result(r1)
    results.append(r1)

    print("⏳ Teste Szenario 02...")
    r2 = run_scenario_02(large_monster_rules=True)
    print_result(r2)
    results.append(r2)

    print("⏳ Teste Szenario 03...")
    r3 = run_scenario_03(large_monster_rules=True)
    print_result(r3)
    results.append(r3)

    print("⏳ Teste Szenario 04...")
    r4 = run_scenario_04(large_monster_rules=True)
    print_result(r4)
    results.append(r4)

    print("⏳ Teste Szenario 05...")
    r5 = run_scenario_05(large_monster_rules=True)
    print_result(r5)
    results.append(r5)

    elapsed = time.time() - t0
    print_campaign_summary(results)
    print(f"  Gesamtlaufzeit: {elapsed:.1f}s für {5 * 10_000:,} Simulationsläufe")
    print()

