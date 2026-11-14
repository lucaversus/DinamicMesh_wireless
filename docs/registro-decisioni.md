# Registro delle decisioni – Linea RGB architetturale wireless

Aggiornato al 9 novembre 2026. Raccoglie in un posto solo le decisioni prese, il perché, i documenti di riferimento e cosa resta aperto. I dettagli tecnici sono nella [specifica](specifica-tecnica.md).

## Decisioni prese

| # | Data | Decisione | Motivo | Riferimento |
| --- | --- | --- | --- | --- |
| 1 | 08/11/2026 | Linea per facciate, edifici, ponti e grandi strutture; niente residenziale | Mercato architetturale e infrastrutturale | Specifica, Obiettivo e ambito |
| 2 | 08/11/2026 | Agli apparecchi arriva solo l'alimentazione; i dati viaggiano via radio | Il cablaggio DMX è il problema da eliminare | Specifica, Architettura |
| 3 | 08/11/2026 | Compatibilità con console DMX/Art-Net/sACN tramite bridge opzionale; ecosistema proprietario | Restare comandabili dai sistemi esistenti senza imporre hardware a tutti | Specifica, Hardware |
| 4 | 08/11/2026 | Fase 1: scene, colori e sequenze programmate. Il video pixel per pixel è una fase 2 con variante cablata | La radio non ha banda per il pixel mapping su centinaia di punti | Specifica; calcoli di dimensionamento |
| 5 | 08/11/2026 | 5 canali per apparecchio: RGB+W+Ambra oppure RGB+bianco caldo+bianco freddo, stessa elettronica | Coprire entrambe le esigenze con una sola scheda | Specifica, Requisiti |
| 6 | 08/11/2026 | Trasporto radio ESP-NOW a 2,4 GHz su ESP32-C5, con comandi temporizzati ("scena N all'istante T") | Latenza bassa, nessuna licenza, sincronia garantita dal tempo di esecuzione | Specifica, Latenza e trasporto radio |
| 7 | 08/11/2026 | Nessun modulo LumenRadio/CRMX | Costo per apparecchio, rete a stella, dipendenza dal fornitore | Specifica; analisi concorrenza |
| 8 | 08/11/2026 | Rete mesh tra apparecchi, senza gateway obbligatorio; un apparecchio fa da coordinatore | Elemento distintivo sul mercato; un solo prodotto da sviluppare e certificare | Specifica, Architettura |
| 9 | 08/11/2026 | Nessun Bluetooth, né per la mesh né per l'app | Qualifica Bluetooth SIG a pagamento; condivisione della radio con ESP-NOW sull'ESP32-C5 | Specifica, Certificazioni |
| 10 | 08/11/2026 | App web via Wi-Fi; configurazione "connessa" con router o access point dedicato all'impianto, separato dalla rete dello stabile, con uscita internet | Telefono con internet, assistenza remota, ora esatta, aggiornamenti | Specifica, Collegamento dell'app |
| 11 | 08/11/2026 | Certificazione a basso costo: modulo radio già certificato, solo 2,4 GHz, autocertificazione CE, una scheda per tutta la linea | Piccola azienda | Specifica, Strategia di certificazione |
| 12 | 08/11/2026 | Antenna: tappo plastico per le barre lineari; nodo esterno resinato o antenna passante per i proiettori | Corpi in alluminio e acciaio schermano la radio | Specifica, Antenna |
| 13 | 08/11/2026 | La specifica vive solo nel repository GitHub; il documento su Claude è archiviato | Una sola fonte aggiornata | README |
| 14 | 08/11/2026 | Nessuna trasmissione dati sul cavo di alimentazione nella prima versione; predisposizione per un modem su bus DC da valutare per le barre a 24/48 V | Lumentalk e simili sono lenti e dipendono dall'impianto elettrico | Report Lumentalk |
| 15 | 08/11/2026 | Coesistenza a 2,4 GHz: protocollo a stato che si ripara da solo, ripetizioni, scelta e cambio coordinato del canale, diagnostica continua | Le interferenze vanno tollerate, non evitate | Specifica, Coesistenza; simulazioni |
| 16 | 08/11/2026 | Valori iniziali dalle simulazioni: inoltro mesh sempre attivo, 3 copie del coordinatore, 6 Mbps, rinfresco dello stato ogni 0,5-1 s, cambio canale automatico | Risultati Monte Carlo su facciata e ponte | [Simulazioni](simulazioni-coesistenza.md) |
| 17 | 08/11/2026 | Gli spot motorizzati per interni (pan 360°, tilt 180°, fermo meccanico, nessuno slip ring) sono nodi della stessa rete | Stesso firmware, stessa app, stessa certificazione radio | Repository [Spotlight_Motion](https://github.com/lucaversus/Spotlight_Motion) |
| 18 | 09/11/2026 | Strumento di test della rete: un unico apparecchio a batteria in 6 esemplari identici, con schermo touch da 5", ESP32-S3 per interfaccia e due ESP32-C5 (nodo e monitor), scanner di spettro CC2500, GPS con PPS | Provare il firmware al banco, tarare il simulatore, fare il rilievo radio prima della vendita | Repository [DinamicMesh_tester](https://github.com/lucaversus/DinamicMesh_tester) |
| 19 | 09/11/2026 | I proiettori partono dalla sorgente Bridgelux Vesta RGBW D10/D13 (array con area luminosa unica da 10 o 13 mm, bianco CRI 95 regolabile 1800-10.000 K, lenti Moony 15-50°, anodo comune, NTC a bordo) | Scelta di Luca; è la migliore sorgente RGBW trovata, con supporto e ottiche già pronti | [Analisi Vesta](sorgente-bridgelux-vesta.md) |
| 20 | 09/11/2026 | Al massimo 5 canali con sorgenti Bridgelux e 30 W per apparecchio, in tutte le tipologie; per potenze maggiori si affiancano più apparecchi | Una sola elettronica e un solo progetto termico | Specifica, Requisiti |
| 21 | 09/11/2026 | Scheda luce a 5 canali, condivisa con gli spot motorizzati: nel corpo, con microcontrollore che genera il PWM a 16 bit, collegata alla scheda nodo via RS-485 | Un solo progetto per proiettori fissi e motorizzati; risolve il PWM a 16 bit | Specifica, Scheda luce condivisa; [Spotlight_Motion](https://github.com/lucaversus/Spotlight_Motion) |
| 22 | 09/11/2026 | I prodotti da esterni non si accendono mai di giorno; protezione termica su tre livelli (firmware, termostato hardware, blocco diurno) | Un'accensione sotto il sole surriscalderebbe la scheda | Specifica, Protezione termica e blocco diurno |
| 23 | 09/11/2026 | Blocco diurno sbloccabile solo dall'installatore, per 10 minuti | Prove e manutenzione senza rischi | Specifica, Protezione termica e blocco diurno |
| 24 | 10/11/2026 | Spot motorizzati: pan continuo con slip ring (in ogni snodo solo 48 V e massa, con i dati modulati sopra) e tilt 0–90° (portato a 0–100° il 14/11/2026). Aggiorna la decisione 17 | Con il pan continuo 90° di tilt coprono tutta la semisfera sotto l'apparecchio, con metà della torsione dei fili | Repository [Spotlight_Motion](https://github.com/lucaversus/Spotlight_Motion) |

## Cosa hanno detto le analisi

**Concorrenza** ([report](../reports/Analisi%20concorrenza%20illuminazione%20dinamica.md)):
- Il mercato delle facciate dinamiche è quasi tutto cablato (DMX/RDM, DALI, cavo unico per alimentazione e dati).
- La radio integrata nell'apparecchio è rara ed è sempre DMX wireless a stella, mai mesh. Le mesh esistenti (Casambi, LumenRadio) lavorano solo a scene memorizzate.
- Nessuno offre 5 canali di comando indipendenti. Lumenpulse Opticolor+ mescola più sorgenti dentro l'apparecchio, ma con 4 canali di comando.
- Prezzi pubblici: lineari RGBW da evento a circa 180-230 €/m netti; Thorn Contrast RGBW a circa 3.000-3.700 €; un ricevitore CRMX esterno a circa 590 € netti. I marchi premium non pubblicano listini in euro.
- In Italia il progetto tipico è fatto da decine o centinaia di proiettori RGBW, con scene e calendari, promosso da multiutility.

**Lumentalk** ([report](../reports/Lumentalk%20dati%20su%20linea%20elettrica.md)):
- È il concorrente concettuale più vicino (nessun cavo dati), ma i limiti sono scritti in scheda: 48 canali DMX per rete, passi da 1 secondo, dissolvenze di almeno 1 minuto.
- Il loro argomento contro il wireless è la sicurezza: va preparata la risposta (cifratura, chiavi per impianto, firmware firmato, EN 18031).

**Rete e interferenze** ([dimensionamento](specifica-tecnica.md), [simulazioni](simulazioni-coesistenza.md)):
- Su una facciata 10×10 m un comando di scena arriva in meno di 1 ms per salto; il controllo dal vivo regge fino a circa 100 apparecchi a 16 bit.
- Il Wi-Fi udibile, anche al 60% del canale, ritarda ma non fa perdere comandi.
- Il rischio vero è la sorgente nascosta e continua (telecamera): 1 comando su 5 non arriva a tutti in tempo; il rinfresco dello stato riallinea gli apparecchi; serve il cambio di canale automatico.
- L'inoltro mesh conta più delle ripetizioni del coordinatore. 6 Mbps rende meglio di 1 Mbps sotto interferenza a raffiche.
- Il controllo dal vivo senza ripetizioni perde fino al 38% degli aggiornamenti con sorgenti nascoste: va protetto a parte.

**Sorgenti LED e ottiche** ([report](../reports/COB%20LED%20multicolore%20e%20lenti.md)):
- Nessun COB a 5 canali di qualità sul mercato: i produttori di riferimento si fermano a RGBW. L'unico RGBWA è cinese (Guangmai 40 W), economico ma con bianco freddo Ra 70 e Rth alta.
- Fasci da 4 a 10° solo con sorgenti compatte e una lente per sorgente: il proiettore diventa una matrice di celle. Un COB grande con riflettore non scende sotto circa 17-20°.
- Ambra: il PC-amber tiene l'87% della luce a 85 °C contro il 36% dell'ambra diretto, ma invecchia peggio.
- In un corpo sigillato: vetro frontale davanti alle lenti plastiche, materiali a basso rilascio di vapori, LED con prova allo zolfo, niente resina sui LED.
- Calibrazione per apparecchio e compensazione della temperatura nel firmware della scheda nodo.

## Punti aperti

Elenco completo nella sezione "Scelte aperte" della specifica. I più importanti:
1. Prove al banco: catena lunga, portata, interferenza, robustezza; misura dei parametri radio reali dell'ESP32-C5 da reinserire nel simulatore.
2. Protezione del controllo dal vivo: inoltro mesh dei dati, copia locale nella zona disturbata, oppure abilitazione solo su canale verificato.
3. Ponti: simulare e provare due coordinatori, uno per estremità.
4. Conferma con il laboratorio: ESP-NOW come apparecchio adattivo per EN 300 328; autodichiarazione per EN 18031.
5. ~~Temperatura minima del modulo ESP32-C5~~: chiuso il 9/11/2026, il modulo ESP32-C5-WROOM-1U funziona da -40 a +85 °C (datasheet Espressif). Restano da verificare gli altri componenti della scheda.
6. Prezzi di progetto dei concorrenti italiani ed europei e di Lumenpulse (sede a Calenzano): richiedere preventivi.
7. Frequenza PWM e risoluzione di dimming; protezione dalle sovratensioni (riferimento dei migliori: 10 kV).
8. Sorgente e ottica: scegliere tra cella con emettitore RGBW + quinto LED e cluster di LED a colore singolo per i proiettori; qualificare il COB Guangmai RGBWA come variante economica; scegliere tra ambra diretto e PC-amber. Campioni e preventivi da chiedere elencati nel [report](../reports/COB%20LED%20multicolore%20e%20lenti.md).
9. Prove termiche della scheda luce: corpo IP66 al sole simulato a LED spento, accensione in quelle condizioni, avvio a -40 °C; da qui le soglie di protezione.

## Prossimi passi proposti

Lo strumento di test ha un repository dedicato, [DinamicMesh_tester](https://github.com/lucaversus/DinamicMesh_tester) (aperto il 9/11/2026).


1. Simulare due coordinatori sul ponte e le tre protezioni del controllo dal vivo.
2. Ordinare 5 schede ESP32-C5-DevKitC-1 e LED RGBWA di prova per il banco.
3. Scrivere il primo firmware di prova: inoltro mesh, comandi temporizzati, rinfresco dello stato, misura dell'occupazione dei canali.
