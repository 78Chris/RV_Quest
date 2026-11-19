/**
 * Encounter Cards Generator for RV_Quest
 * Produces A4 gutter-fold print sheets (Tarot 81.67 x 138 mm, folding to standard height).
 */
const fs = require('fs');
const path = require('path');

const ROOT_DIR = path.resolve(__dirname, '..');
const PRINTABLES_DIR = path.join(ROOT_DIR, 'printables');
const ART_DIR = path.join(PRINTABLES_DIR, 'art_assets', 'MasterArtwork', 'Cards');

const CARD_BACK_IMG = './art_assets/MasterArtwork/Cards/Card%20Backs/vintage_medieval_woodcut_etching_of_a_dark_dungeon_doorway_en_67ef1647-9bfe-4d93-95eb-efadf7cba3a4_1.png';

const ENCOUNTER_CARDS = [
  {
    id: 'B01',
    name: 'Banden-Vorposten',
    subtitle: 'Goblins & Plünderer · Raumbegegnung',
    art: './art_assets/MasterArtwork/Cards/Encounters/A_dynamic_dungeon_encounter_scene_two_snarling_green-skinned__7e304e48-8d54-4895-9bb7-abd41e9f219a_3.png',
    lore: '»Hinter hastig aufgetürmten Kisten funkeln gierige gelbe Augen. Ehe die Fackel den Raum erhellt, sirrt bereits die erste Bogensehne durch die Finsternis.«',
    monsters: '2× Goblin-Späher [V]<br>1× Goblin-Bogenschütze [H]',
    element: '1× Umgestürzte Kiste (Deckung)',
    threat: 'Standard-Initiative',
    specialTitle: 'Befestigter Posten',
    specialBody: 'Die Goblins nutzen die Barrikade als Deckung (+1 Verteidigung gegen Fernkampf). Die vorderen Späher blockieren den Durchgang zur hinteren Raumhälfte.',
    footerDeck: 'Begegnungsdeck',
    footerNum: 'B01 / B16',
    rarity: 'Begegnung'
  },
  {
    id: 'B02',
    name: 'Hinterhalt aus den Schatten!',
    subtitle: 'Goblins & Plünderer · Überraschung',
    art: './art_assets/MasterArtwork/Cards/Encounters/A_dynamic_dungeon_encounter_scene_armored_metal_boot_of_a_her_6bb891d0-2057-4200-9bb9-35c16d3edd9f_3.png',
    lore: '»Ein leises Klirren, ein reißender Draht – und schrille Schädelglocken zerschneiden die Stille! Aus den Felsnischen stürzen gierige Klingen auf die Vorhut herab.«',
    monsters: '2× Goblin-Späher [V]<br>1× Goblin-Bogenschütze [H]',
    element: '1× Stolperdraht-Falle',
    threat: '»HINTERHALT!«',
    specialTitle: 'Überraschungsangriff',
    specialBody: '<strong>»Hinterhalt!«</strong> Alle Monster dieses Raumes aktivieren in Runde 1 <strong>vor allen Helden</strong>! Der vorderste Held muss <code>GES (SG 6)</code> bestehen oder stürzt zu Boden (verliert 2 Bewegungspunkte).',
    footerDeck: 'Begegnungsdeck',
    footerNum: 'B02 / B16',
    rarity: 'Hinterhalt'
  },
  {
    id: 'B03',
    name: 'Plünderer-Nest',
    subtitle: 'Goblins & Plünderer · Raubbeute',
    art: './art_assets/MasterArtwork/Cards/Encounters/A_dynamic_dungeon_encounter_scene_three_startled_green-skinne_0a549886-3136-4acd-abf5-da8a1be66aa2_1.png',
    lore: '»Goldstücke klimpern auf nassen Stein. Ertappt bei ihrer Beuteteilung starren die Kreaturen mit weit aufgerissenen Augen und gezückten Hackmessern empor.«',
    monsters: '3× Goblin-Späher [V/H]',
    element: '1× Verschlossene Kiste (1d6 Gold)',
    threat: 'Feiglinge im Chaos',
    specialTitle: 'Gierige Plünderer',
    specialBody: '<strong>Feiglinge:</strong> Flieht ein Goblin unter 50% LP, ruft er keine Verstärkung, sondern lässt vor Schreck einen Teil der Beute fallen. Die Kiste kann mit <code>LIS (SG 6)</code> geöffnet werden.',
    footerDeck: 'Begegnungsdeck',
    footerNum: 'B03 / B16',
    rarity: 'Begegnung'
  },
  {
    id: 'B04',
    name: 'Wachposten mit Bluthund',
    subtitle: 'Goblins & Bestien · Alarmposten',
    art: './art_assets/MasterArtwork/Cards/Encounters/A_dynamic_dungeon_encounter_scene_massive_ferocious_wasteland_e9a82a66-c240-41f7-b0ee-aa632b8a6090_1.png',
    lore: '»Die rostige Kette rasselt straff. Mit gefletschten Fängen zerrt die Bestie am Halsband, während der Goblinführer die Sperre mit boshaftem Kichern löst.«',
    monsters: '1× Goblin-Bogenschütze [H]<br>1× Ödland-Worg [V]',
    element: '1× Lagerfeuer (Feld brennt)',
    threat: 'Sturmangriff des Worgs',
    specialTitle: 'Von der Kette gelassen',
    specialBody: 'Der Ödland-Worg stürmt sofort mit maximaler Bewegungsweite auf den nächsten Helden zu. Figuren, die das <strong>Lagerfeuer</strong> betreten oder hineingestoßen werden, erleiden <strong>1 Feuerschaden</strong>.',
    footerDeck: 'Begegnungsdeck',
    footerNum: 'B04 / B16',
    rarity: 'Begegnung'
  },
  {
    id: 'B05',
    name: 'Ruhelose Wache',
    subtitle: 'Untote & Nekromantie · Phalanx',
    art: './art_assets/MasterArtwork/Cards/Encounters/A_dynamic_dungeon_encounter_scene_two_armored_skeleton_sentin_799eb5c3-1ebb-4254-9702-ac6cdbfdb157_1.png',
    lore: '»Seit Jahrhunderten tot, doch ihre Disziplin bricht nicht. Schulter an Schulter schlagen ihre Bronzespeere im Takt gegen schwere Eichenschilde.«',
    monsters: '2× Skelettkrieger [V]',
    element: '1× Verstaubte Urne',
    threat: 'Disziplinierte Phalanx',
    specialTitle: 'Schildwall der Toten',
    specialBody: '<strong>Schildwall:</strong> Solange beide Skelette auf benachbarten Feldern stehen, erhalten sie <strong>+1 Verteidigung</strong> gegen alle frontalen Angriffe. Das Zerschlagen der Urne wirbelt dichten Aschestaub auf.',
    footerDeck: 'Begegnungsdeck',
    footerNum: 'B05 / B16',
    rarity: 'Begegnung'
  },
  {
    id: 'B06',
    name: 'Erwachen der Ahnen',
    subtitle: 'Untote & Nekromantie · Kryptagrube',
    art: './art_assets/MasterArtwork/Cards/Encounters/A_dynamic_dungeon_encounter_scene_three_decrepit_skeleton_war_4f830d45-5c52-46bc-aa1f-a6901470a567_2.png',
    lore: '»Der Boden erzittert unter knirschendem Fels. Eiskaltes Geisterfeuer flackert in leeren Augenhöhlen auf, als bleiche Knochenfinger aus der Gruft emporgreifen.«',
    monsters: '3× Skelettkrieger [V/H]',
    element: '1× Offene Grube (Schwierig)',
    threat: 'Aufsteigende Horde',
    specialTitle: 'Knochenknacken',
    specialBody: 'Die offene Grube zählt als schwieriges Terrain (2 BP pro Feld). <strong>Knochenknacken:</strong> Eine Magiegelehrte kann durch Ausgeben einer Aktion mit <code>VER (SG 6)</code> 1 Skelett durch reine Willenskraft sofort zerschmettern.',
    footerDeck: 'Begegnungsdeck',
    footerNum: 'B06 / B16',
    rarity: 'Begegnung'
  },
  {
    id: 'B07',
    name: 'Gruft der Bogenschützen',
    subtitle: 'Untote & Fernkampf · Kreuzfeuer',
    art: './art_assets/MasterArtwork/Cards/Encounters/A_dynamic_dungeon_encounter_scene_two_skeletal_bone_archers_l_9a7920e6-d455-4bca-a7f3-fdd59edcd9c1_2.png',
    lore: '»Hinter massiven gotischen Pfeilern lauern tote Schützen. Das Surren alter Sehnen hallt durch die Gruft, noch ehe der Nahkämpfer den Raum betritt.«',
    monsters: '1× Skelettkrieger [V]<br>2× Goblin-Bogenschützen [H]',
    element: '2× Steinsäulen (Volle Deckung)',
    threat: 'Deckungsfeuer',
    specialTitle: 'Taktisches Kreuzfeuer',
    specialBody: 'Die Fernkämpfer feuern geschützt aus voller Deckung hinter den Säulen. Der vorgezogene Skelettkrieger versucht Helden zu binden, damit die Schützen ungestört zielen können.',
    footerDeck: 'Begegnungsdeck',
    footerNum: 'B07 / B16',
    rarity: 'Begegnung'
  },
  {
    id: 'B08',
    name: 'Schändlicher Schrein',
    subtitle: 'Untote & Nekromantie · Altarruine',
    art: './art_assets/MasterArtwork/Cards/Encounters/A_dynamic_dungeon_encounter_scene_ornate_dark_basalt_necroman_cedb2323-f022-4e83-8397-3f11d2ac15b2_1.png',
    lore: '»Purpurne Dunstschwaden wabern aus dem schwarzen Basaltaltar. Wo die Magie den Knochen berührt, schließen sich Risse und abgeplatzter Kalk verhärtet sich von neuem.«',
    monsters: '2× Skelettkrieger [V]',
    element: '1× Dunkelaltar (Nekromantie)',
    threat: 'Nekrotische Aura',
    specialTitle: 'Regeneration des Schreins',
    specialBody: 'Solange der Schrein unversehrt steht, regenerieren alle anwesenden Untoten am Rundenende <strong>1 LP</strong>. Ein Held am Altar kann diesen mit <code>VER (SG 6)</code> oder <code>KRA (SG 7)</code> weihen bzw. zerschlagen.',
    footerDeck: 'Begegnungsdeck',
    footerNum: 'B08 / B16',
    rarity: 'Begegnung'
  },
  {
    id: 'B09',
    name: 'Grabkammer-Hinterhalt!',
    subtitle: 'Untote & Bestien · Sarkophag',
    art: './art_assets/MasterArtwork/Cards/Encounters/A_dynamic_dungeon_encounter_scene_massive_carved_stone_sarcop_eb8ef001-1255-4819-b645-1a1fe3b7c4ef_0.png',
    lore: '»Mit donnerndem Bersten zerspringt die gravierte Sarkophagplatte! In einer Wolke aus Grabstaub bricht der gekrönte Schlächter hervor, flankiert von knurrendem Ungeziefer.«',
    monsters: '2× Skelettkrieger [V]<br>1× Ödland-Worg [V]',
    element: '1× Steinsarkophag (Wertvolle Beute)',
    threat: '»HINTERHALT!«',
    specialTitle: 'Gruft-Ausbruch',
    specialBody: '<strong>»Hinterhalt!«</strong> Die Untoten brechen überraschend hervor und handeln in Runde 1 <strong>vor allen Helden</strong>! Nach dem Sieg birgt der geöffnete Sarkophag <strong>1 Ausrüstungskarte</strong> und <strong>1d6 Gold</strong>.',
    footerDeck: 'Begegnungsdeck',
    footerNum: 'B09 / B16',
    rarity: 'Hinterhalt'
  },
  {
    id: 'B10',
    name: 'Spinnennest',
    subtitle: 'Bestien & Ungeziefer · Gewölbedecke',
    art: './art_assets/MasterArtwork/Cards/Encounters/A_dynamic_dungeon_encounter_scene_colossal_hairy_black_giant__9d58f3d8-d47e-4726-9bd4-441e23d3777b_3.png',
    lore: '»Dicke weiße Gespinste dämpfen jeden Laut. Von der Decke glimmt das bösartige Rot dutzender Facettenaugen, während ätzendes Gift zischend auf die Fliesen tropft.«',
    monsters: '2× Riesenspinne [H]',
    element: 'Klebrige Weben (2 Felder verlangsamt)',
    threat: 'Giftfäden & Netze',
    specialTitle: 'Klebrige Giftweben',
    specialBody: 'Zu Beginn des Kampfes verschießen die Spinnen klebrige Netzstränge auf die vordersten Helden (Rettungswurf <code>GES SG 6</code> oder Zustand <code>Verlangsamt</code>). Das Betreten der Webenfelder kostet +1 BP.',
    footerDeck: 'Begegnungsdeck',
    footerNum: 'B10 / B16',
    rarity: 'Begegnung'
  },
  {
    id: 'B11',
    name: 'Lauernde Brut',
    subtitle: 'Bestien & Goblins · Hinterhalt-Kokon',
    art: './art_assets/MasterArtwork/Cards/Encounters/A_dynamic_dungeon_encounter_scene_two_sneering_green-skinned__3e5fd036-9027-40e9-bba6-902fa21e72f2_2.png',
    lore: '»Höhnisch lachend locken die Goblins die Gruppe unter den moosigen Bogen – blind dafür, dass der wahre Jäger bereits lautlos am Seidenfaden über ihren Köpfen herabgleitet.«',
    monsters: '1× Riesenspinne [V]<br>2× Goblin-Späher [H]',
    element: '1× Seidenkokon (1 Heiltrank)',
    threat: 'Zangenangriff',
    specialTitle: 'Gefährliche Köder',
    specialBody: 'Während die Goblins mit Spottgesten die Aufmerksamkeit fesseln, seilt sich die Spinne direkt auf den Zugführer ab. Ein Aufschlitzen des Kokons mit einer scharfen Waffe offenbart <strong>1 Heiltrank</strong>.',
    footerDeck: 'Begegnungsdeck',
    footerNum: 'B11 / B16',
    rarity: 'Begegnung'
  },
  {
    id: 'B12',
    name: 'Worg-Bau',
    subtitle: 'Bestien & Raubtiere · Höhlenhöhle',
    art: './art_assets/MasterArtwork/Cards/Encounters/A_dynamic_dungeon_encounter_scene_two_ferocious_starving_wast_aea6e6b9-1608-4942-aa17-3c0502331d4d_3.png',
    lore: '»Zernagte Knochen splittern unter schweren Pranken. Ausgehungert und von blinder Wut getrieben schnappen die Raubtiere nach allem, was Fleisch und warmes Blut trägt.«',
    monsters: '2× Ödland-Worge [V]',
    element: 'Zernagte Knochen (1d6 Gold)',
    threat: 'Blutwitterung',
    specialTitle: 'Rasende Raubtiere',
    specialBody: '<strong>Blutwitterung:</strong> Worge verursachen <strong>+1 Schaden</strong> gegen Helden, die bereits unter 50% ihrer maximalen Lebenspunkte gefallen sind. Zwischen den Knochen können mit 1 Interaktion <strong>1d6 Gold</strong> geborgen werden.',
    footerDeck: 'Begegnungsdeck',
    footerNum: 'B12 / B16',
    rarity: 'Begegnung'
  },
  {
    id: 'B13',
    name: 'Krabbelndes Grauen',
    subtitle: 'Bestien & Untote · Deckensturz',
    art: './art_assets/MasterArtwork/Cards/Encounters/A_dynamic_dungeon_encounter_scene_terrifying_giant_spider_dro_006b8b38-8511-47db-9271-877907868c6d_3.png',
    lore: '»Aus einer geborstenen Deckenfissur bricht behaartes Grauen herab. Selbst der steinerne Gruftwächter weicht nicht, während Fangarme den Gang versperren.«',
    monsters: '1× Riesenspinne [H]<br>1× Skelettkrieger [V]',
    element: '1× Deckenloch (Einsturzgefahr)',
    threat: 'Überraschender Fall',
    specialTitle: 'Schrecken von Oben',
    specialBody: 'Die Spinne stürzt in Runde 1 überraschend von der Decke. Befindet sich ein Held direkt unter dem Deckenloch, muss er <code>GES (SG 6)</code> bestehen, um nicht niedergeschlagen zu werden.',
    footerDeck: 'Begegnungsdeck',
    footerNum: 'B13 / B16',
    rarity: 'Begegnung'
  },
  {
    id: 'B14',
    name: 'Verlassene Schatzkammer',
    subtitle: 'Besondere Räume · Eisentruhe & Falle',
    art: './art_assets/MasterArtwork/Cards/Encounters/A_dynamic_dungeon_scene_handsome_human_rogue_in_leather_glove_ed29a474-965f-464d-af12-a16b38d6f7f7_2.png',
    lore: '»Im Staub des verlassenen Gewölbes ruht eine prächtige, eisenbeschlagene Truhe. Doch gierige Finger sollten auf der Hut sein: Der Schnappmechanismus ist noch scharf.«',
    monsters: 'Keine Monster bei Eintritt',
    element: '1× Eisentruhe & Giftnadelfalle',
    threat: 'Stille vor dem Sturm',
    specialTitle: 'Tödliche Belohnung',
    specialBody: '<strong>Stille vor dem Sturm:</strong> Keine Monster zu Beginn! Beim Entschärfen oder Öffnen der Truhe muss <code>LIS (SG 6)</code> bestanden werden (sonst 2 Giftschaden). Nach dem Öffnen: Sofort <strong>1 Ereigniskarte</strong> und <strong>1 Ausrüstungskarte</strong> ziehen!',
    footerDeck: 'Begegnungsdeck',
    footerNum: 'B14 / B16',
    rarity: 'Sonderraum'
  },
  {
    id: 'B15',
    name: 'Heilige Quelle',
    subtitle: 'Besondere Räume · Geweihtes Wasser',
    art: './art_assets/MasterArtwork/Cards/Encounters/A_dynamic_dungeon_scene_armored_skeleton_sentinel_stepping_pr_c15bc810-36a3-48c3-967e-36b986b0023c_3.png',
    lore: '»Ein leuchtendes Wasserbecken strahlt reine, friedliche Wärme aus. Doch ein uralter Wächter in zerschlissener Wappenrobe hebt seine Hellebarde, um Unbefugten den Zutritt zu verwehren.«',
    monsters: '1× Skelettkrieger (Wächter)',
    element: '1× Leuchtendes Wasserbecken',
    threat: 'Geweihte Zuflucht',
    specialTitle: 'Lebensspendende Fluten',
    specialBody: 'Sobald der Wächter besiegt ist, dürfen Helden aus dem Becken trinken: Heilt sofort <strong>3 LP</strong> oder entfernt <strong>2 Erschöpfungs-Boxen</strong> (jeder Held maximal einmal im Szenario).',
    footerDeck: 'Begegnungsdeck',
    footerNum: 'B15 / B16',
    rarity: 'Sonderraum'
  },
  {
    id: 'B16',
    name: 'Der Kerker der Gefangenen',
    subtitle: 'Besondere Räume · Gefängniszelle',
    art: './art_assets/MasterArtwork/Cards/Encounters/A_dynamic_dungeon_encounter_scene_inside_a_damp_underground_p_c923d087-03de-422f-b4a5-5a5fc08b3a02_1.png',
    lore: '»Hinter rostigen Eisenstäben fleht ein gefangener Händler um Befreiung, während grinsende Wachen mit Knüppeln an das Gitter schlagen und sich an seiner Furcht ergötzen.«',
    monsters: '2× Goblin-Späher [V]',
    element: '1× Gefängniszelle (Verschlossen)',
    threat: 'Gefangenenrettung',
    specialTitle: 'Dankbarer Kaufmann',
    specialBody: 'Nach dem Sieg über die Wachen kann die Zelle mit <code>LIS (SG 5)</code> oder <code>KRA (SG 7)</code> geöffnet werden. Der befreite Kaufmann überreicht der Gruppe zum Dank <strong>1 sofortige Ausrüstungskarte</strong>!',
    footerDeck: 'Begegnungsdeck',
    footerNum: 'B16 / B16',
    rarity: 'Sonderraum'
  }
];

function generateHTML() {
  const pages = [];
  const totalSheets = 8; // 16 cards, 2 per sheet

  for (let i = 0; i < ENCOUNTER_CARDS.length; i += 2) {
    const sheetNum = (i / 2) + 1;
    const card1 = ENCOUNTER_CARDS[i];
    const card2 = ENCOUNTER_CARDS[i + 1];

    pages.push(`
  <!-- BOGEN ${sheetNum} (${card1.id} & ${card2.id}) -->
  <div class="page" id="page${sheetNum}">
    <svg class="crop-svg" viewBox="0 0 210 297" width="210mm" height="297mm">
      <line x1="23.33" y1="0.5" x2="23.33" y2="7.5" class="mark-cut" />
      <line x1="105" y1="0.5" x2="105" y2="7.5" class="mark-fold" />
      <line x1="186.67" y1="0.5" x2="186.67" y2="7.5" class="mark-cut" />
      <line x1="23.33" y1="289.5" x2="23.33" y2="296.5" class="mark-cut" />
      <line x1="105" y1="289.5" x2="105" y2="296.5" class="mark-fold" />
      <line x1="186.67" y1="289.5" x2="186.67" y2="296.5" class="mark-cut" />
      <line x1="0.5" y1="8.5" x2="7.5" y2="8.5" class="mark-cut" />
      <line x1="202.5" y1="8.5" x2="209.5" y2="8.5" class="mark-cut" />
      <line x1="0.5" y1="146.5" x2="7.5" y2="146.5" class="mark-cut" />
      <line x1="202.5" y1="146.5" x2="209.5" y2="146.5" class="mark-cut" />
      <line x1="0.5" y1="150.5" x2="7.5" y2="150.5" class="mark-cut" />
      <line x1="202.5" y1="150.5" x2="209.5" y2="150.5" class="mark-cut" />
      <line x1="0.5" y1="288.5" x2="7.5" y2="288.5" class="mark-cut" />
      <line x1="202.5" y1="288.5" x2="209.5" y2="288.5" class="mark-cut" />
    </svg>

    <!-- OBERE KARTE: ${card1.id} -->
    <div class="card-pair pos-1">
      <div class="tarot-face front-face">
        <div class="card-border-frame"></div>
        <div class="card-border-inner"></div>

        <div class="card-header">
          <h2 class="card-title">${card1.name}</h2>
          <p class="card-subtitle">${card1.subtitle}</p>
        </div>

        <div class="art-container">
          <img src="${card1.art}" alt="${card1.name}" class="card-art" />
          <div class="art-vignette"></div>
        </div>

        <div class="lore-box">
          <p class="lore-text">${card1.lore}</p>
        </div>

        <div class="stat-ribbon">
          <div class="stat-chip highlight-stat">
            <span class="stat-label">Aufstellung</span>
            <span class="stat-value monster-val">${card1.monsters}</span>
          </div>
          <div class="stat-chip highlight-shield">
            <span class="stat-label">Raum-Element</span>
            <span class="stat-value element-val">${card1.element}</span>
          </div>
          <div class="stat-chip ${card1.threat.includes('HINTERHALT') ? 'highlight-alert' : 'highlight-gold'}">
            <span class="stat-label">Initiative / Status</span>
            <span class="stat-value threat-val">${card1.threat}</span>
          </div>
        </div>

        <div class="rules-box">
          <div class="section-header">
            <span class="rule-title">${card1.specialTitle}</span>
            <span class="rule-type">Raum-Effekt</span>
          </div>
          <p class="rule-body">${card1.specialBody}</p>
        </div>

        <div class="card-footer">
          <span class="footer-deck">🚪 ${card1.footerDeck}</span>
          <span class="footer-id">${card1.footerNum}</span>
          <span class="footer-rarity">${card1.rarity}</span>
        </div>
      </div>

      <div class="tarot-face back-face">
        <img src="${CARD_BACK_IMG}" alt="Die Tiefen Gewölbe" class="card-back-img" />
        <div class="back-title-overlay">
          <svg class="back-title-svg" viewBox="0 0 51 10.4">
            <text x="25.5" y="6.8" text-anchor="middle" font-family="'UnifrakturMaguntia', cursive" font-size="6.8" fill="#111111" textLength="41" lengthAdjust="spacingAndGlyphs">Die Tiefen Gewölbe</text>
          </svg>
        </div>
      </div>
    </div>

    <!-- UNTERE KARTE: ${card2.id} -->
    <div class="card-pair pos-2">
      <div class="tarot-face front-face">
        <div class="card-border-frame"></div>
        <div class="card-border-inner"></div>

        <div class="card-header">
          <h2 class="card-title">${card2.name}</h2>
          <p class="card-subtitle">${card2.subtitle}</p>
        </div>

        <div class="art-container">
          <img src="${card2.art}" alt="${card2.name}" class="card-art" />
          <div class="art-vignette"></div>
        </div>

        <div class="lore-box">
          <p class="lore-text">${card2.lore}</p>
        </div>

        <div class="stat-ribbon">
          <div class="stat-chip highlight-stat">
            <span class="stat-label">Aufstellung</span>
            <span class="stat-value monster-val">${card2.monsters}</span>
          </div>
          <div class="stat-chip highlight-shield">
            <span class="stat-label">Raum-Element</span>
            <span class="stat-value element-val">${card2.element}</span>
          </div>
          <div class="stat-chip ${card2.threat.includes('HINTERHALT') ? 'highlight-alert' : 'highlight-gold'}">
            <span class="stat-label">Initiative / Status</span>
            <span class="stat-value threat-val">${card2.threat}</span>
          </div>
        </div>

        <div class="rules-box">
          <div class="section-header">
            <span class="rule-title">${card2.specialTitle}</span>
            <span class="rule-type">Raum-Effekt</span>
          </div>
          <p class="rule-body">${card2.specialBody}</p>
        </div>

        <div class="card-footer">
          <span class="footer-deck">🚪 ${card2.footerDeck}</span>
          <span class="footer-id">${card2.footerNum}</span>
          <span class="footer-rarity">${card2.rarity}</span>
        </div>
      </div>

      <div class="tarot-face back-face">
        <img src="${CARD_BACK_IMG}" alt="Die Tiefen Gewölbe" class="card-back-img" />
        <div class="back-title-overlay">
          <svg class="back-title-svg" viewBox="0 0 51 10.4">
            <text x="25.5" y="6.8" text-anchor="middle" font-family="'UnifrakturMaguntia', cursive" font-size="6.8" fill="#111111" textLength="41" lengthAdjust="spacingAndGlyphs">Die Tiefen Gewölbe</text>
          </svg>
        </div>
      </div>
    </div>
  </div>
`);
  }

  const navLinks = [];
  for (let s = 1; s <= totalSheets; s++) {
    const c1 = ENCOUNTER_CARDS[(s - 1) * 2].id;
    const c2 = ENCOUNTER_CARDS[(s - 1) * 2 + 1].id;
    navLinks.push(`<a href="#page${s}" class="nav-link">Bogen ${s} (${c1} & ${c2})</a>`);
  }

  return `<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="utf-8">
  <title>Begegnungsdeck: Die Tiefen Gewölbe (B01–B16) - A4 Gutter-Fold</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;900&family=UnifrakturMaguntia&family=Alegreya:ital,wght@0,400;0,600;0,700;1,400;1,600&family=Alegreya+Sans:ital,wght@0,400;0,500;0,700;1,400&display=swap" rel="stylesheet">
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
    .card-header { text-align: center; position: relative; z-index: 2; padding: 0 0.5mm 0.2mm 0.5mm; }
    .card-title {
      font-family: 'Cinzel', serif; font-size: 10.8pt; font-weight: 900; color: #1a140e;
      letter-spacing: 0.2mm; margin: 0.2mm 0 0.1mm 0; text-transform: uppercase; line-height: 1.05;
    }
    .card-subtitle { font-family: 'Alegreya', serif; font-size: 7.2pt; font-style: italic; color: #5c4736; margin: 0; line-height: 1.1; }
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
      display: grid; grid-template-columns: 1.25fr 1.15fr 1fr; gap: 1.1mm;
      margin: 0.1mm 0.4mm 0.5mm 0.4mm; z-index: 2;
    }
    .stat-chip {
      background: linear-gradient(180deg, #fdfaf4 0%, #efe4d0 100%); border: 0.28mm solid #8c6a3a;
      border-radius: 1.0mm; padding: 0.4mm 0.6mm; text-align: center; display: flex; flex-direction: column;
      justify-content: center; box-shadow: 0 0.3mm 0.8mm rgba(0, 0, 0, 0.12); min-height: 10.5mm;
    }
    .stat-chip.highlight-stat { background: linear-gradient(180deg, #fcedec 0%, #f4d3d2 100%); border-color: #8c1d18; }
    .stat-chip.highlight-shield { background: linear-gradient(180deg, #eff7ff 0%, #d3e5f7 100%); border-color: #3b6b99; }
    .stat-chip.highlight-gold { background: linear-gradient(180deg, #fffcf0 0%, #fae8b8 100%); border-color: #b88e38; }
    .stat-chip.highlight-alert { background: linear-gradient(180deg, #ffebee 0%, #ffcdd2 100%); border-color: #b71c1c; }
    .stat-label { font-size: 5.4pt; font-weight: 700; text-transform: uppercase; letter-spacing: 0.15mm; color: #5c4736; line-height: 1; margin-bottom: 0.2mm; }
    .stat-value { font-family: 'Alegreya Sans', sans-serif; font-size: 6.6pt; font-weight: 700; color: #1a140e; line-height: 1.15; }
    .stat-value.monster-val { color: #8c1d18; }
    .stat-value.element-val { color: #1a446e; }
    .stat-value.threat-val { font-family: 'Cinzel', serif; font-size: 6.8pt; font-weight: 900; color: #7a5410; }
    .stat-chip.highlight-alert .stat-value.threat-val { color: #b71c1c; font-weight: 900; }
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
      top: 121.8mm;
      left: 15.2mm;
      width: 51.0mm;
      height: 10.4mm;
      pointer-events: none;
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
    <span>🚪 <strong>Begegnungsdeck: Die Tiefen Gewölbe (B01–B16)</strong> (16 Karten · 8 Bögen)</span>
    <div class="page-nav">
      ${navLinks.join('\n      ')}
    </div>
    <button class="print-btn" onclick="window.print()">🖨️ Alle 8 Bögen drucken / PDF</button>
  </div>

  ${pages.join('\n')}
</body>
</html>`;
}

const outputPath = path.join(PRINTABLES_DIR, 'encounter_cards_all_gutterfold_a4.html');
fs.writeFileSync(outputPath, generateHTML(), 'utf8');
console.log('Successfully generated Encounter Cards printable sheet at: ' + outputPath);
