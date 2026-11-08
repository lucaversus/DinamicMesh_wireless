# Apparecchi con radio integrata per illuminazione dinamica RGB/RGBW/RGBWA (benchmark, novembre 2026)

Note raccolte l'8 novembre 2026. Prezzi solo dove trovati su una pagina reale, con valuta, fonte e data di consultazione (8/11/2026). Dove una scheda non riporta un dato, è segnato "n.d." (non dichiarato).

## Quali prodotti esistono e con quale tecnologia radio

### Takeaway
Gli apparecchi con radio davvero integrata nel corpo sono quasi tutti del mondo **eventi/noleggio a batteria** (Astera, Chauvet DJ, ADJ, Prolights, BeamZ, cloni cinesi tipo Shehds). Nel mondo **architetturale permanente** (Color Kinetics e simili) la radio resta di solito **esterna** all'apparecchio: si usano box CRMX/ricevitori separati vicino ai proiettori cablati. Lo standard di fatto per la radio "pro" integrata è **LumenRadio CRMX** (Astera, Prolights). Gli altri usano protocolli proprietari (ADJ WiFLY EXR, Chauvet D-Fi). Questo è lo spazio libero per un apparecchio architetturale da facciata alimentato da rete con mesh integrata.

### Cited Findings

**Tabella riassuntiva (dati verificati)**

| Prodotto | Stato | Radio integrata | Portata dichiarata | Colori / LED | Potenza / flusso | IP | Peso | Fonte |
|---|---|---|---|---|---|---|---|---|
| Astera AX5 TriplePAR | in vendita | CRMX (ricevitore), UHF, Bluetooth (solo versione AX5-BTB), Wi-Fi, IR | CRMX/UHF fino a 300 m; Bluetooth fino a 3 m | RGBAW, 3200–6500 K, CRI/TLCI ≤92 | 45 W LED; 1080 lm (3200 K) / 1413 lm (5500 K); fascio 13°, campo 26° | IP65 | 3,4 kg | [Datasheet Astera AX5 V3](https://astera-led.com/wp-content/uploads/AX5_TriplePar_Datasheet_V3.pdf) |
| Astera PixelBrick PB15 | in vendita | CRMX (ricevitore), UHF, Bluetooth (BluetoothBridge integrato), Wi-Fi, IR | CRMX/UHF fino a 300 m; Bluetooth 3 m | RGB + Mint + Amber (RGBMA), CRI ≥96 | 12 W LED, 20 W max; 395–475 lm; fascio 13°, campo 25° | IP65 (scollegato solo con tappo PB15-PLG; cablato con cavi PWB-CAB) | 1,12 kg | [Datasheet PixelBrick V3](https://astera-led.com/wp-content/uploads/Datasheet_PixelBrick_V3.pdf) |
| Chauvet DJ Freedom Par H9 IP | in vendita | Ricetrasmettitore D-Fi (proprietario Chauvet) + ricevitore RF per telecomandi RFC / RFC-XL / FlareCon Air | n.d. | 9×10 W RGBAW+UV (6-in-1) | 50 W; 1258 lm; fascio 23°, campo 46° | IP54 | 2,1 kg | [Thomann IT](https://www.thomann.it/chauvet_dj_freedom_par_h9_ip.htm) |
| ADJ Element HEXIP | **fuori produzione** (lo dice la pagina ADJ) | WiFLY EXR (proprietario ADJ), più telecomandi IR UC-IR / Airstream IR | fino a 760 m (2500 ft) con il WiFLY EXR Battery Transceiver | 4×10 W RGBAW+UV | 45 W; fascio 20°; PWM 1000 Hz | IP54 | 2,9 kg | [ADJ](https://www.adj.com/products/element-hexip) |
| Prolights Smart BatPlus G2 | in vendita | LumenRadio TiMo FX RDM integrato (compatibile CRMX e W-DMX) | n.d. | 4×20 W RGB + bianco caldo, CRI 94/92, CCT 2800–10.000 K | 2051 lm | IP65 "per uso esterno temporaneo" | 5,7 kg | [Music & Lights](https://musiclights.it/en/product/SMARTBATPLUSG2) |
| BeamZ Pro Helios | in vendita (Sudafrica) | n.d. sulla pagina del rivenditore; il kit "Helios ... Battery - WDMX" compare su un altro rivenditore | n.d. | 6×15 W RGBWA-UV | n.d. | IP65 | n.d. | [Bounce Online](https://www.bounceonline.co.za/?p=347373); [Surplustronics](https://surplustronics.co.nz/products/12786-helios-multifunctional-outdoor-uplight-kit-battery-wdmx) |

**Altri prodotti di cui è confermata solo l'esistenza (dal titolo della pagina o dal risultato di ricerca, scheda non letta)**
- Astera AX9 PowerPAR, Titan Tube, HydraPanel: hanno datasheet pubblici — [HydraPanel Datasheet V4](https://astera-led.com/wp-content/uploads/Datasheet_HydraPanel_V4.pdf), [Panavision AX9](https://www.panavision.com/lighting/lighting-products/heads/product-detail/xoon4a5-ax9-powerpar). Hanno anche registrazioni FCC con prefisso X55: X55AX9, X55AX5, X55PB15, X55FP6 (HydraPanel) — [fccid.io X55AX9](https://fccid.io/X55AX9). La pagina FCC non si è caricata, quindi foto interne e antenna restano non verificate.
- Chauvet DJ Freedom Flex H9 IP (in pacchi da 6) — [B&H](https://www.bhphotovideo.com/c/product/1757884-REG/chauvet_dj_freedomflexh9ipx6_freedom_flex_h9_ip.html).
- ADJ WiFLY EXR HEX5 IP: par a batteria, wireless DMX, uso esterno — [ADJ](https://www.adj.com/products/wifly-exr-hex5-ip).
- Prolights: altre varianti della famiglia Smart Bat (SMARTBATIP, SMARTBATHEX, Smart BatWash) — [Music & Lights SMARTBATIP](https://www.musiclights.it/en/product/SMARTBATIP).
- Cloni cinesi (Shehds e altri marchi): uplight a batteria 6×18 W o 12×18 W RGBWA+UV, venduti come "WLAN/Wi-Fi APP + DMX wireless" — [Alibaba Shehds](https://www.alibaba.com/product-introduction/Shehds-Wireless-Remote-Control-Wifi-APP_1601418330969.html); [eBay.de](https://www.ebay.de/itm/146478065496). Marconi SIRIUS 6×18 W RGBWA+UV IP65 a batteria — [SoundStoreXL](https://www.soundstorexl.com/products/marconi-sirius-6x18w-rgbwa-uv-ip65-battery-lamp).
- Fascia consumer/smart-home con Zigbee 3.0 integrato: Milight Zigbee 3.0 RGBW, proiettori IP65 da 30/50/100 W — [Galaxus](https://www.galaxus.ch/en/s14/product/milight-zigbee-30-rgbw-wireless-professional-led-floodlight-100w-10000-lm-ip65-outdoor-wall-lamp-49063277). Paulmann Kikolo, applique Zigbee 3.0 RGBW IP65 da 6,2 W, plastica e alluminio — [Paulmann](https://en.paulmann.com/p/led-exterior-wall-luminaire-smart-home-zigbee-3.0-kikolo-rgbw-ip65-90mm-rgbw-6-2w-440lm-230v-anthracite-plastic-aluminium/94773).
- Casambi pubblica una design guide "Outdoor" per produttori di apparecchi da esterno (prodotti Casambi Ready). Cita ripetitori IP e nodi Zhaga/NEMA IP66 IK09 — [Casambi DG Outdoor V2.1](https://casambi.com/wp-content/uploads/2023/11/Casambi_DG_Outdoor_V2.1.pdf).

**Architetturale permanente: radio esterna, non integrata**
- Progetto Nordyke & Marmon, Indianapolis (articolo del 2012). Due Color Kinetics ColorReach e 192 apparecchi Solid State Lighting in una fontana erano pilotati via radio con box esterni **LumenRadio CRMX Outdoor Flex** (trasmettitore, ripetitore e ricevitore alimentati PoE, antenne omni). I 40 ColorGraze erano invece cablati a un Pharos LPC4. Secondo l'integratore, il sistema "behaves just like a wired rig" — [LSi Online](https://lsionline.co.uk/news/lumenradio-brightens-indianapolis-skyline-1d7dec).

### Inferences
- Nei gruppi verificati, i prodotti "seri" (Astera, Prolights) integrano un modulo **LumenRadio** con licenza. Quelli DJ/fascia media (Chauvet, ADJ) usano un protocollo proprietario che funziona solo con la radio dello stesso marchio. Nessun prodotto verificato usa una mesh tra apparecchi stile ESP-NOW: sono tutti in topologia a stella da un trasmettitore. Una mesh apparecchio-apparecchio sarebbe quindi un elemento di differenziazione per facciate e ponti lunghi.
- Nessun prodotto verificato è un apparecchio architetturale **alimentato da rete con IP66/IP67 e radio integrata** per installazione permanente. I prodotti a batteria arrivano al massimo a IP65, spesso "temporaneo", e lavorano tra 0 e 40/45 °C, quindi non sono adatti a una facciata in inverno.

### Gaps
- Non verificati in questa sessione, quindi da controllare: Showtec, Cameo Droplet/Zenit, Elation (SixBar, KL), Ayrton, Robe, Martin ELP, Anolis, Wever & Ducré, Lumenpulse, Ketra, varianti wireless di Color Kinetics. Lo stesso vale per eventuali proiettori RGB solari da esterno. Non ho trovato fonti primarie sulla loro radio integrata entro il budget di ricerca. Non va dato per scontato che esistano versioni con radio integrata.
- Chauvet "WELL Fit" e Astera Titan/HydraPanel/AX9: specifiche radio, batteria e IP non estratte (datasheet AX9 non raggiungibile).

## Antenna, portata, latenza, sincronizzazione, app e integrazione DMX

### Takeaway
I produttori non dichiarano quasi mai dove sta l'antenna. L'unica fonte tecnica solida è la guida OEM di LumenRadio. Dice che un'antenna interna vicino a parti metalliche a massa degrada molto il segnale, che conviene portarla in alto nel prodotto, e che un errore di polarizzazione di 90° dimezza il segnale ricevuto. Latenza CRMX: 5 ms fissi. Portate dichiarate: 300 m (Astera CRMX) e 760 m (ADJ WiFLY EXR con transceiver dedicato).

### Cited Findings
- Guida OEM CRMX — [LumenRadio CRMX OEM guide](https://dl.lumenradio.com/guides/crmx/oem/crmx-oem-guide_b.pdf):
  - Le antenne a stilo interne sono spesso vicino a piani a massa (parti metalliche dell'involucro) e questo "can significantly degrade" il segnale.
  - Caso reale: in un uplighter l'antenna era schermata dal corpo stesso dell'apparecchio e dal muro. È stato risolto spostandola più in alto nel prodotto.
  - Pro dell'antenna interna: meno ingombro, estetica pulita. Contro: polarizzazione non regolabile, degrado vicino al metallo, impossibile montare un'antenna con più guadagno.
  - Connettori consigliati: N-type per installazioni permanenti e da esterno, RP-TNC per touring. RP-SMA sconsigliato nei nuovi progetti.
  - Il modulo non ha antenna a bordo. Le chip antenna di terze parti vanno qualificate da LumenRadio.
  - Polarizzazione: 90° di differenza tra le antenne possono costare il 50% del segnale ricevuto. Meglio prevedere un orientamento regolabile dall'utente.
  - Conviene la linea di vista e l'antenna il più in alto possibile, perché l'energia RF vicino al suolo viene assorbita.
  - Dati tecnici: banda 2402–2480 MHz; frequency hopping a 1562 Hz con "cognitive coexistence"; potenza 10/35/100/300 mW (300 mW solo USA/Canada); sensibilità −96 dBm @ 0,1% PER; latenza fissa 5 ms; recupero dopo perdita di segnale 1 s.
  - Obblighi di integrazione: tasto link e LED di stato obbligatori; approvazione del progetto da parte di LumenRadio; FCC ID del modulo (XRSCRMXNOVA101) riportato sul prodotto. Va usato il nome "CRMX", non "W-DMX". Ingresso massimo 12,0 V: attenzione ai pacchi Li-ion "12 V" che dopo la carica superano i 13 V.
- Astera AX5 e PixelBrick: CRMX/UHF fino a 300 m, Bluetooth fino a 3 m. Il Bluetooth serve per configurare via app tramite BluetoothBridge. Restano DMX via cavo e IR. Il datasheet non dice nulla sull'antenna — [Datasheet AX5](https://astera-led.com/wp-content/uploads/AX5_TriplePar_Datasheet_V3.pdf); [Datasheet PixelBrick](https://astera-led.com/wp-content/uploads/Datasheet_PixelBrick_V3.pdf).
- ADJ Element HEXIP: WiFLY EXR fino a 760 m con il transceiver ADJ; 5 modi DMX (6/7/8/11/12 canali); nessuna app — [ADJ](https://www.adj.com/products/element-hexip).
- Chauvet Freedom Par H9 IP: D-Fi integrato, DMX a 6/8/16 canali, telecomandi RF. Frequenza e portata non indicate da Thomann — [Thomann IT](https://www.thomann.it/chauvet_dj_freedom_par_h9_ip.htm).
- Prolights Smart BatPlus G2: TiMo FX con RDM, compatibile CRMX e W-DMX. Il CCT ha un canale DMX dedicato — [Music & Lights](https://musiclights.it/en/product/SMARTBATPLUSG2).
- Progetto architetturale (Indianapolis): portata estesa con un ripetitore CRMX e antenne omni −6 dB; alimentazione PoE — [LSi Online](https://lsionline.co.uk/news/lumenradio-brightens-indianapolis-skyline-1d7dec).
- Casambi: la portata si estende con ripetitori; ci sono ripetitori IP per esterno. La guida Outdoor non dà regole sul posizionamento dell'antenna — [Casambi DG Outdoor](https://casambi.com/wp-content/uploads/2023/11/Casambi_DG_Outdoor_V2.1.pdf).

### Inferences
- Per un corpo in alluminio pressofuso da facciata, la strada indicata da LumenRadio è un'antenna esterna con connettore N-type, oppure una finestra non metallica posta in alto e lontana dal muro. Il caso dell'uplighter a ridosso del muro è proprio la situazione di un proiettore da facciata. Lo stesso vale per un ESP32-C5: o antenna esterna/connettorizzata, o finestra in policarbonato/vetro lontana dalla massa.
- Nessuno dei concorrenti verificati dichiara un sincronismo "di rete" tra apparecchi oltre al DMX in stella. La sincronizzazione nasce dal fatto che tutti ricevono lo stesso universo, con latenza fissa (5 ms nel CRMX). Con ESP-NOW in mesh, la latenza cresce a ogni salto e va gestita, ad esempio con timestamp o con un frame sincrono.

### Gaps
- Antenna di Astera, Chauvet, ADJ e Prolights (interna o esterna, posizione): nessun manuale consultato la descrive. Le foto interne FCC (X55AX5, X55PB15, X55AX9) non erano raggiungibili.
- Latenza e portata reali di D-Fi e WiFLY: nessuna misura indipendente trovata.

## Costruzione: corpo, IP, batteria, ricarica, peso, temperature

### Takeaway
Corpi in alluminio (Astera AX5, Prolights G2 in pressofusione), IP54–IP65, pesi tra 1,1 e 5,7 kg. Autonomia dichiarata 12–20 h, ricarica in 4–5 h, temperature di esercizio 0–40/45 °C.

### Cited Findings

| Prodotto | Corpo | Batteria | Autonomia | Ricarica | Temp. esercizio | Dimensioni |
|---|---|---|---|---|---|---|
| Astera AX5 | alluminio | n.d. (70% dopo 300 cicli) | fino a 20 h | 5 h; ingresso AC 90–264 V, powerCON TRUE1 IN/OUT | 0–40 °C | Ø153 × 140,5 mm (senza staffa) |
| Astera PixelBrick | n.d. | n.d. (70% dopo 300 cicli) | fino a 20 h | 24 VDC 0,8 A; valigia di ricarica PB15-CHRCSE, PowerBox | 0–40 °C | 91 × 91 × 94 mm |
| Prolights Smart BatPlus G2 | alluminio pressofuso, cover intercambiabili | Li removibile 21,6 V (capacità n.d.) | 3/6/8/12/16/18 h selezionabili | max 4 h in flight case, AC e DC | 0–45 °C | 192 × 188 × 192 mm |
| ADJ Element HEXIP | n.d. | Li fissa 11,1 V, 6,6 Ah, 73,26 Wh, 9 celle, 0,42 kg | fino a 16 h (un colore, risparmio attivo) | circa 4,5 h, IEC 100–240 V | n.d. | 144 × 144 × 194,5 mm |
| Chauvet Freedom Par H9 IP | n.d. | n.d. | fino a 12 h | n.d. (ingresso 24 VDC) | n.d. | 120 × 120 × 126 mm |

Fonti: [Astera AX5](https://astera-led.com/wp-content/uploads/AX5_TriplePar_Datasheet_V3.pdf), [Astera PixelBrick](https://astera-led.com/wp-content/uploads/Datasheet_PixelBrick_V3.pdf), [Prolights G2](https://musiclights.it/en/product/SMARTBATPLUSG2), [ADJ Element HEXIP](https://www.adj.com/products/element-hexip), [Thomann Chauvet](https://www.thomann.it/chauvet_dj_freedom_par_h9_ip.htm).

- ADJ Element HEXIP: il pannello menu DMX sul retro ha uno sportello resistente all'acqua; ha cavalletto integrato; certificazioni cETLus e CE — [ADJ](https://www.adj.com/products/element-hexip).
- Prolights G2: IP65 dichiarato espressamente "for temporary outdoor use"; la ricarica da rete si può disattivare via software — [Music & Lights](https://musiclights.it/en/product/SMARTBATPLUSG2).

### Inferences
- Il limite inferiore di 0 °C (Astera, Prolights) esclude l'uso permanente in esterno d'inverno in Nord Italia. Un apparecchio Versus Lux alimentato da rete, IP66/67, tra −20 e +50 °C, coprirebbe un caso d'uso che i prodotti a batteria non coprono.

### Gaps
- Capacità in Wh delle batterie Astera e Chauvet: non dichiarata nei documenti consultati.

## Luce, mix colore, potenza, ottiche

### Takeaway
Gli uplight a batteria stanno tra 400 e 2000 lm circa. Il mix va da RGBAW+UV (DJ) a RGBMA o RGB+bianco caldo calibrato con CRI alto (Astera, Prolights). Fasci stretti da 13° a 23°, con filtri per allargarli.

### Cited Findings
- Astera AX5: RGBAW, 45 W, 1080–1413 lm, 13°/26°, filtri FloodFilter 32° e WallwashFilter 17°×46°, strobo 0–25 Hz — [Datasheet](https://astera-led.com/wp-content/uploads/AX5_TriplePar_Datasheet_V3.pdf).
- Astera PixelBrick: RGBMA (Mint + Amber), CRI ≥96, 395–475 lm, 13°/25°, FloodFilter 30° — [Datasheet](https://astera-led.com/wp-content/uploads/Datasheet_PixelBrick_V3.pdf).
- Prolights G2: RGB + bianco caldo, 2051 lm, 1723 lx a 5 m, TM30 Rf 93/91 — [Music & Lights](https://musiclights.it/en/product/SMARTBATPLUSG2).
- Chauvet Freedom Par H9 IP: RGBAW+UV, 1258 lm, 23°/46°, diffusore magnetico — [Thomann](https://www.thomann.it/chauvet_dj_freedom_par_h9_ip.htm).
- ADJ Element HEXIP: RGBAW+UV 4×10 W, 20°, 63 macro colore — [ADJ](https://www.adj.com/products/element-hexip).

### Inferences
- Un apparecchio da facciata a 5 canali (RGB+W+A o RGB+CW+WW) da rete potrebbe superare facilmente questi flussi, che sono limitati dalla batteria. Il benchmark utile sul flusso sono i proiettori architetturali cablati (Color Kinetics ColorReach/Vaya, per esempio [Vaya Flood HP G4](https://www.colorkinetics.com/global/products/vaya/flood-hp-g4)), non gli uplight a batteria.

### Gaps
- Flussi e ottiche di Astera AX9/Titan/HydraPanel non estratti.

## Prezzi (al dettaglio / prezzo di strada)

### Takeaway
Fascia DJ: circa 444 € per apparecchio (Chauvet). Fascia pro Astera: circa 700 € ex IVA per AX5 (in kit da 8) e circa 309 € ex IVA per PixelBrick (in kit da 8). Fascia sudafricana BeamZ: 9375 ZAR.

### Cited Findings

| Prodotto | Prezzo | IVA | Fonte | Data consultazione |
|---|---|---|---|---|
| Chauvet DJ Freedom Par H9 IP (1 pz) | 444 € | IVA inclusa | [Thomann IT](https://www.thomann.it/chauvet_dj_freedom_par_h9_ip.htm) | 08/11/2026 |
| Astera AX5 TriplePAR, kit 8 pz + valigia di ricarica | 5587 € ex IVA / 6705 € IVA incl. (circa 698 € per apparecchio ex IVA, calcolato) | entrambi indicati | [Stage Experts](https://stage-experts.com/products/stage22-astera-ax5-triplepar-package-of-8-in-charging-case) | 08/11/2026 |
| Astera PixelBrick PB15, kit 8 pz + valigia | 2472 € ex IVA (in offerta; prezzo pieno barrato 2967 € IVA incl.); la pagina riporta disponibilità contraddittoria | ex IVA | [Stage Experts](https://stage-experts.com/products/stage22-astera-pixelbrick-pb15-8er-set-15w-rgbma-13-ip65-crmx-btb) | 08/11/2026 |
| BeamZ Pro Helios 6×15 W RGBWA-UV IP65 | 9375 ZAR | n.d. | [Bounce Online](https://www.bounceonline.co.za/?p=347373) | 08/11/2026 |

### Inferences
- Il costo per apparecchio di Astera, circa 700 € ex IVA, comprende batteria, valigia e licenza CRMX. Un apparecchio da rete con ESP32-C5 (modulo da pochi euro, senza royalty) ha un margine di costo potenzialmente ampio rispetto a CRMX. Questa stima non è supportata da una fonte di costo.

### Gaps
- Prezzi di ADJ (Element HEXIP fuori produzione, WiFLY EXR HEX5 IP), Prolights G2, Shehds/Alibaba e Color Kinetics: non estratti.

## Limiti segnalati (portata, interferenze, affidabilità)

### Takeaway
Il problema principale riportato è la congestione dei 2,4 GHz: Wi-Fi, scanner dei biglietti e intercom possono non lasciare canali liberi. Si aggiungono l'incompatibilità tra protocolli di marchi diversi e il degrado del segnale dovuto al corpo metallico e alla vicinanza del muro.

### Cited Findings
- Secondo Learn Stage Lighting:
  - Il wireless DMX a 2,4 GHz può perdere il segnale in ambienti affollati di Wi-Fi. Viene citato un locale in cui Wi-Fi, scanner dei biglietti e altre reti non lasciavano canali liberi; anche intercom e router dello show andavano in crisi.
  - "it doesn't matter if you have the fanciest, most expensive wireless DMX" se non c'è una frequenza libera.
  - Ogni marchio usa un proprio metodo, quindi i prodotti di marchi diversi non dialogano.
  - Consigli: tenere un cavo DMX di riserva e prevedere un look statico di fallback se si perde il controllo.
  - [Learn Stage Lighting](https://www.learnstagelighting.com/blog/should-i-use-wireless-dmx-the-complete-guide-to-running-data-to-your-lights-wirelessly)
- LumenRadio documenta un caso di uplighter con antenna schermata dal proprio corpo e dal muro — [CRMX OEM guide](https://dl.lumenradio.com/guides/crmx/oem/crmx-oem-guide_b.pdf).
- Sul forum ADJ esiste un thread dedicato ai problemi WiFLEX ("wiflex issues"); il contenuto non è stato letto — [ADJ forum](https://forums.adj.com/topic/wiflex-issues).

### Inferences
- Per facciate e ponti in città, il firmware ESP-NOW dovrebbe prevedere:
  - salto di canale o scelta automatica del canale meno occupato (quello che CRMX fa con la "cognitive coexistence");
  - comportamento sicuro alla perdita del segnale: mantenere l'ultima scena o eseguire uno show locale;
  - un tempo di recupero comparabile a 1 s.

### Gaps
- Nessuna recensione indipendente con misure di portata reale su Astera, Chauvet D-Fi o ADJ WiFLY. Thread di ControlBooth, Reddit e PLSN non letti entro il budget di ricerca.
