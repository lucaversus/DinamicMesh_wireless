# Fonti primarie Lumenpulse lette direttamente (8 novembre 2026)

Documenti ufficiali letti nel browser integrato, testo estratto dai PDF. Citazioni testuali in inglese tra virgolette, il resto è sintesi.

## 1. Whitepaper "Understanding Lumentalk" (Adam Warmington, Advanced R&D and Controls Product Manager)

URL: https://www.lumenpulse.com/resources/whitepapers/understanding-lumentalk

- Lumentalk è una tecnologia PLC sviluppata da Lumenpulse che trasferisce dati digitali sul cablaggio AC; trasforma il cablaggio elettrico in una rete di controllo digitale per DMX, DALI, 0-10V o TRIAC.
- Mezzo: rete AC 120-277 V. Il segnale modulato è **sovrapposto** alla forma d'onda di rete (non trasmesso solo vicino allo zero-crossing): consente di trasmettere in qualsiasi momento ed è più resistente a reti disturbate.
- La modulazione è spiegata con l'esempio della FSK; il whitepaper non dichiara esplicitamente frequenza o modulazione di Lumentalk.
- Frequenza portante: "A lower frequency, in general, will have the ability to travel longer distances. A higher frequency enables faster data transfer but decreases resilience to transmission line effects."
- Limite dichiarato: ogni edificio è cablato in modo diverso e "Each device connected to the power network will affect all signal transmitted on the powerlines", quindi va controllata tutta l'apparecchiatura collegata al circuito.
- Componenti: Lumentranslator e Lumenlink modulano e iniettano il segnale; **Lumenear** è la scheda nell'apparecchio che demodula. Indirizzamento individuale o di gruppo.
- "Lumentalk does not perform a direct translation of DMX, DALI, or 0-10V into a PLC, but rather converts the transmitted information as closely as possible."
- Posizionamento: "ideally suited for retrofit applications where running new data wires is not feasible". Esempi: Muider Castle, Castro Street (San Francisco).

## 2. Pagina prodotto Lumentalk

URL: https://www.lumenpulse.com/products/82/lumentalk

- Dimmerazione, cambio colore e regolazione della temperatura colore sulla linea elettrica.
- Compatibile con DMX, DALI, 0-10V, TRIAC; "works on any AC voltage (100VAC - 277VAC), and operates within frequency bands allocated by worldwide regulations (FCC, CENELEC, ARIB)".
- Premio Architectural SSL Product Innovation Awards 2012.
- Progetti collegati: Buckley Recital Hall, Parthenon, Muider Castle, John A. Blatnik Bridge, Castro Street, 90 State Street, Nationwide Plaza e altri 11.
- Immagine promozionale: "Over 400 completed projects".

## 3. Brochure Lumentalk EMEA 2019 rev 2 (37 pagine, codice 131357)

URL: https://www.lumenpulse.com/files/view-file/supportfiles/7d669da3ebe18ad208cc7e8126ac993f/3490/locale_file/lumentalk-brochure-emea-en-2019-rev-2

Prestazioni (FAQ):
- "On a single Lumentalk network it is possible to control up to 1024 luminaires, grouped in up to 48 different zones. You can connect up to 32 independent controllers on the same network."
- "Lumentalk allows dimming of luminaires down to 1% intensity with a communication speed 2.5 times faster than DALI."
- "Latency may occur if there are more than 48 addresses being used. There is nearly zero latency with fewer than 48 addresses."
- "functional range from 100 - 277VAC 50/60Hz. Lumentalk is fully compliant with FCC and CENELEC communication standards".
- Bidirezionale: gli apparecchi memorizzano e comunicano configurazione, temperatura, ore di vita e stato.
- Un Lumenlink collega fino a 3 circuiti o 3 fasi; massimo 3 Lumenlink per rete. Ogni dimmer o controller richiede un Lumentranslator 2.
- Licenza a terzi: "Lumentalk technology is open to other manufacturers through our Lumentalk licensing program."
- Costo: "The cost involved is only the Lumentranslators 2 and luminaires." Nessun prezzo pubblicato.

Uso dinamico (pagina "Colour changing the Lumentalk way"):
- Scenari mostrati: colore statico e "Slow Fade" (scala 0-10 minuti).
- "Lumentalk is ideal for the vast majority of your architectural lighting needs, but if you are looking for a fast colour show, our DMX/RDM systems are the way to go."
- Mix supportati: RGB, RGBW, RGBA, Dynamic White e Dynamic Warm.

Marketing sulla sicurezza: "Unlike wireless, I'm secure. I can't be hacked remotely."

Casi con distinta dei componenti:

| Progetto | Apparecchi Lumentalk | Lumenlink | Lumentranslator 2 | Controllo | Risultati dichiarati |
| --- | --- | --- | --- | --- | --- |
| John A. Blatnik Bridge, Duluth (USA) | 90 | 1 | 1 | 1 Pharos | ponte di 2.430 m; energia -60% |
| Boston City Hall (USA) | 311 | 12 | 3 | 1 Pharos | nessun foro nei muri di cemento da 1 m |
| Buckley Recital Hall, Amherst (USA) | 164 | 3 | 3 | — | manutenzione -50.000 USD/anno |
| Castro Street, San Francisco (USA) | 48 | 1 | 2 | Lumentouch 2.0 | nessuno scavo stradale |
| Château Frontenac, Québec (CAN) | 6 | 1 | 2 | Lumentouch 2.0 | facciata storica |
| Muider Castle, Muiden (NL) | 12 | 1 | 1 | — | energia -80%, nessuno scavo |

Commissioning: rilevamento di tutti i dispositivi sulla linea tramite il protocollo bidirezionale, con LumenID collegato a un Lumentranslator 2 e software LumentalkID (trascina e rilascia nelle "sezioni").

Sede italiana indicata nella brochure: Calenzano (FI), Via della Chiesa 38.

## 4. Manuale LumentalkID rev 5 (11 pagine)

URL: https://www.lumenpulse.com/files/view-file/supportfiles/703f4b089786c2cdfae5d7d35cd49072/3491/locale_file/113205-lp-lumentalkid-manual-rev-5

- Lumentranslator DMX: "DMX Range Length ... 48 is the maximum channel count allowed".
- "choosing up to 48 DMX512 channels of output. Note that the smaller the range, the less bandwidth the Lumentranslator 2 will take up on your Lumentalk network."
- "Group Control: ... all of your Lumentalk-enabled fixtures to function as a synchronized group. This conserves bandwidth and DMX channels."
- Più Lumentranslator nella stessa sezione: controllo condiviso in LTP (latest takes precedence).
- Un progetto può comprendere più reti Lumentalk separate che non comunicano fra loro.
- Il kit LumenID per il commissioning si compra dal distributore; prezzo su richiesta.

## 5. Scheda tecnica Lumenbeam Medium Colour Changing, versione EU metrica (18 pagine)

URL: https://storage.googleapis.com/lumenpulse-medias/prod/document/products-5692-specsheet-fullspecsheet-eu-en-metric.pdf

Vincoli Lumentalk scritti in scheda:
- "1 DMX controller per Lumentalk network, maximum of 48 DMX channels per Lumentalk network (minimum step transition update rate is 1 second, minimum fade time between two colours is 1 minute)."
- "Maximum of 1 transmitter (Lumentranslator or Lumenlink) per system."
- "Maximum of 32 fixtures per LDB-DMX."
- "Consult factory for specific applications and maximum fixture count/cable length recommendations."
- Commissioning in due passi per gli apparecchi DMX/RDM collegati al Data Bridge: LumenID, poi LumentalkID.
- Versioni Lumentalk (LT): RGB, RGBW30K, RGBW40K, RGBA, MRGBA, MRGBWP, MRGROYWP.

Dati di prodotto utili come riferimento:
- 28 W (RGB, RGBW, RGBA discreti), 25 W (Opticolor e Opticolor+).
- Flusso massimo: 1.598 lm RGB; 1.540 lm RGBW30K; 1.284 lm RGBA; 1.158 lm MRGBWP.
- IP66, IK09, -40/+50 °C, L70 > 90.000 h (TM-21), garanzia 5 anni.
- Risoluzione DMX/RDM 8 o 16 bit, 3 o 4 canali per apparecchio.
- **Opticolor+**: sorgenti miscelate alla fonte (MRGBWP: rosso, verde, blu più un bianco; MRGROYWP: rosso, verde, blu royal, arancio, giallo e bianco, secondo la sigla) comandate con **4 indirizzi DMX**. Bianco configurabile in campo da 2200 K a 8000 K. Gli apparecchi escono dalla fabbrica in modalità "Optidrive".
- Cavo unico per alimentazione e dati nelle versioni DMX/RDM, tramite control box (fino a 6 uscite).

## 6. Lumenlink Pro, Lumentranslator 2, Lumentalk Data Bridge

Pagine prodotto: https://www.lumenpulse.com/products/5414 (Lumenlink Pro), https://www.lumenpulse.com/products/5415 (Lumentranslator 2), https://www.lumenpulse.com/products/4952 (Data Bridge).

- **Lumenlink Pro**: gateway multi-circuito; ingressi DMX, 0-10V, DALI, Art-Net, sACN (Ethernet); porta Lumentalk su fino a 6 circuiti; fa anche da ripetitore fra fasi. Monofase o trifase 120, 208, 240, 277 V. 3G ANSI C136.31 per ponti. IP66, rivestimento anticorrosione opzionale, garanzia 5 anni, UL e CE. Dimensioni circa 302 × 203 × 127 mm. Preconfigurato in fabbrica per un solo modo di controllo.
- **Lumentranslator 2**: in scatola da incasso doppia; ingressi DMX, 0-10V, DALI, TRIAC; alimentato dalla stessa linea; UL e CE.
- **Lumentalk Data Bridge**: converte Lumentalk in DMX o 0-10V per apparecchi non Lumentalk; IP66; dichiara "saving up to 30% of total installation costs".
- Lumentranslator (prima generazione) e Lumenlink (prima generazione): fuori produzione.

Dichiarazione CE del Lumenlink Pro (LNKP-230-xx): direttive Bassa Tensione 2014/35/UE, EMC 2014/30/UE e RoHS 2011/65/UE; prodotto in Canada. Nessuna norma armonizzata elencata nella parte letta, e nessuna menzione esplicita di EN 50065.
URL: https://www.lumenpulse.com/files/view-file/supportfiles/8aa7ef83e067271b0f773bca7530c81d/5608/locale_file/eu-declaration-of-conformity-lnkp
