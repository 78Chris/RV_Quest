# Core Rules — Design Draft v0.1

> **Status:** DRAFT — for discussion and review  
> **Design doc:** English | **Printed game:** German

---

## 1. The Five Attributes (Attribute)

Each character has 5 attributes, each rated **0–3**.  
The value is used as a **bonus added to d6 rolls**.

| Abbrev. | German | Governs |
|---|---|---|
| **KRA** | Kraft | Melee attacks, damage, feats of strength |
| **GES** | Geschick | Speed, dodge, ranged attacks, initiative |
| **ZÄH** | Zähigkeit | Hit points, resistance, endurance |
| **VER** | Verstand | Spellcasting, traps, item identification |
| **LIS** | List | Stealth, lockpicking, deception, ambush |

**Scale:**

| Value | Meaning |
|---|---|
| 0 | Untrained — avoid this |
| 1 | Average — capable |
| 2 | Skilled — reliable |
| 3 | Exceptional — dominant |

**Character Attribute Values (first proposal):**

| Character | KRA | GES | ZÄH | VER | LIS | Total |
|---|---|---|---|---|---|---|
| Nordland Berserker | 3 | 1 | 3 | 0 | 1 | 8 |
| Elfische Kriegstänzerin | 2 | 3 | 2 | 1 | 1 | 9 |
| Goblin Halsabschneider | 1 | 2 | 1 | 1 | 3 | 8 |
| Magiegelehrte | 0 | 1 | 1 | 3 | 2 | 7 |

> Note: Magiegelehrte has fewer total points because spells bypass normal KRA/GES limits.

---

## 2. Lebenspunkte (LP — Hit Points)

**Formula: LP = ZÄH × 2 + 6**

| Character | ZÄH | LP |
|---|---|---|
| Nordland Berserker | 3 | 12 LP |
| Elfische Kriegstänzerin | 2 | 10 LP |
| Goblin Halsabschneider | 1 | 8 LP |
| Magiegelehrte | 1 | 8 LP |

> LP are tracked on the character sheet with a simple track (circles to cross off).

---

## 3. The Core Dice Mechanic

### Standard Roll
> **Roll 1d6 + relevant attribute ≥ Schwierigkeitsgrad (SG)**

A **success** is any result equal to or greater than the SG.  
A **failure** is any result below the SG.

### Difficulty Scale (Schwierigkeitsgrad)

| SG | Label | Who can reliably succeed |
|---|---|---|
| 4 | Leicht (Easy) | Anyone with attribute 1+ |
| 6 | Normal (Standard) | Anyone with attribute 2+ |
| 8 | Schwer (Hard) | Anyone with attribute 3, or lucky |
| 10 | Sehr schwer (Very Hard) | Attribute 3 + roll 5-6 only |

### Critical Success (Volltreffer)
> Roll a natural **6** on the die → automatic success, PLUS a bonus effect.

Examples: +1 damage, disarm the enemy, apply a condition for free.

> ❌ **No Patzer rule** — rolling a 1 is simply a failure with no additional complication. Kept forgiving for 2-player co-op.

---

## 4. Vorteil & Nachteil (Advantage & Disadvantage)

When circumstances strongly favour or hinder a character:

- **Vorteil (Advantage):** Roll **2d6**, take the **higher** die + attribute.
- **Nachteil (Disadvantage):** Roll **2d6**, take the **lower** die + attribute.

This is the **only** time 2d6 appear — keeping things simple.

**Typical sources of Vorteil:**
- Attacking from stealth (Halsabschneider's *Meucheln*)
- Attacking an enemy who is stunned or prone
- Using a character's core speciality in ideal conditions

**Typical sources of Nachteil:**
- Attacking while in difficult terrain
- Using an attribute you have at 0
- **Elf–Goblin Proximity Rule:** If the Elfische Kriegstänzerin and the Goblin Halsabschneider occupy **adjacent tiles**, both suffer **Nachteil on any roll that involves cooperation** (helping each other, acting in the same space, etc.). They are too busy being disgusted by each other to work well together. Being forced into a tight corridor is going to be interesting.

---

## 5. Turn Structure (Rundenablauf)

Play proceeds dynamically using the **Raum-Initiative & Initiative-Leiste (Holz-Tracker)** (see `rules/exploration.md`):

### Phase 1 — Initiative (Einmalig pro neuem Raum mit Monstern)
- Sobald ein neuer Raum mit Monstern betreten wird, würfelt jeder Held **1d6 + GES**.
- Monster nutzen ihren festen Initiative-Basiswert von ihrer Monsterkarte (kein Wurf erforderlich).
- Die runden **Holz-Initiative-Plättchen** der Helden und Monster werden in absteigender Reihenfolge in die **gelaserte Initiative-Leiste** gesteckt.
- *Gleichstand:* Helden gewinnen immer gegen Monster.
- *Hinterhalt:* Bei einem Hinterhalt aus einer Begegnungskarte agieren Monster in Runde 1 sofort vor allen Helden.

### Phase 2 — Aktivierung entlang der Leiste
Die Figuren werden nun **streng in der Reihenfolge der Initiative-Leiste** von links nach rechts aktiviert. Jeder Held und jede Monstergruppe führt ihren Zug vollständig aus (Bewegung + Aktion bzw. Monster-KI), bevor das nächste Plättchen an der Reihe ist.

Ein Held darf in seinem Zug eine der folgenden Kombinationen wählen:

| Option | What you do |
|---|---|
| **Bewegen + Angreifen** | Move up to your speed AND make 1 attack |
| **Doppelbewegung** | Move up to double your speed (no attack) |
| **Fähigkeit einsetzen** | Use a special ability (may or may not allow movement) |
| **Zaubern** | Cast a spell (Magiegelehrte only, or Halsabschneider if drunk) |
| **Durchsuchen** | Search the current tile for secrets, traps, or loot |
| **Interagieren** | Open a door, pick a lock, use an item, help an ally |

> **Exception — Kriegstänzerin:** Her *Kriegstanz* gives her **2 attacks** when she takes the *Bewegen + Angreifen* option. Both attacks roll separately.

### Phase 3 — Rundenende (Nachdem das letzte Plättchen agiert hat)
- **Ongoing Effects:** Resolve ongoing damage/effects (burning, poison, stunned, etc.) and remove expired conditions.
- **Ereigniskarte ziehen (Event Card):**
  - Am Rundenende wird **1 Karte vom Ereigniskarten-Deck** gezogen (oder nach Szenario-Vorgabe, z. B. immer dann, wenn ein Raum betreten wird oder ein Runden-Timer abläuft).
  - Ereigniskarten bringen unvorhersehbare Dynamik (z. B. einstürzende Decken, herannahende Goblin-Patrouillen, Fackel flackert, magische Resonanz, ein Geräusch in der Dunkelheit).
  - Nach Auflösung wird die Karte abgelegt (bei leerem Stapel wird der Ablagestapel gemischt).

> **Gruppenstärke (Party Size):** Jedes Szenario wird **immer mit allen 4 Helden** gespielt. Bei 2 Spielern steuert jeder Spieler **2 Helden** (z. B. Spieler 1: Berserker + Magiegelehrte; Spieler 2: Kriegstänzerin + Halsabschneider). Alle Regeln und Szenarien sind auf diese feste 4er-Gruppe gebalancet.

---

## 6. Movement (Bewegung)

- Movement is measured in **tiles** (each tile = one dungeon square).
- Each character has a **Bewegungsweite** (movement speed) per turn.

| Character | Speed (Bewegungsweite) | Rolle |
|---|---|---|
| Nordland Berserker | **4 Felder** | Standfester Vormarsch |
| Elfische Kriegstänzerin | **6 Felder** | Schneller Gefechtstanz / Skirmisher |
| Goblin Halsabschneider | **5 Felder** | Wendig (*Durchwuseln*) |
| Magiegelehrte | **4 Felder** | Bedächtiges akademisches Schritttempo |

- **Mindestbewegung (Floor):** Durch Rüstungen, Schilde oder Zustände kann die Bewegungsweite eines Helden **niemals unter 2 Felder** sinken (ein Held kann in seinem Zug immer mindestens 2 Felder ziehen).
- You may split movement before and after an action (move 2, attack, move 2).
- Difficult terrain costs **2 tiles** to enter instead of 1.
- Enemies block movement (you cannot move through an enemy unless you have *Schattenschritt* or Goblin *Durchwuseln*).

---

## 7. Combat Overview (Kampf)

*(Full details in `rules/combat.md` — this is a summary)*

### Attacking
> Roll **1d6 + KRA** (melee) or **1d6 + GES** (ranged) vs. the target's **Verteidigung (VT)**

**Verteidigung** = a fixed number on each monster card (their "defence rating").  
Heroes have a **base VT** set by their armour.

### Damage (Schaden)
On a **successful hit**, deal damage equal to your weapon's **Schadenswert** (damage value):

| Weapon type | Schadenswert |
|---|---|
| Fäuste / kleine Klinge (unarmed / small blade) | 1 |
| Einhandwaffe (sword, axe, mace) | 2 |
| Zweihandwaffe (two-handed axe, war hammer) | 3 |
| Wurfwaffe (thrown) | 1 |
| Zauber (spell) | varies |

On a **Volltreffer** (natural 6): deal **+1 bonus damage** OR apply a free condition.

### Armour (Rüstung)
Armour **reduces incoming damage** by a fixed amount:

| Armour | Damage Reduction |
|---|---|
| Keine Rüstung (no armour) | 0 |
| Lederrüstung (leather) | 1 |
| Kettenhemd (chainmail) | 2 |
| Plattenpanzer (plate) | 3 |

---

## 8. Magic & Erschöpfung (Fatigue Track)

The **Magiegelehrte** (and any character temporarily able to cast) tracks magical fatigue separately from HP.

### Erschöpfungsleiste (Fatigue Track)
- Represented as a row of **5 boxes** on the character sheet.
- Each spell cast fills **1 box**.
- Powerful spells may cost **2 boxes**.

### Fatigue Thresholds

| Boxes filled | Effect |
|---|---|
| 0–2 | No penalty |
| 3 | Nachteil on all spell rolls |
| 4 | Nachteil on **all** rolls (exhaustion spreading) |
| 5 (full) | Cannot cast. Nachteil on all rolls until rested |

### Recovering Fatigue
- **Between rooms** (after clearing a room): remove **1 box** if no enemies remain.
- **Resting action:** Spend a full turn doing nothing — remove **2 boxes**. Cannot be done in combat.
- **Between scenarios:** Fatigue fully resets.

### Goblinzauber & Fatigue
- When the Goblin Halsabschneider casts via *Goblinzauber* (drunk magic), he uses a **shared Erschöpfungs-track** of 3 boxes (fewer, as his casting is far less controlled).
- The alcohol is consumed regardless of outcome.

---

## 9. Conditions (Zustände)

Short-term effects applied by attacks, spells, or traps.

| Condition | German | Effect | Duration |
|---|---|---|---|
| Burning | Brennend | Take 1 damage at start of your turn | Until extinguished (action) or 2 rounds |
| Stunned | Betäubt | Lose your next turn | 1 round |
| Slowed | Verlangsamt | Movement halved | 1 round |
| Poisoned | Vergiftet | -1 to all rolls | Until healed / scenario ends |
| Hidden | Versteckt | Cannot be targeted; first attack gains Vorteil | Until you attack or enter light |

---

## 10. Healing (Heilung)

- **Heiltränke (Healing Potions):** Restore **3 LP**. Used as an action.
- **Heilrationen (Rations):** Restore **1 LP**. Used at end of scenario between rooms.
- **Between Scenarios:** All heroes restore LP to full (rest and recover).
- **At 0 LP:** Hero is **Bewusstlos** (knocked out). The other player may use 1 action to revive them with 1 LP. If both heroes are at 0 LP simultaneously → scenario fails.

---

## 11. Rules Status & Open Questions

- [x] Attribute values confirmed: Berserker (KRA 3, ZÄH 3), Kriegstänzerin (GES 3), Halsabschneider (LIS 3), Magiegelehrte (VER 3)
- [x] LP formula confirmed: `LP = ZÄH × 2 + 6` (12 / 10 / 8 / 8 LP)
- [x] Gold & economy system: Post-scenario reward + monster bounty + intermission market display
- [x] Spells for Magiegelehrte: 6 spells defined in `characters/starter_cards_and_spells.md`
- [x] Goblinzauber table: 1d6 table defined in `characters/starter_cards_and_spells.md`
- [ ] Character Progression / Level-Up: Do heroes level up (XP/Milestones) or is progression purely equipment-based?

---
