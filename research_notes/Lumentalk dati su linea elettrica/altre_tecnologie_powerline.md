# Altre tecnologie "dati su linea elettrica" (PLC) per illuminazione architetturale RGB, esclusa Lumentalk

Note di ricerca a cura di un sottoagente, 8 novembre 2026. Lumentalk (Lumenpulse) è trattata da un altro ricercatore e qui viene solo citata. Ogni affermazione ha la sua fonte; le deduzioni stanno nelle sezioni "Inferenze". Le fonti sono pagine di produttori, distributori e articoli tecnici consultate il 2026-11-08.

---

## 1. Sistemi commerciali: come viaggiano i dati sul cavo di potenza

### Takeaway
L'unico ecosistema architetturale maturo comparabile a Lumentalk è **Signify Color Kinetics Powercore + IntelliPower** (Data Enabler Pro). Usa onde convogliate (PLC) su cavo di rete 100-277 VAC, fino a 63 ricevitori per ramo e 150 m di linea. Il resto del mercato sono convertitori **DMX-over-Powerline** per spettacolo (GLP DoP, Sundrax PowerGate), che usano PLC a banda larga di tipo HomePlug, e moduli/chip per **DMX su bus DC** (Yamar, Saleconix). Lo streetlighting usa PLC a banda stretta (LonWorks, G3-PLC), che però è troppo lento per effetti dinamici.

### Cited Findings

**Signify Color Kinetics: Powercore / IntelliPower / Data Enabler**
- La funzione dati-su-potenza di Color Kinetics si chiama **IntelliPower** e applica la tecnologia power line carrier (PLC). Powercore indica invece la gestione della potenza nell'apparecchio. — [CK IntelliPower overview](https://www.docs.colorkinetics.com/learn/color-kinetics-intellipower-overview.pdf)
- Il Data Enabler fonde l'alimentazione di rete "2+terra" con i dati DMX o Ethernet e li porta su un normale cablaggio 2+terra. Un **Data Receiver** converte il segnale in 3+terra (linea, neutro, terra, dati) per gli apparecchi Powercore. — [CK IntelliPower overview](https://www.docs.colorkinetics.com/learn/color-kinetics-intellipower-overview.pdf)
- Filtri dati opzionali a monte e a valle riducono il rumore elettrico; se servono lo stabilisce un sopralluogo. — [CK IntelliPower overview](https://www.docs.colorkinetics.com/learn/color-kinetics-intellipower-overview.pdf)
- Su un ramo elettrico stanno **fino a 63 Data Receiver**, limite dato da integrità dei dati e capacità del circuito; di norma c'è un Data Enabler per ramo. — [CK IntelliPower overview](https://www.docs.colorkinetics.com/learn/color-kinetics-intellipower-overview.pdf)
- Distanza dal Data Enabler all'ultimo Data Receiver: **150 m fuori terra, 90 m interrata** (variabile con profondità e stato del cavo). La distanza tra quadro elettrico e Data Enabler non incide. — [CK IntelliPower overview](https://www.docs.colorkinetics.com/learn/color-kinetics-intellipower-overview.pdf)
- Il documento definisce IntelliPower "high-bandwidth", adatto a effetti colore, light show e video, ma **non dà una velocità dati in bit/s**. Protocolli: DMX ed Ethernet (i controller Ethernet di terze parti devono supportare KiNET). — [CK IntelliPower overview](https://www.docs.colorkinetics.com/learn/color-kinetics-intellipower-overview.pdf)
- **Data Enabler Pro** (ZCX400): ingresso 100-277 VAC autorange 50/60 Hz, carico massimo 16 A, consumo massimo 20 W, IP66, funzionamento da -40 a 50 °C. Fonde tensione di linea e dati su un unico cavo a 4 fili verso gli apparecchi Powercore; ha anche uscite DMX ed Ethernet. Item 106-000004-01. — [Data Enabler Pro spec sheet](https://www.docs.colorkinetics.com/support/datasheets/Data_Enabler_Pro_SpecSheet.pdf)
- Il sito Color Kinetics elenca anche un "Data Enabler Pro gen3". — [CK Data Enabler Pro gen3](https://www.colorkinetics.com/global/products/pds/dataenablerpro3) (pagina non letta nel dettaglio)

**DMX-over-Powerline per spettacolo/installazione**
- **GLP DoP Converter** (DIN rail / universal mount): il segnale DMX viene modulato sulla linea elettrica esistente, banda del segnale **4-28 MHz**, fino a **10 universi** sulla stessa linea, un universo per convertitore. Supporta DMX512-A, RDM (E1.20) e protocollo GLP DoP; alimentazione 85-305 VAC. Il convertitore deve stare sulla **stessa linea elettrica** degli apparecchi. Compatibile direttamente con la testa mobile GLP FR1 TM DoP. Fase e interruttori non sono menzionati. — [GLP DoP Converter DINrail](https://glp.de/en/products/glp-dop-converter-dinrail)
- **Sundrax PowerGate** (DMX512 su rete 110/220 V): basato su una versione adattata di **HomePlug 1.0**, OFDM, cifratura AES-128 end-to-end, 1 o 4 universi per dispositivo, da 1 a 256 ricevitori per trasmettitore, fino a 256 gruppi. La versione Arma per esterni è IP65 e lavora da -40 a +85 °C. I problemi dichiarati sono la qualità del cablaggio, le interferenze di caricabatterie e alimentatori e l'uso di fasi diverse. Il produttore ha aggiunto un sistema di sincronizzazione perché anche piccoli ritardi desincronizzano gli apparecchi. — [Sundrax, storia di PowerGate](https://entertainment.sundrax.com/blog/history-of-creation-power-gate-dmx-512-over-powerline-110-220)

**Streetlighting (PLC a banda stretta)**
- G3-PLC è usato nell'illuminazione connessa: Vattenfall (4 comuni svedesi), Panasonic (banchine ferroviarie a Tokyo), **HiMarc (illuminazione pubblica in Italia, ~99% di successo delle comunicazioni PLC)**, Enedis/Neuron (illuminazione stradale con DALI), ferrovie italiane (luci di sicurezza in galleria). Il tempo di andata e ritorno richiesta/risposta è di circa **250 ms**. Esiste **G3-Hybrid**, che combina PLC e RF sub-GHz (863-870 MHz in Europa) in un'unica rete mesh con scelta automatica del canale. — [G3-PLC Alliance, connected lighting](https://g3-alliance.com/download/120/applications/3405/g3-alliance-and-g3-hybrid-for-connected-lighting-systems.pdf)
- Esempio Analog/Maxim: 1000 lampioni a 80 m di passo (80 km di linea). Il messaggio punto-punto richiede ~0,017 s per ~180 byte; il polling di tutti i nodi ~588 s (circa 10 minuti); un broadcast raggiunge tutte le lampade in meno di 0,2 s. — [Analog Devices, PLC for street lighting](https://www.analog.com/en/resources/technical-articles/powerline-communications-for-street-lighting-automation.html)
- LonWorks/Echelon PL-20 (chip PL3120, oggi Renesas): **5,4 kbit/s** lordi in banda CENELEC C e 3,6 kbit/s in banda A, a doppia portante (132/115 kHz in C, 86/75 kHz in A), standard ISO/IEC 14908-3. Il prodotto è "Not Recommended for New Designs". — [Renesas PL3120](https://www.renesas.com/en/products/pl3120)

### Inferenze
- *(Inferenza)* Powercore/IntelliPower è il diretto concorrente del concetto "solo potenza cablata" di Versus Lux. Il limite di 63 nodi e 150 m per ramo, con un Data Enabler costoso per ramo, fissa la scala di riferimento: per un ponte di 300 m servirebbero almeno 2 rami e 2 Data Enabler.
- *(Inferenza)* La banda 4-28 MHz di GLP DoP e la base HomePlug 1.0 di PowerGate indicano che il DMX-over-powerline "da spettacolo" usa **PLC a banda larga** (Mbit/s), non i kbit/s della banda stretta CENELEC. Solo la banda larga regge DMX completo a ~44 Hz.
- *(Inferenza)* I sistemi stradali (LonWorks, G3-PLC) sono progettati per telegestione (accendi/dimmera/diagnostica) con latenze di centinaia di ms e polling di minuti, quindi **non adatti** a effetti dinamici RGB sincronizzati.

### Gaps
- Velocità dati, banda di frequenza e chip di IntelliPower/Powercore non sono pubblicati nei documenti consultati. Nessuna informazione trovata su una "Powercore gen2" specifica né su "Chromasic" (che sembra un ASIC LED di Color Kinetics, non una tecnologia PLC: non verificato).
- Nessuna fonte trovata su prodotti powerline di Traxon/e:cue (la ricerca ha restituito solo nodi pixel e:cue Sympl Pixel Node, non PLC).
- Nessuna fonte affidabile consultata sui controller "PLC DMX" di produttori cinesi (es. moduli DMX-PLC su AliExpress), né su Schréder Owlet PLC (Owlet oggi è soprattutto radio) o Telensa (radio UNB, non PLC: dato da verificare).
- KNX PL110: la pagina Renesas cita solo il nome "PL110", senza specifiche. I valori noti in letteratura (110 kHz, ~1200 bit/s, S-FSK) **non sono stati verificati** con una fonte in questa sessione.
- DALI su powerline: non trovata documentazione specifica, salvo il caso Enedis/Neuron "street lighting with DALI protocol" su G3-PLC citato sopra.

---

## 2. Standard e chip: bande, throughput, latenza, robustezza

### Takeaway
Si distinguono due mondi. La **banda stretta** (3-148,5 kHz CENELEC; fino a ~500 kHz per G3/PRIME/IEEE 1901.2) va da pochi kbit/s a qualche centinaio di kbit/s ed è robusta su lunghe distanze. La **banda larga** (2-30 MHz: HomePlug AV/GreenPHY, IEEE 1901) arriva a Mbit/s ma soffre più attenuazione e diramazioni. Il rumore degli alimentatori switching LED dipende soprattutto dalla qualità del loro filtro EMI.

### Cited Findings

**Bande CENELEC (EN 50065-1)**
- Banda **A 3-95 kHz** riservata ai distributori di energia; bande **B 95-125 kHz, C 125-140 kHz, D 140-148,5 kHz** solo per installazioni degli utenti. La banda C richiede accesso al mezzo **CSMA/CA**. Norma emessa la prima volta nel 1992. Per 150-500 kHz non c'è norma armonizzata (IEEE 1901.2 fissa i limiti). — [Galli et al., arXiv 1602.09019](https://arxiv.org/pdf/1602.09019)
- La PLC a banda stretta ad alta velocità (PRIME, G3-PLC, IEEE 1901.2) opera in 3-500 kHz con "decine o centinaia di kbit/s"; le specifiche industriali più vecchie arrivano a pochi kbit/s. — [arXiv 1602.09019](https://arxiv.org/pdf/1602.09019)
- La PLC a banda larga va da 1,8 a 100 MHz; IEEE 1901 (2010) usa 2-30 MHz, con estensione opzionale a 50 MHz. HomePlug Green PHY è un sottoinsieme di HomePlug AV a basso consumo e basso costo. — [arXiv 1602.09019](https://arxiv.org/pdf/1602.09019)

**Tabella chip / standard**

| Chip / standard | Tipo | Banda | Velocità dichiarata | Note | Fonte |
|---|---|---|---|---|---|
| ST **ST7580** | Banda stretta, FSK/PSK | portante programmabile fino a 250 kHz; conforme EN 50065, FCC Part 15, ARIB | B-FSK 9,6 kbit/s; B/Q/8-PSK fino a 28,8 kbit/s | amplificatore 8-18 V, 1 A RMS, 14 Vpp; UART host 57,6 kbit/s; prezzo non pubblicato | [ST](https://www.st.com/en/product/st7580.html) |
| Renesas (ex Echelon) **PL3120** | LonWorks PL-20 | CENELEC A e C, doppia portante | 5,4 kbit/s (C), 3,6 kbit/s (A) | NRND | [Renesas](https://www.renesas.com/en/products/pl3120) |
| Maxim/ADI **MAX2992** | G3-PLC / IEEE P1901.2 | FCC 10-487,5 kHz | fino a 300 kbit/s (D8PSK), ~150 kbit/s tipici in DQPSK attraverso trasformatori/lunghe distanze; robust mode fino a SNR -1 dB | NRND | [Analog Devices](https://www.analog.com/en/resources/technical-articles/powerline-communications-for-street-lighting-automation.html) |
| Renesas **R9A06G037** | G3-PLC, OFDM | CENELEC A/B/C, FCC, ARIB | "fino a 250 KB/s" (dichiarato) | usato per demo KNX su PLC | [Renesas KNX PLC](https://www.renesas.com/cn/en/solutions/building-automation/connectivity/plc/knx-plc.html) |
| Qualcomm **QCA7000** | HomePlug Green PHY (banda larga) | (2-30 MHz secondo lo standard HomePlug, non dichiarato nel brief) | 4-10 Mbit/s PHY in modalità ROBO (OFDM robusto) | SPI slave/UART; 3,3 V; funziona su 240/120/24 VAC e linee DC | [QCA7000 product brief](https://content.payda.krakow.pl/fileadmin/media/download/datasheets/powerline-communication/plc-homeplug-green-phy/qualcomm_qca7000-product-brief.pdf) |
| Yamar **DMX250** | PLC su DC (e AC con interfaccia esterna) | 251 portanti selezionabili | 250 kbit/s (velocità DMX nativa) | fino a 8 universi DMX in parallelo su frequenze diverse; accoppiamento a linea DC con un solo condensatore | [Yamar DMX250](https://yamar.com/product/dmx250) |
| Yamar **DCB1M** | PLC su DC, PSK | n.d. | 225 kbit/s - 1,4 Mbit/s | UART, SPI, DMX512/RDM, I2C | [DigiKey DCB1M-IC](https://www.digikey.com/en/products/detail/yamar/DCB1M-IC/19525704); [Yamar](https://yamar.com/led-lighting-control-over-dc-powerline/) |
| Yamar SIG102 / SIG100 / SIG60 / DCAN500 | PLC su DC, UART/LIN/CAN | n.d. | n.d. | SIG102 consigliato per comando LED; SIG60 EOL | [Yamar](https://yamar.com/led-lighting-control-over-dc-powerline/) |

- Nota di affidabilità: la pagina prodotto Qualcomm QCA7000 riportava nei metadati "fino a 1200 Mbps", in **contraddizione** con il product brief (4-10 Mbit/s ROBO, coerente con Green PHY). Il primo dato è da considerare errato o riferito ad altra famiglia. — [Qualcomm QCA7000](https://www.qualcomm.com/networking-infrastructure/products/qca7000) vs [product brief](https://content.payda.krakow.pl/fileadmin/media/download/datasheets/powerline-communication/plc-homeplug-green-phy/qualcomm_qca7000-product-brief.pdf)

**Robustezza, rumore LED, attenuazione**
- L'attenuazione varia con la frequenza; le diramazioni della linea dividono il segnale e riducono la portata. Il rumore è dinamico (alimentatori switching, motori, carichi che si accendono/spengono). Il tone mapping adattivo evita le sottobande rumorose. Il sistema per gallerie TLACS supporta cavi fino a 3 km. — [Analog Devices](https://www.analog.com/en/resources/technical-articles/powerline-communications-for-street-lighting-automation.html)
- Su lampade LED misurate con LISN: il rumore dipende soprattutto dalla **qualità del filtro EMI**, non dalla potenza. Una lampada da 1,2 W faceva più rumore di una da 10 W; quelle senza filtro adeguato generavano rumore "di ordini di grandezza" maggiore; due lampade su sette erano vicine o oltre il limite EN 55015. Le frequenze di commutazione tipiche (~40-54 kHz) cadono con le armoniche (80, 120 kHz) **dentro le bande CENELEC**. Gli autori suggeriscono di spostare la portante o la frequenza di commutazione del convertitore. — [Emleh et al., ASTESJ 2021](https://astesj.com/v06/i02/p106)
- Le reti medie tensione sono più attenuate per via dei cavi più lunghi. Lo studio non tratta il passaggio attraverso trasformatori. — [arXiv 1602.09019](https://arxiv.org/pdf/1602.09019)
- PLC funziona sotto terra, attraverso muri e angoli, non risente del meteo, non richiede linea di vista. — [G3-PLC Alliance](https://g3-alliance.com/download/120/applications/3405/g3-alliance-and-g3-hybrid-for-connected-lighting-systems.pdf)
- Fasi diverse in un impianto trifase possono interrompere la trasmissione (esperienza PowerGate). — [Sundrax](https://entertainment.sundrax.com/blog/history-of-creation-power-gate-dmx-512-over-powerline-110-220)

### Inferenze
Le stime di banda seguenti sono calcoli dell'autore, non da fonte. Ipotesi: apparecchio a 5 canali × 8 bit = 40 bit per aggiornamento, refresh 30 Hz, nessun overhead di protocollo (quindi ottimistiche).

| Tecnologia | Velocità lorda | Apparecchi 5 ch a 30 Hz (teorico, senza overhead) |
|---|---|---|
| LonWorks PL-20 (C) | 5,4 kbit/s | ~4 |
| ST7580 8-PSK | 28,8 kbit/s | ~24 |
| G3-PLC (FCC, DQPSK tipico) | ~150 kbit/s | ~125 (ma la banda FCC non è utilizzabile in UE: in CENELEC A la velocità è molto più bassa) |
| DMX nativo / Yamar DMX250 | 250 kbit/s | ~102 (un universo DMX da 512 canali a ~44 Hz) |
| HomePlug Green PHY | 4-10 Mbit/s PHY | migliaia (limite reale dato da latenza e jitter) |

- *(Inferenza)* In Europa, sulla rete a 230 VAC, la banda stretta conforme a EN 50065-1 (3-148,5 kHz) non basta per effetti dinamici fluidi su molti apparecchi. Gli effetti dinamici richiedono banda larga (MHz), come fanno GLP DoP e PowerGate, con i relativi vincoli EMC (sez. 4).
- *(Inferenza)* Gli alimentatori LED hanno condensatori X in ingresso e filtri EMI. Nella banda stretta (decine-centinaia di kHz) presentano bassa impedenza e "assorbono" il segnale; per questo Color Kinetics prevede filtri dati a monte e a valle. Il fenomeno è noto, ma in questa sessione **non ho trovato una misura quantitativa** dell'attenuazione dovuta ai condensatori dei driver.

### Gaps
- Velocità reali di PRIME e IEEE 1901.2 in banda CENELEC A (non FCC): non trovate nelle fonti lette.
- Chip Semtech, Microchip, Vertexcom, MaxLinear/Lantiq e Yitran IT700 non verificati in questa sessione.
- Latenza misurata e jitter di HomePlug/GreenPHY per streaming DMX: nessuna fonte trovata.
- Comportamento attraverso interruttori differenziali/magnetotermici: nessuna fonte specifica. GLP dice solo "stessa linea elettrica".

---

## 3. Alternative su bus DC (24/48 V) e PoE

### Takeaway
Esistono chip e moduli per DMX direttamente su bus DC. Yamar DMX250 (250 kbit/s, fino a 8 universi, accoppiamento con un condensatore, ~5-7,5 € al pezzo) e i moduli Saleconix (14-35 VDC, ~64 €) sono adatti a un'architettura "alimentatore + 2 fili" in cui i dati non passano dai driver AC. PoE è l'approccio opposto (dati con alimentazione su cavo dati).

### Cited Findings
- Yamar propone di controllare reti LED **sulla linea DC di alimentazione**, eliminando il cablaggio dati e il microcontrollore PWM del modulo LED (SIG102). I protocolli supportati sono DMX/RDM, UART e SPI. — [Yamar, LED control over DC powerline](https://yamar.com/led-lighting-control-over-dc-powerline/)
- DMX250: un solo condensatore accoppia il chip alla linea DC; con interfaccia esterna ad alta tensione funziona anche su AC; 250 kbit/s; fino a 8 universi DMX in parallelo su frequenze diverse. — [Yamar DMX250](https://yamar.com/product/dmx250)
- **Saleconix DMX512 DC Powerline Modem**: 14-35 VDC, portante 60 kHz, FSK con deviazione 1 kHz, configurabile trasmettitore/ricevitore, 1-8 canali RGB selezionabili, 0-70 °C, 44×66×17 mm, consumo 360-1200 mW. Velocità indicata "4800 Bd" ma anche "250 KBd" (contraddittorio sulla pagina). — [RobotShop EU](https://eu.robotshop.com/products/saleconix-dmx512-dc-powerline-modem)
- Il QCA7000 (Green PHY) dichiara funzionamento anche su linee 24 VAC e DC. — [QCA7000 product brief](https://content.payda.krakow.pl/fileadmin/media/download/datasheets/powerline-communication/plc-homeplug-green-phy/qualcomm_qca7000-product-brief.pdf)

### Inferenze
- *(Inferenza)* Con un'architettura "alimentatore 48 VDC centralizzato + bus DC agli apparecchi", la PLC su DC evita trasformatori, quadri, differenziali e altri carichi di rete. Il canale è più "pulito" e controllabile dal costruttore, perché i convertitori DC/DC degli apparecchi li progetta Versus Lux. Il prezzo è la caduta di tensione su lunghe tratte (facciate, ponti), che limita la lunghezza dei rami a 24/48 V.
- *(Inferenza)* La portante a 60 kHz con FSK (Saleconix) indica una velocità bassa (ordine di kbit/s), coerente con "4800 Bd". Il dato "250 KBd" si riferisce probabilmente all'interfaccia DMX lato cavo, non al canale powerline.

### Gaps
- Sistemi commerciali architetturali con dati su bus DC (es. Color Kinetics su DC, "SPI su DC" per strip pixel): nessuna fonte specifica trovata in questa sessione.
- PoE per illuminazione architetturale da esterno (costi, distanze 100 m): non approfondito.

---

## 4. Normativa EMC/CE, accoppiamento e costo del front-end PLC

### Takeaway
In Europa la PLC a banda stretta è regolata da **EN 50065-1** (3-148,5 kHz, con livelli e accesso al mezzo per banda). La banda larga in-home 1,6-30 MHz è regolata da **EN 50561-1** (notching e controllo dinamico della potenza obbligatori). Ogni nodo richiede un front-end di accoppiamento (condensatore + trasformatore/filtro su AC, o solo condensatore su DC). Il costo del chip va da ~5 € (Yamar) in su; per ST7580 e QCA7000 i prezzi non sono pubblicati.

### Cited Findings
- EN 50065-1: segnalazione su installazioni elettriche in bassa tensione da 3 kHz a 148,5 kHz, con requisiti generali, bande di frequenza e disturbi elettromagnetici. — [BSI](https://knowledge.bsigroup.com/products/signalling-on-low-voltage-electrical-installations-in-the-frequency-range-3-khz-to-148-5-khz-general-requirements-frequency-bands-and-electromagnetic-disturbances); edizione corrente DIN EN 50065-1 — [DIN Media](https://dinmedia.de/en/standard/din-en-50065-1/145750316)
- EN 50561-1 (approvata a novembre 2012): sistemi PLC in-home 1,6-30 MHz. Distingue porta di alimentazione, porta telecom e porta PLC, fissa tensioni massime e procedure di misura, e impone **controllo dinamico della potenza e notching statico e adattivo** delle bande (es. radioamatori). — [arXiv 1602.09019](https://arxiv.org/pdf/1602.09019)
- Il rumore condotto dalle lampade LED è regolato da EN 55015; alcune lampade commerciali misurate erano vicine o oltre il limite. — [ASTESJ 2021](https://astesj.com/v06/i02/p106)
- ST7580: amplificatore di linea integrato 1 A RMS / 14 Vpp, alimentato a 8-18 V. — [ST](https://www.st.com/en/product/st7580.html)
- Yamar DMX250: accoppiamento a DC con un solo condensatore; per AC serve un'interfaccia esterna ad alta tensione. — [Yamar DMX250](https://yamar.com/product/dmx250)

### Inferenze
- *(Inferenza)* Per un nodo AC a 230 V il BOM PLC include, oltre al chip: condensatore X di accoppiamento, trasformatore di accoppiamento/isolamento, filtro passa-banda, protezioni da sovratensione (TVS) e alimentazione 8-18 V per il driver di linea. Inoltre il driver LED dell'apparecchio va progettato per non attenuare la banda PLC (es. induttanza serie in ingresso). È una stima qualitativa: **non ho trovato un BOM di riferimento con prezzi**.
- *(Inferenza)* Un prodotto PLC a banda larga (stile GLP/PowerGate) deve dimostrare conformità a EN 50561-1 in aggiunta alle norme EMC dell'apparecchio. Per una piccola azienda è un onere di certificazione maggiore del radio a 2,4/5 GHz con modulo ESP32 già certificato (RED).

### Gaps
- Livelli d'uscita massimi in dBµV per banda di EN 50065-1: la norma è a pagamento, non letta.
- Prezzo budgetario ST7580 e QCA7000 non pubblicati (ST: "contattare vendite"). Nessuna fonte con prezzo trovata per un trasformatore di accoppiamento PLC.

---

## 5. Pro e contro rispetto alla mesh radio (ESP32-C5 / ESP-NOW) su facciate e ponti

### Takeaway
La PLC vince su facciate/ponti dove la radio ha problemi di propagazione (strutture in acciaio, distanze lunghe, nessuna linea di vista) e dove si vuole un canale "di proprietà" del cablaggio. Perde su banda disponibile in Europa (banda stretta), su dipendenza dalla qualità dell'impianto elettrico (fasi, carichi rumorosi, driver) e su costo per nodo e certificazione. Un **ibrido** (sul modello di G3-Hybrid, PLC + RF con scelta automatica) è una strada già standardizzata nello streetlighting.

### Cited Findings
- PLC: funziona sotto terra, tra muri e angoli, non dipende dal meteo né dalla linea di vista; l'operatore "possiede il canale". — [G3-PLC Alliance](https://g3-alliance.com/download/120/applications/3405/g3-alliance-and-g3-hybrid-for-connected-lighting-systems.pdf)
- G3-Hybrid combina PLC e RF con selezione automatica del canale; la modalità ibrida permette a più nodi di comunicare nella rete. — [G3-PLC Alliance](https://g3-alliance.com/download/120/applications/3405/g3-alliance-and-g3-hybrid-for-connected-lighting-systems.pdf)
- La PLC dipende dalla qualità del cablaggio e soffre interferenze da alimentatori e fasi diverse; servono meccanismi di sincronizzazione per evitare sfasamenti tra apparecchi. — [Sundrax](https://entertainment.sundrax.com/blog/history-of-creation-power-gate-dmx-512-over-powerline-110-220)
- Color Kinetics richiede un sopralluogo per decidere i filtri dati e limita a 63 nodi / 150 m per ramo. — [CK IntelliPower overview](https://www.docs.colorkinetics.com/learn/color-kinetics-intellipower-overview.pdf)
- Mesh PLC: tutto il traffico inoltrato condivide il link verso il concentratore, che diventa il collo di bottiglia. — [Analog Devices](https://www.analog.com/en/resources/technical-articles/powerline-communications-for-street-lighting-automation.html)
- Sicurezza: PowerGate usa AES-128 end-to-end. — [Sundrax](https://entertainment.sundrax.com/blog/history-of-creation-power-gate-dmx-512-over-powerline-110-220)

### Inferenze (tabella comparativa, giudizi dell'autore basati sulle fonti sopra)

| Criterio | PLC banda stretta (CENELEC) | PLC banda larga (HomePlug/GLP) | PLC su bus DC (Yamar) | Mesh radio ESP32-C5/ESP-NOW |
|---|---|---|---|---|
| Banda per effetti dinamici / pixel mapping | Insufficiente (kbit/s) | Ampia (Mbit/s) | ~DMX (250 kbit/s, fino a 8 universi) | Ampia, ma condivisa e soggetta a interferenze 2,4/5 GHz |
| Dipendenza dall'impianto | Alta (driver, carichi, fasi) | Alta (attenuazione, diramazioni, fasi) | Bassa (bus controllato dal costruttore) | Nessuna sull'impianto; dipende dalla propagazione |
| Ponti in acciaio / retrofit senza linea di vista | Buona | Media | Buona | Critica (riflessioni, schermature) |
| Installazione | Nessun cavo dati; servono sopralluogo e filtri | Come a sinistra; serve "stessa linea" | Serve alimentazione DC centralizzata | Nessun cavo dati; serve pianificazione RF |
| Certificazione | EN 50065-1 | EN 50561-1 + notching | EMC dell'apparecchio (bus DC interno) | RED (moduli pre-certificati) |
| Costo nodo (solo comunicazione) | chip + accoppiamento AC (n.d.) | chip GreenPHY + AFE (n.d.) | ~5-7,5 € chip DMX250 | modulo ESP32-C5 (n.d. qui) |

- *(Inferenza)* Ibrido sensato per Versus Lux: radio mesh come canale principale per gli effetti, con un canale PLC a banda stretta (o PLC su DC sul tratto del ponte) come **backup lento** per comandi critici (on/off, scene di emergenza, diagnostica, ripristino della mesh). È lo stesso principio di G3-Hybrid.

### Gaps
- Nessun confronto pubblicato tra PLC e mesh radio su ponti o facciate.
- Nessun dato di affidabilità sul campo per Powercore/IntelliPower (solo il 99% di HiMarc per lo streetlighting G3).

---

## 6. Prezzi dei componenti commerciali

### Takeaway
I prezzi pubblici vanno da ~5 € per un chip DMX-su-powerline a ~1.590 $ per un Data Enabler Pro Color Kinetics. Per gli altri prodotti (GLP DoP, PowerGate, ST7580, QCA7000) non ho trovato un prezzo affidabile.

### Cited Findings

| Componente | Prezzo | Valuta / quantità | Fonte (consultata 2026-11-08) |
|---|---|---|---|
| Color Kinetics Data Enabler Pro, 106-000004-00 (UL) | 1.587,48 | "$" (presumibilmente USD), prezzo unitario, risultava esaurito | [Wiedamark](https://wiedamark.com/?p=110299) |
| Yamar DMX250 (chip) | 7,56 / 6,30 / 4,98 | USD e EUR uguali; 1-49 / 50-99 / 100-999 pz; 1000+ su richiesta | [Yamar DMX250](https://yamar.com/product/dmx250) |
| Saleconix DMX512 DC Powerline Modem | 64,13 | EUR, IVA inclusa, 1 pz | [RobotShop EU](https://eu.robotshop.com/products/saleconix-dmx512-dc-powerline-modem) |
| ST ST7580 | non pubblicato | rimando a ST / distributori | [ST](https://www.st.com/en/product/st7580.html) |
| Yamar DCB1M-IC | non letto (pagina dinamica) | — | [DigiKey](https://www.digikey.com/en/products/detail/yamar/DCB1M-IC/19525704) |

### Inferenze
- *(Inferenza)* Un ramo Powercore (fino a 63 apparecchi) costa ~1.590 $ solo di Data Enabler, cioè ≥25 $ per apparecchio di sola infrastruttura dati, esclusi Data Receiver e filtri. È un ordine di grandezza utile per posizionare il costo della soluzione radio.

### Gaps
- Prezzi di GLP DoP Converter (PSSL elenca i codici 78181/78182 ma il prezzo non è stato letto), Sundrax PowerGate, moduli QCA7000 (es. PLC Stamp micro 2, Bel Fuse Green PHY) e chip ST7580: non verificati.
- Prezzi in EUR di Data Enabler Pro su listini europei: non trovati.
