# Lumentalk: dati sul cavo di alimentazione, punti forti e limiti

*Approfondimento per la linea RGB architetturale wireless di Versus Lux. Fonti consultate l'8 novembre 2026. Le sezioni 1-5 riportano fatti con fonte; la sezione 6 contiene valutazioni per Versus Lux. Note dettagliate in `research_notes/Lumentalk dati su linea elettrica/`.*

Lumentalk di Lumenpulse porta i comandi di illuminazione sui cavi di alimentazione AC esistenti (100-277 V), senza cavo dati. Funziona ed è collaudato (oltre 400 progetti dichiarati dal 2012, fra cui il Blatnik Bridge e il Boston City Hall), ma è pensato per scene, colori statici e dissolvenze lente. Le schede tecniche ufficiali fissano limiti precisi: un solo trasmettitore e un solo controller DMX per rete, al massimo 48 canali DMX per rete, aggiornamento a passi di almeno 1 secondo e dissolvenza minima di 1 minuto fra due colori. La stessa brochure Lumenpulse consiglia il DMX/RDM cablato per gli spettacoli di colore veloci. Lumentalk quindi risolve lo stesso problema di Versus Lux (niente cavo dati) ma copre solo la parte "scene lente" del mercato: la mesh radio con comandi temporizzati arriva più lontano su dinamica, numero di canali indipendenti e sincronia.

## 1. Come funziona

**Principio fisico.** Lumentalk è una tecnologia a onde convogliate (PLC, power line communication) sviluppata da Lumenpulse. Il segnale modulato è sovrapposto alla sinusoide di rete, invece di essere trasmesso solo vicino al passaggio per lo zero: così può trasmettere in ogni istante ed è più resistente alle reti disturbate ([whitepaper Lumenpulse](https://www.lumenpulse.com/resources/whitepapers/understanding-lumentalk)). Lumenpulse dichiara di operare nelle bande regolamentate FCC, CENELEC e ARIB ([pagina prodotto](https://www.lumenpulse.com/products/82/lumentalk)).

**Modulazione e chip.** Il whitepaper non dichiara la modulazione usata, ma la spiega con l'esempio della FSK. Il brevetto US9307619 (priorità 2010) indica la FSK come modulazione preferita, con DFSK e DPSK come alternative ([Google Patents](https://patents.google.com/patent/US9307619)). Nel 2015 Lumenpulse ha acquisito Ariane Controls, che aveva un chip PLC proprietario ([Buildings.com](https://www.buildings.com/building-systems-om/lighting/article/55255033/solid-state-lighting-and-controls-developer-lumenpulse-acquires-ariane-controls-for-chip-portfolio-support)). La tecnologia Ariane (chip PLM-1) era FSK half-duplex fra 50 e 500 kHz, da 100 a 30.000 baud ([Design & Reuse](https://design-reuse.com/news/19272/plc-ip-powerline-communications.html)). Il brevetto Ariane US5852636 usa come esempio una portante di circa 262 kHz ([Google Patents](https://patents.google.com/patent/US5852636)), fuori dalle bande europee EN 50065 che arrivano a 148,5 kHz. Quale portante usi davvero la versione europea non è pubblicato.

**Componenti.**

| Componente | Funzione | Dati principali |
| --- | --- | --- |
| Lumentranslator 2 | Converte il segnale del controller in Lumentalk e lo inietta sulla linea | Ingressi DMX, 0-10V, DALI, TRIAC; in scatola da incasso doppia; alimentato dalla linea stessa; UL e CE ([scheda](https://www.lumenpulse.com/products/5415)) |
| Lumenlink Pro | Gateway multi-circuito e ripetitore fra fasi | Ingressi DMX, 0-10V, DALI, Art-Net, sACN; fino a 6 circuiti; monofase o trifase 120-277 V; IP66; 3G ANSI C136.31 per ponti; garanzia 5 anni ([scheda](https://www.lumenpulse.com/products/5414)) |
| Lumenear | Scheda ricevente dentro ogni apparecchio | Demodula e comanda il driver ([whitepaper](https://www.lumenpulse.com/resources/whitepapers/understanding-lumentalk)) |
| Lumentalk Data Bridge | Riconverte Lumentalk in DMX o 0-10V per apparecchi non Lumentalk | IP66; massimo 32 apparecchi per bridge DMX ([scheda](https://www.lumenpulse.com/products/4952)) |
| LumenID + LumentalkID | Interfaccia USB e software di messa in servizio | Rileva i dispositivi sulla linea, li raggruppa in "sezioni" |

Il whitepaper precisa che Lumentalk non traduce direttamente DMX, DALI o 0-10V, ma converte l'informazione "il più fedelmente possibile".

**Bidirezionalità.** La brochure dichiara un protocollo bidirezionale: gli apparecchi vengono rilevati sulla linea durante la messa in servizio e possono restituire configurazione, temperatura, ore di vita e stato ([brochure EMEA 2019](https://www.lumenpulse.com/files/view-file/supportfiles/7d669da3ebe18ad208cc7e8126ac993f/3490/locale_file/lumentalk-brochure-emea-en-2019-rev-2)).

## 2. Prestazioni e limiti dichiarati

Due fonti ufficiali danno numeri diversi: la brochure di marketing e le schede tecniche degli apparecchi. Le schede sono più restrittive e sono quelle che valgono in progetto.

| Parametro | Brochure EMEA 2019 | Scheda Lumenbeam Medium CC, EU 2026 |
| --- | --- | --- |
| Apparecchi per rete | fino a 1024 | "consult factory" |
| Zone | fino a 48 | — |
| Controller per rete | fino a 32 | 1 controller DMX per rete |
| Trasmettitori | uno per ogni controller | 1 trasmettitore (Lumentranslator o Lumenlink) per sistema |
| Canali DMX | — | massimo 48 per rete |
| Velocità | "2,5 volte più veloce del DALI" | aggiornamento minimo a passi di 1 secondo |
| Dissolvenze | "Slow Fade", scala 0-10 minuti | dissolvenza minima di 1 minuto fra due colori |
| Latenza | "quasi zero" con meno di 48 indirizzi; possibile ritardo oltre | — |
| Lunghezza cavi | "più lunga del DMX tradizionale" | "consult factory" |

Fonti: [brochure](https://www.lumenpulse.com/files/view-file/supportfiles/7d669da3ebe18ad208cc7e8126ac993f/3490/locale_file/lumentalk-brochure-emea-en-2019-rev-2), [scheda Lumenbeam Medium Colour Changing EU](https://storage.googleapis.com/lumenpulse-medias/prod/document/products-5692-specsheet-fullspecsheet-eu-en-metric.pdf), [manuale LumentalkID](https://www.lumenpulse.com/files/view-file/supportfiles/703f4b089786c2cdfae5d7d35cd49072/3491/locale_file/113205-lp-lumentalkid-manual-rev-5).

Il manuale conferma il limite di banda: un Lumentranslator DMX ascolta al massimo 48 canali, e "più piccolo è l'intervallo, meno banda occupa sulla rete Lumentalk". Per risparmiare banda suggerisce di comandare gli apparecchi come gruppo sincronizzato.

**Cosa significano 48 canali.** Con 4 canali per apparecchio (RGBW) si comandano individualmente 12 apparecchi o gruppi; con 5 canali, 9. Sul Blatnik Bridge, 90 apparecchi stanno su un solo Lumentranslator 2 e un solo Lumenlink: si comandano quindi per gruppi, non uno per uno (deduzione dai numeri della brochure).

**Uso consigliato dal produttore.** La brochure mostra solo colore statico e dissolvenze lente, e scrive: "if you are looking for a fast colour show, our DMX/RDM systems are the way to go". Il whitepaper lo definisce "ideally suited for retrofit applications".

**Vincoli elettrici.** Ogni dispositivo collegato alla rete influenza il segnale, quindi va verificato tutto ciò che sta sul circuito ([whitepaper](https://www.lumenpulse.com/resources/whitepapers/understanding-lumentalk)). Le schede USA indicano che sullo stesso circuito non vanno apparecchi di altri produttori (fonte: [scheda Lumenbeam NA](https://storage.googleapis.com/lumenpulse-medias/prod/document/products-5136-specsheet-fullspecsheet-na-en-imperial.pdf), letta dalla ricerca ma non riverificata da me). Per passare fra circuiti e fasi serve il Lumenlink.

**Certificazione.** La dichiarazione CE del Lumenlink Pro cita le direttive Bassa Tensione, EMC e RoHS, ma nella parte letta non elenca norme armonizzate né EN 50065 ([DoC](https://www.lumenpulse.com/files/view-file/supportfiles/8aa7ef83e067271b0f773bca7530c81d/5608/locale_file/eu-declaration-of-conformity-lnkp)).

**Prezzi.** Nessun prezzo pubblico. La brochure dice solo che il costo è quello dei Lumentranslator 2 e degli apparecchi; il Data Bridge dichiara un risparmio "fino al 30% dei costi totali di installazione". Il kit di messa in servizio LumenID si compra dal distributore.

## 3. Progetti realizzati

| Progetto | Apparecchi | Componenti | Risultati dichiarati |
| --- | --- | --- | --- |
| John A. Blatnik Bridge, Duluth (USA), 2013 | 90 | 1 Lumenlink, 1 Lumentranslator 2, 1 Pharos | energia -60%; nessun nuovo cavo né quadro |
| Boston City Hall (USA) | 311 | 12 Lumenlink, 3 Lumentranslator 2, 1 Pharos | colore senza forare muri di cemento da 1 m |
| Buckley Recital Hall, Amherst (USA) | 164 | 3 Lumenlink, 3 Lumentranslator 2 | manutenzione -50.000 USD/anno |
| Castro Street, San Francisco (USA) | 48 | 1 Lumenlink, 2 Lumentranslator 2 | nessuno scavo stradale |
| Château Frontenac, Québec (CAN) | 6 | 1 Lumenlink, 2 Lumentranslator 2 | facciata storica intatta |
| Muider Castle, Muiden (NL) | 12 | 1 Lumenlink, 1 Lumentranslator 2 | energia -80%, nessuno scavo |

Fonte: [brochure EMEA 2019](https://www.lumenpulse.com/files/view-file/supportfiles/7d669da3ebe18ad208cc7e8126ac993f/3490/locale_file/lumentalk-brochure-emea-en-2019-rev-2).

Sul Blatnik Bridge la brochure parla di "un ponte lungo 2.430 metri". MnDOT indica l'accensione il 25 ottobre 2013 nell'ambito di una riabilitazione da 12,9 milioni di dollari ([MnDOT](https://newsline.dot.state.mn.us/archive/13/Oct/30.html)), e lo studio SEH parla dell'illuminazione della campata a traliccio di 1.140 piedi, circa 347 m ([SEH](https://www.sehinc.com/portfolio/duluth-john-blatnik-bridge-lighting-design)). È probabile che 2.430 m sia la lunghezza del ponte e non il tratto comandato via Lumentalk (deduzione). Non ho trovato segnalazioni indipendenti di problemi o malfunzionamenti; le fonti sui progetti sono quasi tutte del produttore.

**Proprietà e licenze.** Dal luglio 2026 Platinum Equity partecipa al controllo di LMPG, la casa madre di Lumenpulse ([Inside Lighting](https://inside.lighting/news/26-07/lmpgs-ownership-evolution-gains-new-partner)). Lumentalk è licenziabile ad altri produttori ("Lumentalk licensing program"); nel 2013 è stato licenziato a Lighting Services Inc. ([Light Now](https://www.lightnowblog.com/2013/01/lighting-services-inc-and-lumenpulse-sign-licensing-agreement/)). Lumenpulse ha una sede italiana a Calenzano (FI), indicata nella brochure.

## 4. Un dato che corregge l'analisi della concorrenza

La scheda del Lumenbeam Medium Colour Changing offre, oltre a RGB, RGBW e RGBA, le versioni **Opticolor+**: MRGBWP e MRGROYWP. Sono sorgenti miscelate alla fonte (la sigla MRGROYWP indica rosso, verde, blu royal, arancio, giallo e bianco) comandate con **4 indirizzi DMX**, con bianco regolabile in campo da 2200 a 8000 K e modalità "Optidrive" impostata in fabbrica ([scheda EU](https://storage.googleapis.com/lumenpulse-medias/prod/document/products-5692-specsheet-fullspecsheet-eu-en-metric.pdf)). Il report "Analisi concorrenza illuminazione dinamica" diceva che nessun prodotto architetturale offre più di 4 colori: per Lumenpulse va precisato che esistono apparecchi con più di 4 sorgenti, anche se comandati con 4 canali. Il dato è stato aggiunto in nota al report.

Altri dati della stessa scheda, utili come riferimento: 25-28 W, 1.158-1.598 lm, IP66, IK09, -40/+50 °C, L70 oltre 90.000 h, 16 bit, garanzia 5 anni.

## 5. Le altre tecnologie "dati sul cavo di potenza"

| Sistema | Mezzo | Prestazioni dichiarate | Note |
| --- | --- | --- | --- |
| Color Kinetics IntelliPower / Powercore, Data Enabler Pro | Rete AC 100-277 V | fino a 63 ricevitori per ramo; 150 m in aria, 90 m interrati | DMX o Ethernet/KiNET; filtri da valutare con sopralluogo; circa 1.587 USD (Wiedamark, esaurito) ([CK](https://www.docs.colorkinetics.com/learn/color-kinetics-intellipower-overview.pdf)) |
| GLP DoP (DMX su rete) | Rete AC, banda larga 4-28 MHz | fino a 10 universi | convertitore sulla stessa linea degli apparecchi ([GLP](https://glp.de/en/products/glp-dop-converter-dinrail)) |
| Sundrax PowerGate | Rete AC, HomePlug 1.0 | DMX512 | cifratura AES-128; problemi segnalati con fasi diverse e alimentatori rumorosi ([Sundrax](https://entertainment.sundrax.com/blog/history-of-creation-power-gate-dmx-512-over-powerline-110-220)) |
| ST7580 (chip) | Rete AC, banda stretta | fino a 28,8 kbit/s | ([ST](https://www.st.com/en/product/st7580.html)) |
| LonWorks PL3120 (chip) | Rete AC, banda C | 5,4 kbit/s | ([Renesas](https://www.renesas.com/en/products/pl3120)) |
| G3-PLC / G3-Hybrid | Rete AC + radio sub-GHz | latenza andata e ritorno circa 250 ms nell'illuminazione stradale | ([G3 Alliance](https://g3-alliance.com/download/120/applications/3405/g3-alliance-and-g3-hybrid-for-connected-lighting-systems.pdf), [Analog Devices](https://www.analog.com/en/resources/technical-articles/powerline-communications-for-street-lighting-automation.html)) |
| Yamar DMX250 (chip) | Bus DC | 250 kbit/s, fino a 8 universi | accoppiamento con un condensatore; 7,56 / 6,30 / 4,98 al pezzo per 1-49 / 50-99 / 100-999 pezzi ([Yamar](https://yamar.com/product/dmx250), [DigiKey](https://www.digikey.com/en/products/detail/yamar/DCB1M-IC/19525704)) |

**Normativa europea.** EN 50065-1 regola la banda 3-148,5 kHz: banda A riservata ai distributori di energia, bande B, C, D agli utenti, con accesso CSMA/CA obbligatorio in banda C. La banda larga in ambito domestico (1,6-30 MHz) è regolata da EN 50561-1, con obbligo di notch e controllo dinamico della potenza. Le frequenze di commutazione tipiche dei driver LED (circa 40-54 kHz) e le loro armoniche cadono proprio nelle bande CENELEC: il disturbo dipende soprattutto dalla qualità del filtro EMI del driver (note in `altre_tecnologie_powerline.md`).

**Ordine di grandezza della banda.** Con apparecchi a 5 canali aggiornati 30 volte al secondo, senza contare gli overhead, la banda stretta europea basta per circa 4 apparecchi (LonWorks) o circa 24 (ST7580); un DMX completo a 250 kbit/s per circa 100 (calcolo della ricerca, ottimistico).

## 6. Cosa significa per Versus Lux

*Valutazioni, non fatti citati.*

**Lumentalk è il concorrente concettuale più vicino, ma non sulla dinamica.** Vende la stessa promessa (nessun cavo dati, ideale per beni tutelati e ponti) ed è collaudato da 14 anni. Però i suoi limiti scritti (48 canali per rete, passi da 1 secondo, dissolvenze di almeno 1 minuto) lo confinano alle scene lente. La mesh ESP-NOW con comandi temporizzati, calcolata nella specifica, porta un comando di scena a tutta una facciata in pochi millisecondi e regge il controllo dal vivo fino a circa 100 apparecchi indipendenti. È questo il punto da mettere in evidenza nel confronto commerciale.

| Aspetto | Lumentalk | Mesh Versus Lux (da specifica) |
| --- | --- | --- |
| Mezzo | Cavo di alimentazione AC | Radio 2,4 GHz |
| Hardware aggiuntivo | Lumentranslator 2 e Lumenlink a quadro | Nessuno (bridge DMX solo se serve la console) |
| Canali indipendenti | 48 per rete | centinaia; limite pratico sul live circa 100 apparecchi a 16 bit |
| Dinamica | passi da 1 s, dissolvenze da 1 min | effetti sincronizzati, controllo dal vivo |
| Sincronia | non dichiarata | comandi temporizzati, stima circa 1 ms |
| Dipendenza dall'impianto elettrico | alta: carichi, filtri, fasi, circuiti | nessuna; dipende dalla propagazione radio |
| Sicurezza | "non attaccabile da remoto" (marketing) | cifratura e chiavi per impianto, da progettare bene |
| Punto debole | banda, qualità della rete | metallo, ostacoli, interferenze a 2,4 GHz |

**Il loro argomento contro di voi è la sicurezza.** La brochure scrive testualmente "Unlike wireless, I'm secure. I can't be hacked remotely". Va preparata una risposta concreta: traffico cifrato e autenticato, chiavi diverse per ogni impianto, firmware firmato, conformità EN 18031. È anche un obbligo normativo, quindi conviene trasformarlo in argomento di vendita.

**PLC come canale di riserva: da valutare più avanti, non nella prima versione.** Il vostro protocollo trasmette pochi byte per comando, quindi anche una PLC lenta in banda CENELEC basterebbe per i comandi di scena e il sincronismo orario quando la radio non arriva (un apparecchio schermato, un ostacolo). È lo schema ibrido già usato nello stradale con G3-Hybrid. Però aggiunge un front-end PLC per apparecchio, prove EN 50065, dipendenza dalla qualità della rete e sensibilità al rumore dei driver. Più promettente, per le barre lineari alimentate in 24/48 V DC, è la PLC su bus DC (tipo Yamar DMX250, pochi euro a chip): niente rete a 230 V, 250 kbit/s, accoppiamento semplice. Suggerimento: lasciare sulla scheda nodo la predisposizione per un modem su bus DC e valutarlo dopo le prove radio sul campo.

**Specifiche da riprendere da Lumenpulse.**
- Bidirezionalità con diagnostica (temperatura, ore, stato) e rilevamento automatico dei dispositivi: è già nella vostra specifica, va mantenuta.
- Lumenlink Pro certificato 3G ANSI C136.31 per i ponti: stesso requisito per i vostri apparecchi e per il bridge.
- Opticolor+: più sorgenti miscelate dentro l'apparecchio con meno canali di comando e bianco regolabile in campo. Conferma che il 5 canali va venduto anche come qualità del bianco e del colore, non come numero di canali.

**Punti aperti.**
1. Frequenza portante e conformità EN 50065 della versione europea di Lumentalk: chiedere alla sede di Calenzano.
2. Prezzi di Lumentranslator 2, Lumenlink Pro e apparecchi in versione LT rispetto alla versione DMX: preventivo diretto.
3. Numero massimo reale di apparecchi e lunghezza dei cavi per circuito ("consult factory").
4. Esperienze di installatori italiani con Lumentalk.

## Fonti

- [Lumenpulse – Understanding Lumentalk (whitepaper)](https://www.lumenpulse.com/resources/whitepapers/understanding-lumentalk)
- [Lumenpulse – Lumentalk, pagina prodotto](https://www.lumenpulse.com/products/82/lumentalk)
- [Lumenpulse – Brochure Lumentalk EMEA 2019 rev 2](https://www.lumenpulse.com/files/view-file/supportfiles/7d669da3ebe18ad208cc7e8126ac993f/3490/locale_file/lumentalk-brochure-emea-en-2019-rev-2)
- [Lumenpulse – Manuale LumentalkID rev 5](https://www.lumenpulse.com/files/view-file/supportfiles/703f4b089786c2cdfae5d7d35cd49072/3491/locale_file/113205-lp-lumentalkid-manual-rev-5)
- [Lumenpulse – Scheda Lumenbeam Medium Colour Changing EU](https://storage.googleapis.com/lumenpulse-medias/prod/document/products-5692-specsheet-fullspecsheet-eu-en-metric.pdf)
- [Lumenpulse – Lumenlink Pro](https://www.lumenpulse.com/products/5414), [Lumentranslator 2](https://www.lumenpulse.com/products/5415), [Lumentalk Data Bridge](https://www.lumenpulse.com/products/4952)
- [Lumenpulse – Dichiarazione CE Lumenlink Pro](https://www.lumenpulse.com/files/view-file/supportfiles/8aa7ef83e067271b0f773bca7530c81d/5608/locale_file/eu-declaration-of-conformity-lnkp)
- [Google Patents – US9307619](https://patents.google.com/patent/US9307619), [US5852636](https://patents.google.com/patent/US5852636)
- [Buildings.com – acquisizione Ariane Controls](https://www.buildings.com/building-systems-om/lighting/article/55255033/solid-state-lighting-and-controls-developer-lumenpulse-acquires-ariane-controls-for-chip-portfolio-support)
- [Design & Reuse – Ariane PLC IP](https://design-reuse.com/news/19272/plc-ip-powerline-communications.html)
- [MnDOT – Blatnik Bridge](https://newsline.dot.state.mn.us/archive/13/Oct/30.html), [SEH – Blatnik Bridge lighting](https://www.sehinc.com/portfolio/duluth-john-blatnik-bridge-lighting-design)
- [Inside Lighting – proprietà LMPG](https://inside.lighting/news/26-07/lmpgs-ownership-evolution-gains-new-partner)
- [Light Now – licenza a Lighting Services Inc.](https://www.lightnowblog.com/2013/01/lighting-services-inc-and-lumenpulse-sign-licensing-agreement/)
- [Color Kinetics – IntelliPower overview](https://www.docs.colorkinetics.com/learn/color-kinetics-intellipower-overview.pdf)
- [GLP – DoP converter](https://glp.de/en/products/glp-dop-converter-dinrail), [Sundrax – PowerGate](https://entertainment.sundrax.com/blog/history-of-creation-power-gate-dmx-512-over-powerline-110-220)
- [ST – ST7580](https://www.st.com/en/product/st7580.html), [Renesas – PL3120](https://www.renesas.com/en/products/pl3120), [Yamar – DMX250](https://yamar.com/product/dmx250)
- [G3-PLC Alliance – G3-Hybrid per l'illuminazione](https://g3-alliance.com/download/120/applications/3405/g3-alliance-and-g3-hybrid-for-connected-lighting-systems.pdf), [Analog Devices – PLC per illuminazione stradale](https://www.analog.com/en/resources/technical-articles/powerline-communications-for-street-lighting-automation.html)
