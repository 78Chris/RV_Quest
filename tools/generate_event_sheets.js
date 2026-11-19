/**
 * Event Cards Generator for RV_Quest
 * Produces A4 gutter-fold print sheets (Tarot 81.67 x 138 mm, folding to standard height).
 */
const fs = require('fs');
const path = require('path');

const ROOT_DIR = path.resolve(__dirname, '..');
const PRINTABLES_DIR = path.join(ROOT_DIR, 'printables');

const CARD_BACK_IMG = './art_assets/MasterArtwork/Cards/Card%20Backs/vintage_medieval_woodcut_etching_of_the_wheel_of_fate_and_des_82b3e498-b408-49ea-a526-fe14d3629fa7_0.png';

const EVENT_CARDS = [
  {
    id: 'E01',
    numStr: '#01 / 18',
    name: 'Herannahende Schritte',
    subtitle: 'Gefahr · Unerwartete Patrouille',
    art: './art_assets/MasterArtwork/Cards/Events/A_dynamic_dungeon_action_scene_seen_from_over_the_shoulder_in_b218cb9b-ddc6-48f3-8210-e7af55a5e1ab_2.png',
    lore: '»Schweres Eisen hallt über feuchten Schiefer. Aus den Schatten hinter der letzten Wegbiegung schält sich der schleppende Schritt einer Wachpatrouille.«',
    typeChip: 'Gefahr',
    targetChip: 'Eingangszone',
    timingChip: 'Sofort',
    rulesTitle: 'Patrouillen-Alarm',
    rulesBody: 'Eine Patrouille nähert sich unbemerkt! Platziere sofort <strong>1 zufälligen Standard-Gegner</strong> (Goblin-Späher oder Skelettkrieger) am Eingang des aktuellen Raumes. Der Gegner schließt sich sofort dem Kampf an.',
    footerDeck: 'Ereignisdeck',
    rarity: 'Ereignis'
  },
  {
    id: 'E02',
    numStr: '#02 / 18',
    name: 'Deckensturz',
    subtitle: 'Falle · Einstürzendes Gewölbe',
    art: './art_assets/MasterArtwork/Cards/Events/A_dynamic_in-the-moment_dungeon_action_scene_brave_warrior_ra_bbf564ba-4a9b-496f-8199-242a4976e5cc_0.png',
    lore: '»Ein dumpfes Knacken im Bogenwerk kündigt das Unheil an. Dann stürzen geborstene Mauerquader in einer dichten Staubwolke auf die Gruppe herab.«',
    typeChip: 'Falle',
    targetChip: 'Alle Helden',
    timingChip: 'Sofort',
    rulesTitle: 'Steinschlag',
    rulesBody: 'Das Gewölbe bebt! Alle <strong>Helden</strong> im Raum würfeln einen Rettungswurf auf <code>GES (SG 6)</code>. Bei Misserfolg: Erleide <strong>1 Schaden</strong> durch herabfallende Trümmer und Geröll.',
    footerDeck: 'Ereignisdeck',
    rarity: 'Ereignis'
  },
  {
    id: 'E03',
    numStr: '#03 / 18',
    name: 'Fackel verlischt',
    subtitle: 'Hindernis · Dunkelheit',
    art: './art_assets/MasterArtwork/Cards/Events/A_dynamic_in-the-moment_dungeon_action_scene_gust_of_eerie_wi_0793dea3-6554-418e-b4cf-6518a83bd471_1.png',
    lore: '»Ein eisiger Windhauch fährt zischend durch das Kreuzgewölbe. Das Pech zischelt kurz auf, Glut stiebt davon – und lastende Schwärze hüllt den Gang ein.«',
    typeChip: 'Hindernis',
    targetChip: 'Fernkampf',
    timingChip: 'Anhaltend',
    rulesTitle: 'Verhüllende Schwärze',
    rulesBody: 'Plötzlicher Luftzug löscht offenes Feuer! Bis ein Held <strong>1 Interaktions-Aktion</strong> zum Wiederanzünden ausgibt, haben <strong>alle Fernkampfangriffe Nachteil</strong> (würfle 2d6, wähle den schlechteren Würfel).',
    footerDeck: 'Ereignisdeck',
    rarity: 'Ereignis'
  },
  {
    id: 'E04',
    numStr: '#04 / 18',
    name: 'Fluchtsperre',
    subtitle: 'Falle · Fallgitter',
    art: './art_assets/MasterArtwork/Cards/Events/A_dynamic_in-the-moment_dungeon_action_scene_of_a_handsome_at_10fd7909-3f5f-43b4-9b7e-16ff126550a0_3.png',
    lore: '»Mit donnerndem Schlag saust das gezahnte Eisengitter nieder! Funken sprühen vom nassen Fels – und schneiden jedes Zögern erbarmungslos ab.«',
    typeChip: 'Falle',
    targetChip: 'Rückweg',
    timingChip: 'Dauerhaft',
    rulesTitle: 'Weg Versperrt',
    rulesBody: 'Ein schweres Fallgitter saust krachend hinter der Gruppe herab! Der Rückweg durch die vorherige Tür ist für den Rest des Szenarios versperrt. Flucht ist unmöglich; nur der Weg nach vorne bleibt.',
    footerDeck: 'Ereignisdeck',
    rarity: 'Ereignis'
  },
  {
    id: 'E05',
    numStr: '#05 / 18',
    name: 'Magische Resonanz',
    subtitle: 'Magie · Arkaner Puls',
    art: './art_assets/MasterArtwork/Cards/Events/A_dynamic_in-the-moment_dungeon_action_scene_imperial_mage_sc_f3a8ff9d-4701-42f9-90bf-19c2bb880080_1.png',
    lore: '»Die Luft vibriert wie eine angeschlagene Saite. Uralte Ley-Linien flammen auf und fluten den Verstand der Zaubernden mit roher arkaner Kraft.«',
    typeChip: 'Magie',
    targetChip: 'Magiegelehrte',
    timingChip: 'Sofort',
    rulesTitle: 'Arkaner Strom',
    rulesBody: 'Ein arkaner Puls flutet den Dungeon! Die Magiegelehrte regeneriert sofort <strong>1 Erschöpfungs-Box</strong>. Ist keine Magiegelehrte im Spiel, heilt der Held mit den wenigsten LP sofort <strong>1 LP</strong>.',
    footerDeck: 'Ereignisdeck',
    rarity: 'Ereignis'
  },
  {
    id: 'E06',
    numStr: '#06 / 18',
    name: 'Heilige Quelle',
    subtitle: 'Segen · Geweihtes Wasser',
    art: './art_assets/MasterArtwork/Cards/Events/A_dynamic_in-the-moment_dungeon_action_scene_wounded_adventur_5fa9016e-0efe-4cee-b7af-b53fb31a0840_1.png',
    lore: '»Aus einer Felsspalte plätschert klares, silbernes Quellwasser. Wo die kühlen Tropfen die Lippen berühren, weicht der pochende Schmerz frischer Wunden.«',
    typeChip: 'Segen',
    targetChip: '1 Held',
    timingChip: 'Sofort',
    rulesTitle: 'Quell des Lebens',
    rulesBody: 'Ein unberührtes Becken mit heiligem Wasser entspringt in einer Wandnische! <strong>Ein beliebiger Held im Raum</strong> darf sofort trinken: Heilt sofort <strong>2 LP</strong> oder entfernt den Zustand <code>Vergiftet</code>.',
    footerDeck: 'Ereignisdeck',
    rarity: 'Ereignis'
  },
  {
    id: 'E07',
    numStr: '#07 / 18',
    name: 'Kriechende Dämpfe',
    subtitle: 'Giftgas · Schwefelbrut',
    art: './art_assets/MasterArtwork/Cards/Events/A_dynamic_dungeon_hazard_scene_dominated_by_massive_billowing_58ae2581-7ac3-46e9-8d8d-c28e7b8f4eab_2.png',
    lore: '»Gelbgrüne Gasschwaden quellen zischend aus Bodenritzen. Ein beißender Schwefelgestank brennt in den Lungen und raubt jedem Krieger den Atem.«',
    typeChip: 'Giftgas',
    targetChip: 'Alle Helden',
    timingChip: 'Sofort',
    rulesTitle: 'Schwefeldunst',
    rulesBody: 'Giftiger Schwefel strömt aus Ritzen im Boden! Alle Helden im Raum müssen einen Rettungswurf auf <code>ZÄH (SG 6)</code> ablegen. Bei Misserfolg: Erleide sofort den Zustand <strong><code>Vergiftet</code></strong> (1 Schaden pro Runde).',
    footerDeck: 'Ereignisdeck',
    rarity: 'Ereignis'
  },
  {
    id: 'E08',
    numStr: '#08 / 18',
    name: 'Goblin-Schadenfreude',
    subtitle: 'Humor · Fuselfund',
    art: './art_assets/MasterArtwork/Cards/Events/A_dynamic_in-the-moment_dungeon_action_scene_cunning_rogue_go_84484357-97af-4d83-877b-78b14c34846d_0.png',
    lore: '»Ein feistes Grinsen huscht über grüne Züge. Hinter vermoderten Fässern klimpert eine verstaubte Tonflasche – der Inhalt brennt wie flüssiges Pech!«',
    typeChip: 'Sozial',
    targetChip: 'Halsabschneider',
    timingChip: 'Sofort',
    rulesTitle: 'Geheimes Lager',
    rulesBody: 'Der Goblin entdeckt eine versteckte Schnapsflasche! Trinkt er: Regeneriert sofort <strong>2 Erschöpfung</strong>, muss aber sofort <strong>1 Karte vom Goblinzauberdeck</strong> ziehen und sofort ausführen! Andere Helden: erhalten 1d6 Gold.',
    footerDeck: 'Ereignisdeck',
    rarity: 'Ereignis'
  },
  {
    id: 'E09',
    numStr: '#09 / 18',
    name: 'Hinterhalt aus den Schatten',
    subtitle: 'Gefahr · Brutangriff',
    art: './art_assets/MasterArtwork/Cards/Events/A_dynamic_in-the-moment_dungeon_action_scene_two_monstrous_fu_6a948a05-fbc9-4531-8854-f6b539842094_2.png',
    lore: '»Lautlose Schatten lösen sich aus den Deckengewölben. Ehe der Schild gehoben ist, schlagen pelzige Klauen und gifttriefende Zangen zu!«',
    typeChip: 'Gefahr',
    targetChip: 'Schwächster Held',
    timingChip: 'Sofort',
    rulesTitle: 'Spinnensturz',
    rulesBody: '<strong>2 Riesenspinnen</strong> seilen sich lautlos von der Decke ab! Sie landen direkt auf benachbarten Feldern des Helden mit den <strong>wenigsten verbliebenen LP</strong> und führen sofort einen freien Überraschungsangriff aus.',
    footerDeck: 'Ereignisdeck',
    rarity: 'Ereignis'
  },
  {
    id: 'E10',
    numStr: '#10 / 18',
    name: 'Versteckte Nische',
    subtitle: 'Fund · Mauernische',
    art: './art_assets/MasterArtwork/Cards/Events/A_dynamic_in-the-moment_dungeon_action_scene_rogue_fingers_pu_612d59b9-4cbd-41de-8902-eec676cabddf_3.png',
    lore: '»Ein Hohlraum hinter feuchtem Mauerwerk gibt nach. Im samtgefütterten Fach ruht die vergessene Habe eines längst gefallenen Abenteurers.«',
    typeChip: 'Fund',
    targetChip: 'Gruppe',
    timingChip: 'Sofort',
    rulesTitle: 'Vergessenes Versteck',
    rulesBody: 'Ein lockerer Wandstein offenbart ein uraltes Geheimversteck! Die Gruppe zieht sofort <strong>1 Karte vom Ausrüstungsdeck</strong> und darf diese sofort an einen beliebigen Helden im Raum aushändigen.',
    footerDeck: 'Ereignisdeck',
    rarity: 'Ereignis'
  },
  {
    id: 'E11',
    numStr: '#11 / 18',
    name: 'Glitschiger Boden',
    subtitle: 'Hindernis · Schimmel & Schleim',
    art: './art_assets/MasterArtwork/Cards/Events/A_dynamic_in-the-moment_dungeon_action_scene_heavily_armored__c63af9d1-cbb2-4df9-a7ae-d2a15eecd566_3.png',
    lore: '»Schmierige Algen und modrige Moose verwandeln die Fliesen in eine Rutschbahn. Wer hier die Beine nicht unter Kontrolle hat, landet unsanft im Schlick.«',
    typeChip: 'Hindernis',
    targetChip: 'Bewegung',
    timingChip: '1 Runde',
    rulesTitle: 'Rutschgefahr',
    rulesBody: 'Schimmel und Moos bedecken die Fliesen! Bis zum Ende der nächsten Spielrunde kostet <strong>jedes Bewegungsfeld 2 Bewegungspunkte (BP)</strong>. Zudem ist in dieser Runde <strong>keine Doppelbewegung</strong> erlaubt.',
    footerDeck: 'Ereignisdeck',
    rarity: 'Ereignis'
  },
  {
    id: 'E12',
    numStr: '#12 / 18',
    name: 'Verhöhnung des Berserkers',
    subtitle: 'Psychologie · Schmachruf',
    art: './art_assets/MasterArtwork/Cards/Events/A_dynamic_in-the-moment_dungeon_action_scene_wild_northland_b_b7a8fe93-f9b6-47e3-ba09-7beb00aa4c24_1.png',
    lore: '»Aus finsteren Schächten dröhnen höhnische Schmährufe wider die Ahnen des Nordens. Das Blut gerät in Wallung – Vernunft weicht blindem Zorn!«',
    typeChip: 'Raserei',
    targetChip: 'Berserker',
    timingChip: 'Nächster Zug',
    rulesTitle: 'Blutrausch',
    rulesBody: 'Der Nordland-Berserker <strong>MUSS</strong> in seinem nächsten Zug auf den nächsten sichtbaren Gegner zustürmen (volle Bewegung nach vorn) und angreifen. Er erhält für diesen Angriff <strong>+1 Schaden</strong>, erleidet aber bis zu seinem nächsten Zug <strong>+1 Schaden durch gegnerische Angriffe</strong>.',
    footerDeck: 'Ereignisdeck',
    rarity: 'Ereignis'
  },
  {
    id: 'E13',
    numStr: '#13 / 18',
    name: 'Göttlicher Schimmer',
    subtitle: 'Segen · Ahnengeist',
    art: './art_assets/MasterArtwork/Cards/Events/A_dynamic_in-the-moment_dungeon_action_scene_noble_elven_blad_28f3d0e1-14f5-435b-bbe2-20027b64977a_0.png',
    lore: '»Ein Hauch warmen Lichts durchbricht das finstere Gewölbe. Der Geist alter Waldläufer beflügelt die Glieder und schärft die Sinne für den Gegenangriff.«',
    typeChip: 'Segen',
    targetChip: 'Alle Helden',
    timingChip: 'Aktueller Raum',
    rulesTitle: 'Segnung des Lichts',
    rulesBody: 'Der Geist der Waldelfen berührt die Gruppe! Beim <strong>nächsten Raum-Initiativewurf</strong> addieren alle Helden <strong>+1 Bonus</strong> auf ihren Wurf. Zudem erhalten alle Helden im aktuellen Raum sofort <strong>+1 Feld Bewegungsweite</strong>.',
    footerDeck: 'Ereignisdeck',
    rarity: 'Ereignis'
  },
  {
    id: 'E14',
    numStr: '#14 / 18',
    name: 'Diebische Ratten',
    subtitle: 'Ärgernis · Schwarmraub',
    art: './art_assets/MasterArtwork/Cards/Events/A_dynamic_in-the-moment_dungeon_action_scene_swarm_of_bold_hu_229eb7b5-65d9-4da9-b6b1-8d7a5c07510c_3.png',
    lore: '»Rote Augen funkeln im Schutt. Mit flinken Pfoten zerbeißen die hungrigen Nager Riemen und Säcke und schleppen Beute in ihre engen Baue.«',
    typeChip: 'Ärgernis',
    targetChip: 'Gruppenkasse',
    timingChip: 'Sofort',
    rulesTitle: 'Rucksackraub',
    rulesBody: 'Eine Horde frecher Dungeon-Ratten huscht durch das Gruppenlager! Die Gruppe verliert sofort nach Wahl: <strong>3 Gold aus der Gemeinschaftskasse</strong> ODER <strong>1 Essensration / Trank</strong> eines Helden an die fliehenden Biester.',
    footerDeck: 'Ereignisdeck',
    rarity: 'Ereignis'
  },
  {
    id: 'E15',
    numStr: '#15 / 18',
    name: 'Arkane Überladung',
    subtitle: 'Gefahr · Magischer Schock',
    art: './art_assets/MasterArtwork/Cards/Events/A_dynamic_in-the-moment_dungeon_action_scene_terrified_party__613b7433-39e2-4036-9c22-6292a7254af1_2.png',
    lore: '»Amulette lodern gleißend blau auf, Fokusstäbe summen bedrohlich. Ein unkontrollierter Funkenregen entlädt sich schmerzhaft in die Träger.«',
    typeChip: 'Magie-Gefahr',
    targetChip: 'Träger mag. Items',
    timingChip: 'Sofort',
    rulesTitle: 'Rückkopplung',
    rulesBody: 'Alle magischen Gegenstände und Zaubersprüche knistern wild! Jede Figur (Held oder Monster), die mindestens 1 Zubehör, Trank oder Zauber besitzt, erleidet sofort <strong>1 unblockbaren Schaden</strong>.',
    footerDeck: 'Ereignisdeck',
    rarity: 'Ereignis'
  },
  {
    id: 'E16',
    numStr: '#16 / 18',
    name: 'Klickendes Bodenblech',
    subtitle: 'Falle · Wandbolzen',
    art: './art_assets/MasterArtwork/Cards/Events/A_dynamic_in-the-moment_dungeon_action_scene_plate_boot_depre_ecffd755-8e99-4f5d-a3b6-7371d3c284fd_1.png',
    lore: '»Ein trockenes *Klick* unter der Stiefelsohle lässt das Herz stocken. Im nächsten Augenblick sirren geschwärzte Eisenbolzen aus getarnten Wandschlitzen!«',
    typeChip: 'Falle',
    targetChip: 'Vorderster Held',
    timingChip: 'Sofort',
    rulesTitle: 'Ausgelöste Falle',
    rulesBody: 'Der vorderste Held hat eine mechanische Druckplatte betreten! Pfeile schießen aus der Wand: Würfle sofort einen Rettungswurf auf <code>GES (SG 6)</code> gegen <strong>2 Schaden</strong> (Rüstung reduziert normal).',
    footerDeck: 'Ereignisdeck',
    rarity: 'Ereignis'
  },
  {
    id: 'E17',
    numStr: '#17 / 18',
    name: 'Unheimliche Stille',
    subtitle: 'Atmosphäre · Anspannung',
    art: './art_assets/MasterArtwork/Cards/Events/A_dynamic_in-the-moment_dungeon_action_scene_party_of_four_gr_96d832b9-5c40-455a-b0bf-c56cf33d8d6e_1.png',
    lore: '»Jedes Tropfen, jedes Knurren erlischt wie auf Geheiß. In der erdrückenden Totenstille schlägt das eigene Herz wie eine Kriegstrommel im Ohr.«',
    typeChip: 'Atmosphäre',
    targetChip: 'Alle Helden',
    timingChip: '1 Runde',
    rulesTitle: 'Totenstille',
    rulesBody: 'Das Knurren der Monster verstummt plötzlich... Nichts passiert in dieser Runde, aber alle Helden spüren die äußerste Anspannung: Jeder Held erhält sofort <strong>Fokus</strong> (+1 Bonus auf seinen nächsten Wurf).',
    footerDeck: 'Ereignisdeck',
    rarity: 'Ereignis'
  },
  {
    id: 'E18',
    numStr: '#18 / 18',
    name: 'Goldener Fund',
    subtitle: 'Schatz · Vergessene Münzen',
    art: './art_assets/MasterArtwork/Cards/Events/A_dynamic_in-the-moment_dungeon_action_scene_grinning_explore_99c31296-7198-48ad-9ab6-1ec8bb343a55_2.png',
    lore: '»Zwischen verstaubten Knochen schimmert gediegenes Metall hervor. Ein zerschlissener Lederbeutel birgt kaiserliche Münzen und funkelnde Edelsteine.«',
    typeChip: 'Schatz',
    targetChip: 'Gruppenkasse',
    timingChip: 'Sofort',
    rulesTitle: 'Münzsegen',
    rulesBody: 'Zwischen den Gebeinen glänzt ein alter Geldbeutel! Die Gruppe erhält sofort <strong>4 Gold</strong> direkt in den gemeinsamen Vorratstopf.',
    footerDeck: 'Ereignisdeck',
    rarity: 'Ereignis'
  }
];

function generateHTML() {
  const pages = [];
  const totalSheets = 9; // 18 cards, 2 per sheet

  for (let i = 0; i < EVENT_CARDS.length; i += 2) {
    const sheetNum = (i / 2) + 1;
    const card1 = EVENT_CARDS[i];
    const card2 = EVENT_CARDS[i + 1];

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
          <div class="stat-chip ${card1.typeChip.includes('Gefahr') || card1.typeChip.includes('Falle') || card1.typeChip.includes('Giftgas') ? 'highlight-stat' : 'highlight-gold'}">
            <span class="stat-label">Typ</span>
            <span class="stat-value type-val">${card1.typeChip}</span>
          </div>
          <div class="stat-chip highlight-shield">
            <span class="stat-label">Ziel</span>
            <span class="stat-value target-val">${card1.targetChip}</span>
          </div>
          <div class="stat-chip highlight-gold">
            <span class="stat-label">Zeitpunkt</span>
            <span class="stat-value timing-val">${card1.timingChip}</span>
          </div>
        </div>

        <div class="rules-box">
          <div class="section-header">
            <span class="rule-title">${card1.rulesTitle}</span>
            <span class="rule-type">Ereignis-Wirkung</span>
          </div>
          <p class="rule-body">${card1.rulesBody}</p>
        </div>

        <div class="card-footer">
          <span class="footer-deck">🎡 ${card1.footerDeck}</span>
          <span class="footer-id">${card1.numStr}</span>
          <span class="footer-rarity">${card1.rarity}</span>
        </div>
      </div>

      <div class="tarot-face back-face">
        <img src="${CARD_BACK_IMG}" alt="Rad des Schicksals" class="card-back-img" />
        <div class="back-title-overlay">
          <svg class="back-title-svg" viewBox="0 0 66.4 29.3">
            <text x="33.2" y="17.2" text-anchor="middle" font-family="'UnifrakturMaguntia', cursive" font-size="8.5" fill="#111111" textLength="56.4" lengthAdjust="spacingAndGlyphs">Rad des Schicksals</text>
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
          <div class="stat-chip ${card2.typeChip.includes('Gefahr') || card2.typeChip.includes('Falle') || card2.typeChip.includes('Giftgas') ? 'highlight-stat' : 'highlight-gold'}">
            <span class="stat-label">Typ</span>
            <span class="stat-value type-val">${card2.typeChip}</span>
          </div>
          <div class="stat-chip highlight-shield">
            <span class="stat-label">Ziel</span>
            <span class="stat-value target-val">${card2.targetChip}</span>
          </div>
          <div class="stat-chip highlight-gold">
            <span class="stat-label">Zeitpunkt</span>
            <span class="stat-value timing-val">${card2.timingChip}</span>
          </div>
        </div>

        <div class="rules-box">
          <div class="section-header">
            <span class="rule-title">${card2.rulesTitle}</span>
            <span class="rule-type">Ereignis-Wirkung</span>
          </div>
          <p class="rule-body">${card2.rulesBody}</p>
        </div>

        <div class="card-footer">
          <span class="footer-deck">🎡 ${card2.footerDeck}</span>
          <span class="footer-id">${card2.numStr}</span>
          <span class="footer-rarity">${card2.rarity}</span>
        </div>
      </div>

      <div class="tarot-face back-face">
        <img src="${CARD_BACK_IMG}" alt="Rad des Schicksals" class="card-back-img" />
        <div class="back-title-overlay">
          <svg class="back-title-svg" viewBox="0 0 66.4 29.3">
            <text x="33.2" y="17.2" text-anchor="middle" font-family="'UnifrakturMaguntia', cursive" font-size="8.5" fill="#111111" textLength="56.4" lengthAdjust="spacingAndGlyphs">Rad des Schicksals</text>
          </svg>
        </div>
      </div>
    </div>
  </div>
`);
  }

  const navLinks = [];
  for (let s = 1; s <= totalSheets; s++) {
    const c1 = EVENT_CARDS[(s - 1) * 2].id;
    const c2 = EVENT_CARDS[(s - 1) * 2 + 1].id;
    navLinks.push(`<a href="#page${s}" class="nav-link">Bogen ${s} (${c1} & ${c2})</a>`);
  }

  return `<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="utf-8">
  <title>Ereignisdeck: Rad des Schicksals (#01–#18) - A4 Gutter-Fold</title>
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
      display: grid; grid-template-columns: 1fr 1.2fr 1fr; gap: 1.1mm;
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
      top: 107.3mm;
      left: 7.3mm;
      width: 66.4mm;
      height: 29.3mm;
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
    <span>🎡 <strong>Ereignisdeck: Rad des Schicksals (#01–#18)</strong> (18 Karten · 9 Bögen)</span>
    <div class="page-nav">
      ${navLinks.join('\n      ')}
    </div>
    <button class="print-btn" onclick="window.print()">🖨️ Alle 9 Bögen drucken / PDF</button>
  </div>

  ${pages.join('\n')}
</body>
</html>`;
}

const outputPath = path.join(PRINTABLES_DIR, 'event_cards_all_gutterfold_a4.html');
fs.writeFileSync(outputPath, generateHTML(), 'utf8');
console.log('Successfully generated Event Cards printable sheet at: ' + outputPath);
