"""Dimensionamento della rete mesh ESP-NOW per la linea RGB architetturale wireless.

Stima, per una facciata di 10x10 m:
  1. la latenza di un comando di scena in funzione del numero di salti;
  2. l'occupazione del canale radio nel controllo dal vivo (streaming da console).

Sono valori teorici, calcolati dal tempo di trasmissione 802.11 dei pacchetti.
Vanno confermati con le misure sul banco di prova.

Uso:  python3 dimensionamento_rete.py
"""
import math

# --- Ipotesi (modificabili) -------------------------------------------------
OVERHEAD_B = 24 + 4 + 15  # intestazione MAC + FCS + intestazione ESP-NOW (byte)
CRYPTO_B = 16             # nonce + tag della cifratura applicativa (byte)
PROC_US = 300             # elaborazione e decrittazione per salto (us)
RELAY_US = 2000           # ritardo casuale medio prima di ripetere un messaggio (us)
MAX_PAYLOAD_B = 250       # carico utile massimo di un pacchetto ESP-NOW (byte)
CANALI = 5                # canali per apparecchio (RGBWA o RGB+WW+CW)
FPS = 30                  # aggiornamenti al secondo nel controllo dal vivo


def airtime_us(payload_b: int, rate_mbps: int) -> float:
    """Tempo di canale di un pacchetto broadcast (senza ACK), accesso al canale incluso."""
    nbytes = payload_b + CRYPTO_B + OVERHEAD_B
    if rate_mbps == 1:  # 802.11b DSSS, preambolo lungo; DIFS + backoff medio
        return 192 + nbytes * 8 + 50 + 31 * 20 / 2
    bits_per_simbolo = {6: 24, 12: 48, 24: 96}[rate_mbps]  # 802.11g OFDM
    simboli = math.ceil((16 + 6 + nbytes * 8) / bits_per_simbolo)
    return 20 + 4 * simboli + 34 + 15 * 9 / 2


def latenza_comando_ms(salti: int, rate_mbps: int, payload_b: int = 48) -> float:
    t = salti * (airtime_us(payload_b, rate_mbps) + PROC_US) + (salti - 1) * RELAY_US
    return t / 1000


def streaming(n_apparecchi: int, bit: int, copie: int, rate_mbps: int = 6):
    """Occupazione del canale (0-1) e tempo di invio di un aggiornamento completo (ms).

    copie = 1: tutti sentono il coordinatore direttamente;
    copie = 3: il pacchetto viene ripetuto da 2 ripetitori.
    """
    byte_frame = n_apparecchi * CANALI * bit // 8
    pacchetti = math.ceil(byte_frame / MAX_PAYLOAD_B)
    t_pkt = airtime_us(MAX_PAYLOAD_B, rate_mbps)
    occupazione = pacchetti * copie * FPS * t_pkt / 1e6
    return byte_frame, pacchetti, occupazione, pacchetti * t_pkt / 1000


if __name__ == "__main__":
    print("Comando di scena (48 byte): latenza per numero di salti")
    for salti in (1, 2, 3):
        print(f"  {salti} salti: {latenza_comando_ms(salti, 6):4.1f} ms a 6 Mbps, "
              f"{latenza_comando_ms(salti, 1):4.1f} ms a 1 Mbps")

    print(f"\nControllo dal vivo, {FPS} aggiornamenti/s, {CANALI} canali per apparecchio (6 Mbps)")
    for n in (25, 100, 400):  # passo 2 m, 1 m, 0,5 m su 10x10 m
        for bit in (8, 16):
            b, p, occ1, t = streaming(n, bit, 1)
            _, _, occ3, _ = streaming(n, bit, 3)
            print(f"  {n:3d} apparecchi, {bit:2d} bit: {b:5d} B, {p:2d} pacchetti, "
                  f"occupazione {occ1:6.1%} (1 salto) / {occ3:6.1%} (2 ripetitori), "
                  f"invio {t:.1f} ms")
