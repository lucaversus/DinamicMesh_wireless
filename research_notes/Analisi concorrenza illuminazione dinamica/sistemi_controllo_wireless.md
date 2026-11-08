# Sistemi di controllo wireless per illuminazione architetturale dinamica (facciate, ponti, monumenti) — catalogo concorrenza

Note di ricerca, stato al 8 novembre 2026. Ricerca web limitata (~35 chiamate): molti dati sono presi da pagine prodotto e rivenditori; dove una pagina non riportava un dato è segnato come lacuna. Le informazioni datate sono marcate con la data della fonte.

## 1. Quali piattaforme esistono e quali sono le loro caratteristiche radio (banda, topologia, nodi, portata, latenza, universi)

### Takeaway
Il mercato si divide in tre famiglie nettamente distinte: (a) **wireless DMX punto-multipunto a stella** (LumenRadio CRMX, Wireless Solution W-DMX, Astera) che trasporta DMX live con latenza fissa ~5 ms ma 1–2 universi per trasmettitore e senza mesh; (b) **mesh a bassa banda per dimmerazione/scene** (Casambi BLE, AirGlow/MiraMesh, Zigbee di Interact Pro, Lutron Clear Connect, WiZ Pro Wi-Fi, Bluetooth Mesh NLC/Silvair, DALI+ su Thread) con 100–250 nodi per rete e scene memorizzate; (c) **controller per facciate/ponti cablati** (Pharos, Color Kinetics/Interact Landmark, e:cue) che nei grandi progetti documentati usano Ethernet/DMX cablato, non radio. Nessuna fonte trovata descrive un sistema commerciale che offra contemporaneamente mesh tra apparecchi + effetti RGB dinamici sincronizzati + molti universi: è lo spazio che il progetto ESP32-C5/ESP-NOW di Versus Lux punta a occupare.

### Cited Findings

**LumenRadio (Svezia) — CRMX / CRMX2 (wireless DMX, stella)**
- Moduli OEM CRMX: TimoTwo FX (CRMX + W-DMX transceiver con Bluetooth, RDM in RX e TX opzionale, modulo SMT pre-certificato), TiMo FX/RX (antenna on-chip e connettore u.FL), Pluggy FX/RX (pin header 2x6), CRMXchip (ricevitore QFN48 6x6 mm, "il più piccolo ricevitore wireless DMX al mondo"). Tutti i moduli supportano nativamente sia CRMX sia W-DMX. Prezzi e licenze non indicati; rimanda a sales@lumenradio.com — [LumenRadio CRMX OEM sales flyer](https://lumenradio.com/support-materials/crmx-oem-sales-flyer)
- Elenco moduli OEM LumenRadio: TimoTwo, TiMo FX, TiMo RX, Pluggy RX, CRMXchip, W-DALI OEM module (controllo indoor), W-BACnet, W-Modbus, AirGlow OEM module (controllo outdoor), Mira OEM modules (mesh); "già certificati e pronti per l'integrazione", basati su "patented wireless mesh technology" — [LumenRadio – Radio modules for OEMs](https://lumenradio.com/?p=8645)
- Galileo MAX: trasmettitore CRMX a **2 universi**, ingresso Ethernet Art-Net e sACN, DMX512-A e RDM, protocolli RF CRMX, CRMX2, W-DMX G3 e G4S, **latenza fissa 5 ms**, portata "centinaia di metri", IP X0 (per esterno serve custodia IP65 certificata); prezzo non pubblicato sulla pagina — [LumenRadio Galileo MAX](https://lumenradio.com/products/galileo-max/)
- Galileo TX: trasmettitore single-universe DIN-rail, DMX512-A/RDM, CRMX Classic, W-DMX G3/G4S, Bluetooth 5.0, 2402–2480 MHz, potenza 7–280 mW, latenza 5 ms, crittografia 128 bit con FEC, configurazione via app Bluetooth, omologazioni CE, FCC, IC, MET, KC, MIC, UKCA; prezzo non mostrato nella pagina stampabile — [Huss Licht & Ton – Galileo TX](https://www.huss-licht-ton.de/print_product_info.php/en/products_id/49248)
- Comunicato LSI sul rilascio dei moduli OEM CRMX (data della notizia non verificata) — [LSI Online](https://lsionline.com/news/lumenradio-releases-crmx-oem-modules-joqgnl)

**LumenRadio — AirGlow / MiraMesh (mesh outdoor, DALI-2/D4i)**
- AirGlow OEM Module (SKU 820-8301): mesh MiraMesh brevettata "self-contained, self-healing", nessun gateway; 2,45 GHz ISM (2402–2480 MHz); fino a **8 hop**; fino a **1500 m in vista** tra nodi mesh, Bluetooth fino a 35 m; latenza descritta solo come "sub second response time"; DALI-2 e D4i, fino a **6 canali DALI DT6** (RGBW/A, CW, WW meshed); app smartphone per commissioning, OTA; configurazione salvata **in cloud** cifrata; certificazioni ETSI EN 300 328 v2.2.2, FCC Part 15 modulare (fino a 100 mW), IC, MIC, KCC; 18,5 × 33,5 mm, SMT, connettore U.FL, niente antenna interna; prezzo non pubblicato; numero max di nodi non indicato — [LumenRadio AirGlow OEM module](https://lumenradio.com/?p=3826)
- All'annuncio (16 marzo 2018) AirGlow supportava sia Bluetooth Mesh sia Mira IPv6 Mesh, funzionamento standalone senza cloud/gateway, 2 interfacce DALI con alimentatore integrato, uscita 1-10 V, 2 ingressi pulsante, relè di rete — [PLSN, 2018](https://plsn.com/?p=285753)
- Esiste una versione AirGlow Zhaga Book 18 D4i (art. 820-4002) venduta in Svezia — [Ahlsell](https://www.ahlsell.se/en/products/electric/lighting-70-83/79-luminaire-accessories/other-light-fitting-accessories/other/7985401---radionod-zhaga-book-18-d4i-820-4002)

**Wireless Solution Sweden — W-DMX (stella)**
- BlackBox F-1 G6: 2,4 GHz; RDM, Art-Net e sACN solo con upgrade Wi-Fi opzionale — [Thomann AE](https://www.thomann.ae/wireless_solution_blackbox_f_1_g6_transceiver.htm)
- Manuale G6: Adaptive Frequency Hopping + TDMA, limiti di banda selezionabili (piena, metà, terzi); F-2 ha due radio (A e B), un universo ciascuna; numero di ricevitori per trasmettitore illimitato; retrocompatibile con G3 in modalità compatibilità; **CRMX supportato tramite licenza acquistata a parte** via app W-DMX Configurator; modulo Wi-Fi opzionale con Art-Net I/II/III + RDM e sACN; uso indoor (IP non dichiarato); portata e latenza non specificate — [Manuale BlackBox F-1 G6](https://manuals.plus/w-dmx/f-1-blackbox-g6-wdmx-blackbox-f1-g6-transceiver-manual.pdf)
- La tecnologia W-DMX G6 è rimarchiata anche da Chauvet (Micro T-1 TRX G6) — [SoundPro](https://soundpro.com/products/chauvet-pro-microt1trxg6)

**Astera — AsteraBox ART7 (CRMX + proprietario)**
- AsteraBox ART7: trasmettitore wireless DMX CRMX fino a 300 m, UHF fino a 300 m, Wi-Fi, BluetoothBridge (3 m) per AsteraApp, ingresso DMX su jack 3,5 mm con adattatore XLR; batteria 60 h (app) / 18 h (CRMX). Prodotto orientato a eventi/film, non installazione fissa — [Production Gear UK](https://productiongear.co.uk/products/astera-asterabox-art7-wifi)

**Casambi (Finlandia) — Bluetooth Low Energy mesh proprietaria**
- Limiti di rete: **Evolution 250 nodi** (Classic 127, solo manutenzione); 250 gruppi; **255 scene per rete**; **80 step per animazione**; 255 timer; 1 gateway cloud per rete; Site consigliati < 50 reti; maggior traffico = reti più piccole; latenza e portata non dichiarate — [Casambi Support – System constraints](https://support.casambi.com/support/solutions/articles/12000096178-system-constraints-overview-network-limits)
- Evolution aggiunge controllo colore XY e XY+TW per DALI DT8, fino a 8 elementi custom per apparecchio, fino a 8 canali PWM sul CBM-002 — [Casambi Support – Evolution vs Classic](https://support.casambi.com/support/solutions/articles/12000064587-what-are-the-differences-between-evolution-and-classic-)
- CBU-ASD: uscita 0-10 V o DALI (broadcast, alimenta il bus DALI), supporto colore RGB o temperatura colore, app gratuita — [Inspyer Lighting](https://www.inspyerlighting.co.uk/products/casambi-wireless-control-unit-for-led-drivers)

**Tridonic — basicDIM Wireless (Casambi Ready)**
- basicDIM Wireless OTD: BLE 4.0/5.0 2,4 GHz < +20 dBm EIRP, Casambi Ready, mesh fino a **250 nodi**, portata fino a **150 m** in vista con montaggio > 4 m, **IP66 / IK09**, −40…+70 °C, uscita DALI, sensore di luce integrato, presa Zhaga Book 18 Ed.3, OTA; il datasheet non menziona DT8/RGB; destinazione parcheggi, strade, parchi — [Tridonic datasheet basicDIM Wireless Outdoor](https://resources.tridonic.com/PDB/Ressource/GroupPdf/en/basicDIM_Wireless_Outdoor_31230.pdf)

**Signify / Philips**
- Interact Pro (sistema wireless da guida "Interact ready"): **Zigbee** (anche Zigbee Green Power), **200 nodi per rete**, 40 nodi per gruppo senza gateway / 200 con gateway, 100 reti per progetto, 128 scene per rete, 64 gruppi; tutti gli apparecchi devono restare alimentati 24/7; nessuna menzione di colore — [Interact – System limitations](https://sme.interact-lighting.com/web/help/prf-pra/2.7/system-guide/system-limitations.html)
- Interact Landmark (facciate/monumenti): rete di monitoraggio e controllo su **switch Ethernet** standard; compatibile con tutti gli apparecchi dinamici Color Kinetics e Vaya, con Light System Manager e controller Pharos; gateway Color Kinetics; gestione contenuti remota; nessuna opzione wireless citata — [Interact Landmark specification](https://dev.dms.wizconnected.com/content/B2B_LI/en_AA/microsites/interact/specification/interact-landmark.html)
- Caso CEPSA: 2.500 apparecchi per facciata gestiti con Interact Landmark — [Interact customer story CEPSA](https://www.interact-lighting.com/en-us/customer-stories/cepsa)
- WiZ Pro: moduli Wi-Fi + Bluetooth, commissioning senza gateway via app WiZ Pro Setup, "fino a 200 punti luce" per progetti piccoli/medi, scene dinamiche multi-colore, bridge box a 1, 2 o 5 canali, dashboard cloud opzionale — [Catalogo WiZ Pro RGB EU, dic. 2022](https://www.assets.signify.com/is/content/Signify/Assets/signify/united-states/20221223-wiz-pro-cataloge-rgb-eu.pdf)

**Lutron — Athena / Ketra**
- Athena: radio **Clear Connect Type X**; **100 dispositivi Type X per gateway**; 16 processori per sistema, 1.600 per edificio; seeTouch DMX Interface a 32 canali; cloud tramite dashboard/app, Server Mode opzionale; elenca Ketra, Rania, Lumaris come gamme apparecchi; nessun apparecchio outdoor citato — [Lutron Athena System Architecture](https://assets.lutron.com/a/documents/3685737_Athena_System_Architecture.pdf)

**Pharos Architectural Controls (UK)**
- Ponte delle Catene di Budapest: 1.180 apparecchi LED, controller Pharos Designer LPC X (20 universi), 4 Designer EDN con 20 porte DMX ciascuno per distribuzione eDMX **via Ethernet** lungo il ponte; nessun wireless citato (articolo ~2024) — [Live Design Online](https://www.livedesignonline.com/lighting/pharos-illuminate-famous-budapest-chain-bridge)

**OSRAM / Traxon e:cue**
- ETH2DALI (2 universi DALI, 128 dispositivi, 1 uscita DMX) e Lighting Application Suite 7.0 con e:pix/DMX/DALI; nessuna capacità wireless citata. Nota: l'URL riporta "2026/08" ma l'articolo è datato **23 settembre 2014** — [LEDinside](https://ledinside.com/products/2026/08/traxon_technologies_introduces_new_led_control_solutions)
- Butler XT2: controller DMX su guida DIN con orologio — [Architect Magazine](https://www.architectmagazine.com/technology/products/butler-xt2-traxon-e-cue_o/)

**Nicolaudie / Sunlite — STICK**
- STICK-CW4: controller DMX da parete Wi-Fi programmabile, 1024 canali (dati dai titoli dei listini) — [Flexfire LEDs](https://www.flexfireleds.com/products/nicolaudie-stick-cw4-wi-fi-programmable-dmx-controller); [Ultraleds](https://www.ultraleds.co.uk/nicolaudie-1-zone-5-15v-dmx512-wifi-touch-led-wall-plate-1024-channels)

**DALI+ (DALI Alliance) — DALI su IP/Thread**
- DALI+ = DALI su rete mesh wireless Thread, IP; estende installazioni DALI esistenti; presentato a Light + Building 2026 (comunicato 19 marzo 2026); nessun numero di prodotti certificati o di supporto DT8 nel documento — [DALI Alliance at Light + Building 2026 (PDF)](https://dali-alliance.org/data/downloadables/4/7/3/dali-alliance-at-light-build-2026.pdf)
- La DALI Alliance ha lanciato specifiche di test e certificazione per DALI+ — [US Lighting Trends](https://uslightingtrends.com/news/dali-alliance-launches-test-and-certification-specifications-for-dali); cooperazione Thread Group–DALI Alliance annunciata il 20 maggio 2021 — [BusinessWire](https://www.businesswire.com/news/home/20210520005105/en/Thread-Group-and-DALI-Alliance-Cooperate-on-DALI-with-Thread-for-Commercial-Lighting)

**Bluetooth Mesh NLC / Silvair**
- Bluetooth SIG ha introdotto i profili Networked Lighting Control (NLC) — [Silvair blog](https://blog.silvair.com/blog/resources-bluetooth-sig-introduces-networked-lighting-control-nlc-profiles/); specifica [BLC NLCP v1.0.1](https://files.bluetooth.com/download/blcnlcp_v1-0-1)

**Lightcloud (Current / RAB)**
- Lightcloud Blue: apparecchi RGB con "Direct Connect" all'app via Bluetooth, nessun gateway o hub — [RAB Lighting WFR6B/RGB](https://www.rablighting.com/product/WFR6B/RGB)

**ESP32 / ESP-NOW (progetti, non prodotti commerciali certificati)**
- Bridge Art-Net→ESP-NOW (ESP32 + W5500): master riceve Art-Net UDP 6454 su Ethernet cablato per non contendere la radio, rilancia DMX su ESP-NOW; frame 512 canali in 3 pacchetti ≤ 200 byte con numeri di sequenza; **max 20 slave** (limite peer ESP-NOW unicast); 1 universo per slave (0–15), broadcast se più slave condividono un universo; heartbeat PING 2 s/timeout 8 s; portata ~200 m in campo aperto; nessun dato di latenza o perdita pacchetti; progetto DIY open source, nessuna certificazione — [WIZnet Maker](https://maker.wiznet.io/irina/projects/artnet-to-esp-now-dmx512-bridge--esp32-w5500-wireless-lighting-system/)
- Altri progetti DIY: DMXoverNOW (kripton) — [relatedrepos](https://relatedrepos.com/gh/kripton/DMXoverNOW); Lumiband (braccialetti DMX ESP32) — [Hackaday.io](https://hackaday.io/project/205505-lumiband-gen3-wireless-dmx-led-wristband-esp32); controller ESP-NOW per WLED — [ecosyste.ms](https://awesome.ecosyste.ms/projects/github.com%2Fallaguna%2Fesp-now-wled-controller)

### Inferences
- I sistemi CRMX/W-DMX sono a stella (un trasmettitore, molti ricevitori) e la portata per facciate lunghe/ponti dipende dalla posizione del trasmettitore; la mesh ESP-NOW tra apparecchi di Versus Lux si differenzierebbe proprio sul multi-hop, che CRMX non offre.
- Le mesh "general lighting" (Casambi, Zigbee Interact Pro, Clear Connect, Bluetooth NLC) hanno limiti di 100–250 nodi per rete, coerenti con una progettazione per uffici/negozi, non per facciate con migliaia di pixel.
- Il caso ESP-NOW DIY mostra il limite dei 20 peer unicast: un sistema commerciale su ESP-NOW deve usare broadcast/multicast con propria affidabilità (FEC, ripetizioni, time-stamp) — scelta già prevista dal progetto Versus Lux (comandi di scena con time-stamp).

### Gaps
- **ETC Mosaic**, **Madrix** (wireless?), **Enlighted**, **Helvar**, **Zencontrol**, **ams OSRAM**, **Zigbee/Thread/Matter professionale**, sistemi **LoRa/sub-GHz** per facciate: non ho raccolto fonti nel budget di ricerca disponibile. Da conoscenza pregressa (non verificata qui): Pharos e ETC Mosaic sono controller cablati Ethernet/DMX; Madrix è software/hardware Art-Net/sACN cablato. Da verificare.
- Portata e latenza di W-DMX G6 non trovate nel manuale; latenza di Casambi non dichiarata da Casambi.
- Numero massimo di nodi per rete AirGlow/MiraMesh non pubblicato.
- Stato reale dei prodotti DALI+ certificati a novembre 2026 e supporto colore DT8 su DALI+: non trovato.
- Signify Color Kinetics non sembra avere opzioni wireless per facciate nelle fonti trovate (solo Ethernet/Landmark); da confermare.

## 2. Effetti RGB dinamici sincronizzati o solo scene statiche? DMX live o solo scene memorizzate?

### Takeaway
Solo le soluzioni wireless DMX (CRMX, W-DMX, Astera) trasportano DMX live in tempo reale (latenza 5 ms per Galileo), ma limitate a 1–2 universi per trasmettitore. Le mesh BLE/Zigbee/Thread/Clear Connect lavorano con scene e animazioni memorizzate (Casambi: 80 step per animazione) e con latenze dichiarate solo genericamente ("sub second" per AirGlow), quindi non sono adatte a pixel-mapping o video su facciata.

### Cited Findings
- Galileo MAX: latenza fissa 5 ms, 2 universi, DMX/Art-Net/sACN in ingresso — [LumenRadio Galileo MAX](https://lumenradio.com/products/galileo-max/)
- Galileo TX: latenza 5 ms, 1 universo — [Huss Licht & Ton](https://www.huss-licht-ton.de/print_product_info.php/en/products_id/49248)
- W-DMX F-2 G6: due radio, un universo ciascuna — [Manuale G6](https://manuals.plus/w-dmx/f-1-blackbox-g6-wdmx-blackbox-f1-g6-transceiver-manual.pdf)
- Casambi: animazioni come sequenze di scene memorizzate, massimo 80 step (scene + attese), 255 scene per rete; nessun limite/latenza per effetti RGB dichiarato — [Casambi Support](https://support.casambi.com/support/solutions/articles/12000096178-system-constraints-overview-network-limits)
- AirGlow: RGBW e tunable white in mesh, "sub second response time" — [LumenRadio AirGlow](https://lumenradio.com/?p=3826)
- WiZ Pro: "scene di luce dinamiche" multi-colore — [Catalogo WiZ Pro](https://www.assets.signify.com/is/content/Signify/Assets/signify/united-states/20221223-wiz-pro-cataloge-rgb-eu.pdf)
- Interact Landmark: contenuti dinamici Color Kinetics, cambi scena da remoto, ma rete Ethernet — [Interact Landmark](https://dev.dms.wizconnected.com/content/B2B_LI/en_AA/microsites/interact/specification/interact-landmark.html)

### Inferences
- Il posizionamento naturale per Versus Lux è "dinamico vero senza cavo dati": effetti generati localmente nel nodo e sincronizzati via time-stamp (come le scene memorizzate delle mesh, ma con clock comune), più eventuale streaming DMX limitato tramite bridge. Un confronto diretto sui ms di sincronismo tra apparecchi farebbe da argomento commerciale, dato che i concorrenti mesh non pubblicano questo dato.

### Gaps
- Nessuna misura indipendente trovata della sincronia (skew) tra apparecchi in reti Casambi/Zigbee durante animazioni colore.

## 3. Integrazione con console DMX/Art-Net/sACN; gateway necessari

### Takeaway
CRMX e W-DMX si integrano nativamente con console (ingresso DMX; Art-Net/sACN su Galileo MAX o con modulo Wi-Fi per W-DMX). Le mesh di general lighting richiedono interfacce dedicate e limitate (es. Lutron seeTouch DMX a 32 canali); i sistemi facciata cablati (Pharos, Landmark) sono nativamente Ethernet/eDMX.

### Cited Findings
- Galileo MAX: ingresso Ethernet Art-Net e sACN — [LumenRadio](https://lumenradio.com/products/galileo-max/)
- W-DMX G6: Art-Net I/II/III + RDM e sACN solo con modulo Wi-Fi opzionale venduto a parte — [Manuale G6](https://manuals.plus/w-dmx/f-1-blackbox-g6-wdmx-blackbox-f1-g6-transceiver-manual.pdf); [Thomann](https://www.thomann.ae/wireless_solution_blackbox_f_1_g6_transceiver.htm)
- Lutron Athena: seeTouch DMX Interface 32 canali — [Lutron](https://assets.lutron.com/a/documents/3685737_Athena_System_Architecture.pdf)
- Pharos LPC X + EDN: eDMX Ethernet — [Live Design](https://www.livedesignonline.com/lighting/pharos-illuminate-famous-budapest-chain-bridge)
- Interact Landmark: compatibile con controller Pharos e Light System Manager, Multi-Protocol Converter per Vaya e altri dispositivi DMX/RDM — [Interact Landmark](https://dev.dms.wizconnected.com/content/B2B_LI/en_AA/microsites/interact/specification/interact-landmark.html)
- Esiste un gateway Casambi Lithernet (documentazione beta) — [readthedocs](https://io-module-documentation.readthedocs.io/en/latest/iom/BETA/Casambi%20Lithernet%20Gateway.html)

### Inferences
- Il bridge DMX/Art-Net/sACN opzionale previsto da Versus Lux è necessario per competere con CRMX nel segmento "light designer con console"; senza di esso il prodotto si confronterebbe solo con Casambi/WiZ.

### Gaps
- Dettagli del gateway Casambi Lithernet (funzioni DMX? canali?) non verificati.

## 4. Metodo di commissioning; cloud vs locale

### Takeaway
Prevale il commissioning da app smartphone via Bluetooth (Casambi, AirGlow, Galileo TX, WiZ Pro Setup, Astera). Il cloud è spesso presente come archivio configurazione o dashboard (AirGlow salva la configurazione in cloud; WiZ Pro e Lutron offrono dashboard cloud), mentre i sistemi DMX sono puramente locali.

### Cited Findings
- AirGlow: app smartphone, OTA, configurazione salvata in cloud cifrata — [LumenRadio](https://lumenradio.com/?p=3826)
- Galileo TX: configurazione via app Bluetooth e proxy RDM — [Huss](https://www.huss-licht-ton.de/print_product_info.php/en/products_id/49248)
- W-DMX G6: app W-DMX Configurator — [Manuale G6](https://manuals.plus/w-dmx/f-1-blackbox-g6-wdmx-blackbox-f1-g6-transceiver-manual.pdf)
- Casambi: app gratuita; massimo 1 gateway cloud per rete; 10 account di accesso — [Inspyer](https://www.inspyerlighting.co.uk/products/casambi-wireless-control-unit-for-led-drivers); [Casambi Support](https://support.casambi.com/support/solutions/articles/12000096178-system-constraints-overview-network-limits)
- WiZ Pro: app Setup senza gateway, dashboard cloud multi-sito che richiede Wi-Fi — [Catalogo WiZ Pro](https://www.assets.signify.com/is/content/Signify/Assets/signify/united-states/20221223-wiz-pro-cataloge-rgb-eu.pdf)
- Lutron Athena: cloud via dashboard/app, Server Mode opzionale — [Lutron](https://assets.lutron.com/a/documents/3685737_Athena_System_Architecture.pdf)
- Lightcloud Blue: app via Bluetooth senza gateway — [RAB](https://www.rablighting.com/product/WFR6B/RGB)

### Inferences
- La scelta Versus Lux "web app via Wi-Fi, nessun Bluetooth, locale" è un differenziatore (nessuna app da installare, nessun cloud obbligatorio), ma va considerato che il mercato si aspetta commissioning da smartphone; una web app servita dal coordinatore soddisfa questa aspettativa.

### Gaps
- Funzionamento offline di Lutron Athena e WiZ Pro senza cloud non dettagliato nelle fonti.

## 5. Modello di licenza/certificazione per OEM

### Takeaway
LumenRadio vende moduli pre-certificati (radio omologata) senza pubblicare prezzi o royalty; Wireless Solution vende la compatibilità CRMX come licenza a pagamento separata; Casambi funziona con l'ecosistema "Casambi Ready" (es. Tridonic); i costi di certificazione/royalty non sono pubblici in nessuna fonte trovata.

### Cited Findings
- Moduli LumenRadio "pre-certified", acquisto via vendite dirette — [CRMX OEM flyer](https://lumenradio.com/support-materials/crmx-oem-sales-flyer)
- AirGlow modulo con certificazioni ETSI EN 300 328, FCC modular, IC, MIC, KCC — [LumenRadio](https://lumenradio.com/?p=3826)
- W-DMX G6: supporto CRMX con licenza acquistata separatamente — [Manuale G6](https://manuals.plus/w-dmx/f-1-blackbox-g6-wdmx-blackbox-f1-g6-transceiver-manual.pdf)
- Tridonic basicDIM Wireless è "Casambi Ready" — [Casambi news](https://casambi.com/news/tridonic-releases-the-next-generation-casambi-ready-basicdim-wireless-module/); [Tridonic datasheet](https://resources.tridonic.com/PDB/Ressource/GroupPdf/en/basicDIM_Wireless_Outdoor_31230.pdf)
- DALI Alliance gestisce la certificazione DALI-2 (logo) e ha specifiche di test DALI+ — [DALI Alliance L+B 2026](https://dali-alliance.org/data/downloadables/4/7/3/dali-alliance-at-light-build-2026.pdf); [US Lighting Trends](https://uslightingtrends.com/news/dali-alliance-launches-test-and-certification-specifications-for-dali)

### Inferences
- Una soluzione ESP32-C5 proprietaria evita royalty di ecosistema (Casambi Ready, CRMX), ma richiede a Versus Lux di sostenere direttamente le prove RED (EN 300 328 per 2,4 GHz; e per il C5 anche le bande 5 GHz se Wi-Fi a 5 GHz attivo). I moduli Espressif pre-certificati riducono questo onere.

### Gaps
- Prezzi moduli TimoTwo/TiMo/CRMXchip, costo licenza CRMX su W-DMX, quote Casambi Ready, quote membership DALI Alliance, costi Bluetooth SIG: **non pubblicati** nelle fonti trovate.

## 6. Prezzi (moduli, gateway, trasmettitori, per nodo)

### Takeaway
Prezzi pubblici trovati solo per prodotti finiti di canale: un transceiver W-DMX BlackBox F-1 G6 costa ~840 €, un AsteraBox ART7 ~302 £ + IVA, un'unità Casambi CBU-ASD 73 £. Prezzi dei moduli OEM (LumenRadio, Casambi) non pubblicati.

### Cited Findings
- Wireless Solution BlackBox F-1 G6: **€839,50** (o AED 3.635, indicativo), Thomann, consultato nov. 2026 — [Thomann AE](https://www.thomann.ae/wireless_solution_blackbox_f_1_g6_transceiver.htm)
- Astera AsteraBox ART7 Wi-Fi: **£301,95 + IVA (£362,34 IVA incl.)**, Production Gear UK, consultato nov. 2026 — [Production Gear](https://productiongear.co.uk/products/astera-asterabox-art7-wifi)
- Casambi CBU-ASD: **£73,00**, Inspyer Lighting UK, consultato nov. 2026 — [Inspyer](https://www.inspyerlighting.co.uk/products/casambi-wireless-control-unit-for-led-drivers)
- LumenRadio Galileo MAX e Galileo TX: prezzo non pubblicato sulle pagine consultate — [LumenRadio](https://lumenradio.com/products/galileo-max/); [Huss](https://www.huss-licht-ton.de/print_product_info.php/en/products_id/49248)
- AirGlow OEM module: prezzo non pubblicato — [LumenRadio](https://lumenradio.com/?p=3826)

### Inferences
- Il costo di un collegamento wireless DMX professionale per ricevitore (centinaia di euro) è di ordini di grandezza superiore al BOM radio di un nodo ESP32-C5 (pochi euro): argomento forte per la mesh integrata in ogni apparecchio, purché affidabilità e sincronismo siano dimostrati.

### Gaps
- Prezzi di TimoTwo/CRMXchip (DigiKey/Mouser non restituiti dalla ricerca), Galileo RX, W-DMX R-512 Lite G6, gateway Casambi, Interact Landmark, Lutron Athena, WiZ Pro, Pharos LPC X: non raccolti o non pubblicati.

## 7. Punti deboli e limiti noti

### Takeaway
I limiti documentati sono strutturali più che aneddotici: CRMX/W-DMX = pochi universi per trasmettitore e stella senza mesh; mesh BLE/Zigbee = 100–250 nodi, scene memorizzate, prestazioni che calano con il traffico; ESP-NOW DIY = 20 peer e nessuna certificazione. Non ho trovato recensioni di forum attendibili su problemi di sincronia RGB.

### Cited Findings
- Casambi: "più traffico di rete significa reti più piccole"; più sensori di luce generano carichi che riducono le prestazioni; Classic solo in manutenzione — [Casambi Support](https://support.casambi.com/support/solutions/articles/12000096178-system-constraints-overview-network-limits)
- Casambi pubblica una tabella di troubleshooting (aprile 2026) — [Casambi troubleshooting table](https://casambi.com/wp-content/uploads/2026/04/troubleshooting-table.pdf); discussione utenti su problemi di integrazione — [Homey Community "Casambi issues"](https://community.homey.app/t/casambi-issues/151313.md) (contenuto non letto)
- Interact Pro: apparecchi da tenere alimentati 24/7, non si può interrompere la rete per spegnere — [Interact](https://sme.interact-lighting.com/web/help/prf-pra/2.7/system-guide/system-limitations.html)
- Galileo MAX IP X0: all'esterno serve custodia IP65 — [LumenRadio](https://lumenradio.com/products/galileo-max/)
- W-DMX G6: solo uso indoor, portata ridotta da vetro/cemento, serve linea di vista; CRMX solo a pagamento — [Manuale G6](https://manuals.plus/w-dmx/f-1-blackbox-g6-wdmx-blackbox-f1-g6-transceiver-manual.pdf)
- Tridonic outdoor: portata 150 m ridotta da edifici, alberi, meteo, sporco — [Tridonic](https://resources.tridonic.com/PDB/Ressource/GroupPdf/en/basicDIM_Wireless_Outdoor_31230.pdf)
- ESP-NOW DIY: max 20 slave, nessun dato di perdita pacchetti, nessuna certificazione — [WIZnet Maker](https://maker.wiznet.io/irina/projects/artnet-to-esp-now-dmx512-bridge--esp32-w5500-wireless-lighting-system/)

### Inferences
- Il requisito "alimentazione 24/7" vale anche per la mesh Versus Lux (i nodi ripetono): va dichiarato nelle istruzioni, come fa Signify.
- Corpi in alluminio/acciaio attenuano la radio: tutti i moduli outdoor citati usano antenne esterne (U.FL su AirGlow, RP-SMA su Galileo TX); l'antenna esterna o la finestra radio-trasparente è un punto di progetto critico.

### Gaps
- Nessuna fonte forum (ControlBooth, Reddit) letta su affidabilità CRMX in installazioni fisse outdoor o su Casambi per facciate; da approfondire.
