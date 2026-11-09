# Ottiche (lenti TIR, riflettori, ottiche colour-mixing) per COB multicolore e LED multi-chip in proiettori architetturali da esterno

Note di ricerca raccolte il 9/11/2026. Tutte le fonti sono state consultate in quella data. Dove un dato non si è trovato è segnalato nelle "Gaps": nessun prezzo o dato tecnico è stato stimato.

## 1. Produttori e famiglie di ottiche per sorgenti multicolore (RGBW / RGBA / multi-chip)

### Takeaway
Le famiglie "colour mixing" documentate e verificate sono LEDiL (RGBX, GABRIELLA/GABRIELLA-MIDI, HEKLA-SOCKET-RZ con lenti AMY/YASMEEN/ZORYA, riflettori ANGELINA per COB fino a LES 32 mm con sublente di miscelazione opzionale), Gaggione (LLC59x, collimatore Ø45 mm, fino a circa 4-6° FWHM su sorgente RGBW da 4 mm²) e Khatod (lenti RGBW Ø35/Ø45 mm da 8° a 40°, PMMA, >90% di efficienza, -40/+90 °C, con Moving Lenslet Array opzionale). Per LedLink c'è un catalogo verificabile, con lenti COB e lenti per Cree MC-E RGBW e prezzi da distributore. Per "B&M lens" non si trova un catalogo pubblico affidabile.

### Cited Findings

**LEDiL (Finlandia)**
- RGBX: lenti TIR da Ø30,4 mm "for RGBW colour mixing", per package RGB fino a 5050. Hanno una sublente di miscelazione a scatto e un holder; il fascio passa da spot a medium o da spot a ovale cambiando la sublente — [LEDiL RGBX datasheet](https://www.ledil.com/data/prod/RGBX/RGBX-fds.pdf)

| Codice | Dim. (mm) | H (mm) | Fascio (~FWHM) | LED compatibile |
|---|---|---|---|---|
| CP13682_RGBX2-S | 30,4×30,4 | 28,20 | 20° spot | Cree XM-L RGB |
| CP10960_RGBX-SS | 30,0×30,0 | 28,00 | 20° smooth spot | Osram Ostar-SMT RGB |
| CP13938_RGBX2-M | 30,4×30,4 | 28,20 | 30° medium | Cree XM-L RGB |
| CP10961_RGBX-SS | 30,4×30,4 | 28,80 | 20° smooth spot | Cree MC-E |
| CP10944_RGBX-M | 30,4×30,4 | 28,80 | 30° medium | Cree MC-E RGB |
| CP13939_RGBX2-O | 30,4×30,4 | 28,20 | 50°+ × 24° ovale | Cree XM-L RGB |

  Fonte della tabella: [LEDiL RGBX datasheet](https://www.ledil.com/data/prod/RGBX/RGBX-fds.pdf). Il datasheet non indica efficienza, temperatura di esercizio né materiale. Avverte inoltre che l'angolo reale "varia con colore, dimensione del chip e tolleranza di posizione del chip".
- GABRIELLA-MIDI è una lente RGB e tunable white con superficie a microstruttura (esagonale "floret") "for near perfect colour uniformity", pensata per illuminazione architetturale indoor/outdoor, palco e flood. È ottimizzata per LED RGB 5050 e compatibile con i 7070 (OSRAM OSTAR Stage, Cree XM-L Colour, LEDengin LZ4). Esiste nelle varianti S (stretto, lunga gittata), M (più luce verso il basso, per proiettore inclinato), O (ovale) e W. Si monta con biadesivo, viti opzionali e pin di posizionamento. Ci stanno il 44% di LED in più su un PAR64 rispetto alla GABRIELLA-45 — [LEDiL news GABRIELLA-MIDI](https://www.ledil.com/news_all/gabriella-midi-rgb-and-tunable-white-colour-mixing-lens/)
- Diametri GABRIELLA: 38 mm (MIDI), 37,8 mm (MIDI-M), 45 mm (GABRIELLA-45) — [Mouser, pagina GABRIELLA](https://www.mouser.fr/new/ledil/ledil-gabriella-lenses)
- CA16204_GABRIELLA-MIDI-W: 35°, PMMA, Ø37,8 mm, H 21,51 mm. La descrizione della stessa pagina riporta invece Ø37,5 / H 24,2 mm (dato incoerente) — [RS Irlanda](https://ie.rs-online.com/web/p/led-lenses-reflectors/2066656)
- GABRIELLA-45 è disponibile come kit lente + holder: CX15818 (medium 23°) e CX15819 (wide 31°) — [RS UK 1741244](https://uk.rs-online.com/web/p/led-lenses-reflectors/1741244?gb=s); [RS UK 1741245](https://uk.rs-online.com/web/p/led-lenses-reflectors/1741245?gb=s)
- HEKLA-SOCKET-RZ (C19950) è un socket con "integrated RGBW mixing dome" che, secondo LEDiL, elimina distorsione cromatica e fringing. È compatibile con Bridgelux 10RGBW e 13RGBW, cluster RGBW custom e moduli RGBW a 4 chip. Accetta senza modifiche le ottiche AMY-50/70/110, YASMEEN-50/70 e ZORYA. Si fissa con 2 viti, interasse 35 mm, ed è compatibile con PCB Zhaga Book 10. LEDiL lo considera più adatto al colour mixing della HEKLA-RZ-LENS, che è orientata al tunable white — [LEDiL news HEKLA-SOCKET-RZ](https://www.ledil.com/news_all/hekla-socket-rz-‒-your-effortless-entry-to-the-rgbw-world/)
- ANGELINA è un riflettore di sistema Ø82 mm, H 31 mm, per COB fino a 32 mm di LES, con sublente di colour mixing opzionale. Varianti: S ~20° (F13325), M ~30° (F13401), W ~50° (F13402), XW ~91° (F13838), più le versioni -B per connettori BJB e B+W. Il testo introduttivo dello stesso datasheet dà angoli diversi (17°/28°/45°). Anche qui vale l'avvertenza che l'angolo cambia con colore, dimensione e posizione dei chip — [LEDiL ANGELINA datasheet](https://www.ledil.com/data/prod/Angelina/Angelina-fds.pdf)
- La guida LEDiL alle lenti TIR classifica la capacità di miscelazione per tipo di fascio. Real Spot (4-25° FWHM): nessuna miscelazione, perché il design esclude gli elementi di mixing. Smooth Spot (8-25°) e Oval (8-20° × 40-50°): bassa. Diffused Spot (8-25°, con superficie superiore diffondente), Medium (18-35°) e Wide (35-80°): moderata. Il picco cd/lm è "very high" per Real Spot e "very low" per Wide — [LEDiL Guide to TIR lenses](https://ledil.com/?p=2148)

**Gaggione / Lednlight (Francia)**
- LLC59x è un collimatore Ø45 mm con porta d'ingresso da 10 mm, compatibile secondo il produttore con "all existing multi colour solutions" (multi-chip e cluster di single-chip). Dal grafico, misurato con LED RGBW flat-top da 4 mm², si leggono: LLC59U (ultra narrow) ~5,7° FWHM / ~6,2° FWTM; LLC59N ~10,1° FWHM; LLC59C ("colour" narrow) ~11,6° FWHM / ~18,3° FWTM. Il testo invece dichiara "4° FWHM with 1 mm² LES" per la U e "<10°" per la C, e i valori della N risultano incoerenti (FWTM minore di FWHM): sono da verificare col produttore. La U offre "extreme beam consistency and cut-off", la N è un "compromesso fra angolo e miscelazione" — [Gaggione Focus On LLC59x (CDI)](https://led.cdiweb.com/Datasheets/gaggione/Gaggione-Focus-On-LLC59x.pdf). Esiste anche un datasheet LLC59x del 20/10/2021 nel catalogo espositori di Light+Building — [Messe Frankfurt](https://exhibitorsearch.messefrankfurt.com/images/original/mics/10000016202401/0012161525/1658849682477_DATASHEET_LLC59x_20.10.2021.pdf) (non letto)

**Khatod (Italia)**
- Lenti RGBW colour mixing Ø35 mm e Ø45 mm, da 8° (ultra-narrow) a 40°. Con il Moving Lenslet Array (MLA) opzionale montato sopra si ottiene uno zoom 12-50°. Efficienza ottica >90% dichiarata su tutto il range, materiale PMMA ottico, temperatura di esercizio e stoccaggio da -40 a +90 °C — [LED professional, 2013](https://led-professional.com/products/led-optics/khatod-unveils-its-newest-series-of-ultra-narrow-color-mixing-optics)
- Codici attuali in catalogo "Color Mixing Lenses" (4 pagine di risultati): PL1564 (MLA narrow/medium/wide), PL1590UN e PL1545UN (ultra narrow), PL1545NA e PL1590NA (narrow), PL1590ME, PL113320 e PL113325 (medium), PL113310 (narrow), PL113335 (wide). Khatod scrive che le lenti mescolano i 4 fasci RGBW "without chromatic dispersion" e che le ottiche non trasmettono UV né calore — [Khatod Color Mixing Lenses](https://khatod.com/en/products/general-led-lighting/lenses/color-mixing-lenses)

**LedLink Optics (Taiwan/Cina)**
- Si presenta come "expertise in designing and manufacturing optics for emerging solid state lighting companies". Su Mouser ha serie per street lighting (3030/3535/5050), "Lenses, Reflectors & Holders" e lenti secondarie per LED di potenza Cree e Osram — [Mouser LedLink Optics](https://www.mouser.in/en/manufacturer/ledlink-optics/)
- LL01CR-BCQxxL06 è una lente per Cree MC-E RGBW. LL01CR-BCQ15L06: 18° FWHM / 35° field angle. LL01CR-BCQ1530L06 (ellittica): 16°×30° FWHM / 32°×51° field. Valori nel datasheet probabilmente in cd/lm: 6,6 e 4,6. Diametro 34,75 mm, H 19,25 mm, PMMA ottico, trasmittanza media 400-700 nm >90%, esercizio da -40 a +70 °C (max +80 °C) — [Datasheet LedLink MC-E RGBW](https://storage.sea.com.ua/tech_info/LEDlink/LL01ED-BCQxxL06_CREE%20MC-E%28RGBW%29.pdf)
- LL01ZZ-DRY38L06-M2 è una lente singola per COB, 38°, Ø68,5 mm, H 28,5 mm, PMMA. La pagina non indica né i COB compatibili né l'efficienza — [Özdisan](https://www.ozdisan.com/en/p/LED-Lens-422/ledlink-ll01zz-dry38l06-m2-958281)

**Carclo (UK)**
- La gamma 20 mm "frosted top" (comunicato del 2006) ha fasci da 12° e 21° FWHM (misurati su Luxeon 1 W bianco). Carclo dichiara una buona miscelazione da LED multi-chip/RGB, senza dati quantitativi — [LEDs Magazine](https://www.ledsmagazine.com/company-newsfeed/article/16690004/carclo-led-optics-20mm-frosted-range-now-available)
- Esempio attuale di catalogo: 10196 "Frosted Wide Spot" — [LEDSupply](https://ledsupply.com/led-optics/10196-carclo-lens-frosted-wide-spot-led-optic)

**Fraen (USA/Italia)**
- In passato Fraen ha presentato la serie FML per il colour mixing — [LEDs Magazine](https://www.ledsmagazine.com/company-newsfeed/article/16680204/fraen-offers-fml-series-lens-for-color-mixing). Esiste anche il datasheet FXCM-5D-47B, dove la sigla "CM" lascia supporre "colour mixing" — [datasheet Ampheo](https://resources.ampheo.com/static/datasheets/fraen-corporation/fxcm-5d-47b.pdf) (non letto). Fraen ha inoltre sviluppato ottiche "multi-TIR nested lens" per COB — [LEDs Magazine](https://www.ledsmagazine.com/company-newsfeed/article/16684827/fraen-develops-optics-with-multi-tir-nested-lens-technology-for-cob-leds)

**Altri**
- "B&M Optics Co., Ltd" compare solo come voce produttore in un aggregatore di datasheet — [datasheets.com](https://datasheets.com/id/manufacturer/b-m-optics-co---ltd-37241). Non è emerso un catalogo ufficiale online.
- Altri produttori asiatici di lenti COB emersi dalle ricerche: Bicom Optics — [LEDs Magazine directory](https://www.ledsmagazine.com/directory/company/14077515/bicom-optics); ILENSTECH (lente narrow 36° su Alibaba) — [Alibaba](https://www.alibaba.com/product-introduction/ILENSTECH-36-Degree-Narrow-Beam-Optical_50044987925.html). Esistono anche lenti COB rettangolari asimmetriche 60×120° e 75×135° — [Luxalight 81×47](https://luxalight.eu/en/products/led/led-lens-81x47mm-60x120-degrees-cob-power-led); [Luxalight 98×81](https://luxalight.eu/en/products/led/led-lens-98x81mm-75x135-degrees-cob-power-led)

### Inferences
- Per i fasci 4-10° su sorgenti RGBW, i candidati più documentati sono Gaggione LLC59U/C (Ø45 mm) e Khatod ultra-narrow 8° (Ø35/45 mm). Funzionano con sorgenti piccole (LES 1-4 mm², cioè emettitori 4-in-1, non COB grandi). Per un proiettore da 20-300 W servono quindi array di molte ottiche (multi-ottica) invece di un singolo COB.
- Per i fasci ellittici esistono soluzioni a sublente o lente ovale: LEDiL RGBX2-O 50°×24°, LedLink 16°×30°, LEDiL GABRIELLA-MIDI-O. Il 10×60° in versione colour mixing non risulta a catalogo nelle fonti lette. Si può ottenere con lenti narrow + vetro di chiusura lenticolare (vedi sezione 2).
- Con un unico COB RGBW di grande LES l'unica via documentata è un riflettore come ANGELINA (LES ≤ 32 mm) con sublente di miscelazione, ma si arriva al massimo a circa 17-20°: non si raggiungono i 4-10°.

### Gaps
- Le famiglie LEDiL ipotizzate nella richiesta (FLORENCE, CRISTINA, BOOM, BARBARA, MIRELLA, VIVIANNE) non sono state verificate: non sono emerse nelle ricerche su ottiche colour mixing. STRADA esiste ma è una lente stradale ([esempio C15109 STRADA-SQ-FS3](https://cz.exshinetech.com/datasheets/cd/C15109-STRADA-SQ-FS3.pdf)), non pensata per il colour mixing.
- Per LEDiL mancano nei datasheet letti efficienza, materiale e temperatura delle famiglie RGBX e ANGELINA.
- Carclo: nessun dato attuale su famiglie colour mixing da 10/20/26,5 mm né sull'uniformità cromatica.
- Fraen FCN/FXCM, Darkoo, Optoflux, Mingxing e Kunshan: non verificati.
- B&M lens: non si trova un catalogo pubblico. Il catalogo andrà chiesto direttamente al fornitore, che Versus Lux ha già.
- Dati quantitativi di uniformità cromatica (Δu'v' nel fascio) non sono stati trovati per nessuna famiglia.
- Resistenza UV e idoneità come vetro frontale di chiusura non sono documentate. Khatod dice solo che le ottiche "non trasmettono UV". LEDiL indica come sistemi di sigillatura il vetro piano o il potting ([Guide TIR](https://ledil.com/?p=2148)), quindi in un IP66/67 la lente in PMMA va dietro un vetro di chiusura separato.

## 2. Riflettori vs TIR per COB, diffusori, micro-lenti e superfici testurizzate

### Takeaway
Le TIR controllano meglio la luce e danno tagli più netti. I riflettori lasciano molta luce non controllata, hanno un taglio più morbido e sono l'unica opzione pratica per COB grandi. Il colour mixing si ottiene sempre a scapito del fascio stretto: più diffusione significa più étendue e fascio più largo, mentre i fasci "Real Spot" non miscelano.

### Cited Findings
- TIR e riflettore lavorano sullo stesso principio, ma la TIR "ha più controllo sulla luce". Nel riflettore gran parte della luce non tocca la superficie e resta non controllata, e il taglio del fascio è meno netto, soprattutto negli spot stretti — [LEDiL Guide to TIR lenses](https://ledil.com/?p=2148)
- Capacità di miscelazione per tipo di TIR: Real Spot nessuna, Smooth/Oval bassa, Diffused/Medium/Wide moderata. L'intensità di picco (cd/lm) cala nello stesso ordine — [LEDiL Guide to TIR lenses](https://ledil.com/?p=2148)
- I diffusori nel cammino ottico miscelano bene, ma aumentano l'étendue e perdono luce, quindi non vanno bene quando servono fasci stretti. Un rod (mixing rod) chiaro dà illuminamento uniforme in uscita, ma l'intensità resta mal miscelata. Micro-lenti alle estremità del rod migliorano la miscelazione dell'intensità, mentre superfici troppo ripide causano TIR interne e perdite. Con die a layout misto (es. Luminus LZC-03MD07) serve diffusione — [Optics for Hire blog](https://www.opticsforhire.com/blog/color-mixing-of-the-rgbw-leds-with-variable-spot/)
- L'angolo di fascio cambia con colore, dimensione e posizione dei chip, per cui ogni canale ha un fascio leggermente diverso: è questa l'origine dei bordi colorati — [LEDiL RGBX](https://www.ledil.com/data/prod/RGBX/RGBX-fds.pdf); [LEDiL ANGELINA](https://www.ledil.com/data/prod/Angelina/Angelina-fds.pdf)
- Il Moving Lenslet Array Khatod (sopra lenti RGBW) allarga 12-50° mantenendo, secondo il produttore, efficienza >90% — [LED professional](https://led-professional.com/products/led-optics/khatod-unveils-its-newest-series-of-ultra-narrow-color-mixing-optics)
- Gaggione dichiara esplicitamente il compromesso: LLC59N è un "balanced compromise between beam angle and colour mixing capability" — [Gaggione LLC59x](https://led.cdiweb.com/Datasheets/gaggione/Gaggione-Focus-On-LLC59x.pdf)

### Inferences
- Per i 4-10° conviene usare una TIR stretta per ogni emettitore RGBW compatto (LES piccolo), accettando una leggera frangia sul bordo, oppure un collimatore specifico per colour mixing (tipo LLC59C), che dà circa 10-12° FWHM ma un FWTM più largo.
- Per i fasci ellittici (10×30°, 10×60°) e il wall-wash asimmetrico, un vetro frontale lenticolare o prismatico (spread lens) sopra lenti narrow fa sia da chiusura IP sia da miscelatore lungo l'asse allargato. È una pratica comune, ma non c'è una fonte specifica fra quelle lette.

### Gaps
- Non sono state trovate misure pubblicate che quantifichino la perdita di efficienza dovuta a diffusori o texture (es. % per grado di haze).
- Mancano confronti quantitativi TIR vs riflettore sull'uniformità cromatica.

## 3. Come risolvono il colour mixing i concorrenti premium

### Takeaway
Lumenpulse con Opticolor mescola "alla sorgente", cioè a livello di package e ottica, con miscelazione nel campo molto vicino. Per Martin, SGM e Color Kinetics non sono state trovate fonti tecniche in questa ricerca.

### Cited Findings
- Opticolor di Lumenpulse "mixes color at the source, at the LED package level, within the LED optic". La miscelazione avviene a distanza ultra-ravvicinata (il colore è già uniforme a pochi pollici dall'apparecchio). Usa un binning stretto (varianza 5 nm), è compatibile con DMX/RDM, Lumentalk e DALI DT8, ed è offerto su alcuni Lumenbeam e Lumenquad dal giugno 2022 — [Lightnow blog, 2022](https://www.lightnowblog.com/2022/05/product-monday-lumenpulse-launches-mix-at-source-color-changing-technology/); [Lumenpulse Opticolor](https://www.lumenpulse.com/opticolor?region=eu)
- Opticolor è stato esteso ad altre famiglie — [Electrical Industry News](https://electricalindustry.ca/product-news/opticolor-line-lumenpulse)
- WE-EF presenta i proiettori FLC240/FLC260 con lo slogan "Very focused, perfectly mixed" — [WE-EF](https://dev.we-ef.com/news/flc240-flc260-ees) (pagina non letta nel dettaglio)

### Inferences
- L'approccio "mix at source" (emettitori multicolore molto compatti, 4-in-1 o 5-in-1, più ottica con microstruttura per ogni emettitore) è coerente con le ottiche di catalogo viste sopra, come GABRIELLA, RGBX, LLC59 e Khatod RGBW. È plausibilmente la strada più accessibile per Versus Lux.

### Gaps
- Mancano dettagli tecnici di Opticolor: layout dei chip, angoli disponibili, dati di uniformità.
- Martin Exterior, SGM e Color Kinetics ColorReach non sono stati ricercati in modo approfondito: nessuna fonte disponibile in queste note.

## 4. Prezzi

### Takeaway
Sono stati trovati due prezzi verificati da distributore: una lente COB LedLink a circa 2,2-2,7 USD/pz e una LEDiL GABRIELLA-MIDI-W a 4,70 EUR/pz per 50 pezzi. Il resto va chiesto ai distributori o ai fornitori.

### Cited Findings

| Prodotto | Prezzo | Quantità | Fonte | Data |
|---|---|---|---|---|
| LedLink LL01ZZ-DRY38L06-M2 (COB, 38°, Ø68,5 mm, PMMA) | 2,65043 USD | 1 pz | [Özdisan](https://www.ozdisan.com/en/p/LED-Lens-422/ledlink-ll01zz-dry38l06-m2-958281) | 9/11/2026 |
| idem | 2,45410 USD | 5 pz | idem | 9/11/2026 |
| idem | 2,25777 USD | 10 pz | idem | 9/11/2026 |
| idem | 2,16746 USD | 50 pz | idem | 9/11/2026 |
| LEDiL CA16204_GABRIELLA-MIDI-W (35°, PMMA) | 4,704 EUR/pz (235,20 EUR per tray da 50, IVA esclusa; 289,30 EUR IVA inclusa) | 50 pz | [RS Irlanda](https://ie.rs-online.com/web/p/led-lenses-reflectors/2066656) | 9/11/2026 (in back order, spedizione dal 12/1/2027) |

- Per LedLink, Özdisan indica lead time di 5-6 settimane, MOQ 1 e MPQ 10 — [Özdisan](https://www.ozdisan.com/en/p/LED-Lens-422/ledlink-ll01zz-dry38l06-m2-958281)

### Gaps
- Mancano i prezzi di Gaggione LLC59x, Khatod RGBW, LEDiL RGBX, ANGELINA e HEKLA-SOCKET-RZ, Carclo frosted e B&M lens. Pagine prodotto dove cercarli: [Future Electronics GABRIELLA-MIDI-S](https://futureelectronics.com/p/semiconductors--Led-lighting-components--led-lighting-optics-lenses--single-lens-led-optics/c16193-gabriella-midi-s-ledil-6170842), [Avnet](https://www.avnet.com/americas/product/ledil/c16193_gabriella-midi-s/evolve-57902036), [Comet.bg](https://store.comet.bg/en/Catalogue/Product/41702).
- Non sono stati raccolti prezzi Alibaba o Made-in-China per lenti COB colour mixing.
