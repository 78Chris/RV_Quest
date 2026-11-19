/**
 * Card Generator CLI for RV_Quest
 * Reads markdown card definitions & images, generates A4 gutter-fold print sheets.
 */
const fs = require('fs');
const path = require('path');

const ROOT_DIR = path.resolve(__dirname, '..');
const PRINTABLES_DIR = path.join(ROOT_DIR, 'printables');
const ART_DIR = path.join(PRINTABLES_DIR, 'art_assets', 'MasterArtwork', 'Cards');

const DECKS = {
  armor: {
    title: 'Ausrüstungsdeck: Rüstungen & Schilde (#25–#36)',
    sourcePrompt: path.join(PRINTABLES_DIR, 'EQUIPMENT_PROMPTS_ARMOR.md'),
    sourceList: path.join(ROOT_DIR, 'components', 'card_list.md'),
    imageDir: path.join(ART_DIR, 'Armour'),
    cardBack: 'Board_game_card_back_colord_woodcut_style_forbidden_midnight__21652bf5-8ecb-4a43-8d05-67df8e29d436_3.png',
    cardBackTitle: 'Der Schattenbazar',
    defaultType: 'Rüstung',
    idRange: [25, 36],
    outFile: path.join(PRINTABLES_DIR, 'armor_cards_all_gutterfold_a4.html')
  },
  melee: {
    title: 'Ausrüstungsdeck: Nahkampfwaffen (#01–#16)',
    sourcePrompt: path.join(PRINTABLES_DIR, 'EQUIPMENT_PROMPTS_MELEE.md'),
    sourceList: path.join(ROOT_DIR, 'components', 'card_list.md'),
    imageDir: path.join(ART_DIR, 'Weapons'),
    cardBack: 'Board_game_card_back_colord_woodcut_style_forbidden_midnight__21652bf5-8ecb-4a43-8d05-67df8e29d436_3.png',
    cardBackTitle: 'Der Schattenbazar',
    defaultType: 'Waffe',
    idRange: [1, 16],
    outFile: path.join(PRINTABLES_DIR, 'melee_cards_all_gutterfold_a4.html')
  },
  ranged: {
    title: 'Ausrüstungsdeck: Fernkampfwaffen (#17–#24)',
    sourcePrompt: path.join(PRINTABLES_DIR, 'EQUIPMENT_PROMPTS_RANGED.md'),
    sourceList: path.join(ROOT_DIR, 'components', 'card_list.md'),
    imageDir: path.join(ART_DIR, 'Weapons'),
    cardBack: 'Board_game_card_back_colord_woodcut_style_forbidden_midnight__21652bf5-8ecb-4a43-8d05-67df8e29d436_3.png',
    cardBackTitle: 'Der Schattenbazar',
    defaultType: 'Waffe',
    idRange: [17, 24],
    outFile: path.join(PRINTABLES_DIR, 'ranged_cards_all_gutterfold_a4.html')
  },
  consumables: {
    title: 'Ausrüstungsdeck: Verbrauchsgegenstände (#37–#46)',
    sourcePrompt: path.join(PRINTABLES_DIR, 'EQUIPMENT_PROMPTS_CONSUMABLES.md'),
    sourceList: path.join(ROOT_DIR, 'components', 'card_list.md'),
    imageDir: path.join(ART_DIR, 'Trinkets'),
    cardBack: 'Board_game_card_back_colord_woodcut_style_forbidden_midnight__21652bf5-8ecb-4a43-8d05-67df8e29d436_3.png',
    cardBackTitle: 'Der Schattenbazar',
    defaultType: 'Verbrauch',
    idRange: [37, 46],
    outFile: path.join(PRINTABLES_DIR, 'consumable_cards_all_gutterfold_a4.html')
  },
  trinkets: {
    title: 'Ausrüstungsdeck: Zubehör & Relikte (#47–#54)',
    sourcePrompt: path.join(PRINTABLES_DIR, 'EQUIPMENT_PROMPTS_TRINKETS.md'),
    sourceList: path.join(ROOT_DIR, 'components', 'card_list.md'),
    imageDir: path.join(ART_DIR, 'Trinkets'),
    cardBack: 'Board_game_card_back_colord_woodcut_style_forbidden_midnight__21652bf5-8ecb-4a43-8d05-67df8e29d436_3.png',
    cardBackTitle: 'Der Schattenbazar',
    defaultType: 'Zubehör',
    idRange: [47, 54],
    outFile: path.join(PRINTABLES_DIR, 'trinket_cards_all_gutterfold_a4.html')
  }
};

/**
 * Standard atmospheric lore quotes for equipment
 */
const LORE_TEXTS = {
  // Melee
  1: '»Ausgewogen geschmiedet für Soldaten der Reichswehr. Eine Klinge ohne Schnörkel, die im dichten Gewölbegemenge niemals enttäuscht.«',
  2: '»Schwerer als die Vernunft gebietet. Mit dieser Klinge spaltet man Schild und Träger in einem einzigen, wuchtigen Hieb.«',
  3: '»Sechs gehärtete Stahlflansche auf massivem Metallschaft. Hinterlässt keine Wunden, sondern zermalmtes Gebein.«',
  4: '»In den Schmieden von Athel Loren aus Mondsilber gezogen. Gleitet durch die Luft wie der Herbstwind durch verdorrtes Laub.«',
  5: '»Die Waffe der Palastwache. Ihr Gewicht verlangt zwei feste Hände, doch ihr Rundumschwung räumt jede Vormauer frei.«',
  6: '»Eine schmale Nadel aus mattschwarzem Stahl. Dringt durch jede Schwachstelle, ehe das Opfer den kalten Hauch spürt.«',
  7: '»Gezahnter Stahl für grausame Hiebe. Reißt tiefe Furchen, die den Feind noch lange nach dem Schlag schwächen.«',
  8: '»Uralte Schriftzeichen glimmen blau im geschwärzten Eisen. Jeder Aufschlag entlädt einen dumpfen, donnernden Schock.«',
  9: '»Eiserne Spitze, Axtblatt und Reißhaken. Hält Feinde auf Distanz und schlägt sicher über die Schultern der ersten Reihe hinweg.«',
  10: '»Kompakter Zwergenstahl, getaucht in Erzkohle. Zertrümmert mühelos die Rüstungsplatten selbst ältester Gruftkrieger.«',
  11: '»Gusseiserner Stachelball an fünf schweren Kettengliedern. Umgeht hochgezogene Schilde mit erbarmungsloser Wucht.«',
  12: '»Feinster Klingenstahl und kunstvoll geschwungener Korbgriff. Ein Stich dorthin, wo der Panzer sich öffnet.«',
  13: '»Eine breite Fehlschärfe zum Fangen gegnerischer Hiebe. Die verlässliche Begleiterin für jeden erfahrenen Duellanten.«',
  14: '»Riesiges Henkersbeil des eisigen Nordens. Ein einziger Fehltritt kostet Zeit, doch ein Treffer beendet jede Debatte.«',
  15: '»Eschenholz und geschärfter Blattstahl. Wer auf die Phalanx zustürmt, läuft geradewegs in sein Verderben.«',
  16: '»Vom Syndikat geschwärzte Klinge mit geheimem Federmechanismus. Tödliche Präzision aus dem Schatten heraus.«',
  // Ranged
  17: '»Aus bestem Eibenholz gespannt. Zielsicher und schnell genug, um fliehendes Wild und heranstürmende Goblins zu stoppen.«',
  18: '»Verstärkter Stahlbogen und Nussholzschaft. Schlägt selbst durch gehärtete Eisenbleche wie durch Pergament.«',
  19: '»Ein hochgewachsener Bogen aus federndem Weißholz. Pfeile fliegen flach und lautlos über gewaltige Distanzen.«',
  20: '»Drei perfekt ausbalancierte Wurfklingen. Ein Griff an den Gürtel, und das Ziel wird noch vor dem Ansturm genagelt.«',
  21: '»Solider Wurfspeer mit gehärteter Eisenspitze. Durchbohrt heranstürmende Bestien und bricht deren Schwung.«',
  22: '»Ausgetüfteltes Zahnrad- und Hebelwerk. Ermöglicht Salven scharfer Bolzen in atemberaubender Folge.«',
  23: '»Kompakte Bartaxtköpfe auf griffigen Eschenholzschäften. Schleudert selbst zähe Angreifer meterweit zurück.«',
  24: '»Dunkles Bambusrohr mit Runengravuren. Lautlose Nadeln, deren Gift das Herz des Ziels fast unbemerkt lähmt.«',
  // Armor
  25: '»Aus zähem Hirschleder gegerbt und mit geschwärzten Nieten verstärkt. Leicht genug, um lautlos durch die Katakomben zu huschen.«',
  26: '»Tausende ineinander verflochtene Ringe aus kaltem Eisen. Dämpft selbst wuchtige Schwerthiebe und das Reißen scharfer Monsterklauen.«',
  27: '»Echtes Meisterstück der imperialen Plattenschmiede. Verwandelt den Träger in eine uneinnehmbare wandelnde Festung.«',
  28: '»Zähes Eschenholz mit genietetem Eisenbuckel. Fängt tödliche Schwerthiebe ab, ohne die Beweglichkeit einzuschränken.«',
  29: '»Schwerer Setzschild aus massiven Eichenplanken. Bietet der ganzen Gruppe verlässliche Deckung vor herabregnenden Pfeilen.«',
  30: '»Gewoben aus Schattenfäden und Elfenstoff. Bricht die Konturen des Trägers im Halbdunkel vollkommen auf.«',
  31: '»Kompakter eiserner Faustschild. Klein genug für schmale Gänge und wendig genug für blitzschnelle Paraden.«',
  32: '»Mit brutalen Eisendornen besetzter Holzschild. Jeder geblockte Hieb wird für den Angreifer zur schmerzhaften Falle.«',
  33: '»Geschmiedeter Eisenhut der Stadtwache. Schützt zuverlässig vor herabstürzenden Trümmern und betäubenden Keulenhieben.«',
  34: '»Furchterregende Trophäe aus dem Ödland. Verleiht dem Träger den unaufhaltsamen Zorn eines anstürmenden Tiers.«',
  35: '»Überlappende Horn- und Zwergenstahlplättchen. Schützt wie schwerer Harnisch, biegt sich aber geschmeidig bei jedem Schritt.«',
  36: '»Mit schützenden Schutzglyphen überzogene Rüstung. Neutralisiert sengendes Feuer und eisige Kälte bevor sie Fleisch treffen.«',
  // Consumables
  37: '»Glühende rubinrote Flüssigkeit in geschliffenem Kristall. Schließt selbst klaffende Wunden in Sekundenschnelle.«',
  38: '»Der verlässliche Begleiter eines jeden Abenteurers. Stoppt Blutungen und bringt verlorene Lebensgeister zurück.«',
  39: '»Dickflüssiges bernsteinfarbenes Gebräu. Lässt Muskeln und Knochen wie massives Eichenholz erstarren.«',
  40: '»Funkelndes azurblaues Elixier. Beschleunigt den Puls und lässt die Welt ringsumher wie in Zeitlupe erscheinen.«',
  41: '»Zähflüssiges Gift aus den finstersten Sümpfen. Schon ein Tropfen auf der Klinge schwächt jeden Feind zusehends.«',
  42: '»Zwergischer Sprengstoff in dickem Gusseisen. Ein Funke genügt, um ganze Räume in sengendes Flammenmeer zu tauchen.«',
  43: '»Mächtige Alchemistenkräuter in getriebener Bronzeschale. Der aufsteigende Rauch klärt den Geist und vertreibt alle Erschöpfung.«',
  44: '»Klares smaragdgrünes Gegengift. Zersetzt selbst die tückischsten Monstergifte und löst lähmende Betäubung auf.«',
  45: '»Trockenfleisch, Zwergenbrot und Hartkäse. Eine kräftigende Rast stellt die Ausdauer aller Gefährten wieder her.«',
  46: '»Instabiles alchemistisches Gemisch. Zerplatzt beim Aufprall in ein zischendes Flammenmeer, das den Weg versperrt.«',
  // Trinkets
  47: '»Ein feines goldenes Medaillon an geflochtenem Lederband. Scheint das Schicksal im rechten Moment zu wenden.«',
  48: '»Aus verschlungenem Silber und leuchtendem Smaragd geschmiedet. Lässt den Träger trittsicher über jedes Hindernis gleiten.«',
  49: '»Geschwärzter Federstahl im feinen Lederetui. Gefertigt nach den Geheimnissen der Schlossergilde zu Altdorf.«',
  50: '»Filigraner Stirnreif aus Silber und Saphir. Fokussiert arkanes Wissen und erlaubt das Wirken mächtiger Zauber ohne Ermüdung.«',
  51: '»Lautlose Stiefel aus weichem Schattenleder. Ermöglichen das mühelose Entkommen aus bedrohlichen Nahkämpfen.«',
  52: '»Uralter mit Schutzrunen gravierter Rabenschädel-Talisman. Bewahrt den Träger vor dem endgültigen Schritt über die Schwelle.«',
  53: '»Pechgetränkte Fackel auf starkem Eichenholz. Vertreibt die lähmende Finsternis selbst aus den tiefsten Gruftkammern.«',
  54: '»Aus Tierknochen geschnitzte Würfel mit ungleichmäßigen Kanten. Ein gewagtes Spiel auf Leben und Tod.«'
};

/**
 * Parse equipment cards from card_list.md
 */
function parseCardList(filePath, [minId, maxId], deckKey) {
  if (!fs.existsSync(filePath)) return [];
  const lines = fs.readFileSync(filePath, 'utf-8').split(/\r?\n/);
  const cards = [];

  const sectionHeaders = {
    melee: '### A. Nahkampfwaffen',
    ranged: '### B. Fernkampfwaffen',
    armor: '### C. Rüstungen',
    consumables: '### D. Verbrauchsgegenstände',
    trinkets: '### E. Zubehör'
  };

  let inTargetSection = false;

  for (const line of lines) {
    const trimmed = line.trim();
    if (trimmed.startsWith('### ')) {
      inTargetSection = sectionHeaders[deckKey] && trimmed.includes(sectionHeaders[deckKey]);
    }

    if (!inTargetSection) continue;
    if (!trimmed.startsWith('|')) continue;
    const parts = trimmed.split('|').map(p => p.trim());
    if (parts.length < 5) continue;

    // Check if column 1 is numeric ID
    const rawId = parts[1].replace(/[^0-9]/g, '');
    if (!rawId) continue;
    const id = parseInt(rawId, 10);
    if (isNaN(id) || id < minId || id > maxId) continue;

    const name = parts[2].replace(/\*\*/g, '').trim();
    const slot = parts[3].trim();

    let stat = '';
    let gold = '';
    let effect = '';

    if (deckKey === 'trinkets') {
      // Trinkets table: | # | Name | Slot | Gold | Effekt |
      gold = parts[4].trim();
      effect = parts[5].trim();
      stat = '–';
    } else if (parts.length >= 8) {
      stat = parts[4].trim();
      gold = parts[5].trim();
      effect = parts[6].trim();
    } else if (parts.length === 7) {
      stat = parts[4].trim();
      gold = parts[5].trim();
      effect = parts[6].trim();
    }

    cards.push({ id, name, slot, stat, gold, effect });
  }

  return cards;
}

/**
 * Match image in directory to card
 */
function findImageForCard(card, imageDir) {
  if (!fs.existsSync(imageDir)) return null;
  const files = fs.readdirSync(imageDir).filter(f => f.endsWith('.png') || f.endsWith('.jpg'));
  if (files.length === 0) return null;

  const clean = str => str.toLowerCase().replace(/[^a-z0-9]/g, ' ');
  const cardTokens = clean(card.name).split(/\s+/).filter(w => w.length > 3);

  // Exact card ID / known filename maps
  const known = {
    1: 'broadsword',
    2: 'massive_heavy_war_axe',
    3: 'medieval_gothic_fl',
    4: 'elven_longsword',
    5: 'two-handed_greatsword',
    6: 'stiletto',
    7: 'cavalry_sabre',
    8: 'dwarven_warhammer',
    9: 'palace_guard_halberd',
    10: 'heavy_iron_warhamm',
    11: 'inquisitors_flail',
    12: 'dueling_rapier',
    13: 'main-gauche_parrying_dagger',
    14: 'executioners_axe',
    15: 'long_military_pike',
    16: 'shadow_blade',
    17: 'shortbow',
    18: 'heavy_military_crossbow',
    19: 'elven_longbow',
    20: 'throwing_knives',
    21: 'javelin',
    22: 'repeating_crossbow',
    23: 'throwing_axes',
    24: 'bamboo_blowgun',
    37: 'large_ornate_faceted_glass_flask',
    38: 'small_simple_round_glass_vial',
    39: 'thick_sturdy_amber-brown',
    40: 'sleek_tall_elegant_glass_vial',
    41: 'small_sinister_dark_glass_vial',
    42: 'heavy_iron-cased_dwarven_grenade',
    43: 'ornate_bronze_incense_burner',
    44: 'delicate_glass_ampoule',
    45: 'leather-wrapped_bundle',
    46: 'round_glass_flask',
    47: 'ornate_golden_amulet',
    48: 'rustic_silver_signet_ring',
    49: 'master_locksmith_tool_roll',
    50: 'noble_arcane_head_band',
    51: 'rogue_boots',
    52: 'raven_skull',
    53: 'torch',
    54: 'goblin_bone_d6_dice'
  };

  if (known[card.id]) {
    const key = known[card.id];
    const match = files.find(f => f.toLowerCase().includes(key));
    if (match) return match;
  }

  // Common synonyms mapping
  const syns = {
    'lederwams': ['leather', 'jerkin', 'vest'],
    'kettenhemd': ['chainmail', 'hauberk'],
    'plattenpanzer': ['plate', 'gothic', 'cuirass'],
    'rundschild': ['round', 'shield', 'viking'],
    'turmschild': ['tower', 'shield', 'pavise'],
    'schattenmantel': ['cloak', 'hooded', 'elven'],
    'faustschild': ['buckler', 'fist'],
    'buckler': ['buckler', 'fist'],
    'stachelschild': ['spike', 'shield', 'wooden'],
    'eisenhelm': ['kettle_hat', 'helmet', 'guard'],
    'hörnerhelm': ['horned', 'helmet', 'barbarian'],
    'schuppenpanzer': ['scale', 'dwarven'],
    'prunkrüstung': ['royal_knight', 'ceremonial', 'arcane']
  };

  for (const token of cardTokens) {
    if (syns[token]) {
      const match = files.find(f => {
        const lower = f.toLowerCase();
        return syns[token].every(s => lower.includes(s));
      });
      if (match) return match;
    }
  }

  // Fallback token matching
  let bestFile = null;
  let maxMatches = 0;
  for (const file of files) {
    const lower = file.toLowerCase();
    let count = 0;
    for (const t of cardTokens) {
      if (lower.includes(t)) count++;
    }
    if (count > maxMatches) {
      maxMatches = count;
      bestFile = file;
    }
  }

  return bestFile;
}

/**
 * Generate full A4 HTML
 */
function generateHtml(deckKey) {
  const config = DECKS[deckKey];
  if (!config) {
    console.error(`Unbekanntes Deck: ${deckKey}. Verfügbar: ${Object.keys(DECKS).join(', ')}`);
    process.exit(1);
  }

  console.log(`Lese Kartendaten für [${deckKey}] (${config.idRange[0]}–${config.idRange[1]})...`);
  const cards = parseCardList(config.sourceList, config.idRange, deckKey);
  console.log(`Gefundene Karten: ${cards.length}`);

  if (cards.length === 0) {
    console.error('Keine Karten gefunden.');
    return;
  }

  // Group into pairs (2 per A4 sheet)
  const pairs = [];
  for (let i = 0; i < cards.length; i += 2) {
    pairs.push([cards[i], cards[i + 1] || null]);
  }

  const relBackImgPath = `art_assets/MasterArtwork/Cards/Card Backs/${config.cardBack}`;

  let pagesHtml = '';
  let pageNavHtml = '';

  pairs.forEach((pair, pageIdx) => {
    const pageNum = pageIdx + 1;
    const [c1, c2] = pair;
    const label = c2 ? `#${c1.id} & #${c2.id}` : `#${c1.id}`;

    pageNavHtml += `<a href="#page${pageNum}" class="nav-link">Bogen ${pageNum} (${label})</a>\n`;

    pagesHtml += `
  <!-- BOGEN ${pageNum} (${label}) -->
  <div class="page" id="page${pageNum}">
    <svg class="crop-svg" viewBox="0 0 210 297" width="210mm" height="297mm">
      <line x1="23.33" y1="0.5" x2="23.33" y2="7.5" class="mark-cut" />
      <line x1="105" y1="0.5" x2="105" y2="7.5" class="mark-fold" />
      <line x1="186.67" y1="0.5" x2="186.67" y2="7.5" class="mark-cut" />

      <line x1="1.0" y1="8.5" x2="20.0" y2="8.5" class="mark-cut" />
      <line x1="190.0" y1="8.5" x2="209.0" y2="8.5" class="mark-cut" />
      <line x1="1.0" y1="146.5" x2="20.0" y2="146.5" class="mark-cut" />
      <line x1="190.0" y1="146.5" x2="209.0" y2="146.5" class="mark-cut" />

      <line x1="23.33" y1="147.0" x2="23.33" y2="150.0" class="mark-cut" />
      <line x1="105" y1="147.0" x2="105" y2="150.0" class="mark-fold" />
      <line x1="186.67" y1="147.0" x2="186.67" y2="150.0" class="mark-cut" />

      <line x1="1.0" y1="150.5" x2="20.0" y2="150.5" class="mark-cut" />
      <line x1="190.0" y1="150.5" x2="209.0" y2="150.5" class="mark-cut" />
      <line x1="1.0" y1="288.5" x2="20.0" y2="288.5" class="mark-cut" />
      <line x1="190.0" y1="288.5" x2="209.0" y2="288.5" class="mark-cut" />

      <line x1="23.33" y1="289.5" x2="23.33" y2="296.5" class="mark-cut" />
      <line x1="105" y1="289.5" x2="105" y2="296.5" class="mark-fold" />
      <line x1="186.67" y1="289.5" x2="186.67" y2="296.5" class="mark-cut" />

      <line x1="105" y1="8.5" x2="105" y2="146.5" stroke="#777777" stroke-width="0.14" stroke-dasharray="2, 2" opacity="0.65" />
      <line x1="105" y1="150.5" x2="105" y2="288.5" stroke="#777777" stroke-width="0.14" stroke-dasharray="2, 2" opacity="0.65" />
    </svg>
`;

    function renderCard(card, pos) {
      if (!card) return '';
      const imgFile = findImageForCard(card, config.imageDir);
      const relImg = imgFile ? path.relative(PRINTABLES_DIR, path.join(config.imageDir, imgFile)).replace(/\\/g, '/') : '';

      const isShield = card.slot.toLowerCase().includes('schild') || card.name.toLowerCase().includes('schild') || card.name.toLowerCase().includes('buckler');
      const isArmor = card.slot.toLowerCase().includes('rüstung');
      const isHelm = card.slot.toLowerCase().includes('kopf') || card.name.toLowerCase().includes('helm');

      const cardType = isShield ? 'Schild' : isArmor ? 'Rüstung' : isHelm ? 'Zubehör' : config.defaultType;
      
      let statLabel = '⚔️ Schaden';
      let statHighlightClass = 'highlight-stat';

      if (isShield || isArmor) {
        statLabel = '🛡️ ' + (isShield ? 'Reduktion' : 'Rüstung');
        statHighlightClass = 'highlight-shield';
      } else if (deckKey === 'trinkets') {
        statLabel = card.stat !== '–' && card.stat ? '🗝️ Modifikator' : '✨ Effekt';
        statHighlightClass = 'highlight-stat-green';
      } else if (deckKey === 'consumables') {
        statLabel = '🧪 Typ';
        statHighlightClass = 'highlight-stat-green';
      }

      const statVal = (card.stat && card.stat !== '–') ? card.stat : (card.slot.includes('Trank') ? 'Trank' : 'Spezial');
      const loreText = LORE_TEXTS[card.id] || '»Aus den Schatten des Basars geborgen. Nützlich für jene, die sich in die finsteren Tiefen wagen.«';

      return `
    <!-- KARTE #${card.id}: ${card.name} -->
    <div class="card-pair ${pos}">
      <div class="tarot-face front-face">
        <div class="card-border-frame"></div>
        <div class="card-border-inner"></div>
        <div class="card-header">
          <h2 class="card-title">${card.name}</h2>
          <p class="card-subtitle">◈ Ausrüstungsdeck · ${cardType}</p>
        </div>
        <div class="art-container">
          ${relImg ? `<img class="card-art" src="${relImg}" alt="${card.name}">` : '<div style="display:flex;align-items:center;justify-content:center;height:100%;color:#888;">[Kein Bild]</div>'}
          <div class="art-vignette"></div>
        </div>
        <div class="lore-box">
          <p class="lore-text">${loreText}</p>
        </div>
        <div class="stat-ribbon">
          <div class="stat-chip ${statHighlightClass}"><span class="stat-label">${statLabel}</span><span class="stat-value">${statVal}</span></div>
          <div class="stat-chip"><span class="stat-label">Slot</span><span class="stat-value" style="font-size:7.5pt;">${card.slot}</span></div>
          <div class="stat-chip highlight-gold"><span class="stat-label">💰 Wert</span><span class="stat-value" style="font-size:7.5pt; color:#7a5410;">${card.gold} Gold</span></div>
        </div>
        <div class="rules-box">
          <div class="section-header">
            <span>📜 Gegenstandseffekt</span>
            <span class="rule-title">Sonderregel</span>
          </div>
          <p class="rule-body">${card.effect}</p>
        </div>
        <div class="card-footer">
          <span>🗡️ ${config.cardBackTitle}</span>
          <span>#${String(card.id).padStart(2, '0')} / 54</span>
        </div>
      </div>
      <div class="tarot-face back-face">
        <img class="card-back-img" src="${relBackImgPath}" alt="Rückseite">
      </div>
    </div>`;
    }

    pagesHtml += renderCard(c1, 'pos-1');
    if (c2) pagesHtml += renderCard(c2, 'pos-2');
    pagesHtml += `\n  </div>\n`;
  });

  const fullHtml = `<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="utf-8">
  <title>${config.title} - A4 Gutter-Fold</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;900&family=Alegreya:ital,wght@0,400;0,600;0,700;1,400;1,600&family=Alegreya+Sans:ital,wght@0,400;0,500;0,700;1,400&display=swap" rel="stylesheet">
  <style>
    @page { size: A4 portrait; margin: 0; }
    * { box-sizing: border-box; }
    html, body {
      margin: 0; padding: 0; background: #ffffff;
      font-family: 'Alegreya Sans', sans-serif; color: #1a140e;
      -webkit-print-color-adjust: exact; print-color-adjust: exact;
    }
    @media screen {
      body {
        background: #1c1814; padding: 30px 0; display: flex; flex-direction: column; align-items: center; gap: 30px;
      }
      .toolbar {
        position: fixed; top: 15px; right: 20px; background: #140f0c; border: 1px solid #5c4736;
        color: #dfcaa7; padding: 10px 18px; border-radius: 8px; font-size: 13px; display: flex;
        gap: 15px; align-items: center; box-shadow: 0 4px 20px rgba(0, 0, 0, 0.6); z-index: 1000;
      }
      .print-btn {
        background: #9e782f; color: #fff; border: none; padding: 7px 16px; border-radius: 4px;
        cursor: pointer; font-weight: bold; font-size: 13px; box-shadow: 0 2px 6px rgba(0, 0, 0, 0.3);
      }
      .print-btn:hover { background: #b88e38; }
      .page-nav { display: flex; gap: 6px; }
      .nav-link {
        color: #dfcaa7; text-decoration: none; padding: 4px 8px; border-radius: 3px;
        background: rgba(255, 255, 255, 0.08); font-size: 11px; font-weight: bold;
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
    .card-header { text-align: center; position: relative; z-index: 2; padding: 0 0.5mm 0.3mm 0.5mm; }
    .card-title {
      font-family: 'Cinzel', serif; font-size: 11.2pt; font-weight: 900; color: #1a140e;
      letter-spacing: 0.2mm; margin: 0.2mm 0 0.1mm 0; text-transform: uppercase; line-height: 1.05;
    }
    .card-subtitle { font-family: 'Alegreya', serif; font-size: 7.6pt; font-style: italic; color: #5c4736; margin: 0; line-height: 1.1; }
    .art-container {
      width: 56.5mm; height: 56.5mm; aspect-ratio: 1 / 1; position: relative; border-radius: 1.3mm;
      overflow: hidden; border: 0.45mm solid #3b2c1d; background: #ffffff; margin: 0.4mm auto 0.6mm auto;
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
      padding: 0.6mm 1.6mm;
      margin: 0.2mm 0.4mm 0.5mm 0.4mm;
      text-align: center;
      z-index: 2;
      box-shadow: 0 0.3mm 0.8mm rgba(0, 0, 0, 0.05);
    }
    .lore-text {
      font-family: 'Alegreya', serif; font-size: 6.8pt; font-style: italic;
      color: #453424; line-height: 1.2; margin: 0; letter-spacing: 0.02mm;
    }
    .stat-ribbon {
      display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.2mm;
      margin: 0.2mm 0.4mm 0.6mm 0.4mm; z-index: 2;
    }
    .stat-chip {
      background: linear-gradient(180deg, #fdfaf4 0%, #efe4d0 100%); border: 0.28mm solid #8c6a3a;
      border-radius: 1.0mm; padding: 0.4mm 0.8mm; text-align: center; display: flex; flex-direction: column;
      justify-content: center; box-shadow: 0 0.3mm 0.8mm rgba(0, 0, 0, 0.12);
    }
    .stat-chip.highlight-stat { background: linear-gradient(180deg, #fcedec 0%, #f4d3d2 100%); border-color: #8c1d18; }
    .stat-chip.highlight-shield { background: linear-gradient(180deg, #eff7ff 0%, #d3e5f7 100%); border-color: #3b6b99; }
    .stat-chip.highlight-stat-green { background: linear-gradient(180deg, #eef7f0 0%, #d2e7d7 100%); border-color: #2a6639; }
    .stat-chip.highlight-gold { background: linear-gradient(180deg, #fffcf0 0%, #fae8b8 100%); border-color: #b88e38; }
    .stat-label { font-size: 5.6pt; font-weight: 700; text-transform: uppercase; letter-spacing: 0.2mm; color: #5c4736; line-height: 1; margin-bottom: 0.2mm; }
    .stat-value { font-family: 'Cinzel', serif; font-size: 10.5pt; font-weight: 900; color: #1a140e; line-height: 1; }
    .stat-chip.highlight-stat .stat-value { color: #8c1d18; }
    .stat-chip.highlight-shield .stat-value { color: #1a446e; }
    .stat-chip.highlight-stat-green .stat-value { color: #1c522a; }
    .stat-chip.highlight-gold .stat-value { color: #7a5410; }
    .rules-box {
      background: #ffffff; border: 0.32mm solid #4a3828; border-radius: 1.1mm;
      padding: 0.8mm 1.6mm 0.9mm 1.6mm; display: flex; flex-direction: column; gap: 0.6mm;
      margin: 0 0.4mm 0.5mm 0.4mm; z-index: 2; box-shadow: inset 0 0 1.5mm rgba(0, 0, 0, 0.04);
    }
    .section-header {
      font-family: 'Cinzel', serif; font-size: 6.8pt; font-weight: 700; color: #8c1d18;
      letter-spacing: 0.25mm; text-transform: uppercase; border-bottom: 0.2mm solid rgba(140, 29, 24, 0.25);
      padding-bottom: 0.2mm; display: flex; justify-content: space-between; align-items: center;
    }
    .rule-title { font-family: 'Cinzel', serif; font-weight: 900; color: #2b1f15; }
    .rule-body { font-size: 7.2pt; line-height: 1.25; color: #1a140e; margin: 0; }
    .rule-body strong { color: #8c1d18; font-weight: 700; }
    .card-footer {
      display: flex; justify-content: space-between; align-items: center; padding: 0.2mm 1.0mm 0 1.0mm;
      font-size: 5.6pt; font-weight: 700; color: #5c4736; letter-spacing: 0.1mm; z-index: 2; text-transform: uppercase;
    }
    .back-face { background: #140f0c; }
    .card-back-img { width: 100%; height: 100%; object-fit: cover; display: block; }
    .crop-svg { position: absolute; top: 0; left: 0; width: 210mm; height: 297mm; pointer-events: none; }
    .mark-cut { stroke: #111111; stroke-width: 0.22; stroke-linecap: square; }
    .mark-fold { stroke: #992222; stroke-width: 0.28; stroke-dasharray: 1.5, 1; }
  </style>
</head>
<body>
  <div class="toolbar no-print">
    <span>🛡️ <strong>${config.title}</strong> (${cards.length} Karten · ${pairs.length} Bögen)</span>
    <div class="page-nav">
      ${pageNavHtml}
    </div>
    <button class="print-btn" onclick="window.print()">🖨️ Alle ${pairs.length} Bögen drucken / PDF</button>
  </div>
  ${pagesHtml}
</body>
</html>`;

  fs.writeFileSync(config.outFile, fullHtml, 'utf-8');
  console.log(`✅ Erfolgreich generiert: ${config.outFile}`);
}

const targetDeck = process.argv[2] || 'armor';
generateHtml(targetDeck);
