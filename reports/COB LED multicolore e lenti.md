# Sorgenti LED multicolore e ottiche per la linea RGB architetturale

Versus Lux · ricerca del 9 novembre 2026 · note complete e fonti in [`research_notes/COB LED multicolore e lenti/`](<../research_notes/COB%20LED%20multicolore%20e%20lenti/>)

> **Aggiornamento del 9/11/2026.** Il report non includeva la **Bridgelux Vesta RGBW D10/D13**. È un array RGBW con area luminosa unica da 10 o 13 mm, bianco CRI 95 regolabile da 1800 a 10.000 K, lenti Moony da 15 a 50° e NTC a bordo. È stata scelta come sorgente di partenza per i proiettori: vedi l'[analisi dedicata](../docs/sorgente-bridgelux-vesta.md). Resta vero che nessun produttore di riferimento offre l'ambra a bordo. Dal catalogo LEDiL è emerso anche il **Lumileds LUXEON HL1Z RGBW array** (11 mm), alternativa da verificare. Le lenti per la Vesta sono nell'[analisi delle ottiche LEDiL](../docs/ottiche-ledil-vesta.md).

## In sintesi

- **Un COB a 5 canali di qualità non esiste.** Tra i produttori di riferimento (Luminus, ams OSRAM, Cree LED, Lumileds, Bridgelux) l'offerta multicolore si ferma a RGBW su 4 canali. Il quinto canale, ambra o secondo bianco, va aggiunto con un emettitore separato. L'unico COB RGBWA a 5 canali trovato è cinese (Guangmai, 40 W). È economico ma ha:
  - bianco freddo a Ra 70;
  - binning largo;
  - resistenza termica circa 10 volte quella dei prodotti occidentali.
- **Fascio stretto e COB grande non vanno d'accordo.** Con un COB di grande superficie emittente si arriva al massimo a circa 17-20° con un riflettore. Per i fasci da 4 a 10°, quelli che servono per facciate alte e ponti, servono sorgenti compatte (4-5 colori in pochi millimetri), ciascuna con la sua lente. Un proiettore diventa quindi una matrice di "celle" sorgente+lente, che è anche la strada dei concorrenti premium (Lumenpulse Opticolor mescola il colore "alla sorgente").
- **L'ambra è il canale critico.** Passando da 25 a 85 °C:
  - l'ambra diretto (AlInGaP) perde quasi due terzi della luce e si sposta di circa 6 nm verso il rosso;
  - l'ambra a fosfori (PC-amber) perde solo il 13% e non cambia tonalità, ma invecchia peggio di tutti gli altri colori.

  Per un apparecchio da esterno fino a +50 °C ambiente conviene il PC-amber, pilotato a corrente ridotta.
- **Le lenti in PMMA o PC non sono una chiusura stagna.** In un IP66/67 vanno dietro un vetro frontale separato. Il vetro può essere lenticolare e fare anche da allargatore del fascio (10×30°, 10×60°).
- **Il rischio chimico è reale.** In un corpo sigillato i vapori di guarnizioni, colle e coating possono far perdere fino al 90% della luce in 450 ore. Lo zolfo (gomma vulcanizzata, aree industriali e costiere) annerisce i leadframe argentati. Servono materiali compatibili, LED con test allo zolfo e mai resina o coating sopra i LED.
- **Il colore va calibrato apparecchio per apparecchio.** I premium (Color Kinetics, ETC) misurano ogni canale in fabbrica e salvano i dati nell'apparecchio, con tolleranza sotto 2 SDCM. La nostra scheda ESP32-C5 lo può fare: una matrice di calibrazione in memoria più la compensazione con la temperatura letta da una NTC.

**Proposta.** Per i proiettori: una cella base con un emettitore compatto multicolore sotto una lente colour-mixing, ripetuta 4-24 volte a seconda della potenza. Per i lineari: SMD mid-power multicolore su PCB lungo, sotto una striscia di lenti e un vetro. Il COB Guangmai resta un'opzione low-cost per i proiettori a fascio largo, da qualificare con prove interne. I campioni e i preventivi da chiedere sono in fondo.

---

## 1. Come si fa una sorgente a 5 canali

Il mercato offre tre architetture:

| Architettura | Esempi | Pro | Contro |
| --- | --- | --- | --- |
| **A. COB unico a 5 canali** | Guangmai GJZ-J040RGBAW6 (RGBWA, 40 W) | Un solo componente, miscelazione alla sorgente, montaggio semplice | Solo produttori cinesi di fascia media; fasci non sotto ~17-20°; bianco freddo Ra 70; Rth 8 °C/W |
| **B. Emettitore 4-in-1 + quinto colore separato** | OSTAR Stage, Luminus SBM-40, Cree XM-L Color (tutti RGBW) + LED ambra o bianco | Componenti occidentali con datasheet completi, alta densità di potenza | Il quinto colore sta sotto un'altra lente o fuori dal centro ottico: frange di colore se non si progetta bene |
| **C. Cluster di LED a colore singolo** | Lumileds LUXEON C Color Line (14 colori, tra cui PC-amber e lime) | Si sceglie ogni colore, compreso il PC-amber e due bianchi; nessuna dipendenza da un 4-in-1 | Area emittente più grande del 4-in-1, quindi miscelazione più difficile; PCB e ottica da progettare |

Le ottiche dichiarano esplicitamente di poter lavorare con la C:
- Gaggione dichiara il collimatore LLC59x compatibile con "tutte le soluzioni multicolore", cluster di chip singoli compresi.
- LEDiL ha un supporto con cupola di miscelazione (HEKLA-SOCKET-RZ) pensato anche per cluster custom.

## 2. Sorgenti verificate

### Multicolore in un solo package

| Sorgente | Tipo | Canali | Dati principali | Rth | Stato e prezzo |
| --- | --- | --- | --- | --- | --- |
| **Guangmai GJZ-J040RGBAW6** | COB 56×40 mm, supporto in rame | **R G B W A** | 24-28 V e 350 mA per canale. A 25 °C: W 800-1000 lm (6000-6500 K, Ra 70), R 400-600, G 400-600 (dato incoerente in pagina), B 160-240, A 300-400 lm. Chip Epileds | 8 °C/W j-b | Prezzo su richiesta; i COB RGBW 30-50 W dello stesso produttore costano 4,5-7,5 US$ (MOQ 500) |
| **Luminus CTM-14 RGBW** | COB vero, LES 14,5 mm | R G B + bianco 2700 K CRI≥90 | 24 V e 200 mA per canale (max 250 mA, 6,5 W). A Tj 85 °C: G 650, W 438, B 115, R 94 lm | 0,67 K/W j-c | Datasheet "Preliminary"; prezzo non trovato |
| **Luminus CTM-9 RGBW** | COB, LES 9,5 mm | come sopra | 12 V e 200 mA per canale (max 3,25 W): G 325, W 219, B 58, R 47 lm | 1,8 K/W | come sopra |
| **ams OSRAM OSTAR Stage LE RTDUW S2WP** | SMD, 4 chip in 2,5×3,2 mm, finestra in vetro | R G B + bianco freddo | Fino a 5 A per chip. A 1,4 A: G 355-710, W 450-710, R 140-280 lm. Circa 15,6 W totali a 1,4 A | 0,70 K/W | In piena produzione; unico con resistenza allo zolfo dichiarata (classe 3B). Prezzo non letto |
| **Luminus SBM-40-RGBW** | SMD 4-in-1, 5,8×4,7 mm | R G B W | 1 A max per colore. A 700 mA: W 182, G 168, R 68 lm | non letta | Attivo. DigiKey: 7,35 US$ (1 pz), 4,52 (100), 4,49 (1.500) |
| **Cree XM-L Color Gen 2** | SMD 5×5 mm, 4 chip | R G B W | 1,75 A max per chip, Tj max 150 °C | non letta | A catalogo Mouser, senza prezzo |
| **Hongli HL-C3535F12RGBW** | SMD 3535 4-in-1 | R G B W | 350 mA, 5 W max. R 50-70, G 100-120, W 70-130 lm a seconda di CCT e CRI | 2 °C/W | Cinese, prezzo non trovato |
| **Bridgelux RGBW 3838** / **Lumileds LUXEON 5052 RGBW** | mid-power 4-in-1 | R G B W (bianco 1800-6500 K) | 0,36 W per canale | – | Adatti ai lineari, non ai proiettori. Bridgelux dichiara l'uso architetturale e in piscina |

Cosa vuol dire per noi:
- **Nessuno ha l'ambra a bordo**, quindi la versione RGBWA richiede sempre l'architettura A (Guangmai) oppure un emettitore ambra aggiunto.
- **Il rosso è sempre il canale che limita il bianco di miscela.** Sul CTM-14 ci sono 94 lm di rosso contro 650 di verde. Nella versione RGB+W+A l'ambra aiuta proprio sui toni caldi.
- **Il CTM ha un solo bianco a 2700 K.** Per la versione RGB+WW+CW serve comunque un secondo bianco esterno.
- **I CTM arrivano al massimo a circa 13 e 26 W totali.** Bastano per i proiettori piccoli; dai 50 W in su servono più sorgenti per apparecchio.

### LED a colore singolo per i cluster (architettura C)

Dal datasheet Lumileds LUXEON C Color Line (350 mA, Tj 85 °C):

| Colore | Flusso tipico | Spostamento con la temperatura | Tj max |
| --- | --- | --- | --- |
| Rosso 624-634 nm | 39 lm | 0,06 nm/°C | 120 °C |
| Ambra diretto 585-600 nm | 30 lm | 0,06 nm/°C | 120 °C |
| **PC-amber** | **94 lm** | −0,01 nm/°C (praticamente fermo) | 120 °C |
| Verde 520-540 nm | 97 lm | 0,04 nm/°C | 135 °C |
| Blu 465-485 nm | 37 lm | 0,03 nm/°C | 135 °C |
| Lime (a fosfori) | 152 lm | −0,01 nm/°C | 135 °C |

A parità di corrente il PC-amber fa tre volte la luce dell'ambra diretto.

## 3. Il canale ambra: diretto o a fosfori

Dati Lumileds (presentazione DOE 2020) a 350 mA:

| | PC-amber | Ambra diretto (AlInGaP) |
| --- | --- | --- |
| Flusso a 25 °C → 85 °C | 119 → 104 lm | 73 → 26 lm |
| Luce che resta a caldo | **87%** | **36%** |
| Spostamento di tonalità | −0,6 nm | +5,6 nm |
| Larghezza dello spettro | 78 nm | 14 nm (colore più puro) |
| Invecchiamento (LM-80, DOE 2018) | Il peggiore di tutti: L70 fino a circa 35.700 h nelle condizioni dure, deriva di colore misurabile | Ottimo, come il rosso |

**Indicazione.** Per un apparecchio sigillato fino a +50 °C ambiente il PC-amber è la scelta tecnica. Con l'ambra diretto il colore cambierebbe visibilmente tra una sera d'inverno e una d'estate, e dopo il riscaldamento dell'apparecchio. Per contenerne l'invecchiamento conviene pilotarlo sotto la corrente massima e contare in firmware le ore di funzionamento per canale, così da correggerne il calo.

## 4. RGB+W+A oppure RGB+WW+CW

Non abbiamo trovato confronti pubblicati con numeri (gamut, CRI, TM-30, efficienza) tra le due miscele. Il ragionamento è qualitativo:

- **RGB+W+A** dà toni caldi saturi (oro, ambra, tramonto) e un bianco caldo più ricco del solo W. È il più adatto alle facciate storiche e ai monumenti.
- **RGB+WW+CW** dà la regolazione continua della temperatura del bianco. È il più adatto quando l'impianto lavora soprattutto in bianco e usa il colore per gli eventi.

Il mercato premium si ferma a 4 canali. Lumenpulse, ad esempio, offre RGB+W 3000 K, RGB+W 4000 K e RGB+Ambra come varianti separate. **I 5 canali sono quindi un elemento distintivo**, coerente con la decisione 5 del registro.

Il confronto si può fare noi prima di ordinare: con gli spettri reali dei LED scelti e la libreria Python `colour-science` si calcolano gamut, CRI e TM-30 delle due miscele.

## 5. Ottiche per i proiettori

### Il compromesso fondamentale

Più un'ottica mescola i colori, più allarga il fascio. La guida LEDiL alle lenti TIR lo mette in tabella:

| Tipo di fascio | Angolo | Miscelazione del colore |
| --- | --- | --- |
| Real Spot | 4-25° | Nessuna |
| Smooth Spot, ovale | 8-25° | Bassa |
| Diffuso, medio, largo | 8-80° | Moderata |

Inoltre ogni colore esce con un angolo un po' diverso, perché i chip hanno dimensioni e posizioni diverse. Da qui nascono i bordi colorati.

Ne seguono tre conseguenze:
- **Fasci 4-10°:** servono sorgenti di pochi millimetri e collimatori dedicati al colour mixing. Si accetta una leggera frangia sul bordo, che a 30-50 m sulla facciata non si nota.
- **Fasci 20-60°:** qui la miscelazione è buona con quasi tutte le famiglie colour-mixing.
- **COB grande:** con un riflettore e una sublente di miscelazione non si scende sotto circa 17-20°.

### Famiglie verificate

| Produttore e famiglia | Formato | Fasci | Per quali sorgenti | Note |
| --- | --- | --- | --- | --- |
| **Gaggione LLC59x** (Francia) | Collimatore Ø45 mm | U circa 4-6°, C "colour" circa 10-12° | Tutte le multicolore, anche cluster di chip singoli | La migliore per i fasci stretti; dati del produttore in parte incoerenti, da verificare con campioni |
| **Khatod RGBW** (Italia) | Ø35 e Ø45 mm, PMMA | Da 8° a 40°; con microlenti opzionali zoom 12-50° | RGBW 4-in-1 | Efficienza >90% e -40/+90 °C dichiarati. Fornitore italiano |
| **LEDiL GABRIELLA-MIDI / -45** | Ø38 e Ø45 mm, superficie a microstruttura | S stretto, M, ovale, W 35° | RGB 5050, 7070 (OSTAR Stage, XM-L Color) | Progettata per l'architetturale esterno; 4,70 € al pezzo (50 pz, RS) |
| **LEDiL RGBX** | 30 mm, sublente intercambiabile | 20°, 30°, ovale 50°×24° | XM-L RGB, Ostar-SMT, MC-E | Il fascio si cambia con la sola sublente |
| **LEDiL HEKLA-SOCKET-RZ** | Supporto con cupola di miscelazione + lenti AMY, YASMEEN, ZORYA | Varie | Bridgelux RGBW, cluster RGBW custom, Zhaga Book 10 | Adatto all'architettura C |
| **LEDiL ANGELINA** | Riflettore Ø82 mm | Circa 20°, 30°, 50°, 91° | COB fino a 32 mm di LES, sublente di miscelazione opzionale | L'unica via documentata per un COB grande (Guangmai, CTM) |
| **Carclo** | Varie | Non riportati | Cinque codici dedicati a OSTAR Stage | Dati da chiedere |
| **LedLink** (Taiwan) | Ø35 mm (MC-E RGBW), Ø68,5 mm (COB 38°) | 18°, 16×30°, 38° | MC-E RGBW, COB | Lente COB a 2,2-2,7 US$; esercizio solo fino a +70 °C (max +80 °C) |
| **B&M** (fornitore attuale) | – | – | – | Nessun catalogo pubblico: va chiesto direttamente |

**Nessun produttore pubblica dati di uniformità del colore nel fascio** (Δu'v'). Va misurata noi con i campioni.

## 6. Ottiche per i lineari (grazer e wall washer)

- **Riferimento di mercato.** Color Kinetics Graze Compact RGBA: 305 mm, 8,1 W, 445 lm, IP66, da -40 a +50 °C, lente in vetro, fasci 10×60°, 30×60°, 60×60° e 100×100°. La luce esce già miscelata, quindi basta poca distanza dalla parete.
- **LEDiL LINNEA:**
  - striscia in PC da 285 mm per PCB Zhaga da 20-24 mm;
  - fasci ovale 35°×70°, asimmetrico wall-wash (ZT25), uplight, 60° e 90°;
  - dichiarata per interni: in esterno va dietro un vetro.
- **LEDiL LINDA:** strisce larghe, da 27° in su.
- **Lacuna principale.** Non abbiamo trovato a catalogo un'ottica lineare colour-mixing stretta, 10×60° o 5-10°, con dati pubblici. Le strade sono due:
  - lenti dedicate dei fornitori asiatici (B&M, LedLink), da validare al goniofotometro;
  - lenti singole strette in fila, con un vetro frontale lenticolare che allarga il fascio lungo l'asse della barra e intanto mescola i colori in quella direzione.

**Sorgenti per i lineari.** Gli SMD mid-power 4-in-1 (Bridgelux RGBW 3838, LUXEON 5052 RGBW) o i 3535 4-in-1 cinesi, alternati lungo la barra con un LED per il quinto canale. Lungo l'asse la miscelazione è facile; il passo dei LED va scelto con prove, perché non abbiamo trovato regole pubblicate.

## 7. Tenuta all'esterno

| Rischio | Cosa succede | Contromisura |
| --- | --- | --- |
| **Vapori (VOC) nel corpo sigillato** | Il silicone dei LED si scurisce: fino a −90% di luce in 450 h nella prova Cree. Blu e bianco sono i più colpiti. Il danno è reversibile solo ventilando | Guarnizioni in silicone a basso rilascio, niente EPDM o gomma vulcanizzata a zolfo, niente cianoacrilati né solventi aromatici, cottura dei materiali prima della chiusura, prova di compatibilità di almeno 1.000 h |
| **Zolfo** | Annerisce i leadframe argentati: ponti, zone industriali, costa | LED con leadframe dorato (es. Lumileds HR30) o con prova IEC 60068-2-43 dichiarata. Oggi solo OSTAR Stage la dichiara (classe 3B) tra i multicolore |
| **Coating e resina** | Sopra la lente del LED alterano il colore e la luce | Coating della lista compatibile Cree solo sull'elettronica; la resina già in uso solo sul driver, mai sui LED |
| **UV e acqua sulle lenti plastiche** | PMMA e PC non sono chiusure stagne e il PC ingiallisce all'UV | Vetro frontale temprato, eventualmente lenticolare |
| **Package plastici mid-power** | Ingialliscono per foto-ossidazione, soprattutto nel blu (dato DOE) | Preferire package ceramici o mid-power "alta affidabilità" |

## 8. Temperatura e calibrazione: cosa fa il firmware

Il colore di un apparecchio multicolore dipende più dalla temperatura che dall'invecchiamento: lo confermano i dati LM-80 analizzati dal DOE. Rosso e ambra diretto cambiano con il caldo il doppio di verde e blu. Per un colore stabile servono quattro cose:

1. **Obiettivo termico.** Restare intorno a Tj 85 °C per rosso e ambra con +50 °C ambiente, e limitare la differenza tra freddo e regime a circa 30 °C (nostra indicazione, non da fonte). Nella versione più potente, limitare la potenza totale quando tutti i canali sono al massimo.
2. **NTC sulla scheda LED.** Una tabella per canale corregge il flusso in base alla temperatura, partendo da rosso e ambra.
3. **Calibrazione di fine linea.** Lo spettrometro misura ogni canale a temperatura stabilizzata. La matrice di colore e la temperatura di riferimento si salvano nella memoria dell'ESP32-C5. L'apparecchio calcola il mix per raggiungere il colore richiesto.
4. **Gamut comune solo per bianchi e pastelli**, come Chromasync di Color Kinetics: i colori saturi restano liberi, così ogni apparecchio usa tutto il proprio gamut. Obiettivo: meno di 2 SDCM tra apparecchi.

Tutto questo sta nella scheda nodo già prevista: un ingresso analogico per la NTC e qualche kB di memoria. Non serve hardware aggiuntivo.

## 9. Prezzi raccolti

Prezzi letti il 9/11/2026.

| Componente | Prezzo | Quantità | Fonte |
| --- | --- | --- | --- |
| COB RGBW 10-12 W Guangmai | 1,2-1,8 US$ | MOQ 100 | Made-in-China |
| COB RGBW 30-50 W Guangmai | 4,2-7,5 US$ | MOQ 500-1.000 | Made-in-China |
| COB RGBWA 40 W Guangmai | su richiesta | – | gmleds.com |
| Luminus SBM-40-RGBW | 7,35 / 4,52 / 4,49 US$ | 1 / 100 / 1.500 | DigiKey |
| Cree XM-L RGBW su stella 20 mm | 25,49 US$ | 1 | LEDSupply |
| Lente LEDiL GABRIELLA-MIDI-W | 4,70 € | 50 | RS Irlanda |
| Lente COB LedLink 38° Ø68,5 mm | 2,65 / 2,17 US$ | 1 / 50 | Özdisan |

Mancano i prezzi di OSTAR Stage, Luminus CTM, Gaggione, Khatod, LEDiL RGBX e ANGELINA. Le pagine dei distributori sono nelle note.

**Ordine di grandezza di una cella per proiettori** (nostra stima, da confermare con i preventivi): emettitore 4-in-1 occidentale a 4,5-8 US$, più un LED per il quinto canale, più una lente colour-mixing a 4-6 €. Un proiettore da 12 celle costa quindi circa 110-170 € di sola parte ottica e LED, prima di PCB e dissipatore.

## 10. Proposta per Versus Lux

### Proiettori (20-300 W)

1. **Linea principale: celle ripetute.** Una cella è un emettitore multicolore compatto più una lente colour-mixing Ø35-45 mm. Lo stesso PCB a celle copre tutte le potenze (4, 8, 12, 24 celle) e tutti i fasci, cambiando solo la lente:
   - fasci stretti: Gaggione LLC59x o Khatod ultra narrow;
   - fasci medi e ovali: GABRIELLA, RGBX o Khatod.

   Due candidati per la cella, da provare in parallelo:
   - **B:** OSTAR Stage RGBW più un PC-amber o un secondo bianco nella stessa cella, sotto la stessa lente. Va verificato quanto il quinto LED fuori centro sporca il fascio.
   - **C:** un cluster compatto di 5 LED a colore singolo (LUXEON C, PC-amber compreso) sotto un collimatore che accetta i cluster (LLC59x) o sotto il supporto HEKLA-SOCKET-RZ.
2. **Variante economica a fascio largo: COB Guangmai RGBWA.** Usa un riflettore tipo ANGELINA, per fasci da 20° in su e per il flood. Prima va chiesta a Guangmai una versione con bianco caldo e Ra 80 o più; poi la qualifica al banco (spettrometro, prova termica, compatibilità dei materiali).

### Lineari (10-60 W/m)

SMD mid-power 4-in-1 alternati al LED del quinto canale su PCB lungo, sotto una striscia di lenti dietro un vetro temprato:
- LEDiL LINNEA per wall-wash e ovale;
- lenti B&M o LedLink da qualificare per il 10×60° stretto.

### Ordini e richieste

| Cosa | A chi |
| --- | --- |
| Campioni COB RGBWA 40 W con bianco caldo, prezzo, LM-80, dati termici | Guangmai |
| Campioni e prezzi LLC59x, con dati verificati (le schede sono incoerenti) | Gaggione |
| Campioni e listino lenti RGBW | Khatod |
| Campioni GABRIELLA-MIDI (S, M, O), RGBX, HEKLA-SOCKET-RZ | LEDiL o distributore |
| Campioni OSTAR Stage S2WP, LUXEON C (rosso, verde, blu, PC-amber, bianchi) | Distributore (Mouser, DigiKey, RS) |
| Catalogo lenti lineari strette e lenti colour-mixing | B&M |
| Disponibilità di sorgenti multicolore | Fornitori LED attuali dell'azienda |

### Prove da fare

1. **Simulazione spettrale** RGBWA contro RGB+CCT con gli spettri reali: gamut, CRI, TM-30.
2. **Prova termica** delle celle con tutti i canali accesi a +50 °C, misurando calo di luce e spostamento del colore.
3. **Uniformità del colore** nel fascio e a parete, per ogni combinazione sorgente+lente.
4. **Compatibilità dei materiali** (guarnizioni, colle, coating) per 1.000 ore, in un corpo chiuso con LED di controllo.

## 11. Cosa non siamo riusciti a verificare

- **Prezzi Alibaba e AliExpress:** bloccati dal captcha.
- **Produttori non coperti.** Non abbiamo trovato COB multicolore verificabili per:
  - Nationstar, MLS, Jufei, APT, Refond;
  - Nichia, Seoul, Samsung, Everlight, LG Innotek, Citizen (non cercati).
- **Nessun COB RGB+CCT** a 5 canali verificato.
- **Dati mancanti dei componenti:** curve di calo con la temperatura di rosso e ambra per OSTAR e Luminus; dati LM-80 dei prodotti multicolore; resistenza allo zolfo per tutti tranne OSTAR Stage.
- **Ottiche:** dati di uniformità del colore di qualunque famiglia; ottiche lineari strette colour-mixing; prezzi di quasi tutte le lenti.
- **Concorrenti:** quali sorgenti montano Color Kinetics, Lumenpulse, SGM e Martin. Non lo dichiarano.
- **Fornitori attuali dell'azienda:** se offrono sorgenti multicolore.

## Fonti principali

- [Guangmai, COB RGBWA 40 W](https://www.gmleds.com/cob-led/color-cob-led/5-channels-40w-rgbwa-cob-led.html) · [datasheet COB RGBW 12 W](https://ht.gmleds.com/Content/upload/pdf/202331250/12w-COB-RGBW.pdf?rnd=807) · [Made-in-China, COB RGBW](https://www.made-in-china.com/products-search/hot-china-products/Rgbw_Cob_Led.html)
- [Luminus CTM-X RGBW datasheet](https://download.luminus.com/datasheets/Luminus_CTM-X-RGBW_Datasheet.pdf) · [DigiKey SBM-40-RGBW](https://azcus.digikey.com/en/products/detail/luminus-devices-inc/SBM-40-RGBW-LC41-QC100/15903654)
- [ams OSRAM OSTAR Stage LE RTDUW S2WP](https://ams-osram.com/products/leds/multi-color-leds/osram-osram-ostar-stage-le-rtduw-s2wp) · [datasheet](https://www.mouser.lt/datasheet/3/5912/1/LE_RTDUW_S2WP_EN.pdf)
- [Mouser, Cree XM-L Color Gen 2](https://www.mouser.com.tr/cree-xlamp-xml-color-g2-leds) · [Lumileds Color LEDs](https://lumileds.com/products/color-leds) · [Lumileds LUXEON C Color Line DS144](https://static.chipdip.ru/lib/021/DOC014021940.pdf)
- [Hongli HL-C3535F12RGBW1GA-1C4B](https://doc.platan.ru/pdf/datasheets/hongli/HL-C3535F12RGBW1GA-1C4B.pdf) · [Bridgelux RGBW](https://www.BRIDGELUX.com/sites/default/files/2024-02/product_sell_sheet_-_bridgelux_rgbw_products_20240130.pdf)
- [DOE, Epler (Lumileds): ambra diretto contro PC-amber](https://www.energy.gov/sites/default/files/2020/02/f71/ssl-rd2020-epler-amber.pdf) · [DOE, LM-80 dei LED colorati (2018)](https://www.energy.gov/documents/sslrtilm80-color-ledsjuly2018pdf)
- [LEDiL RGBX](https://www.ledil.com/data/prod/RGBX/RGBX-fds.pdf) · [GABRIELLA-MIDI](https://www.ledil.com/news_all/gabriella-midi-rgb-and-tunable-white-colour-mixing-lens/) · [HEKLA-SOCKET-RZ](https://www.ledil.com/news_all/hekla-socket-rz-‒-your-effortless-entry-to-the-rgbw-world/) · [ANGELINA](https://www.ledil.com/data/prod/Angelina/Angelina-fds.pdf) · [LINNEA](https://www.ledil.com/data/prod/Linnea/Linnea-sfds.pdf) · [Guida LEDiL alle lenti TIR](https://ledil.com/?p=2148)
- [Gaggione LLC59x](https://led.cdiweb.com/Datasheets/gaggione/Gaggione-Focus-On-LLC59x.pdf) · [Khatod, lenti colour mixing](https://khatod.com/en/products/general-led-lighting/lenses/color-mixing-lenses) · [LedLink MC-E RGBW](https://storage.sea.com.ua/tech_info/LEDlink/LL01ED-BCQxxL06_CREE%20MC-E%28RGBW%29.pdf) · [Carclo per OSTAR Stage](https://www.carclo-optics.com/osram-ostarr-stage-le-uw-s2wn)
- [Color Kinetics Graze Compact RGBA](https://www.docs.colorkinetics.com/specsheets/GrazeCompact_Color/Graze_Compact_Powercore_RGBA_100-277VAC_High_Power_30x60_305mm_1ft.pdf) · [Chromasync](https://www.docs.colorkinetics.com/learn/color-kinetics-chromasync-overview.pdf) · [ETC, calibrazione del colore](https://support.etcconnect.com/ETC/Getting_Started_with_ETC_and_FAQ/LED_Fixture_Color_Calibration_and_Matching) · [Lumenpulse Opticolor](https://www.lumenpulse.com/opticolor?region=eu)
- [Cree, compatibilità chimica](https://downloads.cree-led.com/files/da/x/XLamp-Chemical-Compatibility.pdf) · [Lall e altri, VOC e LED (OSTI)](https://www.osti.gov/servlets/purl/1212875) · [LUXEON HR30, prova allo zolfo](https://ledinside.com/node/25086)
