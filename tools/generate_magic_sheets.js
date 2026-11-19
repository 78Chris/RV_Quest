/**
 * Magic Cards Generator for RV_Quest
 * Produces A4 gutter-fold print sheets (Tarot 81.67 x 138 mm, folding to standard height).
 * Includes:
 *   - 6 Spells of the Magiegelehrte (Z1–Z6) with "Codex Arcanum" card back
 *   - 8 Chaos/Goblin Spells (G01–G08) with "Goblin-Fusel" card back
 */
const fs = require('fs');
const path = require('path');

const ROOT_DIR = path.resolve(__dirname, '..');
const PRINTABLES_DIR = path.join(ROOT_DIR, 'printables');

const CODEX_ARCANUM_BACK_IMG = './art_assets/MasterArtwork/Cards/Card%20Backs/vintage_medieval_woodcut_etching_of_an_ancient_imperial_wizar_bd9e6812-0ff4-4a7c-abda-11b26cc5672c_3.png';
const GOBLIN_FUSEL_BACK_IMG = './art_assets/MasterArtwork/Cards/Card%20Backs/vintage_medieval_woodcut_etching_of_a_battered_rogue_goblin_g_40cf9f65-3cc5-4a40-a5da-ab879092fef9_2.png';

const MAGIC_CARDS = [
  // --- DIE 6 AKADEMIE-ZAUBER DER MAGIEGELEHRTEN ---
  {
    id: 'Z1',
    numStr: '#Z1 / 06',
    deckName: 'Codex Arcanum',
    name: 'Feuerstrahl',
    subtitle: 'Offensivzauber · Elementare Pyromantie',
    art: './art_assets/MasterArtwork/Cards/Magic/A_dynamic_dungeon_action_scene_screaming_savage_goblin_archer_423af1cf-6280-4054-9b01-2a68f7aadc9e_0.png',
    lore: '»Fokussierte Hitze bündelt sich in der Handfläche. Ein gleißender Strahl flüssigen Feuers schlägt krachend in den Feind ein.«',
    chip1Label: 'Reichweite',
    chip1Val: '4 Felder',
    chip1Class: 'target-val',
    chip2Label: 'Erschöpfung',
    chip2Val: '1 Box',
    chip2Class: 'timing-val',
    chip3Label: 'Schaden',
    chip3Val: '3 Feuerschaden',
    chip3Class: 'type-val',
    chip3BoxClass: 'highlight-stat',
    rulesTitle: 'Feuerlanze',
    rulesBody: 'Angriffswurf (<code>1d6 + VER</code>) gegen VT des Ziels: Verursacht <strong>3 Schaden</strong>. Bei einem Volltreffer (natürliche 6 auf dem d6) erhält das Ziel zusätzlich den Zustand <strong>Brennend</strong> (1 direkter Schaden zu Rundenbeginn).',
    footerDeck: 'Codex Arcanum · Magiegelehrte',
    rarity: 'Akademie-Zauber',
    cardBackImg: CODEX_ARCANUM_BACK_IMG,
    cardBackTitle: 'Codex Arcanum',
    accentColor: '#9c2a1a', // Pyromancy Crimson
    accentGlow: 'rgba(156, 42, 26, 0.25)'
  },
  {
    id: 'Z2',
    numStr: '#Z2 / 06',
    deckName: 'Codex Arcanum',
    name: 'Arkaner Schild',
    subtitle: 'Defensivzauber · Schutzabjuration',
    art: './art_assets/MasterArtwork/Cards/Magic/A_dynamic_dungeon_action_scene_glowing_cyan-blue_hexagonal_ru_daaaaf2c-a9b7-4c21-b54c-cb25de0ed0bf_0.png',
    lore: '»Geometrische Lichtmuster weben eine undurchdringliche Barriere. Klingen und Pfeile zerschellen an flirrenden Glyphen.«',
    chip1Label: 'Reichweite',
    chip1Val: 'Selbst / 2 F.',
    chip1Class: 'target-val',
    chip2Label: 'Erschöpfung',
    chip2Val: '1 Box',
    chip2Class: 'timing-val',
    chip3Label: 'Schutz',
    chip3Val: '+2 Rüstung',
    chip3Class: 'type-val',
    chip3BoxClass: 'highlight-shield',
    rulesTitle: 'Schutzbarriere',
    rulesBody: 'Als <strong>Sofortige Reaktion</strong> bei einem Angriff oder reguläre Aktion gewirkt: Das gewählte Ziel erhält bis zum Beginn des nächsten eigenen Zuges <strong>+2 Schaden-Reduktion</strong> gegen den nächsten feindlichen Angriff.',
    footerDeck: 'Codex Arcanum · Magiegelehrte',
    rarity: 'Akademie-Zauber',
    cardBackImg: CODEX_ARCANUM_BACK_IMG,
    cardBackTitle: 'Codex Arcanum',
    accentColor: '#1d5e8a', // Cyan Abjuration
    accentGlow: 'rgba(29, 94, 138, 0.25)'
  },
  {
    id: 'Z3',
    numStr: '#Z3 / 06',
    deckName: 'Codex Arcanum',
    name: 'Eisige Fesseln',
    subtitle: 'Kontrollzauber · Kryomantie',
    art: './art_assets/MasterArtwork/Cards/Magic/A_dynamic_dungeon_action_scene_snarling_monstrous_wasteland_w_8c2d63a2-25ca-4f8d-b6bc-da68232ea442_2.png',
    lore: '»Klirrender Raureif kriecht über den Stein. Gefrierende Kälte packt die Beine der Kreatur und kettet sie an den nackten Fels.«',
    chip1Label: 'Reichweite',
    chip1Val: '3 Felder',
    chip1Class: 'target-val',
    chip2Label: 'Erschöpfung',
    chip2Val: '1 Box',
    chip2Class: 'timing-val',
    chip3Label: 'Effekt',
    chip3Val: '1 Eis + Betäubt',
    chip3Class: 'type-val',
    chip3BoxClass: 'highlight-stat',
    rulesTitle: 'Frostbann',
    rulesBody: 'Zauberwurf (<code>1d6 + VER</code>) gegen die VT des Ziels: Bei Erfolg erleidet das Ziel sofort <strong>1 Eisschaden</strong> und erhält den Zustand <strong>Betäubt</strong> (Standee flachlegen; verliert den nächsten Zug). <em>Bosse sind immun gegen Betäubt und werden stattdessen Verlangsamt</em>.',
    footerDeck: 'Codex Arcanum · Magiegelehrte',
    rarity: 'Akademie-Zauber',
    cardBackImg: CODEX_ARCANUM_BACK_IMG,
    cardBackTitle: 'Codex Arcanum',
    accentColor: '#2b757e', // Frost Teal
    accentGlow: 'rgba(43, 117, 126, 0.25)'
  },
  {
    id: 'Z4',
    numStr: '#Z4 / 06',
    deckName: 'Codex Arcanum',
    name: 'Arkane Druckwelle',
    subtitle: 'Flächenzauber · Kinetischer Impuls',
    art: './art_assets/MasterArtwork/Cards/Magic/A_dynamic_dungeon_action_scene_group_of_four_goblin_scouts_be_e6fb0984-738b-4ed6-919e-58fc4fbc7063_2.png',
    lore: '»Ein ringförmiger Schockimpuls reißt die Luft entzwei. Feinde werden wie welke Blätter von den Beinen gefegt.«',
    chip1Label: 'Reichweite',
    chip1Val: '1 Feld Umkr.',
    chip1Class: 'target-val',
    chip2Label: 'Erschöpfung',
    chip2Val: '2 Boxen',
    chip2Class: 'timing-val',
    chip3Label: 'Schaden',
    chip3Val: '2 Fl-Schaden',
    chip3Class: 'type-val',
    chip3BoxClass: 'highlight-stat',
    rulesTitle: 'Druckstoß & Rückwurf',
    rulesBody: 'Mächtige Kraftentladung! Alle Figuren auf direkt angrenzenden Feldern (Freund und Feind!) erleiden <strong>2 Schaden</strong> und werden <strong>1 Feld weit zurückgestoßen</strong>. Unterbricht vorbereitete Aktionen.',
    footerDeck: 'Codex Arcanum · Magiegelehrte',
    rarity: 'Akademie-Zauber',
    cardBackImg: CODEX_ARCANUM_BACK_IMG,
    cardBackTitle: 'Codex Arcanum',
    accentColor: '#6c3483', // Force Violet
    accentGlow: 'rgba(108, 52, 131, 0.25)'
  },
  {
    id: 'Z5',
    numStr: '#Z5 / 06',
    deckName: 'Codex Arcanum',
    name: 'Telekinese',
    subtitle: 'Manipulationszauber · Fernwirken',
    art: './art_assets/MasterArtwork/Cards/Magic/A_dynamic_dungeon_action_scene_bewildered_snarling_goblin_rea_a277be3d-0d4a-428d-ba54-83cf4d415399_2.png',
    lore: '»Unsichtbare Finger greifen durch den Raum. Schalter kippen, Riegel schnappen auf und Klingen entgleiten verblüfften Fäusten.«',
    chip1Label: 'Reichweite',
    chip1Val: '4 Felder',
    chip1Class: 'target-val',
    chip2Label: 'Erschöpfung',
    chip2Val: '1 Box',
    chip2Class: 'timing-val',
    chip3Label: 'Typ',
    chip3Val: 'Interaktion',
    chip3Class: 'type-val',
    chip3BoxClass: 'highlight-gold',
    rulesTitle: 'Geistige Manipulation',
    rulesBody: 'Öffne auf Distanz eine unverschlossene Tür, betätige Hebel oder hole Loot heran. <strong>Im Kampf (Zauberwurf vs. VT):</strong> Entwaffnet humanoide Feinde (<strong>-1 Schaden bis Kampfende</strong>). Waffenlose Bestien &amp; Bosse können nicht entwaffnet werden, werden aber <strong>2 Felder zurückgestoßen</strong>.',
    footerDeck: 'Codex Arcanum · Magiegelehrte',
    rarity: 'Akademie-Zauber',
    cardBackImg: CODEX_ARCANUM_BACK_IMG,
    cardBackTitle: 'Codex Arcanum',
    accentColor: '#4a6984', // Telekinesis Slate
    accentGlow: 'rgba(74, 105, 132, 0.25)'
  },
  {
    id: 'Z6',
    numStr: '#Z6 / 06',
    deckName: 'Codex Arcanum',
    name: 'Blendendes Licht',
    subtitle: 'Schwächungszauber · Heilige Luminanz',
    art: './art_assets/MasterArtwork/Cards/Magic/A_dynamic_dungeon_action_scene_two_decrepit_skeleton_warriors_a9f28f28-5e44-4f78-81e6-de98dbf38cf6_0.png',
    lore: '»Eine gleißende Sonneneruption zerreißt die Finsternis der Krypta. Kreaturen der Nacht schreien schmerzerfüllt auf und taumeln blind.«',
    chip1Label: 'Reichweite',
    chip1Val: '3 Felder',
    chip1Class: 'target-val',
    chip2Label: 'Erschöpfung',
    chip2Val: '1 Box',
    chip2Class: 'timing-val',
    chip3Label: 'Ziel',
    chip3Val: 'Bis zu 2 Feinde',
    chip3Class: 'type-val',
    chip3BoxClass: 'highlight-shield',
    rulesTitle: 'Lichtblitz & Verblendung',
    rulesBody: 'Ein Ziel oder eine Gruppe von bis zu <strong>2 benachbarten Feinden</strong> wird geblendet. Betroffene Ziele erleiden bis zum Ende der aktuellen Runde <strong>Nachteil auf alle Angriffe</strong> (2d6, der niedrigere Würfel zählt).',
    footerDeck: 'Codex Arcanum · Magiegelehrte',
    rarity: 'Akademie-Zauber',
    cardBackImg: CODEX_ARCANUM_BACK_IMG,
    cardBackTitle: 'Codex Arcanum',
    accentColor: '#967425', // Solar Gold
    accentGlow: 'rgba(150, 116, 37, 0.25)'
  },

  // --- DIE 8 CHAOTISCHEN GOBLINZAUBER (DRUNK MAGIC) ---
  {
    id: 'G01',
    numStr: '#01 / 08',
    deckName: 'Goblinzauber',
    name: 'Rülpser des Verderbens',
    subtitle: 'Fehlzündung · Schwefelodem',
    art: './art_assets/MasterArtwork/Cards/Magic/A_comical_dynamic_dungeon_action_scene_drunken_smirking_rogue_e78e8ca8-0143-4206-af0a-aaabc7c79e3d_2.png',
    lore: '»Ein herzhafter Schluck Fusel entlädt sich in einer giftgrünen Wolke fauliger Eier. Die Kriegstänzerin würgt vor Ekel.«',
    chip1Label: 'Reichweite',
    chip1Val: 'Angrenzend',
    chip1Class: 'target-val',
    chip2Label: 'Kosten',
    chip2Val: '1 Schluck Fusel',
    chip2Class: 'timing-val',
    chip3Label: 'Wirkung',
    chip3Val: 'Nachteil (Alle)',
    chip3Class: 'type-val',
    chip3BoxClass: 'highlight-stat',
    rulesTitle: 'Schwefelwolke',
    rulesBody: 'Eine stinkende Schwefelwolke bricht hervor! <strong>Alle angrenzenden Figuren</strong> (Freund und Feind!) husten tränenden Auges und erleiden <strong>Nachteil auf ihren nächsten Wurf</strong>. Der Goblin kichert unverschämt.',
    footerDeck: 'Goblinzauber · Halsabschneider',
    rarity: 'Chaosmagie',
    cardBackImg: GOBLIN_FUSEL_BACK_IMG,
    cardBackTitle: 'Goblin-Fusel',
    accentColor: '#58731f', // Acid Moss
    accentGlow: 'rgba(88, 115, 31, 0.25)'
  },
  {
    id: 'G02',
    numStr: '#02 / 08',
    deckName: 'Goblinzauber',
    name: 'Guck mal, da drüben!',
    subtitle: 'Ablenkung · Trugbild-Rauch',
    art: './art_assets/MasterArtwork/Cards/Magic/A_comical_dynamic_dungeon_action_scene_two_confused_skeleton__5367dbeb-8037-45be-a886-7d578956bddc_1.png',
    lore: '»Eine lila Rauchpuppe fuchtelt beleidigend mit den Armen. Während die Skelette darauf eindreschen, verschwindet der echte Goblin klammheimlich.«',
    chip1Label: 'Reichweite',
    chip1Val: 'Selbst',
    chip1Class: 'target-val',
    chip2Label: 'Kosten',
    chip2Val: '1 Schluck Fusel',
    chip2Class: 'timing-val',
    chip3Label: 'Zustand',
    chip3Val: 'Verborgen',
    chip3Class: 'type-val',
    chip3BoxClass: 'highlight-shield',
    rulesTitle: 'Phantomschleier',
    rulesBody: 'Ein verblüffendes Trugbild narrt die Gegner! Alle anwesenden Monster wenden sich irritiert ab. Der Goblin erhält sofort den Zustand <strong>Verborgen / Versteckt</strong>, selbst wenn er mitten auf offener Fläche steht!',
    footerDeck: 'Goblinzauber · Halsabschneider',
    rarity: 'Chaosmagie',
    cardBackImg: GOBLIN_FUSEL_BACK_IMG,
    cardBackTitle: 'Goblin-Fusel',
    accentColor: '#7d3c98', // Illusion Violet
    accentGlow: 'rgba(125, 60, 152, 0.25)'
  },
  {
    id: 'G03',
    numStr: '#03 / 08',
    deckName: 'Goblinzauber',
    name: 'Zufälliger Funkenregen',
    subtitle: 'Chaotischer Schaden · Zündelei',
    art: './art_assets/MasterArtwork/Cards/Magic/A_comical_dynamic_dungeon_action_scene_panicked_wide-eyed_gob_d35aa72b-4616-473a-b0c9-7bbcc24c3767_3.png',
    lore: '»Fitzelnde Funken spritzen kreuz und quer aus den Krallenspitzen. Herrlich warm – bis plötzlich der eigene Lederärmel lichterloh brennt!«',
    chip1Label: 'Reichweite',
    chip1Val: '3 Felder',
    chip1Class: 'target-val',
    chip2Label: 'Kosten',
    chip2Val: '1 Schluck Fusel',
    chip2Class: 'timing-val',
    chip3Label: 'Schaden',
    chip3Val: '2 Feuerschaden',
    chip3Class: 'type-val',
    chip3BoxClass: 'highlight-stat',
    rulesTitle: 'Funkenflug & Ärmelbrand',
    rulesBody: 'Wähle 1 Ziel in Reichweite: Erleidet <strong>2 Feuerschaden</strong>. Würfle danach sofort <code>1d6</code>: Bei einer <strong>1</strong> fängt auch die eigene Kleidung des Goblins Feuer und er erhält den Zustand <strong>Brennend</strong>.',
    footerDeck: 'Goblinzauber · Halsabschneider',
    rarity: 'Chaosmagie',
    cardBackImg: GOBLIN_FUSEL_BACK_IMG,
    cardBackTitle: 'Goblin-Fusel',
    accentColor: '#b95c00', // Spark Orange
    accentGlow: 'rgba(185, 92, 0, 0.25)'
  },
  {
    id: 'G04',
    numStr: '#04 / 08',
    deckName: 'Goblinzauber',
    name: 'Gummiknochen-Schub',
    subtitle: 'Agilität · Schmerzfreie Sehnen',
    art: './art_assets/MasterArtwork/Cards/Magic/A_comical_dynamic_dungeon_action_scene_agile_goblin_leaping_e_c7a02026-2208-4366-aee2-57ae043e936d_2.png',
    lore: '»Vollgepumpt mit hochprozentigem Fusel spürt der kleine Schurke weder Gelenkschmerz noch Vernunft und federt wie ein Gummiball davon.«',
    chip1Label: 'Reichweite',
    chip1Val: 'Selbst',
    chip1Class: 'target-val',
    chip2Label: 'Kosten',
    chip2Val: '1 Schluck Fusel',
    chip2Class: 'timing-val',
    chip3Label: 'Bonus',
    chip3Val: '+3 Bewegung',
    chip3Class: 'type-val',
    chip3BoxClass: 'highlight-gold',
    rulesTitle: 'Elastischer Hechtsprung',
    rulesBody: 'Die Beine federn unnatürlich elastisch! Der Goblin erhält sofort <strong>+3 Felder Bewegungsweite</strong> für diesen Zug und ignoriert jegliches schwierige Gelände (Geröll, Treppen, Schleim) ohne Tempoverlust.',
    footerDeck: 'Goblinzauber · Halsabschneider',
    rarity: 'Chaosmagie',
    cardBackImg: GOBLIN_FUSEL_BACK_IMG,
    cardBackTitle: 'Goblin-Fusel',
    accentColor: '#1e8449', // Rubber Leaf Green
    accentGlow: 'rgba(30, 132, 73, 0.25)'
  },
  {
    id: 'G05',
    numStr: '#05 / 08',
    deckName: 'Goblinzauber',
    name: 'Magischer Klebefinger',
    subtitle: 'Diebstahl · Ektoplasma-Grapscher',
    art: './art_assets/MasterArtwork/Cards/Magic/A_comical_dynamic_dungeon_action_scene_sticky_glowing_violet__6a222261-a43c-439c-bf03-3037dc66659c_0.png',
    lore: '»Ein schleimig-violetter Geistarm schnellt vor! Ehe der Wächter begreift, klebt sein Prunkkelch schon in den gierigen Krallen des Goblins.«',
    chip1Label: 'Reichweite',
    chip1Val: '2 Felder',
    chip1Class: 'target-val',
    chip2Label: 'Kosten',
    chip2Val: '1 Schluck Fusel',
    chip2Class: 'timing-val',
    chip3Label: 'Beute',
    chip3Val: 'Waffe od. Loot',
    chip3Class: 'type-val',
    chip3BoxClass: 'highlight-gold',
    rulesTitle: 'Ektoplasma-Klau',
    rulesBody: 'Ein klebriger Geistarm schnappt zu! Entreiße einem Gegner in 2 Feldern 1 Waffe/Schild (Gegner hat <strong>-1 Schaden bis Rundenende</strong>) ODER ziehe sofort <strong>1 Ausrüstungskarte</strong> vom Nachziehstapel!',
    footerDeck: 'Goblinzauber · Halsabschneider',
    rarity: 'Chaosmagie',
    cardBackImg: GOBLIN_FUSEL_BACK_IMG,
    cardBackTitle: 'Goblin-Fusel',
    accentColor: '#884ea0', // Ectoplasm Purple
    accentGlow: 'rgba(136, 78, 160, 0.25)'
  },
  {
    id: 'G06',
    numStr: '#06 / 08',
    deckName: 'Goblinzauber',
    name: 'Reine Akademie-Magie!',
    subtitle: 'Volltreffer · Göttlicher Zufallsblitz',
    art: './art_assets/MasterArtwork/Cards/Magic/A_comical_dynamic_dungeon_action_scene_colossal_blazing_white_66ba4eef-f25a-4660-a842-df2732eab339_1.png',
    lore: '»Zur maßlosen Empörung der Magiegelehrten gelingt dem trunkenen Wichtel durch reines Schicksalsglück die perfekteste Blitzlanze des Zeitalters.«',
    chip1Label: 'Reichweite',
    chip1Val: 'Sichtlinie',
    chip1Class: 'target-val',
    chip2Label: 'Kosten',
    chip2Val: '1 Schluck Fusel',
    chip2Class: 'timing-val',
    chip3Label: 'Schaden',
    chip3Val: '4 Blitz (Rüst. 0)',
    chip3Class: 'type-val',
    chip3BoxClass: 'highlight-stat',
    rulesTitle: 'Kaiserlicher Donnerkeil',
    rulesBody: 'Ein ohrenbetäubender weißblauer Blitz kracht herab! Ein Ziel in Sichtlinie erleidet verheerende <strong>4 Blitzschaden</strong>, welche jegliche <strong>Rüstung vollständig ignorieren</strong>. Der Goblin tanzt hämisch.',
    footerDeck: 'Goblinzauber · Halsabschneider',
    rarity: 'Chaosmagie',
    cardBackImg: GOBLIN_FUSEL_BACK_IMG,
    cardBackTitle: 'Goblin-Fusel',
    accentColor: '#2471a3', // Thunderbolt Azure
    accentGlow: 'rgba(36, 113, 163, 0.25)'
  },
  {
    id: 'G07',
    numStr: '#07 / 08',
    deckName: 'Goblinzauber',
    name: 'Blitz-Rückschlag',
    subtitle: 'Negativ-Effekt ⚡ · Fehlzündung',
    art: './art_assets/MasterArtwork/Cards/Magic/A_comical_dynamic_dungeon_action_scene_singed_groggy_rogue_go_6e5e7165-14f2-4705-9aea-98de45fb6b3d_0.png',
    lore: '»Autsch! Falsches Ende! Ein ohrenbetäubender Knall hüllt den kleinen Magier in Rußschwaden. Seine Ohren rauchen und die Haare stehen zu Berge.«',
    chip1Label: 'Ziel',
    chip1Val: 'Selbst!',
    chip1Class: 'type-val',
    chip2Label: 'Kosten',
    chip2Val: '1 Schluck Fusel',
    chip2Class: 'timing-val',
    chip3Label: 'Rückschlag',
    chip3Val: '2 Schaden + Stun',
    chip3Class: 'type-val',
    chip3BoxClass: 'highlight-stat',
    rulesTitle: 'Rohrkrepierer',
    rulesBody: 'Die Magie entlädt sich nach hinten! Der Goblin erleidet selbst <strong>2 Blitzschaden</strong> (ignoriert Rüstung!) und wird sofort <strong>Betäubt</strong> (verliert die nächste Hauptaktion). Sein Gesicht ist tief rußgeschwärzt.',
    footerDeck: 'Goblinzauber · Halsabschneider',
    rarity: 'Fehlzündung',
    cardBackImg: GOBLIN_FUSEL_BACK_IMG,
    cardBackTitle: 'Goblin-Fusel',
    accentColor: '#922b21', // Danger Backfire Rust
    accentGlow: 'rgba(146, 43, 33, 0.25)'
  },
  {
    id: 'G08',
    numStr: '#08 / 08',
    deckName: 'Goblinzauber',
    name: 'Huhn der Verdammnis',
    subtitle: 'Chaos-Beschwörung 🐔 · Bestien-Raserei',
    art: './art_assets/MasterArtwork/Cards/Magic/A_comical_dynamic_dungeon_action_scene_comical_explosion_of_s_88254818-7f87-42c3-a5e6-a1b91f9de206_0.png',
    lore: '»Gack-gack?! Mit lautem Knall und einer Federwolke steht ein panisches Huhn im Saal. Jedes Raubtier verfällt augenblicklich in tollwütige Jagdgier.«',
    chip1Label: 'Platzierung',
    chip1Val: '1d6 Dir / 1d6 Dist',
    chip1Class: 'target-val',
    chip2Label: 'Kosten',
    chip2Val: '1 Schluck Fusel',
    chip2Class: 'timing-val',
    chip3Label: 'Kreatur',
    chip3Val: 'Huhn (1 LP)',
    chip3Class: 'type-val',
    chip3BoxClass: 'highlight-gold',
    rulesTitle: 'Raserei der Bestien',
    rulesBody: 'Platziere den <strong>Huhn-Marker</strong> via <code>1d6 Richtung + 1d6 Distanz</code>. <strong>Bestien-Raserei:</strong> Alle anwesenden Bestien (Worge, Ratten, Spinnen) brechen Angriffe auf Helden ab und jagen vorrangig das Huhn, bis es tot ist (<strong>1 LP</strong>)!',
    footerDeck: 'Goblinzauber · Halsabschneider',
    rarity: 'Chaos-Marker',
    cardBackImg: GOBLIN_FUSEL_BACK_IMG,
    cardBackTitle: 'Goblin-Fusel',
    accentColor: '#b7950b', // Poultry Ochre
    accentGlow: 'rgba(183, 149, 11, 0.25)'
  }
];

function generateHTML() {
  const cardsPerPage = 2; // 2 card pairs per A4 page
  const totalPages = Math.ceil(MAGIC_CARDS.length / cardsPerPage);
  const pages = [];
  const navLinks = [];

  for (let p = 0; p < totalPages; p++) {
    const pageNum = p + 1;
    const pageId = `page-${pageNum}`;
    const startIdx = p * cardsPerPage;
    const pageCards = MAGIC_CARDS.slice(startIdx, startIdx + cardsPerPage);

    navLinks.push(`<a href="#${pageId}" class="nav-link">Bogen ${pageNum}</a>`);

    let pairsHtml = '';
    pageCards.forEach((card, idx) => {
      const posClass = idx === 0 ? 'pos-1' : 'pos-2';
      const c1Box = card.chip1BoxClass ? ` ${card.chip1BoxClass}` : '';
      const c2Box = card.chip2BoxClass ? ` ${card.chip2BoxClass}` : '';
      const c3Box = card.chip3BoxClass ? ` ${card.chip3BoxClass}` : '';

      pairsHtml += `
      <!-- CARD PAIR ${card.id}: FRONT (LEFT) + DIEGETIC BACK (RIGHT) -->
      <div class="card-pair ${posClass}">
        <!-- FRONT FACE (LEFT) -->
        <div class="tarot-face front-face">
          <div class="card-border-frame" style="border-color: ${card.accentColor || '#2c2016'};"></div>
          <div class="card-border-inner"></div>

          <div class="card-header">
            <h1 class="card-title">${card.name}</h1>
            <p class="card-subtitle">${card.subtitle}</p>
          </div>

          <div class="art-container">
            <img src="${card.art}" alt="${card.name}" class="card-art" />
            <div class="art-vignette"></div>
          </div>

          <div class="lore-box">
            <p class="lore-text">${card.lore}</p>
          </div>

          <div class="stat-ribbon">
            <div class="stat-chip${c1Box}">
              <span class="stat-label">${card.chip1Label}</span>
              <span class="stat-value ${card.chip1Class}">${card.chip1Val}</span>
            </div>
            <div class="stat-chip${c2Box}">
              <span class="stat-label">${card.chip2Label}</span>
              <span class="stat-value ${card.chip2Class}">${card.chip2Val}</span>
            </div>
            <div class="stat-chip${c3Box}">
              <span class="stat-label">${card.chip3Label}</span>
              <span class="stat-value ${card.chip3Class}">${card.chip3Val}</span>
            </div>
          </div>

          <div class="rules-box">
            <div class="section-header" style="color: ${card.accentColor || '#8c1d18'};">
              <span class="rule-title">${card.rulesTitle}</span>
              <span class="rule-type">${card.deckName}</span>
            </div>
            <p class="rule-body">${card.rulesBody}</p>
          </div>

          <div class="card-footer">
            <span class="footer-left">${card.footerDeck}</span>
            <span class="footer-center">${card.numStr}</span>
            <span class="footer-right">${card.rarity}</span>
          </div>
        </div>

        <!-- BACK FACE (RIGHT) -->
        <div class="tarot-face back-face">
          <img src="${card.cardBackImg}" alt="${card.cardBackTitle}" class="card-back-img" />
          ${card.cardBackTitle === 'Codex Arcanum' ? `
          <div class="back-title-overlay overlay-codex-arcanum">
            <svg class="back-title-svg" viewBox="0 0 58.5 9.0">
              <text x="29.25" y="6.1"
                    text-anchor="middle"
                    font-family="'UnifrakturMaguntia', cursive"
                    font-size="7.4"
                    fill="#111111"
                    textLength="48"
                    lengthAdjust="spacingAndGlyphs">Codex Arcanum</text>
            </svg>
          </div>
          ` : `
          <div class="back-title-overlay overlay-goblin-fusel">
            <svg class="back-title-svg" viewBox="0 0 58.5 10.3">
              <text x="29.25" y="7.0"
                    text-anchor="middle"
                    font-family="'UnifrakturMaguntia', cursive"
                    font-size="8.4"
                    fill="#111111"
                    textLength="46"
                    lengthAdjust="spacingAndGlyphs">Goblin-Fusel</text>
            </svg>
          </div>
          `}
        </div>
      </div>
      `;
    });

    pages.push(`
    <div class="page" id="${pageId}">
      <!-- CROP MARKS & FOLD GUIDE -->
      <svg class="crop-svg" xmlns="http://www.w3.org/2000/svg">
        <!-- Vertical fold line along X = 105 mm (Sheet midline) -->
        <line x1="105mm" y1="5mm" x2="105mm" y2="8.5mm" class="mark-fold" />
        <line x1="105mm" y1="146.5mm" x2="105mm" y2="150.5mm" class="mark-fold" />
        <line x1="105mm" y1="288.5mm" x2="105mm" y2="292mm" class="mark-fold" />

        <!-- Pair 1 Cut lines (Y: 8.5mm, 146.5mm; X: 23.33mm, 186.67mm) -->
        <line x1="18mm" y1="8.5mm" x2="23.33mm" y2="8.5mm" class="mark-cut" />
        <line x1="186.67mm" y1="8.5mm" x2="192mm" y2="8.5mm" class="mark-cut" />
        <line x1="18mm" y1="146.5mm" x2="23.33mm" y2="146.5mm" class="mark-cut" />
        <line x1="186.67mm" y1="146.5mm" x2="192mm" y2="146.5mm" class="mark-cut" />
        <line x1="23.33mm" y1="4mm" x2="23.33mm" y2="8.5mm" class="mark-cut" />
        <line x1="186.67mm" y1="4mm" x2="186.67mm" y2="8.5mm" class="mark-cut" />

        <!-- Pair 2 Cut lines (Y: 150.5mm, 288.5mm; X: 23.33mm, 186.67mm) -->
        <line x1="18mm" y1="150.5mm" x2="23.33mm" y2="150.5mm" class="mark-cut" />
        <line x1="186.67mm" y1="150.5mm" x2="192mm" y2="150.5mm" class="mark-cut" />
        <line x1="18mm" y1="288.5mm" x2="23.33mm" y2="288.5mm" class="mark-cut" />
        <line x1="186.67mm" y1="288.5mm" x2="192mm" y2="288.5mm" class="mark-cut" />
        <line x1="23.33mm" y1="288.5mm" x2="23.33mm" y2="293mm" class="mark-cut" />
        <line x1="186.67mm" y1="288.5mm" x2="186.67mm" y2="293mm" class="mark-cut" />
      </svg>

      ${pairsHtml}
    </div>
    `);
  }

  return `<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <title>RV_Quest · Magie- & Zauberkarten (Codex Arcanum & Goblinzauber)</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Alegreya+Sans:ital,wght@0,400;0,700;1,400;1,700&family=Alegreya:ital,wght@0,400;0,700;1,400&family=Cinzel:wght@600;700;900&family=UnifrakturMaguntia&display=swap" rel="stylesheet">
  <style>
    @page { size: A4 portrait; margin: 0; }
    * { box-sizing: border-box; margin: 0; padding: 0; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
    body {
      background: #2a2521;
      font-family: 'Alegreya', Georgia, serif;
      color: #1a140e;
      display: flex;
      flex-direction: column;
      align-items: center;
      padding: 20px 0;
      gap: 20px;
    }
    @media screen {
      .toolbar {
        position: sticky; top: 10px; z-index: 1000;
        background: #1b1612; border: 1px solid #7a5f28; border-radius: 8px;
        padding: 10px 18px; display: flex; align-items: center; gap: 14px;
        box-shadow: 0 4px 18px rgba(0, 0, 0, 0.6); color: #e9dbc2; font-family: 'Cinzel', serif; font-size: 13px;
      }
      .toolbar button {
        background: linear-gradient(180deg, #9e782f 0%, #6f5119 100%);
        border: 1px solid #d4af37; border-radius: 4px; color: #fff;
        padding: 6px 14px; font-family: 'Cinzel', serif; font-weight: 700;
        cursor: pointer; font-size: 12px; transition: transform 0.1s;
      }
      .toolbar button:hover { transform: scale(1.03); background: #b88d37; }
      .page-nav { display: flex; gap: 6px; }
      .nav-link {
        color: #d4af37; text-decoration: none; padding: 4px 8px; border-radius: 3px;
        border: 1px solid #5a4620; font-size: 11px;
      }
      .nav-link:hover { background: #9e782f; color: #fff; }
      .page { background: #ffffff; box-shadow: 0 8px 30px rgba(0, 0, 0, 0.45); }
    }
    @media print {
      .no-print { display: none !important; }
      body { background: #ffffff !important; padding: 0; }
      .page { box-shadow: none !important; page-break-after: always; break-after: page; }
    }
    .page { width: 210mm; height: 297mm; position: relative; overflow: hidden; background: #ffffff; }
    .card-pair { position: absolute; left: 23.33mm; width: 163.34mm; height: 138mm; display: flex; }
    .card-pair.pos-1 { top: 8.5mm; }
    .card-pair.pos-2 { top: 150.5mm; }
    .tarot-face { width: 81.67mm; height: 138mm; position: relative; overflow: hidden; }
    .front-face {
      background: radial-gradient(circle at 50% 25%, #fdfbf7 0%, #f4ece0 65%, #e6d7c2 100%);
      padding: 2.2mm 3.2mm 2.0mm 3.2mm; display: flex; flex-direction: column; justify-content: space-between;
    }
    .card-border-frame {
      position: absolute; top: 1.1mm; bottom: 1.1mm; left: 1.1mm; right: 1.1mm;
      border: 0.45mm solid #2c2016; border-radius: 1.5mm; pointer-events: none;
    }
    .card-border-inner {
      position: absolute; top: 1.7mm; bottom: 1.7mm; left: 1.7mm; right: 1.7mm;
      border: 0.22mm solid #9e782f; border-radius: 1.2mm; pointer-events: none; opacity: 0.85;
    }
    .card-header { text-align: center; position: relative; z-index: 2; padding: 0 0.5mm 0.2mm 0.5mm; }
    .card-title {
      font-family: 'Cinzel', serif; font-size: 10.6pt; font-weight: 900; color: #1a140e;
      letter-spacing: 0.2mm; margin: 0.2mm 0 0.1mm 0; text-transform: uppercase; line-height: 1.05;
    }
    .card-subtitle { font-family: 'Alegreya', serif; font-size: 7.0pt; font-style: italic; color: #5c4736; margin: 0; line-height: 1.1; }
    .art-container {
      width: 56.5mm; height: 56.5mm; aspect-ratio: 1 / 1; position: relative; border-radius: 1.3mm;
      overflow: hidden; border: 0.45mm solid #3b2c1d; background: #ffffff; margin: 0.3mm auto 0.5mm auto;
      box-shadow: 0 0.8mm 2.2mm rgba(0, 0, 0, 0.18);
    }
    .card-art {
      width: 100%; height: 100%; object-fit: contain; object-position: center center;
      display: block; background-color: #ffffff; filter: contrast(1.03) saturate(1.02);
    }
    .art-vignette {
      position: absolute; inset: 0; box-shadow: inset 0 0 4mm rgba(60, 40, 20, 0.25);
      pointer-events: none; border: 0.2mm solid rgba(158, 120, 47, 0.45);
    }
    .lore-box {
      background: rgba(246, 237, 220, 0.75);
      border-left: 0.65mm solid #8c6a3a;
      border-right: 0.65mm solid #8c6a3a;
      border-top: 0.2mm solid rgba(140, 106, 58, 0.3);
      border-bottom: 0.2mm solid rgba(140, 106, 58, 0.3);
      border-radius: 0.6mm;
      padding: 0.5mm 1.5mm;
      margin: 0.1mm 0.4mm 0.4mm 0.4mm;
      text-align: center;
      z-index: 2;
      box-shadow: 0 0.3mm 0.8mm rgba(0, 0, 0, 0.05);
    }
    .lore-text {
      font-family: 'Alegreya', serif; font-size: 6.6pt; font-style: italic;
      color: #453424; line-height: 1.18; margin: 0; letter-spacing: 0.02mm;
    }
    .stat-ribbon {
      display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 0.8mm;
      margin: 0.2mm 0.4mm 0.4mm 0.4mm; z-index: 2;
    }
    .stat-chip {
      background: #ffffff; border: 0.32mm solid #6e5741; border-radius: 0.9mm;
      padding: 0.5mm 0.4mm; text-align: center; display: flex; flex-direction: column;
      justify-content: center; align-items: center; min-height: 6.8mm;
      box-shadow: 0 0.2mm 0.6mm rgba(0, 0, 0, 0.08);
    }
    .stat-chip.highlight-stat { background: linear-gradient(180deg, #fcedec 0%, #f4d3d2 100%); border-color: #8c1d18; }
    .stat-chip.highlight-shield { background: linear-gradient(180deg, #eff7ff 0%, #d3e5f7 100%); border-color: #3b6b99; }
    .stat-chip.highlight-gold { background: linear-gradient(180deg, #fffcf0 0%, #fae8b8 100%); border-color: #b88e38; }
    .stat-label { font-size: 5.4pt; font-weight: 700; text-transform: uppercase; letter-spacing: 0.15mm; color: #5c4736; line-height: 1; margin-bottom: 0.2mm; }
    .stat-value { font-family: 'Alegreya Sans', sans-serif; font-size: 7.0pt; font-weight: 700; color: #1a140e; line-height: 1.15; }
    .stat-value.type-val { font-family: 'Cinzel', serif; font-weight: 900; color: #8c1d18; }
    .stat-chip.highlight-gold .stat-value.type-val { color: #7a5410; }
    .stat-value.target-val { color: #1a446e; }
    .stat-value.timing-val { font-family: 'Cinzel', serif; font-size: 6.8pt; font-weight: 900; color: #7a5410; }
    .rules-box {
      background: #ffffff; border: 0.32mm solid #4a3828; border-radius: 1.1mm;
      padding: 0.8mm 1.5mm 0.8mm 1.5mm; display: flex; flex-direction: column; gap: 0.5mm;
      margin: 0 0.4mm 0.4mm 0.4mm; z-index: 2; box-shadow: inset 0 0 1.5mm rgba(0, 0, 0, 0.04);
    }
    .section-header {
      font-family: 'Cinzel', serif; font-size: 6.6pt; font-weight: 700; color: #8c1d18;
      letter-spacing: 0.25mm; text-transform: uppercase; border-bottom: 0.2mm solid rgba(140, 29, 24, 0.25);
      padding-bottom: 0.2mm; display: flex; justify-content: space-between; align-items: center;
    }
    .rule-title { font-family: 'Cinzel', serif; font-weight: 900; color: #2b1f15; }
    .rule-type { font-family: 'Alegreya Sans', sans-serif; font-size: 5.6pt; color: #666; text-transform: uppercase; }
    .rule-body { font-size: 6.9pt; line-height: 1.25; color: #1a140e; margin: 0; }
    .rule-body strong { color: #8c1d18; font-weight: 700; }
    .rule-body code { font-family: 'Cinzel', serif; font-weight: 700; font-size: 6.8pt; color: #2b1f15; background: #eee5d8; padding: 0.1mm 0.8mm; border-radius: 0.4mm; }
    .card-footer {
      display: flex; justify-content: space-between; align-items: center; padding: 0.2mm 0.8mm 0 0.8mm;
      font-size: 5.4pt; font-weight: 700; color: #5c4736; letter-spacing: 0.1mm; z-index: 2; text-transform: uppercase;
    }
    .back-face { background: #140f0c; position: relative; }
    .card-back-img { width: 100%; height: 100%; object-fit: cover; display: block; }
    .back-title-overlay {
      position: absolute;
      left: 11.5mm;
      width: 58.5mm;
      pointer-events: none;
    }
    .back-title-overlay.overlay-codex-arcanum {
      top: 124.0mm;
      height: 9.0mm;
    }
    .back-title-overlay.overlay-goblin-fusel {
      top: 116.5mm;
      height: 10.3mm;
    }
    .back-title-svg {
      width: 100%;
      height: 100%;
      display: block;
    }
    .crop-svg { position: absolute; top: 0; left: 0; width: 210mm; height: 297mm; pointer-events: none; }
    .mark-cut { stroke: #111111; stroke-width: 0.22; stroke-linecap: square; }
    .mark-fold { stroke: #992222; stroke-width: 0.28; stroke-dasharray: 1.5, 1; }
  </style>
</head>
<body>
  <div class="toolbar no-print">
    <span>🔮 <strong>Magiedeck: Codex Arcanum & Goblinzauber (#Z1–Z6 & #01–#08)</strong> (14 Karten · 7 Bögen)</span>
    <div class="page-nav">
      ${navLinks.join('\n      ')}
    </div>
    <button class="print-btn" onclick="window.print()">🖨️ Alle 7 Bögen drucken / PDF</button>
  </div>

  ${pages.join('\n')}
</body>
</html>`;
}

const outputPath = path.join(PRINTABLES_DIR, 'magic_cards_all_gutterfold_a4.html');
fs.writeFileSync(outputPath, generateHTML(), 'utf8');
console.log('Successfully generated Magic Cards printable sheet at: ' + outputPath);
