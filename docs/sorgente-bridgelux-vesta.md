# Sorgente di partenza per i proiettori: Bridgelux Vesta RGBW D10/D13

9 novembre 2026 · fonte: Bridgelux, *Vesta Series RGBW D10 and D13 Array Sell Sheet*, Rev. A (04/2025), due pagine, fornita da Luca. Il datasheet completo non l'abbiamo ancora.

## Cos'è

È una matrice di piccoli LED rossi, verdi, blu e bianchi disposti in un cerchio, su un circuito in metallo. Ha un'unica area luminosa da 10 mm (D10) o 13 mm (D13), quindi si monta e si usa come un COB.

- **4 canali.** Il bianco è caldo, a CRI 95.
- **Collegamento ad anodo comune.** Il connettore a 5 contatti ha un positivo comune (A+) e i quattro negativi W−, B−, R−, G−.
- **Sensore di temperatura a bordo.** Sul circuito ci sono una NTC (pad NTC+ e NTC−) e un punto di misura Tc.
- **Il bianco si regola lungo la curva del corpo nero** (bianchi "naturali") da 1800 a 10.000 K, sempre a CRI 95, mescolando il bianco con RGB.
- **Applicazioni dichiarate:** architetturale, spettacolo, piscine e fontane.
- **Accessori Bridgelux:** supporto senza saldatura, lenti "Moony" da 15° a 50° e driver a 4 canali.

## Dati per canale

Valori Gen 2 a Tsp 25 °C (punto di saldatura a 25 °C, cioè a freddo):

| Canale | Corrente | Vf D10 | Vf D13 | Potenza D10 / D13 | Flusso D10 | Flusso D13 | lm/W |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Rosso | 300 mA | 20 V | 34 V | 6 / 10 W | 271 lm | 465 lm | 46 |
| Verde | 350 mA | 19 V | 33 V | 7 / 12 W | 1.014 lm | 1.738 lm | 150 |
| Blu | 350 mA | 21 V | 36 V | 7 / 13 W | 171 lm | 292 lm | 23 |
| Bianco | 350 mA | 21 V | 36 V | 7 / 13 W | 1.055 lm | 1.808 lm | 145 |

- **Potenza totale.** Massimo dichiarato 28 W. Con tutti i canali alla corrente nominale il D13 assorbirebbe 48 W, quindi i quattro canali non possono stare al massimo insieme. Il dissipatore va dimensionato su circa 28 W, e il firmware deve limitare la somma dei canali.
- **Bianco regolabile, D13 Gen 2:**
  - da 2.000 a 2.850 lm, a 21-23 W, tra 2200 e 10.000 K;
  - 2.611 lm a 3000 K;
  - 2.790 lm a 4000 K;
  - 1.229 lm a 1800 K.
- **Bianco regolabile, D10 Gen 2:** da 1.170 a 1.690 lm, a 12-13 W.
- **Tabelle di miscela.** Il foglio dà, per ogni temperatura di colore, la corrente di ciascun canale. Sono un punto di partenza pronto per il motore colore del firmware.

## Confronto con le altre sorgenti della ricerca

| | Vesta D13 RGBW | Luminus CTM-14 RGBW | Guangmai RGBWA 40 W |
| --- | --- | --- | --- |
| Canali | 4 (RGBW) | 4 (RGBW) | 5 (RGBWA) |
| Area luminosa | 13 mm | 14,5 mm | non dichiarata, package 56×40 mm |
| Bianco | caldo, CRI 95, regolabile 1800-10.000 K miscelando | 2700 K, CRI ≥ 90 | 6000-6500 K, Ra 70 |
| Rosso / verde / bianco | 465 / 1.738 / 1.808 lm (Tsp 25 °C) | 94 / 650 / 438 lm (Tj 85 °C) | 400-600 / 400-900 / 800-1.000 lm (25 °C) |
| Potenza massima | 28 W | circa 26 W | 40 W |
| Ottiche del produttore | sì, 15-50° | no | lente piatta 120° |
| Sensore di temperatura | NTC a bordo | no | no |

I flussi non sono misurati alle stesse condizioni: Vesta e Guangmai a freddo, Luminus a caldo. Anche tenendone conto, il Vesta dichiara molta più luce per canale del CTM-14. Rispetto al Guangmai ha un bianco di qualità molto superiore e un ecosistema completo, con supporto e lenti.

**Correzione alla ricerca.** Nel [report](../reports/COB%20LED%20multicolore%20e%20lenti.md) il Vesta non compariva: il ricercatore lo riteneva un COB solo a bianco regolabile, da verificare. Esiste invece in versione RGBW, ed è il miglior candidato trovato finora per i proiettori a fascio medio e largo.

## Cosa cambia per il progetto

### 1. Il secondo profilo a 5 canali potrebbe non servire

Il Vesta produce bianchi da 1800 a 10.000 K a CRI 95 con soli 4 canali, cioè quello che volevamo ottenere con RGB+bianco caldo+bianco freddo. Il profilo RGB+WW+CW diventa quindi meno necessario, almeno per i proiettori.

Il quinto canale della scheda nodo resta libero, oppure si usa per l'ambra nella versione RGBWA: Bridgelux non ha un'ambra nell'array, quindi andrebbe aggiunta come emettitore separato. Da chiedere a Bridgelux:
- se esiste o si può fare una versione con ambra;
- se esistono più temperature di colore del bianco. Le sigle stampate sui circuiti, RGBW2000 e RGBW3000, fanno pensare di sì.

### 2. Il driver va progettato per l'anodo comune

Con il positivo comune non si possono usare quattro driver indipendenti con uscite flottanti, come si fa con LED separati. Le strade sono due:

| Soluzione | Come funziona | Pro | Contro |
| --- | --- | --- | --- |
| **Regolatori lineari sul negativo** | Una tensione unica sull'anodo e un regolatore di corrente per canale, comandato in PWM dall'ESP32 | Semplicissimo, nessuna commutazione, nessun problema EMC | Dissipa la differenza tra alimentazione e Vf: con il D13 a 38 V sono circa 4-5 W in totale, che crescono a caldo perché la Vf cala |
| **Buck con LED tra ingresso e induttanza** | Un convertitore per canale nella configurazione in cui il LED è collegato all'ingresso (anodo all'alimentazione), come fanno i regolatori della famiglia Diodes AL8860/AL8862; dimming in PWM dall'ESP32 | Efficiente, adatto all'anodo comune | Più componenti; la tensione massima del regolatore va verificata sul datasheet (il D13 lavora a 33-36 V) |

Le tensioni da considerare per l'alimentazione:
- **D10, circa 20 V per canale:** va bene con un'alimentazione a 24 V, con poco margine.
- **D13, 33-36 V per canale:** serve 40-48 V.

Questo va riportato nella specifica, nella sezione Hardware.

### 3. Fasci

Le lenti Moony coprono:
- 15°, 24°, 36° e 50° nei diametri 68, 75 e 83 mm;
- 36° e 50° nel diametro 50 mm.

Sotto i 15° non c'è niente. Per i fasci da 4 a 10° delle facciate alte e dei ponti resta valida la soluzione a celle del report, con sorgenti compatte e lenti dedicate. Il Vesta copre quindi la fascia da 15 a 50°, che è la più richiesta per i proiettori da facciata a media distanza.

Le lenti Moony sono in plastica: in un apparecchio IP66/67 vanno dietro il vetro frontale.

### 4. Temperatura e calibrazione

La NTC a bordo è quella che serve per la compensazione del colore con la temperatura descritta nel report: si collega a un ingresso analogico della scheda nodo. I dati del foglio sono a 25 °C. A regime, rosso e bianco renderanno meno e le tabelle di miscela andranno corrette con misure nostre, fatte allo spettrometro a temperatura stabilizzata.

## Domande per Bridgelux

1. Datasheet completo:
   - resistenza termica e Tj massima;
   - curve flusso/temperatura per canale;
   - lunghezze d'onda e tolleranze;
   - valore della NTC.
2. Dati di durata: LM-80/TM-21 per ciascun colore.
3. Resistenza allo zolfo, ad esempio una prova secondo IEC 60068-2-43.
4. Varianti:
   - temperature di colore del bianco disponibili;
   - versione con ambra o con secondo bianco;
   - stato del prodotto, Gen 1 o Gen 2.
5. Prezzi a 100, 500 e 1.000 pezzi per array, supporto e lenti Moony; distributore europeo; tempi di consegna.
6. Lenti Moony: materiale, efficienza e temperatura massima.
7. Driver a 4 canali: con quale ingresso si comanda. Ci serve solo come riferimento, perché il comando lo fa la nostra scheda.

## Prossimi passi proposti

1. Chiedere a Bridgelux il datasheet completo, i prezzi e i campioni:
   - 2 pezzi D10 e 2 pezzi D13;
   - supporto BXHD-RGBW-D50-35-15;
   - lenti Moony 68 mm da 15° e 36°.
2. Schema del primo stadio di potenza ad anodo comune per la scheda nodo, nelle due versioni (lineare e buck), con piedinatura e distinta componenti.
3. Al banco: misure con lo spettrometro a freddo e a caldo, verifica delle tabelle di miscela e prova termica a 28 W in un corpo chiuso.
