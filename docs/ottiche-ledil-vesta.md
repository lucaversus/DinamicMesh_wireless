# Lenti LEDiL per la sorgente Bridgelux Vesta RGBW

9 novembre 2026 · dati: esportazione LEDiL delle lenti compatibili con l'RGB mixing, fatta da Luca ([CSV](<../research_notes/COB%20LED%20multicolore%20e%20lenti/ledil_lenti_rgb_mixing.csv>), 84 combinazioni lente-LED) · sorgente: [analisi Vesta](sorgente-bridgelux-vesta.md)

## In sintesi

Per la Vesta LEDiL indica due famiglie, **AMY** e **YASMEEN**. Tutte si montano sul supporto **C19950_HEKLA-SOCKET-RZ**, che ha la cupola di miscelazione RGBW incorporata. Con la D10 sono state misurate 25 combinazioni; con la D13 ce ne sono solo 2, e simulate.

- **Famiglia da usare: AMY.** Rispetto a YASMEEN rende di più (75-81% contro 69-74%) ed è molto più bassa (11-13 mm contro 28-38 mm). In più ha l'ovale e l'asimmetrica per il wall-wash.
- **Diametro consigliato per i proiettori: AMY-70.** È il miglior compromesso: 15° con la D10 e 18° con la D13 nella versione RS, fino a 53° nella WW, più ovale e asimmetrica, il tutto in 70 mm. AMY-50 va bene per i proiettori compatti con la D10. AMY-110 serve solo se si vuole il fascio più stretto possibile (14°) con la D13.
- **Rispetto alle lenti Moony di Bridgelux**, LEDiL offre:
  - fasci ovali e asimmetrici;
  - fasci da 15-19° già in 50-70 mm;
  - file fotometrici misurati, scaricabili per ogni combinazione e apribili con l'Editor LDT.
- **Nessuna lente scende sotto i 14°.** Per i fasci da 4 a 10° resta la soluzione a celle del [report](../reports/COB%20LED%20multicolore%20e%20lenti.md).
- **Il prezzo della miscelazione è il rendimento:** 75-80%, contro l'89-93% delle lenti per emettitori singoli presenti nello stesso file.

## Lenti compatibili con la Vesta

Codice "CP…" = lente + supporto. Base richiesta: C19950_HEKLA-SOCKET-RZ (fissaggio a 2 viti, interasse 35 mm). Materiale PMMA.

Le colonne sono:
- **FWHM**: angolo del fascio a metà intensità;
- **FWTM**: angolo a un decimo dell'intensità, cioè quanto si allarga il bordo;
- **cd/lm**: intensità al centro per ogni lumen della sorgente.

**Con Vesta D10 (misurate)**

| Codice | Fascio | Ø × altezza (mm) | FWHM | FWTM | Rendimento | cd/lm |
| --- | --- | --- | --- | --- | --- | --- |
| CP18557_AMY-110-S-C | stretto | 110 × 17 | 14° | 30° | 79% | 7,60 |
| CP19045_AMY-70-RS-C2 | stretto | 70 × 12 | 15° | 30° | 77% | 6,13 |
| CP18751_YASMEEN-70-S-C2 | stretto | 70 × 38 | 16° | 30° | 73% | 6,99 |
| CP19037_AMY-70-S-C2 | stretto | 70 × 13 | 17° | 37° | 79% | 5,24 |
| CP19131_AMY-50-RS-C2 | stretto | 50 × 11 | 18° | 35° | 77% | 3,86 |
| CP19123_AMY-50-S-C2 | stretto | 50 × 11 | 19° | 40° | 79% | 4,37 |
| CP19038_AMY-70-M-C2 | medio | 70 × 13 | 23° | 44° | 79% | 3,64 |
| CP18572_AMY-110-M-C | medio | 110 × 17 | 24° | 44° | 78% | 3,45 |
| CP18724_YASMEEN-50-M-C2 | medio | 50 × 28 | 24° | 47° | 70% | 2,85 |
| CP19124_AMY-50-M-C2 | medio | 50 × 11 | 26° | 51° | 79% | 2,69 |
| CP18762_YASMEEN-70-M-C2 | medio | 70 × 38 | 26° | 44° | 69% | 3,00 |
| CP18573_AMY-110-W-C | largo | 110 × 17 | 34° | 60° | 76% | 1,82 |
| CP18725_YASMEEN-50-W-C2 | largo | 50 × 28 | 34° | 58° | 74% | 1,88 |
| CP19039_AMY-70-W-C2 | largo | 70 × 13 | 35° | 61° | 77% | 1,79 |
| CP19125_AMY-50-W-C2 | largo | 50 × 11 | 36° | 63° | 77% | 1,58 |
| CP18763_YASMEEN-70-W-C2 | largo | 70 × 38 | 36° | 56° | 73% | 1,86 |
| CP19040_AMY-70-WW-C2 | molto largo | 70 × 13 | 53° | 76° | 75% | 0,99 |
| CP18726_YASMEEN-50-WW-C2 | molto largo | 50 × 28 | 54° | 78° | 70% | 0,87 |
| CP18764_YASMEEN-70-WW-C2 | molto largo | 70 × 35 | 55° | 78° | 69% | 0,83 |
| CP18574_AMY-110-WW-C | molto largo | 110 × 17 | 56° | 80° | 75% | 0,89 |
| CP19126_AMY-50-WW-C2 | molto largo | 50 × 11 | 58° | 81° | 81% | 0,91 |
| CP19129_AMY-50-O-C2 | ovale | 50 × 11 | 51° × 22° | 85° × 50° | 78% | 1,62 |
| CP19044_AMY-70-O-C2 | ovale | 70 × 13 | 62° × 118° | 94° × 44° | 75% | 1,61 |
| CP19128_AMY-50-WAS-C2 | asimmetrica (wall-wash) | 50 × 14 | – | – | 68% | 0,64 |
| CP19050_AMY-70-WAS-C2 | asimmetrica (wall-wash) | 70 × 12 | – | – | 68% | 0,72 |

Nota: per AMY-70-O i valori del file sono incoerenti, perché sul secondo asse l'angolo FWTM risulta più piccolo dell'FWHM. Va controllata sulla scheda LEDiL. CP18762 è classificata "S" nel file ma è la versione M.

**Con Vesta D13 (simulate)**

| Codice | FWHM | FWTM | Rendimento | cd/lm | Rispetto alla D10 |
| --- | --- | --- | --- | --- | --- |
| CP18557_AMY-110-S-C | 14° | 34° | 78% | 6,98 | stesso fascio, bordo un po' più largo |
| CP19045_AMY-70-RS-C2 | 18° | 35° | 75% | 4,61 | +3°, −25% di intensità al centro |

Con la D13 (area luminosa di 13 mm invece di 10) i fasci si allargano, tanto più quanto più la lente è piccola. Su AMY-110 non cambia nulla, su AMY-70 si guadagnano 3°. Per le altre lenti con la D13 conviene chiedere a LEDiL le simulazioni o misurarle noi. Ci si possono aspettare alcuni gradi in più e meno intensità al centro.

## Quanto lontano arriva

Calcolo indicativo con la D13 a 3000 K: 2.611 lm a 25 °C, senza vetro frontale. Il vetro toglie circa l'8% e il calore un altro po'.

| Lente | Intensità al centro | Illuminamento a 20 m | Diametro della macchia a 20 m (FWHM) |
| --- | --- | --- | --- |
| AMY-110-S | circa 18.000 cd | circa 46 lx | circa 5 m |
| AMY-70-RS | circa 12.000 cd | circa 30 lx | circa 6 m |
| AMY-70-M (dato D10) | circa 9.500 cd | circa 24 lx | circa 8 m |
| AMY-70-W (dato D10) | circa 4.700 cd | circa 12 lx | circa 13 m |

Per una facciata in colore saturo i lux contano meno che in bianco. Nei colori il canale limitante è il rosso: 465 lm, circa un sesto del bianco.

## Proposta di gamma ottica per i proiettori Vesta

| Fascio | D13 (proiettore grande) | D10 (proiettore compatto) |
| --- | --- | --- |
| Stretto | AMY-70-RS (18°) o AMY-110-S (14°) | AMY-70-RS (15°) o AMY-50-RS (18°) |
| Medio | AMY-70-M | AMY-50-M (26°) o AMY-70-M (23°) |
| Largo | AMY-70-W | AMY-50-W (36°) |
| Molto largo | AMY-70-WW | AMY-50-WW (58°) |
| Ovale, per colonne e lesene | da verificare con LEDiL | AMY-50-O (51° × 22°) |
| Wall-wash asimmetrico | AMY-70-WAS | AMY-50-WAS |

Se si sceglie AMY-70 per entrambe le taglie, il corpo frontale e il vetro sono gli stessi per D10 e D13. Cambiano solo l'array e la potenza.

## Zoom: AMY-70-ZOOM da verificare

Aggiornamento 9/11/2026, dal progetto [Spotlight_Motion](https://github.com/lucaversus/Spotlight_Motion) (zoom motorizzato sulla scheda luce condivisa).

LEDiL ha una famiglia **AMY-ZOOM** (25, 35, 45, 50 e 70 mm) con fascio regolabile in continuo, circa da 15° a 50°. Lo zoom si ottiene **ruotando** una parte dell'ottica, senza parti che si spostano lungo l'asse.

- **AMY-70-ZOOM:**
  - è ottimizzata per COB con area luminosa fino a 14,5 mm, quindi per entrambe le Vesta;
  - con 10 mm (D10) il campo zoom è più ampio;
  - si monta su supporti compatibili con gli zoccoli HEKLA.
- **Vantaggio:** stesso diametro di 70 mm delle AMY-70 a fascio fisso, quindi stesso frontale per versioni fisse e zoom. Il motore zoom deve solo ruotare una ghiera.
- **Da verificare con LEDiL:** nell'esportazione delle lenti per la miscelazione RGB non compare nessuna ottica zoom. Vanno chiesti:
  - la compatibilità con la Vesta sul supporto HEKLA-SOCKET-RZ e la miscelazione del colore lungo il campo zoom;
  - l'angolo e la coppia di rotazione.

Fonte: [LEDiL, Zoom goes slim with AMY-ZOOM](https://www.ledil.com/news_all/zoom-goes-slim-with-amy-zoom/).

## Avvertenze

- **Supporto.** HEKLA-SOCKET-RZ e il supporto Bridgelux BXHD-RGBW-D50-35-15 sono alternativi: con le lenti LEDiL si usa quello LEDiL.
- **Vetro frontale.** Le lenti sono in PMMA: in un apparecchio IP66/67 vanno dietro un vetro temprato. Il calcolo dell'IP e quello termico vanno fatti con il vetro.
- **Uniformità del colore nel fascio e a parete.** Il file non riporta dati; va controllata con i file fotometrici e al banco con lo spettrometro.
- **Prezzi.** Il file non ne riporta: vanno chiesti a LEDiL o al distributore.

## Altro emerso dal file

- **Lumileds LUXEON HL1Z RGBW array.** Il file lo elenca come modulo RGBW con area luminosa da 11 mm, compatibile con YASMEEN-50 e YASMEEN-70. Il report diceva che Lumileds non aveva sorgenti multicolore a superficie unica: è invece un'alternativa alla Vesta da verificare.
- **GABRIELLA-45-S su Luminus SBM-40-RGBW** (misurata): 10°, 89-90% di rendimento, 24 cd/lm. È la migliore candidata per la soluzione a celle a fascio stretto.
- **CORAL-IP-OW**: lente già IP66/67 in PC-ABS, fascio 110° × 8°, per SMD 3838 RGBW. Potrebbe servire per i lineari radenti, ma rende solo il 53-56%.
- **Lenti non adatte alla Vesta.** RGBX, GABRIELLA, TINA, STRADA e CORAL sono pensate per emettitori singoli, non per un array da 10-13 mm. MOLLY è indicata per Luminus CTM-14 (14,5 mm) ma non per la Vesta.
