# Sorgenti LED e ottiche per grazer/wall washer lineari multicolore; qualità colore, stabilità e affidabilità outdoor

Note di ricerca (9 novembre 2026) per Versus Lux, linea RGB architetturale wireless 5 canali (RGB+W+A o RGB+WW+CW), IP66/67, -40/+50 °C. Ricerca limitata a circa 20 chiamate: diversi punti restano nelle sezioni "Gaps". Nessun dato è stato inventato; ciò che non è stato trovato è segnalato.

## A1 — Sorgenti LED usate nei grazer lineari RGBW/RGBA premium

### Takeaway
I grazer premium documentati sono quasi tutti a 4 canali (RGBA o RGBW), con efficienze di sistema modeste (circa 54 lm/W per un RGBA compatto Color Kinetics) e con un'ottica che miscela il colore già all'uscita della lente. Le schede pubbliche non indicano quasi mai il package LED, né il numero o il passo dei LED.

### Cited Findings
- Color Kinetics Graze Compact Powercore RGBA, 30x60°, 305 mm: 4 canali R/G/B/A; 445 lm totali (R 175, G 322, B 118, A 224 lm); 8,1 W max; 53,7 lm/W; IP66 per luoghi bagnati; funzionamento da -40 a +50 °C, avvio da -20 a +50 °C; lente in vetro; corpo in alluminio estruso anodizzato 45 x 306 x 42 mm; L70 calcolata 63.326 h. La scheda **non riporta il numero di LED** — [Scheda CK Graze Compact RGBA 30x60 1ft](https://www.docs.colorkinetics.com/specsheets/GrazeCompact_Color/Graze_Compact_Powercore_RGBA_100-277VAC_High_Power_30x60_305mm_1ft.pdf)
- La stessa famiglia offre fasci 10x60°, 30x60°, 60x60° e 100x100°. L'ottica dà "fully mixed light directly out of the luminaire", quindi serve un arretramento (setback) minore — [stessa scheda](https://www.docs.colorkinetics.com/specsheets/GrazeCompact_Color/Graze_Compact_Powercore_RGBA_100-277VAC_High_Power_30x60_305mm_1ft.pdf)
- La famiglia usa Chromasync, che calibra un gamut comune fra apparecchi della stessa famiglia — [stessa scheda](https://www.docs.colorkinetics.com/specsheets/GrazeCompact_Color/Graze_Compact_Powercore_RGBA_100-277VAC_High_Power_30x60_305mm_1ft.pdf)
- Color Kinetics ColorGraze MX4 Powercore RGBA: grazer lineare per esterni, alimentato direttamente a tensione di rete, con "un LED amber separato" aggiunto all'RGB. La pagina prodotto non riporta lunghezze, fasci né flussi — [CK ColorGraze MX4 RGBA](https://colorkinetics.com/global/products/rgb/colorgraze-mx4-powercore-rgba)
- Lumenpulse Lumenfacade Colour Changing:
  - configurazioni RGB, RGB+W 3000K, RGB+W 4000K, RGB+Amber;
  - ottiche da grazing/flood da 8x8° a 90x90°, fra cui 10x30°, 10x60°, 15x25°, 50x80° e wallwash asimmetrico;
  - lunghezze 12/24/36/48 in; controllo DMX/RDM, DALI-2, Lumentalk;
  - vibrazione 3G ANSI C136.31 per i ponti; rivestimento anticorrosione opzionale;
  - stato attuale: **Discontinued**.

  [Lumenpulse Lumenfacade CC](https://lumenpulse.com/products/3862/lumenfacade-color-changing?region=na)

### Inferences
- Il riferimento di mercato per un grazer RGBA da circa 30 cm è circa 8 W e 450 lm. Il target Versus Lux di 10–60 W/m è quindi uguale o superiore alla classe "Compact" (circa 27 W/m). Le versioni a 60 W/m saranno "high output" e richiederanno una gestione termica più seria (vedi B6).
- Offrire sia W 3000K sia W 4000K, come fa Lumenpulse, è prassi di mercato. Il 5° canale (A oppure seconda W) differenzia l'offerta Versus Lux dai 4 canali dei concorrenti.

### Gaps
- Package LED, numero e passo dei LED in ColorGraze, Lumenfacade, Traxon e iGuzzini Linealuce: non trovati nelle pagine consultate (le spec sheet PDF complete non sono state lette).
- Dati su SMD 3535/5050 4-in-1 e 5-in-1 (es. Cree XM-L Color, OSRAM OSTAR/OSLON multichip, Luminus): non ricercati per limiti di budget.

## A2 — Ottiche lineari (lens strip e lenti singole)

### Takeaway
La famiglia Ledil LINNEA (strisce in PC da 285 mm per PCB Zhaga mid-power da 20/24 mm) copre ovale, wallwash asimmetrico, uplight e fasci larghi. Non ha fasci stretti sotto ~35° ed è dichiarata per interni. Per il grazing stretto 5–10° in esterno servono altre famiglie, non verificate qui. Il riferimento premium (Color Kinetics) usa una lente in vetro.

### Cited Findings
- Ledil LINNEA:
  - dimensioni 285 x 40 mm; materiale PC; ottimizzata per PCB Zhaga mid-power da 20 e 24 mm o per moduli Fortimo Edge a 2 file;
  - fissaggio a clip su lamiera/profilo da 0,5 o 1,0 mm;
  - il datasheet parla di "high quality indoor lighting" e non indica IP né efficienza.

  [Ledil LINNEA datasheet](https://www.ledil.com/data/prod/Linnea/Linnea-sfds.pdf)

| Codice Ledil | Fascio | Altezza | Lamiera |
|---|---|---|---|
| F15756_LINNEA-O / F15952_LINNEA-O-B | ~35°+70° ovale | 10,5 mm | 1,0 / 0,5 mm |
| F15861_LINNEA-ZT25 / F16000_LINNEA-ZT25-B | asimmetrico wall-washing | 11,6 / 11,5 mm | 1,0 / 0,5 mm |
| F16048_LINNEA-UP | asimmetrico uplight | 10,3 mm | 1,0 mm |
| F15860_LINNEA-Z2T25 / F15999_-B | doppio asimmetrico | 10,3 mm | 1,0 / 0,5 mm |
| F15524_LINNEA-60 / F15941_-B | ~60°+90° | 9,5 mm | 1,0 / 0,5 mm |
| F15523_LINNEA-90 / F15940_-B | ~90°+90° | 9,5 mm | 1,0 / 0,5 mm |

Fonte tabella: [Ledil LINNEA datasheet](https://www.ledil.com/data/prod/Linnea/Linnea-sfds.pdf)

- RS UK (F15861_LINNEA-ZT25, cod. 186-2375): l'articolo risulta "Unavailable" e RS "non lo stockerà più", quindi nessun prezzo disponibile. Lente PC trasparente, 285,1 x 40 x 11,6 mm — [RS UK](https://uk.rs-online.com/web/p/led-lenses-reflectors/1862375) (consultato 9/11/2026)
- Ledil LINDA-10-M (C18074): lens strip 27°–98° "Wide", montaggio a pannello. La pagina DigiKey letta non mostrava prezzi né specifiche — [DigiKey C18074_LINDA-10-M](https://www.digikey.de/en/products/detail/ledil/C18074-LINDA-10-M/23350685). Esiste anche la variante C18078_LINDA-10-UP, opalina 99°–183° — [DigiKey](https://www.digikey.de/en/products/detail/ledil/C18078-LINDA-10-UP/23350751)
- Ledil STELLA è una famiglia di lenti singole circolari, es. FN13323_STELLA-A asimmetrica e FN14074_STELLA-HB 78° — [RS UK STELLA-A](https://uk.rs-online.com/web/p/led-lenses-reflectors/8892450); non è una striscia lineare.

### Inferences
- LINNEA è nata per PCB mid-power monocromatici a doppia fila e per interni. In un apparecchio IP66/67 andrebbe dietro un vetro di chiusura (protezione UV del PC, condensa). La ZT25 è un buon candidato per un wall-washer asimmetrico, ma va verificata la miscelazione dei colori con SMD 4/5-in-1.
- Per fasci 10x60° e 5–10° di grazing la soluzione più probabile resta quella dei fornitori cinesi (B&M, LedLink) con lenti in PMMA/PC dedicate, oppure lenti singole TIR ellittiche. Le prestazioni vanno validate con goniofotometro: non è stato trovato alcun dato pubblico confrontabile.

### Gaps
- Gaggione, Khatod e Carclo linear (fasci, materiali, prezzi): non verificati.
- Ledil per il grazing stretto (es. famiglie per 10x60°): non identificato con fonte.
- Regola "passo LED vs distanza di miscelazione": nessuna fonte quantitativa trovata.
- Efficienza ottica delle strip LINNEA: non riportata dal datasheet.
- Prezzi correnti Mouser/DigiKey/TME: non ottenuti (pagine senza prezzo o articolo fuori stock).

## B1 — Amber diretto AlInGaP vs amber a fosfori (PC) e coefficienti termici dei colori

### Takeaway
Fra 25 e 85 °C l'amber AlInGaP diretto perde circa il 60–64 % del flusso e si sposta di +5–6 nm verso il rosso. Il PC-amber perde solo il 10–16 % e resta quasi fermo in lunghezza d'onda. In cambio il PC-amber ha la manutenzione del flusso e la stabilità cromatica peggiori fra tutti i colori in LM-80. Rosso e arancio AlInGaP hanno coefficienti di lunghezza d'onda doppi rispetto a verde e blu InGaN.

### Cited Findings
Confronto Lumileds (DOE SSL R&D 2020, presentazione Epler) a 350 mA, valori a 25 °C / 85 °C:

| Parametro | PC-Amber (InGaN + fosforo nitruro) | Amber diretto (AlInGaP) |
|---|---|---|
| Flusso (lm) | 119 / 104 | 73 / 26,4 |
| Efficienza (lm/W) | 118 / 110 | 100 / 37,7 |
| λ dominante (nm) | 589,4 / 588,8 (−0,6 nm) | 590,6 / 596,2 (+5,6 nm) |
| Rapporto caldo/freddo | 0,87 | 0,36 |
| FWHM (nm) | 77,9 / 79,3 | 13,7 / 15,9 |
| Purezza colore (%) | 98,1 / 97,6 | 99,9 / 99,9 |
| Vf (V) | 2,91 / 2,78 | 2,09 / 2,00 |

Fonte tabella: [DOE – Epler, Lumileds, amber](https://www.energy.gov/sites/default/files/2020/02/f71/ssl-rd2020-epler-amber.pdf)

- A 700 mA in impulso, fra Tc 25 e 85 °C, il PC-amber perde il 10–16 % (saturazione termica del fosforo). L'amber diretto perde circa il 60 % (perdita di confinamento dei portatori e red shift di circa 5 nm). Conclusione della fonte: il PC-amber è preferibile nella maggior parte delle applicazioni, ma vanno considerati costo, purezza di colore e Vf più alta — [DOE – Epler](https://www.energy.gov/sites/default/files/2020/02/f71/ssl-rd2020-epler-amber.pdf)

Coefficienti dal datasheet Lumileds LUXEON C Color Line (DS144, 2016; 350 mA, Tj 85 °C):

| Colore | λd (nm) | Flusso tip. | dλ/dT (nm/°C) | dVf/dT (mV/°C) | Tj max | Rth j-sp (K/W) |
|---|---|---|---|---|---|---|
| Royal Blue | 440–460 (picco) | 532 mW | 0,03 | −1,7 | 135 °C | 2,8 |
| Blue | 465–485 | 37 lm | 0,03 | −2,6 | 135 °C | 3,5 |
| Cyan | 490–510 | 72 lm | 0,03 | −2,4 | 135 °C | 3,5 |
| Green | 520–540 | 97 lm | 0,04 | −2,4 | 135 °C | 3,5 |
| Lime (PC) | per cromaticità | 152 lm | −0,01 | −2,7 | 135 °C | 2,8 |
| PC Amber | per cromaticità | 94 lm | −0,01 | −1,7 | 120 °C | 3,0 |
| Amber | 585–600 | 30 lm | 0,06 | −2,0 | 120 °C | 2,8 |
| Red-Orange | 614–624 | 52 lm | 0,06 | −1,6 | 120 °C | 2,8 |
| Red | 624–634 | 39 lm | 0,06 | −1,6 | 120 °C | 2,8 |

Fonte tabella: [Lumileds DS144 LUXEON C Color Line (copia chipdip)](https://static.chipdip.ru/lib/021/DOC014021940.pdf). Nota: l'abbinamento fra valori di Tj max e gruppi di colore è stato ricostruito da una tabella con intestazioni poco leggibili. Le curve flusso/Tj sono solo grafiche, senza valori numerici.

### Inferences
- Il rosso e l'amber AlInGaP sono i canali che "scappano" di più con la temperatura: crolla il flusso e cambia la λ. La compensazione NTC del controller ESP32 deve agire soprattutto su questi due canali, con una LUT flusso(T) per canale ricavata da misure proprie.
- In base al rapporto caldo/freddo 0,36 vs 0,87 e alla λ stabile, per il canale "A" di un 5 canali esterno (fino a +50 °C ambiente) il PC-amber è tecnicamente preferibile. Il prezzo da pagare è una manutenzione LM-80 peggiore (B4) e una purezza leggermente minore.

### Gaps
- Coefficienti equivalenti per ams OSRAM (OSLON/OSTAR multichip), Cree XM-L Color, Luminus e Nichia: non estratti.
- Valori numerici di flusso relativo a 85/100 °C per i singoli colori LUXEON C: solo in grafico.

## B2 — Confronto miscele: RGB+CCT vs RGBW vs RGBWA

### Takeaway
Non è stato trovato alcun confronto pubblicato e quantitativo (gamut, CRI/TM-30, efficienza) fra RGBW, RGBA e RGBWA per facciate. Le fonti reperite sono qualitative.

### Cited Findings
- Un blog di settore (marzo 2026) afferma che RGBAL (con amber e lime) permette CRI/TLCI elevati e bianchi caldi 2700–3200 K, e che RGBAL/RGBIL sono "significativamente superiori" a RGB o RGBW nella miscelazione. Non fornisce dati numerici; fonte debole — [Light Now blog](https://www.lightnowblog.com/2026/03/comparing-rgbal-and-rgbil-color-mixing-approaches/)
- Nel prodotto premium RGBA da 30 cm il verde fornisce 322 lm su 445, il blu solo 118 lm — [CK Graze Compact RGBA](https://www.docs.colorkinetics.com/specsheets/GrazeCompact_Color/Graze_Compact_Powercore_RGBA_100-277VAC_High_Power_30x60_305mm_1ft.pdf)
- Il lime a fosfori (152 lm tip. a 350 mA) è il canale più efficiente della linea LUXEON C, più del doppio del rosso (39 lm) — [Lumileds DS144](https://static.chipdip.ru/lib/021/DOC014021940.pdf)

### Inferences
- Per le facciate, dove servono saturi e bianchi d'accento di buona qualità, un RGB + W (3000 o 4000 K) + A dà un bianco a CRI più alto della sola W e un range caldo (oro, ambra, tramonti) migliore dell'RGBW. È un ragionamento qualitativo, da confermare con simulazioni spettrali sui SPD reali dei LED scelti (es. calcolo TM-30 Rf/Rg in Python con `colour-science`).
- RGB+WW+CW privilegia la regolazione della CCT del bianco. RGB+W+A privilegia i colori caldi saturi.

### Gaps
- Numeri di gamut (area in u'v'), Ra/Rf/Rg ed efficienza per ciascuna miscela: nessuna fonte primaria trovata (application note Lumileds/OSRAM, articoli LED professional/LEDs Magazine non reperiti).

## B3 — Calibrazione e consistenza del colore

### Takeaway
I produttori premium misurano in fabbrica, per ogni apparecchio, flusso e lunghezza d'onda di ogni canale e salvano i dati nel firmware. Il colore richiesto viene poi rimappato su un gamut di destinazione comune, partendo comunque da una binnatura stretta. La tolleranza dichiarata è inferiore a 2 SDCM.

### Cited Findings
- ETC calibra ogni apparecchio in fabbrica: misura output e lunghezza d'onda di ogni emettitore e li memorizza nell'apparecchio. Al momento della richiesta l'apparecchio calcola il proprio mix per raggiungere il target, compensando le differenze di bin, purché il colore sia dentro il gamut. Le fonti non documentano una compensazione in temperatura — [ETC support](https://support.etcconnect.com/ETC/Getting_Started_with_ETC_and_FAQ/LED_Fixture_Color_Calibration_and_Matching)
- Chromasync Pro (Color Kinetics):
  - divide il gamut in una regione "Accuracy" (bianchi e pastelli) e una regione "Saturation" che sfrutta tutto il gamut del singolo apparecchio, con transizione graduale fra le due;
  - si basa su Optibin, che raggruppa i LED per flusso e lunghezza d'onda centrale;
  - variazione dichiarata fra apparecchi inferiore a 2 ellissi di MacAdam (2 SDCM).

  [CK Chromasync overview](https://www.docs.colorkinetics.com/learn/color-kinetics-chromasync-overview.pdf)
- Limitarsi al gamut comune garantisce l'accuratezza, ma riduce l'uso ai soli bianchi e pastelli. Per questo Chromasync lascia liberi i saturi — [CK Chromasync overview](https://www.docs.colorkinetics.com/learn/color-kinetics-chromasync-overview.pdf)
- Nei dati LM-80, per i LED GaN le variazioni di corrente o di Tj hanno spesso un effetto sulla cromaticità pari o superiore all'invecchiamento — [DOE LM-80 color LEDs 2018](https://www.energy.gov/documents/sslrtilm80-color-ledsjuly2018pdf)

### Inferences
- Schema replicabile con l'ESP32:
  1. misura a fine linea, per canale, di XYZ a piena potenza e a Tj nota (spettrometro HPCS-330 già in azienda);
  2. salvataggio di una matrice 3x5 in NVS;
  3. solver del mix verso target xyY, con gamut di destinazione "Accuracy" comune solo per bianchi e pastelli;
  4. correzione del flusso per canale in funzione della T letta dall'NTC (coefficienti in B1).
- La regola del DOE implica che una calibrazione eseguita a freddo, senza compensazione termica, sarà errata a regime. Calibrare a temperatura stabilizzata e salvare anche la T di riferimento.

### Gaps
- Metodi Lumenpulse (Optidrive) e Robe: non documentati nelle fonti trovate.

## B4 — Deriva del colore nel tempo, LM-80/TM-21 per LED colorati

### Takeaway
Nell'LM-80 i LED InGaN diretti e quelli AlGaInP rosso/arancio mantengono bene il flusso. Il PC-amber è il peggiore (L70 anche solo ~35.700 h nelle condizioni severe, Δu'v' > 0,001). I verdi e ciano InGaN mostrano shift cromatici misurabili.

### Cited Findings
- Analisi DOE di 68 set LM-80-15 (oltre 1.400 LED high-power) — [DOE – LM-80 color LEDs (luglio 2018)](https://www.energy.gov/documents/sslrtilm80-color-ledsjuly2018pdf):
  - InGaN royal blue–green: manutenzione simile ai LED bianchi; α spesso fra −2,5e−6 e 2,5e−6;
  - rosso e rosso-arancio AlGaInP: manutenzione eccellente; Δu'v' < 0,001;
  - PC-amber: manutenzione più bassa di tutti; α > 1,0e−5 ad alta corrente e temperatura, cioè L70 ≈ 35.700 h; quasi tutte le condizioni sotto L70 50.000 h; Δu'v' > 0,001 in tutte le condizioni, prime 1.000 h circa −0,001/−0,002 in u'; causa probabile il fosforo;
  - ciano e verde: Δu'v' ≥ 0,001 con direzione variabile anche fra prodotti dello stesso colore nominale;
  - nelle prime 1.000 h il rosso tende ad aumentare il flusso (B > 1), il verde a calare;
  - con la regola 6X, per proiettare α = 2,5e−6 (L70 ≈ 140.000 h) servono almeno 23.333 h di test, quindi la maggior parte dei LED diretti è limitata dalla durata del test;
  - i package mid-power in polimero soffrono foto-ossidazione e ingiallimento, soprattutto alle lunghezze d'onda corte.
- CK Graze Compact RGBA: L70 dichiarata > 54.000 h, calcolata 63.326 h — [scheda CK](https://www.docs.colorkinetics.com/specsheets/GrazeCompact_Color/Graze_Compact_Powercore_RGBA_100-277VAC_High_Power_30x60_305mm_1ft.pdf)

### Inferences
- Se si sceglie il PC-amber, conviene pilotarlo a corrente ridotta. In firmware si può prevedere una correzione d'invecchiamento, ad esempio contando le ore per canale e applicando un fattore ricavato dai dati LM-80 del LED scelto.
- La scelta mid-power SMD (package plastici) espone all'ingiallimento più degli high-power ceramici. È un punto a favore di emettitori ceramici o di package mid-power "high reliability".

### Gaps
- Disponibilità di LM-80 per specifici SMD 4-in-1/5-in-1 cinesi: non verificata, ed è probabilmente da chiedere al fornitore.

## B5 — Affidabilità outdoor: zolfo, VOC, silicone, coating, potting

### Takeaway
I due rischi chimici principali sono due. Il primo sono i VOC intrappolati in un apparecchio sigillato, che scuriscono il silicone (fino al −90 % di flusso in 450 h nel test Cree, reversibile ventilando). Il secondo è lo zolfo sui leadframe argentati, contro cui servono leadframe dorati o LED certificati IEC 60068-2-43. Coating e potting non vanno mai applicati sulla lente del LED.

### Cited Findings
- Cree XLamp Chemical Compatibility — [Cree LED Chemical Compatibility](https://downloads.cree-led.com/files/da/x/XLamp-Chemical-Compatibility.pdf):
  - meccanismo: i VOC diffondono nel silicone e scuriscono sotto calore e fotoni ad alta energia; blu, royal blue e bianco sono i più colpiti, amber, rosso e verde meno;
  - entità: in ambiente sigillato perdita di circa il 90 % del flusso in 450 h; LED ventilati a 325 h recuperano quasi tutto in 24 h; il fenomeno è spesso localizzato e reversibile;
  - sorgenti di outgassing: guarnizioni/O-ring, adesivi, conformal coating, potting, flussante, olio di lavorazione, FR-4 caldo; la maggior parte dei materiali emette durante la cura;
  - sostanze da evitare: aromatici (toluene, xilene), acetati, cianoacrilati, eteri glicolici, formaldeide/butadiene, cloro/candeggina;
  - coating risultati compatibili: Dow Corning 1-2577, 1-4105, 3-1953; Humiseal 1B51NS, 1B73, 1C49LV, 1H20AR1/S, UV40; Parylene; TechSpray Turbo-Coat 2108-P;
  - "non applicare conformal coating direttamente sulla lente del LED";
  - test di compatibilità consigliato: almeno 6 settimane / 1.000 h, materiale a contatto e in prossimità, LED di controllo; i problemi compaiono spesso entro 48 h.
- Studio Auburn/RTI (ECTC 2015) a 85 °C/85 % UR (JESD22-A101C) — [Lall, Zhang, Davis – OSTI](https://www.osti.gov/servlets/purl/1212875):
  - i VOC emessi da gomma ed epossidica hanno causato calo di flusso e shift verso il giallo;
  - il fenomeno è reversibile in ambiente pulito;
  - la gomma vulcanizzata è indicata come possibile sorgente di zolfo;
  - il silicone è stabile e resistente all'UV ma permeabile ai gas.
- Zolfo: Lumileds LUXEON HR30 (mid-power per ambienti aggressivi) usa un leadframe dorato. Ha superato IEC 68-2-43 a 15 ppm per 21 giorni con DLOP < 10 % e Δu'v' < 0,006 — [LEDinside](https://ledinside.com/node/25086)

### Inferences
- Per IP66/67 sigillato: guarnizioni in silicone a basso outgassing (non EPDM o gomma vulcanizzata a zolfo), nessun cianoacrilato, viti frenate con prodotti testati. Prima della chiusura, post-cura o "bake-out" dei materiali.
- Nei capitolati chiedere al fornitore dei LED SMD il test zolfo IEC 60068-2-43 o un leadframe senza argento esposto. Ponti, aree costiere e industriali sono i casi più critici.
- La resinatura PB-1561 già in uso in azienda va limitata a driver ed elettronica. Non deve coprire i LED, salvo prova di compatibilità di almeno 1.000 h con misura dello shift u'v' tramite lo spettrometro.

### Gaps
- Dati numerici sullo shift colore causato da conformal coating o potting sopra i LED (il white paper LED professional sulle protezioni non è stato recuperato).
- Statistiche sui modi di guasto tipici degli apparecchi RGB outdoor (ingresso acqua, connettori, driver): nessuna fonte trovata.
- Note specifiche di Nichia e Seoul sullo zolfo: non lette.

## B6 — Obiettivi termici per sorgenti multicolore in corpi sigillati

### Takeaway
I limiti assoluti del LUXEON C sono Tj max 120 °C per rosso/amber/PC-amber e 135 °C per i canali InGaN. Data la perdita dell'amber AlInGaP (−64 % di flusso a 85 °C), il vero vincolo è la stabilità del colore, non la Tj max.

### Cited Findings
- Tj max LUXEON C: 120 °C (Red, Red-Orange, Amber, PC Amber), 135 °C (InGaN e lime). Rth j-sp da 2,8 a 3,5 K/W — [Lumileds DS144](https://static.chipdip.ru/lib/021/DOC014021940.pdf)
- Amber diretto a 85 °C: rapporto caldo/freddo 0,36; PC-amber: 0,87 — [DOE – Epler](https://www.energy.gov/sites/default/files/2020/02/f71/ssl-rd2020-epler-amber.pdf)
- Il PC-amber subisce uno shift cromatico significativo con ΔTj di 50 °C, non con 30 °C — [DOE LM-80 color 2018](https://www.energy.gov/documents/sslrtilm80-color-ledsjuly2018pdf)
- Riferimento di mercato: CK RGBA da 8,1 W per 305 mm in alluminio estruso, ambiente fino a +50 °C — [scheda CK](https://www.docs.colorkinetics.com/specsheets/GrazeCompact_Color/Graze_Compact_Powercore_RGBA_100-277VAC_High_Power_30x60_305mm_1ft.pdf)

### Inferences
- Target di progetto proposto (inferenza, non da fonte): Tj ≤ 85 °C a +50 °C ambiente per i canali AlInGaP. Mantenere la ΔTj fra freddo e regime sotto ~30 °C per limitare gli shift. Derating firmware basato sull'NTC sulla scheda LED.
- Per la versione da 60 W/m servono probabilmente un profilo ad alette o un limite di potenza totale in modalità "full white" (somma canali). Questa seconda soluzione è comune nei prodotti multicanale ma non è stata verificata con una fonte.

### Gaps
- Linee guida pubblicate su Tj target e derating per apparecchi multicolore sigillati: nessuna fonte specifica trovata.

---

## Checklist finale delle scelte di progetto (sintesi)

| # | Scelta | Indicazione dalle fonti / inferenza |
|---|---|---|
| 1 | Canale amber | Preferire PC-amber (−0,6 nm e 0,87 caldo/freddo) all'AlInGaP (+5,6 nm e 0,36). Accettare la manutenzione LM-80 peggiore e pilotarlo a corrente ridotta |
| 2 | Configurazione | RGB+W(3000/4000K)+A per facciate; RGB+WW+CW se prevale il bianco regolabile. Validare con simulazione TM-30 sugli SPD reali |
| 3 | Package LED | Leadframe dorato o test zolfo IEC 60068-2-43 dichiarato; LM-80 per colore disponibile; preferire package ceramici o high-reliability |
| 4 | Ottica lineare | LINNEA-ZT25 come candidato wallwash dietro vetro; per 10x60° e grazing stretto qualificare B&M/LedLink con goniofotometro; vetro frontale come nel riferimento CK |
| 5 | Calibrazione | Misura XYZ per canale in fabbrica a T stabilizzata, matrice in NVS, gamut "accuracy" comune per bianchi e pastelli, saturi liberi; obiettivo < 2 SDCM (come Chromasync) |
| 6 | Compensazione T | NTC sulla scheda LED; LUT flusso(T) per canale, con priorità a rosso e amber; dλ/dT 0,06 nm/°C per AlInGaP contro 0,03–0,04 per InGaN |
| 7 | Termica | Tj ≤ ~85 °C per i canali AlInGaP a +50 °C ambiente (inferenza); limite di potenza totale in full white |
| 8 | Materiali sigillati | Guarnizioni in silicone a basso outgassing, niente cianoacrilati né solventi aromatici, bake-out, test di compatibilità ≥ 1.000 h |
| 9 | Coating/potting | Mai sulla lente del LED; coating della lista Cree solo sull'elettronica; resina PB-1561 solo sul driver |
| 10 | Durata | Contatore di ore per canale nel firmware per la compensazione dell'invecchiamento (soprattutto PC-amber e verde) |
