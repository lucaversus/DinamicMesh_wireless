# Tecniche costruttive e soluzioni ingegneristiche per apparecchi RGB/RGBW dinamici da esterno (facciate, ponti, ambiente marino)

Nota di metodo: ricerca svolta l'8/11/2026 con circa 25 chiamate (ricerche + lettura di pagine). Molte fonti primarie (norme IEEE/IEC/ANSI, specifiche Qualicoat, foto interne FCC) sono a pagamento o non leggibili come testo: dove un dato non è stato verificato è segnato nei "Gaps". Le "Inferences" sono ragionamenti ingegneristici dell'autore, non fatti citati.

## 1. Tenuta stagna: guarnizioni, resinatura, conformal coating, valvole di equalizzazione, pressacavi

### Takeaway
Per IP66/67 a lunga durata la guarnizione di riferimento è in silicone (schiuma/spugna a basso compression set o LSR stampato), abbinata a una valvola di equalizzazione a membrana (tipo Gore PolyVent): senza valvola un apparecchio chiuso che si raffredda di colpo va in depressione (circa -140 mbar nel caso WE-EF) e "risucchia" umidità oltre la guarnizione. La resinatura totale è la scelta per immersione/chimici; il conformal coating 2K spesso (200-400 µm) è un'alternativa più leggera.

### Cited Findings
**Guarnizioni**
- La spugna EPDM a celle chiuse ha buona resistenza UV ma "compression set e proprietà di tenuta non sono considerate adeguate per la tenuta a lungo termine di involucri IP66"; il neoprene indurisce e prende deformazione permanente; la schiuma uretanica PORON può assorbire acqua e degradarsi con gelo/disgelo — [Stockwell Elastomerics, whitepaper gaskets outdoor LED](https://www.stockwell.com/pdf/stockwell-whitepaper-specifying-gaskets-for-outdoor-led-lighting-fixtures.pdf)
- Schiuma di silicone: compression set <5%, resiste al rilassamento; a media densità sigilla IP66 a circa 50% di schiacciamento (celle chiuse circa 30%); spugna di silicone a celle chiuse: compression set <10%, IP66 a 25-50% di schiacciamento; LSR (20-40 Shore A, 0,25-3 mm) richiede superfici piane e forza di chiusura adeguata, e guarnizioni LSR stampate con cordolo possono raggiungere IP67 (immersione) — [Stockwell](https://www.stockwell.com/pdf/stockwell-whitepaper-specifying-gaskets-for-outdoor-led-lighting-fixtures.pdf)
- Dati di compression set (50% per 22 h a 70 °C / 100 °C): schiuma silicone HT-800 5% / 5%; spugna silicone R10470 10% / 15%; EPDM R497-T 25% / non classificato — [Stockwell](https://www.stockwell.com/pdf/stockwell-whitepaper-specifying-gaskets-for-outdoor-led-lighting-fixtures.pdf)
- Regole pratiche: taglio a getto d'acqua preferito (il laser carbonizza i bordi della schiuma di silicone); adesivo 3M 9485 su alluminio nudo, 3M 9490LE su superfici verniciate a polvere (bassa energia superficiale); guarnizioni della cornice senza adesivo per poterle sostituire in campo — [Stockwell](https://www.stockwell.com/pdf/stockwell-whitepaper-specifying-gaskets-for-outdoor-led-lighting-fixtures.pdf)
- Esiste anche la guarnizione formata in opera (FIPFG, schiuma dosata da robot direttamente sul corpo): Sonderhoff la propone specificamente per corpi di apparecchi — [Sonderhoff, luminaire housings](https://www.sonderhoff.com/en/applications/luminaire-housings) (pagina trovata in ricerca, contenuto non letto in dettaglio)

**Resinatura vs conformal coating**
- Il conformal coating si applica in film sottile anche per limitare lo spostamento di temperatura colore: rivestire la lente sposta tipicamente la luce verso il freddo, in misura variabile per tipo di LED; in esterno serve altissima stabilità UV — [Electrolube](https://electrolube.com/?p=15555)
- I coating standard non bastano per immersione frequente, spruzzi chimici o gas corrosivi; i coating 2K senza solvente (es. 2K500, adatto LED) sono idrofobi, proteggono da acqua, condensa e nebbia salina e si applicano a 200-400 µm con macchine selettive — [Electrolube](https://electrolube.com/?p=15555)
- Resine: epossidica robusta ma rigida (problemi nei cicli termici, cura molto esotermica che può deformare i supporti, scarsa stabilità colore); silicone ottima trasparenza e comportamento agli estremi di temperatura; poliuretano flessibile, trasparente, bassa assorbimento d'acqua. In un caso di lampada per piscina (acqua dolce e salata) l'epossidica è stata sostituita da PU per evitare la deformazione da calore di cura — [Electrolube](https://electrolube.com/?p=15555)
- La resinatura è "la scelta ovvia" per immersione o esposizione chimica; il 2K coating può sostituire la resina in alcuni casi togliendo il peso — [Electrolube](https://electrolube.com/?p=15555)

**Valvole di equalizzazione della pressione**
- Caso WE-EF VFL500 (IP66): la temperatura interna può passare da +65 °C a +15 °C in 10 minuti durante un temporale; in un corpo non ventilato si crea una depressione di circa -140 mbar, che può deformare la copertura acrilica e richiamare sporco e umidità oltre la guarnizione. Soluzione: Gore PolyVent M12x1,5 HA (avvitata, invisibile dall'esterno); vent operativo -40/+125 °C, fino a IP69K; WE-EF dichiara 60.000 h di vita e target >20 anni, nessun guasto finora (dichiarazione del fornitore) — [Gore, PTV-108 case history](https://www.gore.com/system/files/2023-05/PTV-108-R2_luminaires_case_history.pdf)
- Gore afferma che la valvola allunga la vita protegge da "differenziali di pressione che stressano le guarnizioni, formazione di condensa e ingresso di contaminanti" — [Gore white paper service life LED](https://www.gore.com/resources/white-paper-how-extend-service-life-led-outdoor-lighting-using-gore-protective-vents)
- Montaggi possibili: adesivo, filettato, a scatto, saldato — [Gore case history](https://www.gore.com/system/files/2023-05/PTV-108-R2_luminaires_case_history.pdf)
- Esiste anche un brevetto USA su un apparecchio con "gasket vent" (sfiato integrato nella guarnizione) — [USPTO 10690315](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/10690315) (non letto nel dettaglio)

### Inferences
- Per una barra lineare lunga (1-2 m) il volume d'aria è grande e la superficie della guarnizione lunga: è il caso in cui la depressione da raffreddamento improvviso (pioggia estiva su barra calda) pesa di più. Una valvola M12 per barra (o una per testata) è una spesa piccola rispetto al rischio.
- Approccio ibrido plausibile per Versus Lux: corpo sigillato con guarnizione in silicone + valvola Gore, schede LED e driver con conformal coating (acrilico o 2K) come seconda barriera, resinatura solo del vano pressacavo/connessioni. La resinatura totale sopra i LED complica ottica (shift colore), riparabilità e cicli termici.

### Gaps
- Non ho trovato dati verificati su quali marchi premium (Color Kinetics, Traxon, iGuzzini, Lumenpulse, SGM) usino resinatura vs guarnizione: nessuna fonte di produttore lo dichiara esplicitamente nelle pagine lette.
- Pressacavi/connettori IP68 (es. connettori overmoulded, M12, connettori tipo Hirschmann/Wieland) non approfonditi: nessuna fonte letta.
- Il PDF completo del white paper Gore (test e regole di dimensionamento) non è stato leggibile: solo l'abstract.

## 2. Corrosione e finiture: anodizzazione, verniciatura a polvere, Qualicoat/Qualimarine, C5-M, nebbia salina, viteria inox, accoppiamenti galvanici

### Takeaway
Il punto di partenza per ambiente costiero è verniciatura a polvere con pretrattamento certificato Qualicoat "Seaside" e viteria inox isolata dall'alluminio; i numeri precisi (spessori, ore di nebbia salina) vanno presi dalle specifiche ufficiali, che non sono state lette in questa ricerca.

### Cited Findings
- Qualicoat "Seaside" è una qualifica aggiuntiva del verniciatore, prerequisito per rivestimenti ad alta protezione dalla corrosione vicino al mare; la verniciatura Qualicoat usa solo prodotti di pretrattamento e polveri approvati, con test di produzione (invecchiamento, grado di reticolazione) — [Lindner Group](https://www.lindner-group.com/en/about-us/news-events/powder-coating-according-to-qualicoat-standard)
- Esempi di verniciatori con licenza Seaside nel settore serramenti — [Glass Times, Garnalex](https://glasstimes.co.uk/news/garnalex-gains-qualicoat-seaside-class-licence/)
- Alluminio-inox 304: una differenza di potenziale >0,2 V può avviare corrosione galvanica dell'alluminio; in zona marina severa evitare il contatto diretto; il rischio aumenta dove l'umidità ristagna e dove l'anodizzazione è incrinata; il rischio cala se l'alluminio (metallo attivo) ha superficie molto maggiore dell'inox (regola del rapporto di aree) — [BRANZ Build 176](https://www.buildmagazine.org.nz/assets/PDF/Build-176-70-Feature-Building-Materials-Compatability-Of-Aluminium-And-Steel.pdf)
- Metodi di isolamento: rondelle/distanziali non conduttivi, rivestimenti polimerici dell'intero giunto; "la sola vernice può non mantenere separati elettricamente i metalli nel tempo"; progettare per non trattenere acqua e sale — [BRANZ Build 176](https://www.buildmagazine.org.nz/assets/PDF/Build-176-70-Feature-Building-Materials-Compatability-Of-Aluminium-And-Steel.pdf)
- Esempio di prodotto marino citato in catalogo (Arcluce, Hurtigrutemuseet in Norvegia) — [Arcluce Exterior 2024 p.119](https://viva-interiors.com/en/catalogs/arcluce/exterior-2024/22652/page-119) (non letto)

### Inferences
- Viti inox A4 (316) piccole su corpo alluminio grande rispettano la regola del rapporto di aree; aggiungere comunque rondelle in nylon/PTFE o pasta isolante (tipo Tef-Gel/Duralac) nei punti in cui ristagna acqua, e non usare mai staffe in acciaio zincato a contatto con alluminio in ambiente marino.
- Attenzione alle viti che tagliano la verniciatura: il bordo del foro è il punto di partenza tipico della corrosione filiforme (inferenza da pratica comune, non verificata da fonte letta).

### Gaps
- Spessori Qualicoat (classe 1/2/3), requisiti Qualimarine, ore di nebbia salina acetica, classi ISO 12944 C5-M/CX e spessori di anodizzazione (es. classe 20/25 µm Qualanod): non trovati in fonti leggibili. Consultare direttamente qualicoat.net, qualimarine e Qualanod.
- Nessun dato verificato su quante ore ISO 9227 dichiarano i produttori premium.

## 3. Progetto termico: giunzione LED, dissipatori lineari, derating, temperature ambiente

### Takeaway
Il rosso e soprattutto l'ambra (AlInGaP) perdono flusso molto più del bianco con la temperatura: un LED rosso Luminus perde circa 1% di flusso fotometrico per °C. Il progetto termico di un RGBW/RGBA va quindi dimensionato sul canale rosso/ambra, non sul bianco.

### Cited Findings
- Luminus SST-90-R (rosso): coefficiente termico del flusso fotometrico -0,96 %/°C, radiometrico -0,52 %/°C, tensione di giunzione -1,3 mV/°C; Tj max 110 °C; Rth giunzione-case 0,50 °C/W, giunzione-scheda 1,20 °C/W, giunzione-dissipatore 1,40 °C/W (su MCPCB in alluminio con TIM eGraf 1205) — [Luminus SST-90 datasheet](https://download.luminus.com/datasheets/Luminus_SST-90_Datasheet.pdf)
- Osram OSTAR Stage LE RTDUW S2WP (RGBW in un unico package 6,38 x 5,75 mm): temperatura di funzionamento lato superiore -40/+85 °C; potenze elettriche per colore R 3,3 W, G 3,9 W, B 4,2 W, W 4,2 W; corrente di riferimento 1400 mA — [ams-osram](https://ams-osram.com/products/leds/multi-color-leds/osram-osram-ostar-stage-le-rtduw-s2wp)
- Il caso WE-EF documenta temperature interne fino a +65 °C in un apparecchio stradale IP66 — [Gore case history](https://www.gore.com/system/files/2023-05/PTV-108-R2_luminaires_case_history.pdf)
- Il modulo radio LumenRadio CRMX OEM è specificato -20/+70 °C, umidità 0-90% non condensante — [LumenRadio CRMX OEM datasheet](https://www.fullcompass.com/common/files/28444-LumenRadioCRMOEMSeriesDatasheet.pdf); il Casambi CBU-ASD è -20/+50 °C ambiente — [CBU-ASD datasheet](https://mountlighting.co.uk/wp-content/uploads/2025/01/CBU-ASD-Datasheet.pdf)

### Inferences
- Le radio commerciali spesso non coprono -40 °C: se si vuole dichiarare -40/+50 °C ambiente, scegliere ESP32 in versione temperatura estesa (le varianti industriali dei moduli Espressif arrivano a +85/+105 °C; da verificare sul datasheet del modulo scelto) e verificare che la temperatura interna nel vano driver resti entro i limiti con LED al massimo e sole.
- Con -0,96 %/°C sul rosso, passare da Tj 25 °C a 85 °C significa perdere dell'ordine del 50% del rosso, mentre blu e bianco perdono molto meno: senza compensazione termica il bianco "di miscela" e i colori calibrati si spostano verso il blu man mano che l'apparecchio si scalda. Serve un NTC sulla scheda LED e una compensazione per canale nel firmware ESP32.
- Il derating termico (riduzione corrente oltre una soglia di NTC) è pratica standard; va reso proporzionale su tutti i canali per non alterare il colore.

### Gaps
- Nessuna fonte letta su progetto di profili lineari estrusi (alette, rapporto W/m, Rth per metro) né curve di derating di prodotti premium.
- Dati di Cree XM-L Color / Luminus RGBW sulla variazione dell'ambra (PC-Amber vs AlInGaP) non letti.

## 4. Miscelazione colore: LED multichip, ottiche, binning e calibrazione, qualità del bianco, stabilità dell'ambra

### Takeaway
I package multichip RGBW (es. Osram OSTAR Stage) riducono le ombre colorate perché i chip sono a pochi mm, ma i chip hanno flussi e binning separati per colore: la costanza tra lotti si ottiene solo con calibrazione di fabbrica per apparecchio. Questo punto è poco documentato pubblicamente dai produttori.

### Cited Findings
- OSTAR Stage: lunghezze d'onda rosso 612-630 nm, verde "true green" 513-545 nm, blu "deep blue" 439-461 nm, più bianco; angolo 120°; venduto in classi di flusso (bin) a 1400 mA con intervalli larghi (es. 112-280 lm, 355-710 lm a seconda del colore/codice) — [ams-osram](https://ams-osram.com/products/leds/multi-color-leds/osram-osram-ostar-stage-le-rtduw-s2wp)
- L'ampiezza dei bin (dominante del verde su 32 nm, del blu su 22 nm) è dichiarata dal costruttore — [ams-osram](https://ams-osram.com/products/leds/multi-color-leds/osram-osram-ostar-stage-le-rtduw-s2wp)
- Color Kinetics usa motori "IntelliHue" RGBM e RGBW con CCT dichiarata 2000-10000 K e ottiche intercambiabili (es. "OptiField" per wall washing, fasci 6°-10°, lenti di diffusione) — [Wiedamark, Blast Powercore IntelliHue Gen5](https://www.wiedamark.com/product/color-kinetics-423-000037-01-blast-powercore-intellihue-optifield-gen5-rgbm-led-ip66-rated-flood-with-wall-washing-beam-and-2000k-to-10000k-cct-in-black-finish/)

### Inferences
- Con bin di dominante così ampi, due apparecchi dello stesso modello possono mostrare differenze visibili sullo stesso valore DMX: la soluzione industriale è misurare ogni apparecchio a fine linea (spettrometro, es. lo stesso HPCS-330 aziendale) e salvare nella flash dell'ESP32 una matrice di calibrazione 3x5/5 canali verso uno spazio colore comune (CIE xy + Y).
- TIR per singolo LED dà fasci stretti efficienti ma tende a mostrare frange colorate se i chip sono separati; una lente con microstruttura/diffusore o un mixing rod riduce le frange a scapito dell'efficienza. Con package multichip compatti il problema si riduce.
- Il quinto canale (ambra o bianco caldo) serve a coprire la zona 2000-3000 K con CRI accettabile: un bianco ottenuto da soli RGB ha resa cromatica scarsa.

### Gaps
- Nessuna fonte letta su Cree XM-L Color, Luminus RGBW, sulle ottiche di miscelazione (Ledil, Carclo, Khatod) né su procedure di calibrazione pubblicate dai produttori premium.
- Nessun dato su CRI del bianco nei prodotti RGBW concorrenti, né sulla stabilità PC-Amber vs AlInGaP.

## 5. Driver e dimmerazione: corrente costante multicanale, PWM, metriche di flicker, 16 bit

### Takeaway
I limiti Ecodesign 2019/2020 (Pst LM <=1,0; SVM <=0,4) si applicano alle sorgenti luminose alimentate da rete, non agli apparecchi con driver separato; per architetturale la linea guida più usata è IEEE 1789 (modulazione massima % = 0,08 x frequenza nella zona a basso rischio). In pratica un PWM >=1,25 kHz, meglio diversi kHz, evita i problemi anche nelle riprese video.

### Cited Findings
- Regolamento UE 2019/2020, in vigore dal 1/9/2021: flicker visibile Pst LM max 1,0 (0-80 Hz); effetto stroboscopico SVM max 0,4 (80 Hz - 2 kHz); si applica solo a sorgenti LED alimentate da rete (retrofit, moduli AC), non ad apparecchi con driver separato; nessun metodo per il "phantom array" — [Fagerhult, flicker and TLA](https://www.fagerhult.com/knowledge/technology/driver/flicker-and-tla/)
- La dimmerazione ibrida (CCR + PWM) passa a PWM sotto circa il 35% del flusso in alcuni driver — [Fagerhult](https://www.fagerhult.com/knowledge/technology/driver/flicker-and-tla/)
- IEEE 1789: la percentuale massima di flicker si calcola moltiplicando la frequenza per 0,08; es. a 120 Hz il massimo ammesso è 10% — [LEDs Magazine](https://www.ledsmagazine.com/leds-ssl-design/modular-drivers/article/16696708/ieee-par1789-makes-recommendations-on-safe-levels-of-flicker-in-led-based-lighting-updated)
- Altri produttori europei spiegano flicker/TLA nella documentazione tecnica — [ERCO](https://erco.com/en/designing-with-light/lighting-knowledge/led/flicker-7734), [XAL](https://www.xal.com/en/services/know-how/flicker)
- Esempio di IC driver RGB multicanale con PWM a scala di grigi a 16 bit: TI TLC5955 (48 canali, pensato per display/insegne a bassa corrente) — [TI TLC5955](https://www.ti.com/product/TLC5955)

### Inferences
- Per barre da 20-100 W la soluzione tipica è un convertitore buck a corrente costante per canale (controller tipo TI LM3409/TPS92xxx, MPS, Infineon, Analog Devices MAX16833 citato nelle ricerche) con ingresso PWM dall'ESP32. L'ESP32 ha la periferica LEDC con risoluzione fino a ~20 bit a bassa frequenza: a 16 bit si arriva intorno a 1,2 kHz con clock 80 MHz (80 MHz / 65536), a 13-14 bit a 5-10 kHz. Il compromesso risoluzione/frequenza va verificato sul datasheet ESP32; il dithering temporale o un driver dedicato a 16 bit aiutano nei bassi livelli. (Valori dedotti dall'architettura LEDC, non citati da fonte letta.)
- Curva di dimmerazione logaritmica o quadratica e risoluzione >=16 bit effettivi sono necessari per dissolvenze lente su facciate senza "scalini" visibili al buio.
- Anche se Ecodesign non obbliga gli apparecchi con driver, i capitolati architetturali e le riprese TV chiedono spesso di dichiarare frequenza PWM e conformità IEEE 1789: conviene dichiararlo in scheda.

### Gaps
- Testo integrale IEEE 1789 (soglia 1250 Hz, zona "no effect" 0,0333 x f): non verificato da fonte leggibile; DOE energy.gov non raggiungibile.
- Nessuna fonte su quali IC driver usino i produttori premium.

## 6. Protezione da sovratensioni ed elettrica: livelli kV, classe I/II, SPD, 24/48 V DC vs rete, topologie power+data

### Takeaway
Color Kinetics (Powercore: rete 100-277 VAC e dati sullo stesso cavo) affianca agli apparecchi un SPD esterno IP66 da 10 kA / fino a 12 kV certificato IEC 61643-11, che protegge sia la linea di potenza sia la linea dati.

### Cited Findings
- Color Kinetics Surge Protector Powercore: testato In 10 kA; livello di protezione 1,4 kV L-N, 2,5 kV L-PE e N-PE; "ulteriore strato di protezione fino a 12 kV / 10 kA"; certificato IEC 61643-11; contenitore in alluminio pressofuso IP66 / UL50E Type 4 con ingressi PG21 o 3/4" NPT; morsetti 120-277 VAC (L, N, PE) e dati in ingresso, uscita L, N e dati protetti verso gli apparecchi su un solo cavo; da usare come parte di un sistema di terra corretto — [Color Kinetics SPP](https://colorkinetics.com/global/products/pds/spp)
- Famiglie protette: Blast, Burst, Graze, Graze Compact, ReachElite Powercore, più eW, eColor, Vaya senza linea dati — [Color Kinetics SPP](https://colorkinetics.com/global/products/pds/spp)
- Esempio Powercore: BlastElite 100-277 VAC con fascio nativo 10° — [Plum Lighting](https://plumlighting.com/products/bc-96937)

### Inferences
- Con la radio a bordo (nessun cavo dati), Versus Lux elimina il percorso di sovratensione più delicato (la linea DMX/RS-485 lunga). Restano: linea di potenza e, se usato, bus di alimentazione 24/48 V DC lungo la facciata.
- 48 V DC (SELV) permette tratte più lunghe di 24 V con metà corrente; l'alimentatore centrale va protetto da SPD lato rete e l'apparecchio con TVS/varistore sull'ingresso DC. Per apparecchi a rete diretti, i capitolati stradali chiedono tipicamente 6-10 kV di modo comune (valori da confermare sulla norma EN 61547 / capitolati).

### Gaps
- Nessuna fonte letta sui livelli 4/6/10 kV richiesti per esterni, né sulla scelta classe I vs II per apparecchi metallici in facciata.

## 7. Meccanica: vetro IK10, vibrazioni per ponti, staffe di puntamento, antifurto

### Takeaway
Per ponti e viadotti il riferimento è ANSI C136.31 a 3 G (1,5 G per le altre applicazioni); SGM raggiunge 3 G aggiungendo rinforzi metallici su giunti, angoli e collegamenti tra sottoassiemi, non con una linea separata.

### Cited Findings
- ANSI C136.31-2018: capacità minima di resistenza alle vibrazioni di apparecchi stradali e d'area; 3,0 G per ponti e cavalcavia, 1,5 G per le altre applicazioni; il rating 3 G significa resistere alla frequenza di risonanza fondamentale per 100.000 cicli su ciascun asse x, y, z; dopo la prova nessuna parte allentata che comprometta la sicurezza e apparecchio funzionante — [SGM Lighting, vibration](https://www.sgmlighting.com/media/knowledge/vibration)
- IEC 60068-2-6:2008 (vibrazioni sinusoidali, apparecchio funzionante durante la prova, ricerca delle frequenze critiche con sweep e prove a frequenza fissa) — [SGM Lighting](https://www.sgmlighting.com/media/knowledge/vibration)
- SGM rinforza i punti deboli (giunti, angoli, connessioni tra assiemi) per arrivare a 3 G; alcune applicazioni (montagne russe, navi da crociera) superano i parametri ANSI per più risonanze simultanee — [SGM Lighting](https://www.sgmlighting.com/media/knowledge/vibration)
- Prodotti commerciali dichiarano "3G vibration rating" per floodlight — [LEDinside, MaxLite](https://ledinside.com/node/view/23136)

### Inferences
- Per una barra lineare lunga, le risonanze critiche sono tipicamente quelle della barra sul proprio supporto: staffe più ravvicinate, viteria con frenafiletti o rondelle di sicurezza (tipo Nord-Lock) e blocco meccanico del puntamento (dentatura o spina) oltre al semplice serraggio per attrito.
- Antifurto: viti a testa speciale (Torx con perno) e cavo di sicurezza in inox sono soluzioni comuni (non verificato da fonte).

### Gaps
- Nessuna fonte letta su vetri IK10 (spessore vetro temprato tipico) né su sistemi antifurto dei concorrenti.

## 8. Integrazione della radio in corpi metallici

### Takeaway
Un corpo metallico chiuso è una gabbia di Faraday: o si crea una finestra trasparente alla radio (policarbonato, vetroresina, acrilico — anche il vetro frontale/la lente stessa) con l'antenna dietro, a distanza dal metallo, o si porta l'antenna fuori con un connettore passante. Espressif chiede almeno 15 mm di spazio libero attorno all'antenna PCB nell'involucro; Casambi dice esplicitamente di non mettere il proprio modulo in contenitori metallici.

### Cited Findings
- Un involucro interamente metallico blocca quasi tutta la RF; le antenne interne funzionano solo con una finestra RF-trasparente deliberata (policarbonato, vetroresina, acrilico); senza, le prestazioni saranno scarse indipendentemente dal guadagno — [Data Alliance](https://www.data-alliance.net/blog/antennas-mounted-on-metal-enclosures-guidance)
- In alternativa antenna completamente esterna con passante/bulkhead; scegliere antenne indipendenti dal piano di massa (dipolo, puck con massa integrata); se l'antenna usa il corpo come massa serve contatto su metallo nudo, perché vernice o polvere isolano; cavo interno corto, non arrotolare l'eccesso, ferrite sul coassiale; verificare con VNA e prove sul corpo reale, non su prototipo in plastica — [Data Alliance](https://www.data-alliance.net/blog/antennas-mounted-on-metal-enclosures-guidance)
- Espressif (ESP32-S3): antenna PCB del modulo sporgente oltre il bordo della scheda madre, oppure punto di alimentazione vicino al bordo con taglio del PCB sotto e ai lati dell'antenna; sconsigliato il modulo al centro scheda con ritagli sui quattro lati; "clearance di almeno 15 mm" attorno all'antenna nell'involucro in tutte le direzioni; antenna lontana da quarzi, clock, USB/UART; rete di adattamento CLC per la taratura; provare portata e throughput sul prodotto finito — [Espressif PCB layout design (ESP32-S3)](https://docs.espressif.com/projects/esp-hardware-design-guidelines/en/latest/esp32s3/pcb-layout-design.html)
- Casambi CBU-ASD: "non deve essere posizionato in un contenitore metallico o vicino a grandi strutture metalliche. Il metallo blocca efficacemente tutti i segnali radio"; banda 2,4-2,480 GHz; -20/+50 °C; IP20 (va dentro l'apparecchio) — [CBU-ASD datasheet](https://mountlighting.co.uk/wp-content/uploads/2025/01/CBU-ASD-Datasheet.pdf)
- LumenRadio CRMX OEM (moduli da 27,5 x 12 x 65 mm, 10 g): connettore antenna MCX con opzione di antenna integrale; potenza fino a 300 mW (25 dBm, solo Nord America) / 100 mW (20 dBm); sensibilità -96 dBm; portata fino a 1000 m in area urbana con antenne 2 dBi — [LumenRadio CRMX OEM datasheet](https://www.fullcompass.com/common/files/28444-LumenRadioCRMOEMSeriesDatasheet.pdf)
- LumenRadio vende antenne omnidirezionali 2 dBi e 5 dBi con connettore RP-TNC per i propri dispositivi — [Full Compass, LR2DBIOAI](https://www.fullcompass.com/prod/639445-lumenradio-lr2dbioai-indoor-2-dbi-omni-antenna-rp-tnc-male-connector); [Adorama, 5 dBi](https://www.adorama.com/lumen-radio-5-dbi-omni-indoor-antenna-rp-tnc-male-connector/p/lr5dbioai)

### Inferences
- Per una barra in alluminio la soluzione più pulita è mettere la radio in una testata (tappo terminale) in policarbonato/PA caricata vetro, con antenna PCB o chip antenna orientata verso l'esterno e almeno 15 mm dal metallo; in alternativa una piccola antenna esterna con passante IP68 (es. N o RP-SMA con O-ring) per i proiettori in acciaio.
- La lente frontale in PC/PMMA è anch'essa una finestra RF, ma l'antenna dietro la lente "vede" la scheda LED e il dissipatore: va provato. Il vetro temprato lascia passare il 2,4 GHz con attenuazione modesta se senza coating metallico (inferenza, non verificata).
- Ogni apparecchio diventa un'apparecchiatura radio: marcatura CE secondo RED 2014/53/UE con prove EN 300 328 e EN 301 489; per USA serve FCC (modulo certificato riduce il lavoro). Usare un modulo ESP32 già certificato con antenna integrata o con antenna esterna dichiarata nella certificazione.

### Gaps
- Le foto interne FCC (fccid.io) di Astera, Acclaim Dyna Drum con Aria X2, Philips/driver CRMX del Tyne Bridge non sono state recuperate: le pagine fccid.io non sono emerse con queste ricerche. Va fatto a mano cercando il FCC ID stampato sulle etichette.
- Linee guida di integrazione LumenRadio/Casambi per costruttori (documenti OEM) non pubbliche o non trovate.

## 9. Affidabilità: modi di guasto, MTBF/L70, garanzie

### Takeaway
Le fonti lette indicano come cause principali l'ingresso d'acqua (spesso via depressione e guarnizioni che perdono elasticità), lo spostamento cromatico per resinature/coating non stabili e lo stress termico; mancano dati pubblici di tasso di guasto dei produttori.

### Cited Findings
- Guasti delle guarnizioni: compression set permanente (EPDM, neoprene, PORON), indurimento per sole e intemperie, assorbimento d'acqua e gelo/disgelo, rilassamento nel tempo — [Stockwell](https://www.stockwell.com/pdf/stockwell-whitepaper-specifying-gaskets-for-outdoor-led-lighting-fixtures.pdf)
- La depressione da raffreddamento (-140 mbar) richiama umidità e sporco oltre le guarnizioni e può deformare coperture in acrilico — [Gore case history](https://www.gore.com/system/files/2023-05/PTV-108-R2_luminaires_case_history.pdf)
- Coating sulla lente spostano la temperatura colore verso il freddo; epossidiche non stabili di colore e problematiche nei cicli termici — [Electrolube](https://electrolube.com/?p=15555)
- WE-EF dichiara 60.000 h di vita LED/elettronica e oltre 20 anni di vita utile target (dato del produttore riportato da Gore) — [Gore case history](https://www.gore.com/system/files/2023-05/PTV-108-R2_luminaires_case_history.pdf)

### Inferences
- Il canale rosso/ambra, più sensibile alla temperatura, è quello che invecchia e si sposta per primo: un sistema RGBW perde la calibrazione del bianco prima di perdere flusso. Una compensazione con NTC e la possibilità di ricalibrare via radio sono un vantaggio competitivo.
- Il driver (condensatori elettrolitici) è di norma il componente a vita più breve: scegliere condensatori a 105 °C long-life o soluzioni a film/ceramici dove possibile.

### Gaps
- Nessun dato MTBF, L70/L80 o tasso di guasto in campo di prodotti RGB da esterno; termini di garanzia già raccolti nel primo giro di ricerca (vedi altri file della cartella), non ripetuti qui.

## 10. Checklist delle scelte di progetto per Versus Lux

### Takeaway
Elenco operativo derivato dalle fonti sopra; ogni voce rimanda alla sezione con le citazioni. Le voci segnate (da verificare) derivano da inferenze.

### Cited Findings
- [ ] Guarnizioni in schiuma/spugna di silicone (compression set <=10%) o LSR stampata con cordolo per IP67; schiacciamento 25-50% secondo il materiale; niente EPDM/neoprene/PORON per IP66 a lungo termine — [Stockwell](https://www.stockwell.com/pdf/stockwell-whitepaper-specifying-gaskets-for-outdoor-led-lighting-fixtures.pdf)
- [ ] Valvola di equalizzazione a membrana (es. Gore PolyVent M12x1,5) in ogni corpo chiuso, montata in posizione protetta — [Gore](https://www.gore.com/system/files/2023-05/PTV-108-R2_luminaires_case_history.pdf)
- [ ] Conformal coating (acrilico UV-stabile o 2K 200-400 µm) su driver e radio; resinatura PU/silicone solo dove c'è immersione; evitare epossidica sopra i LED — [Electrolube](https://electrolube.com/?p=15555)
- [ ] Verniciatura a polvere da verniciatore con licenza Qualicoat Seaside per versioni costiere — [Lindner](https://www.lindner-group.com/en/about-us/news-events/powder-coating-according-to-qualicoat-standard)
- [ ] Viteria inox A4 con rondelle isolanti nei giunti alluminio-inox; progetto senza ristagni d'acqua — [BRANZ](https://www.buildmagazine.org.nz/assets/PDF/Build-176-70-Feature-Building-Materials-Compatability-Of-Aluminium-And-Steel.pdf)
- [ ] Dimensionare il termico sul canale rosso/ambra (-0,96 %/°C su un rosso Luminus) e montare un NTC sulla scheda LED — [Luminus](https://download.luminus.com/datasheets/Luminus_SST-90_Datasheet.pdf)
- [ ] Valutare package RGBW in un solo chip (es. OSTAR Stage) per ridurre frange colorate; prevedere calibrazione per apparecchio a fine linea per compensare bin ampi — [ams-osram](https://ams-osram.com/products/leds/multi-color-leds/osram-osram-ostar-stage-le-rtduw-s2wp)
- [ ] Frequenza PWM ben sopra la soglia IEEE 1789 (0,08 x f) e dichiarata in scheda; Ecodesign 2019/2020 non obbligatorio per apparecchi con driver ma Pst LM <=1 e SVM <=0,4 come obiettivo — [Fagerhult](https://www.fagerhult.com/knowledge/technology/driver/flicker-and-tla/); [LEDs Magazine](https://www.ledsmagazine.com/leds-ssl-design/modular-drivers/article/16696708/ieee-par1789-makes-recommendations-on-safe-levels-of-flicker-in-led-based-lighting-updated)
- [ ] SPD esterno per linee lunghe (modello Color Kinetics: 10 kA, IEC 61643-11, IP66) a protezione dell'alimentazione di campo — [Color Kinetics SPP](https://colorkinetics.com/global/products/pds/spp)
- [ ] Versione "ponti" con prova ANSI C136.31 a 3 G (100.000 cicli per asse) e rinforzi su giunti/angoli; prove IEC 60068-2-6 — [SGM](https://www.sgmlighting.com/media/knowledge/vibration)
- [ ] Antenna ESP32 dietro una finestra non metallica (testata in policarbonato o lente) con >=15 mm di spazio libero, modulo al bordo scheda; oppure antenna esterna con passante; prove di portata sul prodotto chiuso — [Espressif](https://docs.espressif.com/projects/esp-hardware-design-guidelines/en/latest/esp32s3/pcb-layout-design.html); [Data Alliance](https://www.data-alliance.net/blog/antennas-mounted-on-metal-enclosures-guidance)
- [ ] Verificare la temperatura di funzionamento della radio: i moduli commerciali tipici sono -20/+50 °C (Casambi) o -20/+70 °C (LumenRadio OEM), sotto il -40 °C richiesto — [Casambi](https://mountlighting.co.uk/wp-content/uploads/2025/01/CBU-ASD-Datasheet.pdf); [LumenRadio](https://www.fullcompass.com/common/files/28444-LumenRadioCRMOEMSeriesDatasheet.pdf)

### Inferences
- [ ] (da verificare) Compensazione termica per canale e matrice di calibrazione colore salvate nella flash dell'ESP32, aggiornabili via radio.
- [ ] (da verificare) Risoluzione PWM effettiva >=16 bit con dithering per dissolvenze lente; scegliere il compromesso frequenza/bit della periferica LEDC.
- [ ] (da verificare) Bus 48 V DC SELV per le facciate (correnti dimezzate rispetto a 24 V), TVS sull'ingresso di ogni apparecchio.
- [ ] (da verificare) Staffe di puntamento con blocco meccanico (dentatura/spina) e frenafiletti; viti antimanomissione.
- [ ] (da verificare) Marcatura RED 2014/53/UE (EN 300 328, EN 301 489) usando un modulo ESP32 già certificato.

### Gaps
- Mancano, e vanno recuperati prima della progettazione esecutiva: specifiche Qualicoat/Qualimarine/Qualanod ufficiali con spessori e ore di prova; testo IEEE 1789 completo; livelli di surge per EN 61547 e capitolati; foto interne FCC di apparecchi concorrenti con radio integrata; datasheet completi di LED RGBA/RGBW (Cree XM-L Color, Luminus) con curve dell'ambra.
