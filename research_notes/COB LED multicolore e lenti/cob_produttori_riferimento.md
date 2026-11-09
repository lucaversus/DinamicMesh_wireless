# Sorgenti COB e multi-chip multicolore dei produttori di riferimento (occidentali, giapponesi, coreani) per proiettori architetturali da esterno a 5 canali

Note di ricerca: 9 novembre 2026. Gli accessi alle pagine sono avvenuti in questa data, salvo diversa indicazione. Verificati direttamente: Luminus CTM-X RGBW (datasheet), Luminus SBM-40-RGBW (DigiKey, con prezzi), ams OSRAM OSTAR Stage LE RTDUW S2WP (pagina prodotto + datasheet v1.15), Cree LED XLamp XM-L Color Gen 2 (Mouser), Bridgelux RGBW 3838 (sell sheet), portafoglio colore Lumileds (pagina ufficiale), ottiche Ledil RGBX e Carclo per OSTAR Stage. Restano da verificare: Nichia, Seoul, Samsung, Everlight, LG Innotek e Citizen (vedi Gaps).

---

## 1. Quali prodotti multicolore esistono davvero e sono in produzione (nov 2026)? Configurazione dei canali

### Takeaway
Nessun produttore di riferimento verificato offre oggi una sorgente a 5 canali (RGBWA o RGB+CCT) in un unico package. L'offerta reale è RGBW a 4 canali:
- Luminus CTM-9 e CTM-14 RGBW: COB con LES unico da 9,5 e 14,5 mm.
- Luminus SBM-40-RGBW: SMD 4-in-1, stato Active su DigiKey.
- ams OSRAM OSTAR Stage LE RTDUW S2WP: SMD 4-die, "Full production". Esiste anche una variante RGBCY.
- Cree XLamp XM-L Color Gen 2: 5×5 mm, 4 die.
- Bridgelux RGBW 3838: mid-power.

Lumileds non ha COB colore né emettitori multi-die high-power: ha solo il LUXEON 5052 RGBW mid-power e singoli colori da comporre su PCB.

### Cited Findings

**Tabella riassuntiva dei prodotti verificati**

| Produttore / prodotto | Tipo | Canali | Stato | Fonte |
|---|---|---|---|---|
| Luminus CTM-9-RGBW-12-TW01 | COB, LES 9,5 mm, board 12×15 mm | R, G, B, bianco caldo 2700 K CRI≥90 (niente ambra) | Datasheet "Preliminary", PDS-003116 Rev.03, senza data | [Luminus CTM-X RGBW datasheet](https://download.luminus.com/datasheets/Luminus_CTM-X-RGBW_Datasheet.pdf) |
| Luminus CTM-14-RGBW-24-TW01 | COB, LES 14,5 mm, board 20×24 mm | R, G, B, WW 2700 K CRI≥90 | come sopra | [Luminus CTM-X RGBW datasheet](https://download.luminus.com/datasheets/Luminus_CTM-X-RGBW_Datasheet.pdf) |
| Luminus SBM-40-RGBW-LC41-QC100 | SMD 4-in-1, 5,75×4,68×1,31 mm | R 622, G 527, B 455 nm, W | **Active** (DigiKey), lead time 6 settimane | [DigiKey SBM-40-RGBW](https://azcus.digikey.com/en/products/detail/luminus-devices-inc/SBM-40-RGBW-LC41-QC100/15903654) |
| ams OSRAM OSTAR Stage LE RTDUW S2WP | SMD multi-chip con finestra in vetro, 6,38×5,75×1,26 mm | Red, True Green, Deep Blue, Ultra White | **Full production** (entrambi i codici ordine) | [ams OSRAM LE RTDUW S2WP](https://ams-osram.com/products/leds/multi-color-leds/osram-osram-ostar-stage-le-rtduw-s2wp) |
| OSTAR Stage, variante RGBCY | SMD | R, G, B, ciano(?), giallo(?): il significato delle lettere non è confermato | citata dal produttore, codice non trovato | [ams OSRAM famiglia OSTAR Stage](https://ams-osram.com/products/product-families/osram-ostar-stage); [Carclo](https://www.carclo-optics.com/osram-ostarr-stage-le-uw-s2wn) |
| Cree LED XLamp XM-L Color Gen 2 | SMD 5×5 mm, 4 die indirizzabili | R, G, B, W (W 5700-8000 K oppure 3700-4300 K) | a catalogo su Mouser (stock "Stokta Var") | [Mouser XM-L Color G2](https://www.mouser.com.tr/cree-xlamp-xml-color-g2-leds) |
| Bridgelux RGBW 3838 | 4-in-1, 3,8×4,0×0,8 mm (mid-power, 0,36 W/canale) | R, G, B, W (W tunable 1800-6500 K, CRI 90/95) | sell sheet del 30/01/2024 | [Bridgelux RGBW sell sheet](https://www.BRIDGELUX.com/sites/default/files/2024-02/product_sell_sheet_-_bridgelux_rgbw_products_20240130.pdf) |
| Lumileds LUXEON 5052 RGBW | 4-in-1 mid-power, 120 mA | RGBW, con blue o royal blue + bianco 2200-6500 K | a catalogo | [Lumileds Color LEDs](https://lumileds.com/products/color-leds) |

**Altre informazioni sui singoli produttori**
- Lumileds: la sezione CoB del catalogo contiene solo CoB bianchi (CrispColor, FreshFocus), nessun CoB RGB o multicolore. LUXEON MZ è solo bianco. I prodotti high-power a colore singolo (LUXEON C Color Line con 14 colori + bianco, CZ, Z Color Line, Rubix fino a 1,6 A, HL1Z) servono a comporre cluster multicolore su PCB. Il catalogo non indica PC amber né lime nella sezione colore — [Lumileds Color LEDs](https://lumileds.com/products/color-leds)
- Cree LED (pagina Mouser "Architectural & Entertainment", pubblicata 06/08/2024 e aggiornata 04/09/2024): i multicolore elencati sono XM-L Color Gen 2 (RGBW, 5×5 mm, fino a 1,75 A, "+75% rispetto alla prima generazione"), XLamp Element G (XE-G, miscelazione colori), CLQ6B 4-in-1 RGBW SMD, CLW6A 4-in-1 PLCC8, CLX6E 3-in-1 PLCC6 IPX8 e CLV1H-FKB. Non compaiono XHP colore, MC-E, XP-E2 multicolore né CXA colore — [Mouser Cree A&E](https://www.mouser.in/new/cree/cree-led-architectural-entertainment-lighting)
- ams OSRAM: la famiglia OSTAR Stage usa "high-power RGBW chips" e "includes an RGBCY variant". LE UW S2WN e LE UW S2WP sono elencati fra i multicolore, ma la pagina non spiega le sigle — [ams OSRAM OSTAR Stage](https://ams-osram.com/products/product-families/osram-ostar-stage)
- Luminus: in un listino distributore (Dasenic) per "Multi-Color High Power" compare solo la serie SBM-40 RGB+W — [Dasenic Luminus multi-color](https://static-lang.dasenic.com/manufacturers/luminus/multi-color-high-power-leds)

### Inferences
- Una sorgente a 5 canali richiede un'architettura composta, per esempio:
  - un emettitore RGBW (OSTAR Stage, SBM-40, XM-L Color) più un emettitore ambra separato;
  - oppure un cluster di single-colour (Lumileds LUXEON C/CZ Color Line, che include ambra e PC amber secondo il catalogo storico; da verificare);
  - oppure un COB RGBW con un secondo COB bianco a CCT diversa.
- Il CTM RGBW ha un solo bianco a 2700 K. Per RGB+CCT serve quindi un secondo canale bianco esterno.
- Per i proiettori 20-300 W i COB CTM (max circa 13 W e 26 W totali) bastano solo per i modelli piccoli. Per le potenze alte servono più sorgenti per apparecchio, cioè array di OSTAR Stage o SBM-40 sotto ottiche singole.

### Gaps
- Non ho trovato una pagina di stato ufficiale Luminus (attivo/NRND) per CTM-9/CTM-14 RGBW: il datasheet è ancora "Preliminary" e la pagina DigiKey non era accessibile.
- Il codice ordine e i dati della variante OSTAR Stage RGBCY non sono stati trovati.
- Lo stato attuale (lifecycle) di Cree XM-L Color Gen 2 non è confermato da una pagina Cree ufficiale: è presente su Mouser ma senza indicazione NRND.
- Nichia, Seoul Semiconductor (SunLike è una tecnologia di bianco), Samsung, Everlight, LG Innotek e Citizen non sono stati verificati in questa ricerca. Le uniche notizie Samsung COB trovate riguardano COB bianchi a LES piccolo ([LEDs Magazine](https://www.ledsmagazine.com/architectural-lighting/retail-hospitality/article/16696705/samsung-adds-cob-leds-with-smaller-les-options-and-vivid-color)). Dalla mia conoscenza pregressa, **non verificata**: Citizen CLU e Bridgelux Vesta sono COB tunable white (2 canali, solo bianco) e non RGB. Da confermare prima dell'uso. **Correzione (9/11/2026):** Bridgelux Vesta esiste anche in versione RGBW D10/D13 (sell sheet Rev. A 04/2025), vedi [analisi](../../docs/sorgente-bridgelux-vesta.md).
- Luminus SST-90-RGBW e altri multicolore Luminus storici: il download del datasheet SST-90-RGBW non è riuscito. Esistenza e stato non sono verificati.

---

## 2. Dati elettrici e ottici per canale (Vf, corrente, potenza, flusso, lunghezze d'onda, CCT/CRI)

### Takeaway
L'OSTAR Stage S2WP è l'emettitore compatto più potente fra quelli verificati:
- fino a 5 A per die;
- verde 355-710 lm e bianco 450-710 lm a 1,4 A;
- circa 15,6 W totali a 1,4 A.

Il COB Luminus CTM-14 offre un LES unico da 14,5 mm ma solo circa 6,5 W massimi per canale.

### Cited Findings

**Luminus CTM-X RGBW** (valori per canale, Tj 85 °C) — [datasheet](https://download.luminus.com/datasheets/Luminus_CTM-X-RGBW_Datasheet.pdf)

| Parametro | CTM-9 | CTM-14 |
|---|---|---|
| Corrente nominale / max | 200 / 250 mA | 200 / 250 mA |
| Tensione nominale / max (canale) | 12 / 13 V | 24 / 26 V |
| Potenza nominale / max (canale) | 2 / 3,25 W | 4 / 6,5 W |
| Blu 455-460 nm (min/nom) | 52 / 58 lm | 104 / 115 lm |
| Rosso 620-630 nm | 42 / 47 lm | 84 / 94 lm |
| Verde 525-535 nm | 300 / 325 lm | 600 / 650 lm |
| Bianco 2700 K CRI≥90 | 197 / 219 lm | 394 / 438 lm |
| Angolo di emissione | 130° | 130° |

- Il datasheet avverte che il funzionamento di tutti i canali alla corrente nominale richiede un sistema termico dimensionato. Dichiara angoli di sistema ottenibili da 10° a 40° — [datasheet](https://download.luminus.com/datasheets/Luminus_CTM-X-RGBW_Datasheet.pdf)
- Le tensioni di 12 V e 24 V per canale indicano stringhe di più die in serie, cioè un driver CC con tensione di uscita sufficiente — [datasheet](https://download.luminus.com/datasheets/Luminus_CTM-X-RGBW_Datasheet.pdf)

**ams OSRAM OSTAR Stage LE RTDUW S2WP** (datasheet v1.15 del 18/02/2025, test a 1400 mA) — [datasheet via Mouser](https://www.mouser.lt/datasheet/3/5912/1/LE_RTDUW_S2WP_EN.pdf)

| Colore | λdom tipica (range) | Flusso a 1400 mA (bin, due varianti) | Vf tipica (min-max) | Potenza (pagina prodotto) |
|---|---|---|---|---|
| Rosso | 625 nm (620-632) | 140-280 lm / 112-280 lm | 2,35 V (1,90-2,80) | 3,3 W |
| True Green | 530 nm (524-536) | 355-710 lm / 280-560 lm | 2,80 V (2,20-3,20) | 3,9 W |
| Deep Blue | 453 nm (449-457) | 1800-2800 mW / 1400-2800 mW (radiometrico) | 3,00 V (2,80-3,50) | 4,2 W |
| Ultra White | Cx 0,321 / Cy 0,327, picco 443 nm | 450-710 lm / 355-710 lm | 3,00 V (2,80-3,50) | 4,2 W |

- Corrente massima 5000 mA (Ts 25 °C), corrente minima 40 mA — [datasheet](https://www.mouser.lt/datasheet/3/5912/1/LE_RTDUW_S2WP_EN.pdf)
- Le potenze per colore e i codici ordine (LERTDUWS2WP-LAMB-1+NAPA-P+ABBB-P+NBPB-BQ, Q65112A5475; LERTDUWS2WP-LBMB-1+NBPB-P+BABB-P+PAPB-BQ, Q65113A5243) vengono dalla [pagina prodotto ams OSRAM](https://ams-osram.com/products/leds/multi-color-leds/osram-osram-ostar-stage-le-rtduw-s2wp). Nota: la pagina prodotto riporta per la lunghezza d'onda range più larghi del datasheet (rosso 612-630, verde 513-545, blu 439-461 nm). Fa fede il datasheet.

**Luminus SBM-40-RGBW-LC41-QC100** (700 mA, 25 °C) — [DigiKey](https://azcus.digikey.com/en/products/detail/luminus-devices-inc/SBM-40-RGBW-LC41-QC100/15903654)
- Rosso 622 nm: 68 lm, Vf 2,3 V.
- Verde 527 nm: 168 lm, Vf 3,2 V.
- Blu 455 nm: 865 mW, Vf 3,2 V.
- Bianco: 182 lm, Vf 3,2 V.
- Corrente massima 1 A per colore.

**Cree XM-L Color Gen 2** (flusso minimo a 350 mA) — [Mouser](https://www.mouser.com.tr/cree-xlamp-xml-color-g2-leds)
- Rosso 620-630 nm: 45,7 lm, Vf 2,25 V.
- Verde 520-535 nm: 87,4 lm, Vf 3,3 V.
- Blu 450-465 nm: 13,9 lm, Vf 3,1 V.
- Bianco: 80-100 lm, Vf 3,1 V.
- Corrente massima 1,75 A per die.

**Bridgelux RGBW 3838** (120 mA, 3,0 V, 0,36 W per canale) — [sell sheet](https://www.BRIDGELUX.com/sites/default/files/2024-02/product_sell_sheet_-_bridgelux_rgbw_products_20240130.pdf)
- Rosso 618 nm: 14,3 lm.
- Verde 535,2 nm: 77 lm.
- Blu 457,5 nm: 8,1 lm.
- Bianco 2500 K: 58 lm.

### Inferences
- L'ambra non è presente in nessuna sorgente RGBW verificata, quindi va aggiunta come emettitore separato. La scelta fra AlInGaP diretto e PC amber resta aperta: l'AlInGaP perde molto flusso a caldo, critico con 50 °C ambiente.
- La derating termica del rosso è visibile nel CTM: 47 lm a Tj 85 °C contro valori più alti a 25 °C (da datasheet completo). Per l'OSTAR la derating va letta dalle curve del datasheet (non estratte).
- Per un bilanciamento tipo bianco D65 con RGB, il rosso è il canale limitante in tutte le sorgenti: nel CTM-14 sono 94 lm di rosso contro 650 lm di verde.

### Gaps
- Le curve di derating flusso/temperatura per rosso e ambra non sono state estratte (né Luminus né OSRAM).
- Il CRI del bianco OSTAR Stage non è riportato nell'estratto. Il bianco è "Ultra White", a coordinate di circa 6000-6500 K: è una mia stima, da verificare.
- Il CRI del bianco XM-L Color non è indicato.
- Non sono disponibili dati LM-80/TM-21 per nessuno dei prodotti multicolore verificati.

---

## 3. LES, miscelazione alla sorgente, resistenza termica, Tj max

### Takeaway
Solo i Luminus CTM sono veri COB con LES unico circolare: 9,5 e 14,5 mm, con Rth j-c 1,8 e 0,67 K/W. L'OSTAR Stage ha i 4 die in un'area di 2,5×3,2 mm, con Rth j-s reale di 0,70 K/W tipica. Gli altri prodotti hanno die separati in package 5-6 mm, che richiedono ottiche con sublente di miscelazione.

### Cited Findings
- **CTM-9**: LES 9,5 mm, Rth j-c 1,8 K/W. **CTM-14**: LES 14,5 mm, Rth j-c 0,67 K/W. Per entrambi:
  - Tj max 125 °C;
  - Tcase max 105 °C;
  - ambiente da −40 a +85 °C;
  - PCB da 1 mm;
  - ESD 2 kV HBM.

  — [Luminus datasheet](https://download.luminus.com/datasheets/Luminus_CTM-X-RGBW_Datasheet.pdf)
- **OSTAR Stage S2WP**:
  - 4 die (tecnologia Thinfilm/UX:3) con superficie radiante "Acolor typ. 2.5 x 3.2 mm²";
  - Rth j-s reale 0,70 K/W tipica (0,80 max), elettrica 0,50 K/W tipica;
  - Tj max 125 °C;
  - operatività da −40 a +85 °C;
  - finestra in vetro;
  - pin separati per colore (1-2 R, 3-4 B, 5-6 G, 7-8 W).

  — [datasheet](https://www.mouser.lt/datasheet/3/5912/1/LE_RTDUW_S2WP_EN.pdf)
- **XM-L Color Gen 2**: Tj max 150 °C, 130°, ESD 8 kV; Rth non indicata nella pagina — [Mouser](https://www.mouser.com.tr/cree-xlamp-xml-color-g2-leds)
- **SBM-40-RGBW**: package 2318 (5847 metrico); LES non indicato — [DigiKey](https://azcus.digikey.com/en/products/detail/luminus-devices-inc/SBM-40-RGBW-LC41-QC100/15903654)

### Inferences
- A −40/+50 °C ambiente con IP66/67 (corpo chiuso), una Tcase di 105 °C per il CTM lascia margine ragionevole. Va però verificato con prova termica a tutti i canali accesi.

### Gaps
- Mancano le Rth di XM-L Color Gen 2 e SBM-40-RGBW (vanno lette dai datasheet completi, non estratti).
- La disposizione dei die nel LES del CTM (quanto è uniforme la miscela) non è descritta nel datasheet.

---

## 4. Binning, disponibilità, MOQ, prezzi

### Takeaway
L'unico prezzo verificato è quello del Luminus SBM-40-RGBW su DigiKey: da 7,35 USD (1 pezzo) a 4,49 USD (1.500 pezzi, bobina), in stock 493 pezzi, lead time 6 settimane. Non sono stati ottenuti prezzi verificati per OSTAR Stage, CTM e XM-L Color.

### Cited Findings
**Prezzi DigiKey per SBM-40-RGBW-LC41-QC100** (USD, consultati il 09/11/2026; possibili dazi per spedizioni USA) — [DigiKey](https://azcus.digikey.com/en/products/detail/luminus-devices-inc/SBM-40-RGBW-LC41-QC100/15903654)

| Quantità | Prezzo unitario (USD) | Confezione |
|---|---|---|
| 1 | 7,35 | Cut Tape / Digi-Reel |
| 10 | 5,562 | Cut Tape / Digi-Reel |
| 100 | 4,5154 | Cut Tape / Digi-Reel |
| 500 | 4,74886 | Tape & Reel (MOQ bobina 500) |
| 1.000 | 4,5754 | Tape & Reel |
| 1.500 | 4,48663 | Tape & Reel |

- Prezzi di un listino terzo (Dasenic) per la "SBM-40 Series", valuta indicata come "$" senza specifica, codice esatto non indicato: 1+ 40,00; 10+ 25,74; 100+ 20,00; 250+ 18,01. Sono molto diversi da DigiKey: fonte poco affidabile, da non usare — [Dasenic](https://static-lang.dasenic.com/manufacturers/luminus/multi-color-high-power-leds)
- **Binning OSTAR Stage**: due codici ordine con finestre di flusso diverse (vedi tabella al punto 2). La lunghezza d'onda dominante è contenuta in range di ±6 nm circa — [datasheet](https://www.mouser.lt/datasheet/3/5912/1/LE_RTDUW_S2WP_EN.pdf)
- **Binning CTM**: solo cromaticità del bianco, ellisse a 3 step:
  - centro x 0,4645 / y 0,4110;
  - a = 0,00964, b = 0,00421, θ = 54,39°.

  Nessun bin di flusso, solo valori min/nom — [Luminus datasheet](https://download.luminus.com/datasheets/Luminus_CTM-X-RGBW_Datasheet.pdf)

### Gaps
- Prezzi OSTAR Stage S2WP/S2WN (DigiKey/Mouser/Farnell/RS/TME): le pagine sono state trovate ma non lette, quindi nessun prezzo riportato. Pagine da controllare: [DigiKey S2WN](https://www.digikey.co.uk/en/products/detail/ams-osram-usa-inc/LE-RTDUW-S2WN-KBLA-1-MANA-P-AXAZ-P-MBNB-CQ/9999358), [Farnell S2WN](https://il.farnell.com/ams-osram-group/le-rtduw-s2wn/led-hb-red-green-blue-white-smd/dp/2630065), [RS IT 9154702P](https://it.rs-online.com/web/p/led/9154702P), [RS UK S2WP 1709603](https://uk.rs-online.com/web/p/leds/1709603).
- Prezzi Luminus CTM-9/14 RGBW: DigiKey bloccato (robots).
- Prezzi Cree XM-L Color Gen 2: Mouser non mostra importi nella pagina letta.
- Mancano i MOQ di fabbrica e i lead time per tutti gli altri prodotti.

---

## 5. Ottiche consigliate e partner (Ledil, Carclo, Khatod, Gaggione)

### Takeaway
Per OSTAR Stage esistono ottiche Carclo dedicate, cinque codici per LE UW S2WN. Ledil RGBX (30 mm, con sublente di miscelazione) è ottimizzata per Cree XM-L RGB, Osram Ostar-SMT RGB e Cree MC-E, non per OSTAR Stage né per i Luminus. Per i COB CTM il datasheet non indica ottiche.

### Cited Findings
- Ledil RGBX, tutte con holder, 30-30,4 mm di lato, altezza 28-28,8 mm — [Ledil RGBX datasheet](https://www.ledil.com/data/prod/RGBX/RGBX-fds.pdf):

| Codice | LED | Fascio |
|---|---|---|
| CP13682_RGBX2-S | XM-L RGB | ~20° |
| CP13938_RGBX2-M | XM-L RGB | ~30° |
| CP13939_RGBX2-O | XM-L RGB | ovale ~50°×24° |
| CP10960_RGBX-SS | Ostar-SMT | ~20° |
| CP10961_RGBX-SS | MC-E | ~20° |
| CP10944_RGBX-M | MC-E | ~30° |

  Ledil avverte che l'angolo varia con colore, dimensione e posizione del chip.
- Carclo per OSTAR Stage LE UW S2WN: codici 10048, 10393, 10406, 10628, 10759. Angoli e diametri non riportati nella pagina — [Carclo](https://www.carclo-optics.com/osram-ostarr-stage-le-uw-s2wn)
- ams OSRAM dichiara "off-the-shelf optics are available" per OSTAR Stage — [ams OSRAM famiglia](https://ams-osram.com/products/product-families/osram-ostar-stage)
- Il datasheet Luminus CTM indica solo angoli di sistema da 10° a 40°, senza partner ottici — [datasheet](https://download.luminus.com/datasheets/Luminus_CTM-X-RGBW_Datasheet.pdf)
- Esistono riflettori Ledil Mirella 50 (CN13905/06/07 S/M/W PF RZL), ma la loro compatibilità con sorgenti multicolore non è verificata nei risultati: sono comparsi solo come PDF di terze parti — [70ic Mirella 50 S](https://70ic.com/629626/CN13905MIRELLA-50-S-PF-RZL.pdf)

### Inferences
- Per OSTAR Stage S2WP (RGBW) le ottiche Carclo per S2WN sono probabilmente compatibili come footprint, ma va verificato con il configuratore Carclo/Ledil.

### Gaps
- Non ho trovato liste di compatibilità Khatod o Gaggione per sorgenti RGBW.
- Non ho trovato ottiche/riflettori Ledil specifici per CTM-9/14 RGBW: con LES da 9,5 e 14,5 mm sono plausibili i riflettori per COB della stessa taglia, ma è da verificare.

---

## 6. Holder/montaggio, uso esterno (zolfo, umidità), uso in apparecchi architetturali noti

### Takeaway
L'unico dato di robustezza alla corrosione trovato è OSTAR Stage S2WP in classe 3B, testato a 40 °C / 90 % UR / 15 ppm H2S per 14 giorni. Nessuna fonte trovata collega questi LED a modelli specifici di Color Kinetics, Lumenpulse, SGM o Martin.

### Cited Findings
- OSTAR Stage S2WP: corrosion robustness class 3B (40 °C, 90 % UR, 15 ppm H2S, 14 giorni), finestra in vetro, ESD 2 kV — [datasheet](https://www.mouser.lt/datasheet/3/5912/1/LE_RTDUW_S2WP_EN.pdf)
- OSTAR Stage è un prodotto per "Stage/Entertainment Applications" — [ams OSRAM](https://ams-osram.com/products/leds/multi-color-leds/osram-osram-ostar-stage-le-rtduw-s2wp)
- Il Bridgelux RGBW 3838 è indicato per applicazioni architetturali e piscine/fontane — [Bridgelux](https://www.BRIDGELUX.com/sites/default/files/2024-02/product_sell_sheet_-_bridgelux_rgbw_products_20240130.pdf)
- Il CTM RGBW è su board PCB (12×15 e 20×24 mm) e non come COB ceramico standard. Il datasheet non indica holder TE, Ideal o BJB — [Luminus](https://download.luminus.com/datasheets/Luminus_CTM-X-RGBW_Datasheet.pdf)

### Inferences
- I prodotti SMD (OSTAR Stage, SBM-40, XM-L Color) vanno saldati a rifusione su MCPCB, quindi non c'è un holder solderless. I CTM sono board con pad di saldatura: un holder dedicato va verificato con il produttore.
- In un apparecchio IP66/67, sigillato e con eventuale guarnizione in EPDM o silicone, la resistenza allo zolfo conta comunque. La classe 3B OSRAM è un dato utile; per gli altri prodotti va chiesto al produttore.

### Gaps
- Nessun dato di resistenza allo zolfo o all'umidità per Luminus CTM/SBM, Cree XM-L Color o Bridgelux.
- Nessuna fonte documenta quali sorgenti montano Color Kinetics, Lumenpulse (Opticolor+), SGM o Martin Exterior: i produttori di apparecchi in genere non lo dichiarano.
- Hanno restituito errori o blocchi: datasheet OSTAR S2WN (osram dam), DigiKey CTM, datasheet Luminus SST-90.
