# Progetti realizzati di illuminazione architetturale dinamica (RGB/RGBW) su ponti, facciate, torri e monumenti — tecnologie e soluzioni di controllo

Note di ricerca per Versus Lux (linea RGB wireless). Data di redazione: 8 novembre 2026. Tutti i numeri hanno una fonte; dove la fonte non dà il dato, è indicato "n.d." (non disponibile) e il punto è riportato nei Gap.

## 1. Catalogo dei progetti: chi, dove, quando, quali apparecchi

### Takeaway
I grandi progetti iconici (Bay Lights, Jacques-Cartier, Illuminated River, Empire State, Allianz Arena, Shanghai) sono dominati da Signify/Philips Color Kinetics con controllo cablato o in fibra e piattaforme di gestione remota (Interact Landmark, ActiveSite); il wireless compare soprattutto su beni storici e strutture dove il cavo dati non si può posare (Pont du Gard, Tyne Bridge, Akershus, Götaplatsen, Rhodes Waterside). In Italia i progetti documentati sono quasi tutti promossi da multiutility (Iren, A2A, Acea) con apparecchi RGBW in DMX, spesso su fibra.

### Cited Findings

#### Tabella riassuntiva

| # | Progetto | Luogo | Anno | Apparecchi (marca, quantità) | Colore | Controllo | Wireless? | Costo |
|---|---|---|---|---|---|---|---|---|
| 1 | The Bay Lights (1ª versione) | San Francisco, USA | 2013; reinstallazione permanente 2016 | 25.000 LED su 2,9 km di cavo | bianco (255 livelli) | software Particle Universe, PC remoto | No | 8 M$ (orig.); 4 M$ raccolti per fixture a lungo termine |
| 2 | Bay Lights 360 | San Francisco, USA | lavori da dic. 2024; riaccensione annunciata 20 mar. 2026 | 50.000 LED custom, installatore Musco | n.d. | n.d. | n.d. | 11 M$ |
| 3 | Jacques-Cartier "Living Connections" | Montréal, CA | 2017 | 2.400 Philips CK iColor Accent Powercore; >2.800 apparecchi; 95.000 pixel | RGB | dati social in tempo reale | No (n.d.) | n.d. |
| 4 | Illuminated River (fase 1) | Londra, UK | 2019 (4 ponti) | Philips CK + Interact Landmark; >13.000 apparecchi su 15 ponti; ~10.000 LED per ponte | RGB | Interact Landmark, monitoraggio remoto | No | 45 M£ (budget complessivo) |
| 5 | Tower Bridge | Londra, UK | 2012 | GE: 1.800 apparecchi LED + 2.000 m di lineari, 1.000 scatole di giunzione, 5.000 m di cavo | colore variabile | n.d. | No | n.d. ("nessun costo per i contribuenti") |
| 6 | Zakim Bunker Hill Bridge | Boston, USA | dic. 2012 | Philips CK ColorReach Powercore (oggi ReachElite), quantità n.d. | RGB | riuso cablaggio esistente (IntelliPower) | No | n.d. |
| 7 | Empire State Building (corona/antenna) | New York, USA | 2012 | Philips CK, "quasi 400" apparecchi | 16 M colori | sistema CK computerizzato | No | n.d. |
| 8 | Burj Khalifa (media facade) | Dubai, UAE | sistema rinnovato ~2017 | >1,2 milioni di LED, 33 km di strip | RGB pixel | server centrale + fibra ottica + controller locali | No | n.d. |
| 9 | Burj Khalifa (nuova facciata RGBW) | Dubai, UAE | dic. 2024 | apparecchi RGBW indirizzabili, quantità n.d. | RGBW | n.d. | n.d. | n.d. |
| 10 | Allianz Arena | Monaco, DE | 2015 | Philips, >300.000 LED su ~26.000 m² | 16 M colori | refresh 40 img/s, cloud ActiveSite | No | n.d. |
| 11 | Helix Bridge | Singapore | 2010 | Spacecannon (Zumtobel), ~1.400 apparecchi custom, ~10.000 LED | RGB + bianco | DMX512 + RDM | No | n.d. |
| 12 | Banpo Bridge Moonlight Rainbow Fountain | Seoul, KR | 2008 | 190 Martin Exterior 600 | RGB | 100 sequenze su musica | No | n.d. |
| 13 | Ponti e skyline del Huangpu | Shanghai, CN | 2018 | Signify: >50.000 apparecchi tot., ~7.800 sui ponti Yangpu, Nanpu, Xupu | RGB | Interact Landmark | No | n.d. |
| 14 | Ponte Xianghe | Quanjiao, CN | 2021 | lineari Seekway sugli stralli, quantità n.d. | n.d. | cloud TCP/IP-UDP + sincronizzazione GPS | in parte (sync GPS) | n.d. |
| 15 | Pont du Gard | FR | 2017 | LED RDM a 40 m sul fiume | n.d. | LumenRadio Wireless DMX: 2 TX, 2 repeater, 23 RX | **Sì** | n.d. |
| 16 | Tyne Bridge | Newcastle, UK | n.d. | Philips ColorReach Powercore con modulo CRMX integrato | RGB | DMX/RDM wireless CRMX | **Sì** | n.d. |
| 17 | Akershus Fortress | Oslo, NO | ~2025 | 236 apparecchi, 66 nodi W-DALI in 5 sottoreti | bianco caldo + accento blu | Pharos + LumenRadio W-DALI | **Sì** (0 m di cavo di controllo) | n.d. |
| 18 | Götaplatsen | Göteborg, SE | n.d. | LED, ricevitori CRMX Nova IP65 | n.d. | DMX/RDM wireless | **Sì** | n.d. |
| 19 | Torre di Gesù, Sagrada Família (evento di inaugurazione) | Barcellona, ES | 2026 | 76 Astera HydraPanel, 24 QuikSpot, Astera AX3, 2 Robe iForte LTX | RGB | Astera via CRMX | **Sì** (temporaneo) | n.d. |
| 20 | Rhodes Waterside Bridge | Sydney, AU | n.d. | n.d. | colore per eventi | Casambi (mesh BLE) | **Sì** | n.d. |
| 21 | Heumarkt 7 (facciata) | Vienna, AT | ~2020 | Schrutek; 22 driver DALI + 10 driver 1-10V | n.d. | 4 Casambi ASD + booster | **Sì** | n.d. |
| 22 | Torre Eiffel | Parigi, FR | in esercizio | 336 proiettori al sodio, 20.000 lampadine scintillanti da 6 W, faro allo xeno | oro fisso; colori con proiettori esterni per eventi | sensori, software del faro | No | n.d. |
| 23 | Mole Antonelliana (IT) | Torino | 2019 | 43 Claypaky ODEON Flood (24 Maxi 15°, 3 Maxi 25°, 16 Medium 25°) | RGBW | fibra ottica + convertitore DMX512 a ogni punto | No | n.d. |
| 24 | Ponti storici sul Po (IT) | Torino | dic. 2018 – lug. 2019 | ~200 apparecchi LED su 4 ponti | colore variabile | gestione remota | n.d. | n.d. |
| 25 | Belvedere di Palazzo Lombardia (IT) | Milano | 2019 | 143 apparecchi LED RGB (A2A con Signify e Algorab) | RGB | DMX | n.d. | n.d. |
| 26 | Ponte di Tor Vergata (IT) | Roma | 2025 | 46 Prolights: 32 ArcPod 15QC5M + 14 ArcPod 27Q | RGBW | n.d. | n.d. | n.d. |
| 27 | Domus Tiberiana (IT, termine di confronto) | Roma | 2023 | 101 apparecchi (Areti/Acea), 4,4 kW | tunable white, non RGB | n.d. | n.d. | n.d. |
| 28 | Ponte Vecchio (IT, termine di confronto) | Firenze | 2014 | 102 unità LED interne + 16 strutture esterne | n.d. (non indicato RGB) | n.d. | n.d. | >400.000 € (dono Stefano Ricci) |
| 29 | Torre Arcobaleno (IT) | Milano | 2024 | proiettori LED Disano da 397 W ciascuno, quantità n.d. | n.d. | n.d. | n.d. | n.d. |

#### Schede per progetto

**1–2. The Bay Lights / Bay Lights 360 — San Francisco Bay Bridge (campata ovest)**
- Ideato da Ben Davis (Words Pictures Ideas) nel 2010, realizzato da Illuminate the Arts; artista Leo Villareal. 25.000 LED bianchi su 2,9 km, uno ogni 30 cm, fissati con 60.000 fascette, 30.000 m di cavo speciale, 255 livelli di luminosità per LED; costo iniziale 8 M$ da donazioni private; energia circa 30 $/giorno (~11.000 $/anno) — [Wikipedia](https://en.wikipedia.org/wiki/The_Bay_Lights)
- Smontato a marzo 2015 alla scadenza dei permessi; reinstallazione permanente da ottobre 2015, riaccensione 30 gennaio 2016; raccolti 4 M$ "per installare fixture a lungo termine"; la Bay Area Toll Authority ha stanziato dal 2014 fino a 250.000 $/anno per manutenzione ed elettricità — [Wikipedia](https://en.wikipedia.org/wiki/The_Bay_Lights)
- Fornitura LED Philips per la versione permanente — [BusinessWire, 2016](https://businesswire.com/news/home/20160128005628/en/Artist-Leo-Villareal-Shines-a-Permanent-Light-on-San-Francisco-with-LED-Lighting-from-Philips)
- Guasti: nel 2023 c'erano zone buie e i LED si guastavano più rapidamente di quanto si riuscisse a ripararli; spento il 5 marzo 2023 per "le condizioni difficili sul ponte e sulla baia" — [Wikipedia](https://en.wikipedia.org/wiki/The_Bay_Lights). KQED cita dieci anni di nebbia, vento, sale e gas di scarico — [KQED](https://www.kqed.org/news/12017479/new-bay-bridge-light-installation-underway-after-nearly-2-year-shutdown)
- Bay Lights 360: 50.000 LED custom "progettati per resistere al clima difficile", montati su entrambi i lati dei cavi; 11 M$ raccolti privatamente; posa dall'inizio di dicembre 2024 — [KQED](https://www.kqed.org/news/12017479/new-bay-bridge-light-installation-underway-after-nearly-2-year-shutdown). Installatore Musco Sports Lighting; guasti tecnici a dicembre 2024 hanno causato ritardi — [Wikipedia](https://en.wikipedia.org/wiki/The_Bay_Lights). Controllo originale: software Particle Universe da PC remoto — [KQED](https://www.kqed.org/news/12017479/new-bay-bridge-light-installation-underway-after-nearly-2-year-shutdown)
- Un portale eventi annuncia la riaccensione per il 20 marzo 2026 — [Funcheap SF](https://sf.funcheap.com/city-guide/years-dark-bay-bridges-bay-lights-return-march-20-2026/) (fonte debole: non verificato su fonte primaria)

**3. Pont Jacques-Cartier "Living Connections" — Montréal**
- Committente: Jacques Cartier and Champlain Bridges Inc. (JCCBI); direzione creativa Moment Factory con sei studi locali (Ambiances Design Productions, ATOMIC3, Éclairage Public/Ombrages, Lucion Média, UDO Design); ingegneria WSP–AECOM; impianti elettrici Systèmes Urbains; general contractor Pomerleau; distributore Lumen (Sonepar) — [Philips case study](https://images.philips.com/is/content/PhilipsConsumer/PDFDownloads/ODLI20170517_001-UPD-en_US-PLt-17063CS_Jacques-Cartier_bridge_case_study.pdf)
- 2.400 Philips Color Kinetics iColor Accent Powercore, >2.800 apparecchi sulla travatura reticolare, 95.000 pixel indirizzabili; posa dall'autunno 2016 alla primavera 2017, inaugurazione 17 maggio 2017; 5 spettacoli orari a notte, 365 giorni l'anno; colori, intensità e movimento guidati dalla frequenza della parola "Montréal" sui social — [Philips case study](https://images.philips.com/is/content/PhilipsConsumer/PDFDownloads/ODLI20170517_001-UPD-en_US-PLt-17063CS_Jacques-Cartier_bridge_case_study.pdf)

**4. Illuminated River — Londra (Tamigi)**
- Artista Leo Villareal con Lifschutz Davidson Sandilands; cliente Illuminated River Foundation; fino a 15 ponti, >13.000 apparecchi; Philips Color Kinetics + Interact Landmark con monitoraggio remoto, rilevamento guasti, diagnosi e manutenzione a distanza; contratto di servizio Signify di 10 anni — [LEDinside](https://www.ledinside.com/news/2025/10/london_illuminated_river_project_powered_signify)
- Budget 45 M£, finanziamento privato (Hannah Rothschild, Leonard Blavatnik); fase 1 (Cannon Street, Millennium, Southwark, London Bridge) accesa a luglio 2019; ~10.000 LED per ponte, 16 milioni di colori per apparecchio; spegnimento alle 2 di notte; fasci schermati per limitare la luce sull'acqua (fauna) — [The Art Newspaper](https://www.theartnewspaper.com/2019/07/18/its-lit-leo-villareal-illuminates-four-london-bridges-for-worlds-longest-work-of-art)

**5. Tower Bridge — Londra (2012)**
- GE: 1.800 apparecchi LED, 2.000 m di LED lineari, 5.000 m di cavo, 1.000 scatole di giunzione; intensità e colore variabili; fino al -40% di energia rispetto all'impianto precedente; finanziato da Sindaco di Londra, City of London Corporation, EDF Energy e GE — [LEDs Magazine](https://www.ledsmagazine.com/specialty-ssl/automotive-vehicles/article/16698634/tower-bridge-in-london-receives-olympic-led-makeover)

**6. Leonard P. Zakim Bunker Hill Bridge — Boston**
- Sostituzione degli ioduri metallici con proiettori Color Kinetics ColorReach Powercore (oggi ReachElite); soluzione IntelliPower che ha riusato cablaggi e punti di fissaggio esistenti, riducendo "drasticamente" i costi; consumo energetico ridotto di oltre l'80%; inaugurato a dicembre 2012 — [Color Kinetics](https://www.colorkinetics.com/global/showcase/leonard-zakim-bridge)

**7. Empire State Building — New York**
- Sistema dinamico Philips Color Kinetics, "quasi 400" apparecchi al posto delle luci della torre; >16 milioni di colori invece di una tavolozza di 10; effetti ripple, cross-fade, particle e burst automatizzati; controllo del light spill; completamento previsto a settembre 2012 — [Signify press release](https://www.signify.com/en-gb/our-company/news/press-release-archive/2012/20120509-empire-state-building)

**8–9. Burj Khalifa — Dubai**
- Media facade: >1,2 milioni di LED indirizzabili singolarmente, ~33 km di strip, potenza massima 790 kW (l'articolo riporta anche "790 kWh", dato incoerente); spettacoli tipicamente al 40% di luminosità; contenuti lanciati da un laptop collegato a un server centrale, poi via fibra ottica a controller principali e locali; ridondanza: strip ogni 50 cm, metà spegnibile in alternanza mantenendo lo spettacolo a risoluzione ridotta; >1.825 spettacoli dall'installazione del nuovo sistema; ogni show provato prima su un banco identico in una sala privata; gestito da Emaar — [Gulf News, 2018](https://gulfnews.com/uae/how-burj-khalifa-puts-on-its-stellar-light-shows-1.61074857)
- Nuova facciata RGBW indirizzabile, debutto 1 dicembre 2024 dopo sei mesi di prove su mock-up; marca e quantità non dichiarate — [PAD Magazine](https://padmagazine.co.uk/news/burj-khalifas-facade-shines-with-upgraded-lighting-system/26446)

**10. Allianz Arena — Monaco di Baviera**
- >300.000 LED su ~26.000 m², 16 milioni di colori, refresh fino a 40 immagini/s, programmazione eventi tramite piattaforma cloud Philips ActiveSite, effetti a onda/nuvola progettati da Herzog & de Meuron; -60% di elettricità rispetto alle fluorescenti, 362 t CO2/anno risparmiate; in funzione dal 14 agosto 2015 — [New Atlas](https://newatlas.com/bayern-munich-allianz-arena-philips-led-facade/38936)

**11. Helix Bridge — Singapore**
- ~1.400 apparecchi custom Spacecannon (derivati dai modelli Nike e Maya), quasi 10.000 LED, prevalentemente RGB più bianchi per il percorso pedonale; DMX512 + RDM; progettazione con Technolite e Arup; inaugurato il 24 aprile 2010 — [LED professional](https://www.led-professional.com/project_news/general-lighting/spacecannons-led-custom-fixtures-make-helix-bridge-gleam-in-beautiful-light)

**12. Banpo Bridge Moonlight Rainbow Fountain — Seoul**
- 190 Martin Exterior 600 cambia-colore; 100 sequenze coreografate su musica; fontana OASE, light design Jack Chung (OASE Asia Pacific) con Martin Singapore; cliente Seoul Metropolitan Infrastructure — [LSi Online, 2008](https://lsionline.com/news/martin-illuminates-banpo-bridge-fountain-kbcowu)

**13. Huangpu, Shanghai (ponti Yangpu, Nanpu, Xupu e skyline)**
- >40 edifici e 3 ponti; >50.000 apparecchi totali, di cui ~7.800 LED connessi sui ponti e >27.000 sulle sommità dei grattacieli di Pudong; Interact Landmark per controllo individuale/gruppi, scene feriali/festive, modalità notturna a basso consumo, gestione guasti; risparmio atteso 50–70% dei costi annui — [Signify, 2018](https://www.signify.com/b-dam/signify/en-aa/about/news/2018/20181121-signify-shines-dynamic-light-on-shanghais-buildings-bridges-and-rives/Release_Shanghai_shines_dynamic_light_a211118.pdf)

**14. Ponte Xianghe — Quanjiao (Cina)**
- Lineari LED sugli stralli verniciati come il ponte; sistema cloud Seekway su TCP/IP e UDP con "sincronizzazione globale GPS" dei nodi, controllo da smartphone/tablet/PC, 4 calendari automatici (giornaliero, notturno, weekend, festivo); completato nel 2021 — [Seekway](https://www.seekway.com/info-detail/sustainable-landmark-bridge-illumination-via-cloud-based-control-systems) (contenuto di marketing del produttore, nessun dato indipendente)

**15. Pont du Gard — Francia (UNESCO)**
- LumenRadio Wireless DMX Outdoor: 2 trasmettitori, 2 repeater, 23 ricevitori, sistema di antenne direzionali su misura; apparecchi LED con RDM a 40 m sopra il fiume; monitoraggio in tempo reale con software SuperNova da una sala controllo; integrazione con i son et lumière; lighting designer Claudette Viguier (Adreamlux), installazione Texen con AVAB Transtechnik; 2017 — [LumenRadio](https://lumenradio.com/?p=2117)

**16. Tyne Bridge — Newcastle/Gateshead**
- Torri in granito illuminate a colori con alimentatori Philips ColorReach Powercore con moduli OEM LumenRadio CRMX integrati, "eliminando la necessità di qualsiasi cablaggio di controllo" perché il ponte del 1928 non ha canalizzazioni; integrazione LITE Ltd — [Live Design](https://www.livedesignonline.com/lite-ltd-philips-lumenradio-color-historic-tyne-bridge)

**17. Akershus Fortress — Oslo**
- 236 apparecchi (prima sodio con solo on/off), 66 ricevitori W-DALI in 5 sottoreti mesh, controllo Pharos; distanza massima tra nodi ~100 m; area >1 km × ~400 m; 0 m di nuovo cavo di controllo; nodi pre-programmati e indirizzati fuori sito; test RF in loco per evitare interferenze con le comunicazioni militari; committente Forsvarsbygg; consulenza Zenisk; design e programmazione Lyskontroll (Geir Sire); installatore Installatøren Gruppen; fornitore SML Lighting — [LumenRadio](https://lumenradio.com/stories/akershus-fortress-how-w-dali-brought-new-life-to-an-iconic-landmark/)

**18. Götaplatsen — Göteborg**
- Ricevitori CRMX Nova IP65 sparsi nella piazza: DMX/RDM a tutto l'impianto senza "lavori edili invasivi o costosi" e infrastruttura nascosta; con Hofmann Teknik e Ramboll — [Live Design](https://www.livedesignonline.com/lumenradio-lights-gothenburg-s-gotaplatsen)

**19. Torre di Gesù, Sagrada Família — Barcellona (evento, 2026)**
- 76 Astera HydraPanel e 24 QuikSpot all'interno, Astera AX3 come "lanterne", 2 Robe iForte LTX sulla croce da ~195 m di distanza; sistema Astera controllato via LumenRadio CRMX; light design Juanjo Saunier, programmazione Gustavo Omedes, direzione Igor Cortadellas — [ISP Audio](https://www.isp-audio.com/en/installation-case-studies/lighting-installation/13473-light-connects-architecture-music-and-emotion-in-the-sagrada-familia-s-tower-of-jesus). Nota: è un allestimento per evento, non un impianto permanente di facciata.

**20. Rhodes Waterside Bridge — Sydney**
- Casambi (mesh Bluetooth Low Energy) scelto perché limiti di peso severi imponevano cablaggio di controllo "al minimo assoluto"; comunicazione affidabile sopra un corridoio ferroviario trafficato; colore variabile per eventi; sviluppatore Mirvac; commissioning Afterglow Controls — [Casambi](https://casambi.com/projects/rhodes-waterside-bridge/)

**21. Heumarkt 7 — Vienna**
- Facciata di un edificio del 1826; apparecchi Schrutek con 22 driver DALI e 10 driver 1-10V; 4 unità Casambi ASD con booster; taratura dei livelli da ~25 m, dall'altro lato della strada, con l'app — [Casambi](https://casambi.com/projects/facade-lighting-heumarkt-7-vienna/)

**22. Torre Eiffel — Parigi**
- Illuminazione dorata fissa con 336 proiettori al sodio alta pressione; 20.000 lampadine scintillanti da 6 W (≈8.800 kWh/anno, 0,4% dei consumi del monumento); faro con 4 proiettori motorizzati allo xeno da 6000 W; le colorazioni per eventi usano proiettori esterni installati ad hoc — [Tour Eiffel](https://www.toureiffel.paris/en/the-monument/lights)

**23. Mole Antonelliana — Torino (2019)**
- 43 Claypaky ODEON RGBW (24 Flood Maxi 15°, 3 Flood Maxi 25°, 16 Flood Medium 25°) con LED OSRAM multi-chip, IP65/IK09, -25/+50 °C, rimontati nei punti di installazione esistenti sui tetti vicini (prova a 90 m di distanza, 180 m in diagonale); rete in fibra ottica fino a ogni apparecchio con convertitore DMX512 a ogni punto, controllo da remoto; -50% di elettricità rispetto alle scariche da 1200 W; progettazione, installazione e gestione Iren — [Claypaky](https://www.claypaky.it/en/news/a_new_claypaky_led_lighting_system_for_the_mole_antonelliana)

**24. Ponti storici sul Po — Torino (2018–2019)**
- Umberto I (azzurro), Isabella (verde acqua), Balbis (bianco), più Vittorio Emanuele I (dicembre); circa 200 apparecchi LED; colore e intensità variabili da remoto; sponde in bianco su richiesta della Soprintendenza; posa da team di alpinisti; inaugurazione 4 luglio 2019 alla presenza dei vertici Iren — [Mentelocale](https://www.mentelocale.it/torino/articoli/80069-nuove-luci-torino-ponti-umberto-isabella-balbis.htm)

**25. Belvedere di Palazzo Lombardia — Milano (2019)**
- 143 apparecchi LED RGB al 39° piano, controllo DMX; realizzato da A2A Illuminazione Pubblica con Signify e Algorab; inaugurato il 26 novembre 2019 — [A2A](https://www.gruppoa2a.it/sites/default/files/2022-07/A2A_Nuova%20illuminazione%20Belvedere.pdf)

**26. Ponte di Tor Vergata — Roma (2025, Giubileo)**
- Campata di 83 m; 46 wash RGBW Prolights IP66: 32 ArcPod 15QC5M (15 LED da 10 W, ~5.900 lm, 10°) e 14 ArcPod 27Q (27 LED da 10 W, 23.751 lm, 10°, 3 sezioni) — [Music & Lights](https://musiclights.it/news/653/PROLIGHTS-cura-l-illuminazione-del-Ponte-di-Tor-Vergata)

**27. Domus Tiberiana — Roma (2023, confronto)**
- 101 apparecchi (28 incassi, 12 lineari per gli archi, 51 proiettori per la facciata, 10 lineari interni), luce dinamica tunable white (non RGB), 4,4 kW totali; progetto Areti (Acea) — [Acea](https://www.acea.it/content/dam/acea-corporate/pdf/it/comunicati-stampa/2023/09/ACEACS-20092023.pdf)

**28. Ponte Vecchio — Firenze (2014, confronto)**
- 102 unità LED interne e 16 strutture esterne; -79,33% di energia; costo >400.000 €, dono della maison Stefano Ricci — [ANSA](https://ansa.it/english/news/lifestyle/arts/2014/06/16/florences-ponte-vecchio-gets-new-lights_205b2e8b-f5d3-4ea8-bf1a-ee60e6f97f86.html) (ANSA riporta anche un risparmio per il Comune di 12–15 M€/anno, cifra palesemente incoerente con il costo: da non usare)

**29. Torre Arcobaleno — Milano (2024)**
- Nuovi proiettori LED da 397 W ciascuno (vita ~100.000 h); partner illuminazione Disano; progetto 6R5 Network; sostegno di Comune di Milano e RFI — [D5 Mag](https://d5mag.com/?p=45881)

### Inferences
- Il mercato "di punta" (grandi ponti e grattacieli) compra sistemi completi produttore+controllo+servizio (Signify Interact Landmark con contratti di 10 anni a Londra), non apparecchi sciolti: per una PMI come Versus Lux il posizionamento realistico è sui progetti medi (ponti urbani, monumenti, facciate storiche) dove le multiutility italiane (Iren, A2A, Acea/Areti) fanno da committente-progettista-installatore.
- La configurazione italiana tipica è un numero contenuto di proiettori RGBW potenti (43 alla Mole, 46 a Tor Vergata, ~200 su 4 ponti a Torino) piuttosto che migliaia di pixel: pochi nodi da gestire, adatti a una mesh radio.

### Gaps
- Non ho trovato dati tecnici verificabili per: Ponte della Musica (Roma), Arena di Verona (solo allestimenti temporanei per eventi), Ponte della Costituzione/Calatrava (Venezia), Colosseo (illuminazione RGB permanente), Dubai Frame, ponti di Chongqing e Wuhan, progetti comunali di Bologna e Napoli (a Napoli solo notizie di colorazioni "azzurre" per eventi calcistici, senza dati tecnici), Øresund, Sagrada Família come impianto permanente LumenRadio.
- Ponte San Giorgio (Genova): risultano forniture iGuzzini e Palazzoli, ma la pagina iGuzzini consultata non conteneva dati; non verificato se l'impianto è RGB.
- Per quasi tutti i progetti mancano marca/modello esatti, numero di universi DMX e costi.

## 2. Architetture di controllo e ruolo del wireless

### Takeaway
A grande scala domina il cablato: DMX/RDM (Helix), fibra ottica con convertitori DMX per punto (Mole, Burj Khalifa) e piattaforme IP con gestione remota (Interact Landmark, ActiveSite). Il wireless viene scelto quasi sempre per un motivo preciso — vincoli di tutela, assenza di canalizzazioni, limiti di peso, costo dei lavori — e in quei casi i prodotti usati sono LumenRadio (Wireless DMX/CRMX, W-DALI) e Casambi.

### Cited Findings
- Pont du Gard: LumenRadio scelto in fase di progetto come unica opzione wireless con funzionalità e affidabilità richieste; topologia 2 TX + 2 repeater + 23 RX con antenne direzionali; RDM e monitoraggio con SuperNova — [LumenRadio](https://lumenradio.com/?p=2117)
- Tyne Bridge: CRMX integrato nell'alimentatore del proiettore (modulo OEM) per eliminare il cavo di controllo su un ponte senza canalizzazioni — [Live Design](https://www.livedesignonline.com/lite-ltd-philips-lumenradio-color-historic-tyne-bridge)
- Akershus: W-DALI "unica opzione praticabile" perché forare, scavare o fissare cavi avrebbe danneggiato la muratura; 66 nodi, 5 sottoreti, salti fino a ~100 m, 0 m di cavo di controllo, survey RF in sito — [LumenRadio](https://lumenradio.com/stories/akershus-fortress-how-w-dali-brought-new-life-to-an-iconic-landmark/)
- Götaplatsen: CRMX per evitare lavori edili e mantenere nascosta l'infrastruttura — [Live Design](https://www.livedesignonline.com/lumenradio-lights-gothenburg-s-gotaplatsen)
- Rhodes Waterside Bridge: Casambi per limiti di peso e riduzione del cablaggio sopra la ferrovia — [Casambi](https://casambi.com/projects/rhodes-waterside-bridge/); Heumarkt 7: 4 Casambi ASD con booster, taratura da app a ~25 m — [Casambi](https://casambi.com/projects/facade-lighting-heumarkt-7-vienna/)
- Sincronizzazione senza bus dati comune: sistema cloud con sincronizzazione GPS dei nodi su un ponte strallato cinese — [Seekway](https://www.seekway.com/info-detail/sustainable-landmark-bridge-illumination-via-cloud-based-control-systems)
- Cablato su larga scala: Burj Khalifa con server centrale e fibra verso controller locali — [Gulf News](https://gulfnews.com/uae/how-burj-khalifa-puts-on-its-stellar-light-shows-1.61074857); Mole con fibra e convertitore DMX512 a ogni punto — [Claypaky](https://www.claypaky.it/en/news/a_new_claypaky_led_lighting_system_for_the_mole_antonelliana); Helix con DMX512+RDM — [LED professional](https://www.led-professional.com/project_news/general-lighting/spacecannons-led-custom-fixtures-make-helix-bridge-gleam-in-beautiful-light)
- Riuso del cablaggio esistente come alternativa al wireless: Zakim Bridge con IntelliPower — [Color Kinetics](https://www.colorkinetics.com/global/showcase/leonard-zakim-bridge); Mole con rimontaggio nei punti esistenti — [Claypaky](https://www.claypaky.it/en/news/a_new_claypaky_led_lighting_system_for_the_mole_antonelliana)
- Gestione remota e diagnostica come requisito: Interact Landmark a Londra e Shanghai con rilevamento guasti — [LEDinside](https://www.ledinside.com/news/2025/10/london_illuminated_river_project_powered_signify), [Signify](https://www.signify.com/b-dam/signify/en-aa/about/news/2018/20181121-signify-shines-dynamic-light-on-shanghais-buildings-bridges-and-rives/Release_Shanghai_shines_dynamic_light_a211118.pdf)
- Integrazione DMX su apparecchi Philips: Allianz Arena programmabile tramite cloud ActiveSite — [New Atlas](https://newatlas.com/bayern-munich-allianz-arena-philips-led-facade/38936)

### Inferences
- Il modello vincente per Versus Lux è quello del Tyne Bridge: modulo radio integrato nell'apparecchio/alimentatore, solo cavo di potenza. I casi documentati mostrano che i committenti accettano il wireless quando arriva con RDM/monitoraggio (SuperNova, Pharos) e con survey RF: questi servizi vanno offerti insieme al prodotto.
- I salti radio citati (~100 m ad Akershus, antenne direzionali al Pont du Gard) indicano che su ponti lunghi servono repeater o antenne dedicate: la mesh deve prevedere nodi ripetitori e la possibilità di antenna esterna.
- La sincronizzazione GPS/cloud (caso cinese) è un'alternativa al bus DMX per show coordinati su più strutture; la combinazione mesh + riferimento temporale comune è un punto da approfondire per la linea.
- La presenza del gateway DMX/Art-Net opzionale è coerente con il mercato: quasi tutti i grandi impianti restano su DMX/RDM o IP e i committenti si aspettano integrazione con controller esistenti (Pharos ad Akershus).

### Gaps
- Nessuna fonte trovata con numero di universi DMX/Art-Net/sACN per i progetti del catalogo; nessun caso documentato di KiNET, Madrix o e:cue su ponti (non cercato a fondo per limiti di tempo).
- Nessun caso verificato di controllo via LoRa, 4G/GPRS o Wi-Fi su facciate RGB permanenti; nessun dato su AirGlow.
- Non verificato il sistema di controllo dei ponti di Torino e del Ponte di Tor Vergata.

## 3. Budget, energia, manutenzione e guasti

### Takeaway
I budget pubblicati sono rari e quasi solo per progetti artistici a finanziamento privato (Bay Lights 8 M$ + 4 M$ + 11 M$, Illuminated River 45 M£, Ponte Vecchio >400.000 €); il risparmio energetico dichiarato rispetto alle sorgenti tradizionali va dal 40% all'80%. Il caso di guasto meglio documentato è il Bay Lights, spento nel 2023 per l'ambiente marino.

### Cited Findings
- Costi: Bay Lights 8 M$ iniziali e 4 M$ per fixture permanenti, BATA fino a 250.000 $/anno per manutenzione ed energia — [Wikipedia](https://en.wikipedia.org/wiki/The_Bay_Lights); Bay Lights 360 11 M$ — [KQED](https://www.kqed.org/news/12017479/new-bay-bridge-light-installation-underway-after-nearly-2-year-shutdown); Illuminated River 45 M£ — [The Art Newspaper](https://www.theartnewspaper.com/2019/07/18/its-lit-leo-villareal-illuminates-four-london-bridges-for-worlds-longest-work-of-art); Ponte Vecchio >400.000 € — [ANSA](https://ansa.it/english/news/lifestyle/arts/2014/06/16/florences-ponte-vecchio-gets-new-lights_205b2e8b-f5d3-4ea8-bf1a-ee60e6f97f86.html)
- Energia: Bay Lights ~11.000 $/anno — [Wikipedia](https://en.wikipedia.org/wiki/The_Bay_Lights); Tower Bridge fino a -40% — [LEDs Magazine](https://www.ledsmagazine.com/specialty-ssl/automotive-vehicles/article/16698634/tower-bridge-in-london-receives-olympic-led-makeover); Mole -50% — [Claypaky](https://www.claypaky.it/en/news/a_new_claypaky_led_lighting_system_for_the_mole_antonelliana); Allianz Arena -60% — [New Atlas](https://newatlas.com/bayern-munich-allianz-arena-philips-led-facade/38936); Zakim >-80% — [Color Kinetics](https://www.colorkinetics.com/global/showcase/leonard-zakim-bridge); Ponte Vecchio -79,33% — [ANSA](https://ansa.it/english/news/lifestyle/arts/2014/06/16/florences-ponte-vecchio-gets-new-lights_205b2e8b-f5d3-4ea8-bf1a-ee60e6f97f86.html); Shanghai 50–70% dei costi annui (atteso) — [Signify](https://www.signify.com/b-dam/signify/en-aa/about/news/2018/20181121-signify-shines-dynamic-light-on-shanghais-buildings-bridges-and-rives/Release_Shanghai_shines_dynamic_light_a211118.pdf); Domus Tiberiana 4,4 kW per 101 apparecchi — [Acea](https://www.acea.it/content/dam/acea-corporate/pdf/it/comunicati-stampa/2023/09/ACEACS-20092023.pdf); Burj Khalifa max 790 kW, shows al 40% — [Gulf News](https://gulfnews.com/uae/how-burj-khalifa-puts-on-its-stellar-light-shows-1.61074857)
- Guasti: Bay Lights con LED che si guastavano più velocemente delle riparazioni, spento il 5 marzo 2023 — [Wikipedia](https://en.wikipedia.org/wiki/The_Bay_Lights); causa: nebbia, vento, sale, gas di scarico — [KQED](https://www.kqed.org/news/12017479/new-bay-bridge-light-installation-underway-after-nearly-2-year-shutdown); il rifacimento 2024 ha subito guasti tecnici a dicembre 2024 con ritardi — [Wikipedia](https://en.wikipedia.org/wiki/The_Bay_Lights)
- Strategie di affidabilità: ridondanza a strip alternate al Burj Khalifa — [Gulf News](https://gulfnews.com/uae/how-burj-khalifa-puts-on-its-stellar-light-shows-1.61074857); IP65/IK09 alla Mole — [Claypaky](https://www.claypaky.it/en/news/a_new_claypaky_led_lighting_system_for_the_mole_antonelliana); 10 anni di servizio di monitoraggio remoto a Londra — [LEDinside](https://www.ledinside.com/news/2025/10/london_illuminated_river_project_powered_signify)

### Inferences
- Nei progetti su strutture marine/fluviali il punto debole documentato è la durata degli apparecchi esposti, non il controllo: per Versus Lux contano IP, resinatura, connettori e trattamento anticorrosione quanto la radio.
- La telemetria (RDM/stato del nodo) è la voce che i grandi fornitori vendono come servizio pluriennale: una mesh che riporta lo stato di ogni apparecchio è un argomento di vendita concreto.

### Gaps
- Nessun capitolato o bando comunale italiano con importi trovato in questa ricerca (Iren, A2A, Acea non pubblicano i costi nei comunicati consultati).
- Nessun dato documentato su vandalismo, infiltrazioni d'acqua o corrosione per i progetti italiani; nessun dato sui guasti di sistemi wireless nei casi LumenRadio/Casambi (fonti tutte del produttore).

## 4. Contenuti: scene statiche, calendari, spettacoli, interattività, pixel mapping

### Takeaway
Si va da colorazioni statiche per ricorrenze (Torino, Napoli, Torre Eiffel con proiettori temporanei) a calendari automatici (Shanghai, Quanjiao), spettacoli orari (Jacques-Cartier, Burj Khalifa) e contenuti generativi o guidati da dati (Bay Lights, Jacques-Cartier dai social). Il pixel mapping ad alta densità è limitato ai progetti iconici.

### Cited Findings
- Contenuti guidati da dati: Jacques-Cartier con colori, intensità e movimento in base alla frequenza di "Montréal" sui social; 5 spettacoli orari a notte — [Philips](https://images.philips.com/is/content/PhilipsConsumer/PDFDownloads/ODLI20170517_001-UPD-en_US-PLt-17063CS_Jacques-Cartier_bridge_case_study.pdf)
- Spettacoli video: Burj Khalifa >1.825 show, ognuno provato su banco identico — [Gulf News](https://gulfnews.com/uae/how-burj-khalifa-puts-on-its-stellar-light-shows-1.61074857); Allianz Arena 40 img/s — [New Atlas](https://newatlas.com/bayern-munich-allianz-arena-philips-led-facade/38936)
- Calendari: Shanghai con scene feriali/weekend/festive e modalità notturna — [Signify](https://www.signify.com/b-dam/signify/en-aa/about/news/2018/20181121-signify-shines-dynamic-light-on-shanghais-buildings-bridges-and-rives/Release_Shanghai_shines_dynamic_light_a211118.pdf); Quanjiao con 4 calendari automatici — [Seekway](https://www.seekway.com/info-detail/sustainable-landmark-bridge-illumination-via-cloud-based-control-systems); Illuminated River spento alle 2 — [The Art Newspaper](https://www.theartnewspaper.com/2019/07/18/its-lit-leo-villareal-illuminates-four-london-bridges-for-worlds-longest-work-of-art)
- Colorazioni per ricorrenze: Torre Eiffel (rosso per il Capodanno cinese 2004, blu per la Giornata dell'Europa 2006, rosa ogni ottobre) con proiettori esterni installati ad hoc — [Tour Eiffel](https://www.toureiffel.paris/en/the-monument/lights); Empire State da 10 colori a 16 milioni — [Signify](https://www.signify.com/en-gb/our-company/news/press-release-archive/2012/20120509-empire-state-building); Napoli colora monumenti di azzurro per eventi sportivi — [Corriere dello Sport](https://www.corrieredellosport.it/news/calcio/italia/2023/03/23-105366909/napoli_la_citta_si_illumina_d_azzurro)
- Musica: Banpo con 100 sequenze — [LSi](https://lsionline.com/news/martin-illuminates-banpo-bridge-fountain-kbcowu); Sagrada Família con luce che accompagna la musica — [ISP Audio](https://www.isp-audio.com/en/installation-case-studies/lighting-installation/13473-light-connects-architecture-music-and-emotion-in-the-sagrada-familia-s-tower-of-jesus)
- Vincoli di tutela sui contenuti: a Torino la Soprintendenza ha imposto il bianco per le sponde — [Mentelocale](https://www.mentelocale.it/torino/articoli/80069-nuove-luci-torino-ponti-umberto-isabella-balbis.htm); ad Akershus toni caldi sulla pietra con un solo accento blu — [LumenRadio](https://lumenradio.com/stories/akershus-fortress-how-w-dali-brought-new-life-to-an-iconic-landmark/)

### Inferences
- Per il mercato italiano (monumenti, ponti urbani) il caso d'uso prevalente è "bianco di base + colorazioni per ricorrenze + calendario": bastano scene e calendario affidabili, con pochi dati da trasmettere — profilo adatto a una mesh a bassa banda. Gli show video a 40 fps tipo Allianz Arena richiedono banda e latenza da cavo/fibra o da CRMX, ed è lì che serve il bridge DMX/Art-Net.
- Il quinto canale (bianco/ambra in un RGBW+) risponde alle prescrizioni delle Soprintendenze che chiedono bianchi di qualità sulla pietra.

### Gaps
- Nessuna fonte su contenuti interattivi in tempo reale nei progetti italiani; nessun dato su latenza o frame rate ottenuti con controllo wireless in esterno.
