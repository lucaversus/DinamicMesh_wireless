"""Simulatore Monte Carlo della coesistenza a 2,4 GHz per la rete mesh ESP-NOW.

Modella, in modo semplificato ma con ipotesi esplicite:
  - propagazione: perdita di percorso log-distanza, perdita del corpo dell'apparecchio,
    shadowing lognormale per collegamento e fading veloce per pacchetto;
  - interferenti Wi-Fi a raffiche (periodi ON/OFF esponenziali) con potenza calcolata
    nodo per nodo, attenuazioni di muri e ostacoli;
  - accesso al canale con ascolto (CSMA): un nodo rimanda la trasmissione se sente il
    canale occupato (preamboli Wi-Fi sopra -82 dBm o pacchetti della propria rete);
  - perdita di un pacchetto quando il rapporto segnale/interferenza al ricevitore è sotto
    la soglia della velocità radio usata (effetto cattura incluso) o quando il ricevitore
    sta trasmettendo;
  - protocollo: comando di scena temporizzato con K copie del coordinatore, inoltro mesh
    con soppressione a contatore, rinfresco periodico dello stato completo;
  - controllo dal vivo: flusso a 30 aggiornamenti al secondo dal coordinatore.

Non modella: modulazione bit per bit, cattura parziale, adattamento di velocità, multipercorso
dettagliato, cambio di canale (equivale a passare allo scenario senza interferenze).

Uso:  python3 coesistenza_24ghz.py [--runs 200] [--out risultati]
"""
from __future__ import annotations

import argparse
import zlib
import heapq
import json
import math
from dataclasses import dataclass, field

import numpy as np

# --------------------------------------------------------------------------- PHY
# Valori tipici per ricevitori 802.11b/g di classe ESP32 (ipotesi, da verificare sul datasheet ESP32-C5)
PHY = {
    1: dict(sens=-97.0, sir=3.0, difs=50.0, slot=20.0, cw=31),   # DSSS 1 Mbps, guadagno di processo
    6: dict(sens=-92.0, sir=6.0, difs=34.0, slot=9.0, cw=15),    # OFDM 6 Mbps BPSK 1/2
}
CCA_WIFI = -82.0          # soglia di rilevamento preambolo Wi-Fi (dBm)
OVERHEAD_B = 24 + 4 + 15  # MAC + FCS + intestazione ESP-NOW
CRYPTO_B = 16             # cifratura applicativa
PROC_US = 300.0           # elaborazione per salto
TX_POWER = 15.0           # dBm, potenza dei nodi
BODY_LOSS = 5.0           # dB per estremo (antenna nel corpo / finestra plastica)
SIGMA_SHADOW = 4.0        # dB, shadowing lognormale per collegamento
SIGMA_FAST = 2.0          # dB, fading per pacchetto


def airtime_us(payload_b: int, rate: int) -> float:
    n = payload_b + CRYPTO_B + OVERHEAD_B
    if rate == 1:
        return 192.0 + n * 8.0
    bits_sym = {6: 24, 12: 48}[rate]
    return 20.0 + 4.0 * math.ceil((16 + 6 + n * 8) / bits_sym)


def pathloss(d, n_exp):
    d = np.maximum(d, 1.0)
    return 40.0 + 10.0 * n_exp * np.log10(d)


# --------------------------------------------------------------------------- scenario
@dataclass
class Interferer:
    name: str
    pos: tuple                 # (x, y, z) metri; z<0 dentro l'edificio
    ptx: float                 # dBm EIRP
    occupancy: float           # frazione di tempo ON
    mean_on_ms: float          # durata media di una raffica
    wall_loss: float = 0.0     # dB, attenuazione verso tutti i nodi
    shadow_rule: tuple | None = None   # (asse, soglia, extra_dB): nodi con coord < soglia +extra dB
    # stato realizzato
    p_node: np.ndarray = field(default=None, repr=False)
    starts: np.ndarray = field(default=None, repr=False)
    ends: np.ndarray = field(default=None, repr=False)

    def realize(self, rng, nodes, n_exp, horizon_us):
        d = np.linalg.norm(nodes - np.array(self.pos), axis=1)
        p = self.ptx - pathloss(d, n_exp) - self.wall_loss - BODY_LOSS
        if self.shadow_rule:
            axis, thr, extra = self.shadow_rule
            p = p - np.where(nodes[:, axis] < thr, extra, 0.0)
        self.p_node = p + rng.normal(0, SIGMA_SHADOW, len(nodes))
        # reciprocita': l'interferente sente il nodo se la potenza del nodo al suo ricevitore supera la soglia CCA
        self.hears = (self.p_node - self.ptx + TX_POWER) >= CCA_WIFI
        on = self.mean_on_ms * 1000.0
        off = on * (1.0 - self.occupancy) / self.occupancy
        n = int(horizon_us / (on + off) * 1.5) + 50
        ons = rng.exponential(on, n)
        offs = rng.exponential(off, n)
        t0 = rng.uniform(0, on + off)
        starts = t0 + np.concatenate(([0.0], np.cumsum(ons + offs)[:-1])) + offs
        self.starts = starts
        self.ends = starts + ons

    def overlaps(self, t0, t1):
        i = np.searchsorted(self.ends, t0, side="right")
        return i < len(self.starts) and self.starts[i] < t1, (self.ends[i] if i < len(self.ends) else None)

    def burst_start(self, t0):
        i = np.searchsorted(self.ends, t0, side="right")
        return self.starts[i] if i < len(self.starts) else np.inf


@dataclass
class Topology:
    name: str
    nodes: np.ndarray          # (N,3)
    n_exp: float
    coord: int = 0


def facade(n_side=10, size=10.0):
    step = size / n_side
    xs = (np.arange(n_side) + 0.5) * step
    pts = np.array([(x, y, 0.0) for y in xs for x in xs])
    return Topology(f"facciata {size:.0f}x{size:.0f} m, {n_side*n_side} apparecchi", pts, 2.5, coord=0)


def bridge(length=300.0, spacing=10.0):
    xs = np.arange(0.0, length + 0.1, spacing)
    pts = np.array([(x, 0.0, 0.0) for x in xs])
    return Topology(f"ponte {length:.0f} m, {len(xs)} apparecchi", pts, 2.7, coord=0)


# --------------------------------------------------------------------------- simulazione rete
class Network:
    def __init__(self, topo: Topology, interferers, rate, rng, horizon_us):
        self.t = topo
        self.N = len(topo.nodes)
        self.rate = rate
        self.phy = PHY[rate]
        self.rng = rng
        d = np.linalg.norm(topo.nodes[:, None, :] - topo.nodes[None, :, :], axis=2)
        sh = rng.normal(0, SIGMA_SHADOW, (self.N, self.N))
        sh = (sh + sh.T) / np.sqrt(2)
        self.P = TX_POWER - pathloss(d, topo.n_exp) - 2 * BODY_LOSS + sh   # P[src, dst]
        np.fill_diagonal(self.P, 50.0)
        self.intf = interferers
        for it in self.intf:
            it.realize(rng, topo.nodes, topo.n_exp, horizon_us)
        self.own = []   # trasmissioni proprie: (start, end, src)

    # ---- accesso al canale
    def next_start(self, node, t):
        ph = self.phy
        for _ in range(400):
            bo = self.rng.integers(0, ph["cw"] + 1) * ph["slot"]
            need = ph["difs"] + bo
            block = None
            for it in self.intf:
                if it.p_node[node] >= CCA_WIFI:
                    ov, end = it.overlaps(t, t + need)
                    if ov:
                        block = end if block is None else min(block, end)
            for (s, e, src) in self.own:
                if e > t and s < t + need and (src == node or self.P[src, node] >= CCA_WIFI):
                    block = e if block is None else min(block, e)
            if block is None:
                return t + need
            t = block
        return t

    # ---- ricezione di una trasmissione
    def receive(self, s, e, src):
        S = self.P[src] + self.rng.normal(0, SIGMA_FAST, self.N)
        ok = S >= self.phy["sens"]
        thr = S - self.phy["sir"]
        for it in self.intf:
            ov, _ = it.overlaps(s, e)
            if ov:
                # se l'interferente sente chi trasmette, rimanda le raffiche che inizierebbero durante il pacchetto:
                # collisione solo con una raffica gia' in corso (o iniziata entro uno slot)
                if it.hears[src] and it.burst_start(s) >= s + self.phy["slot"]:
                    continue
                ok &= it.p_node < thr
        for (s2, e2, src2) in self.own:
            if src2 != src and s2 < e and e2 > s:
                ok &= self.P[src2] < thr
                ok[src2] = False          # half duplex
        ok[src] = False
        return ok

    def prune(self, t):
        self.own = [x for x in self.own if x[1] > t - 5000]

    # ---- un messaggio in flooding
    def flood(self, t0, payload, copies, window_us, relay=True, suppress=3, relay_jitter_us=4000.0):
        N, coord = self.N, self.t.coord
        air = airtime_us(payload, self.rate)
        arrival = np.full(N, np.inf)
        arrival[coord] = t0
        heard = np.zeros(N, int)
        hops = np.full(N, -1)
        hops[coord] = 0
        relayed = np.zeros(N, bool)
        ev = []
        seq = 0
        times = [t0] + list(t0 + np.sort(self.rng.uniform(0, window_us, copies - 1)))
        for tt in times:
            heapq.heappush(ev, (tt, seq, "tx", coord)); seq += 1
        busy_until = np.zeros(N)
        while ev:
            t, _, kind, data = heapq.heappop(ev)
            if kind == "tx":
                node = data
                if node != coord and heard[node] >= suppress:
                    continue
                st = self.next_start(node, max(t, busy_until[node]))
                en = st + air
                busy_until[node] = en
                self.own.append((st, en, node))
                heapq.heappush(ev, (en, seq, "rx", (st, en, node))); seq += 1
            else:
                st, en, src = data
                ok = self.receive(st, en, src)
                heard += ok
                new = ok & ~np.isfinite(arrival)
                if new.any():
                    arrival[new] = en + PROC_US
                    hops[new] = hops[src] + 1
                    if relay:
                        for n in np.nonzero(new)[0]:
                            if not relayed[n]:
                                relayed[n] = True
                                tr = en + PROC_US + self.rng.uniform(0, relay_jitter_us)
                                heapq.heappush(ev, (tr, seq, "tx", int(n))); seq += 1
        self.prune(t0 + 1e6)
        return arrival - t0, hops

    # ---- flusso dal vivo (solo coordinatore, salto singolo)
    def stream(self, t0, n_nodes_data, bytes_per_node, fps=30, seconds=3.0):
        coord = self.t.coord
        frame_us = 1e6 / fps
        total = n_nodes_data * bytes_per_node
        pkts = math.ceil(total / 250)
        sizes = [250] * (pkts - 1) + [total - 250 * (pkts - 1)]
        node_pkt = (np.arange(self.N) * bytes_per_node) // 250
        node_pkt = np.minimum(node_pkt, pkts - 1)
        frames = int(seconds * fps)
        got = np.zeros((frames, self.N), bool)
        busy_air = 0.0
        for f in range(frames):
            fs = t0 + f * frame_us
            fe = fs + frame_us
            t = fs
            ok_pkt = np.zeros((pkts, self.N), bool)
            for k, sz in enumerate(sizes):
                st = self.next_start(coord, t)
                air = airtime_us(sz, self.rate)
                en = st + air
                if en > fe:
                    break
                ok_pkt[k] = self.receive(st, en, coord)
                busy_air += air
                t = en
            got[f] = ok_pkt[node_pkt, np.arange(self.N)]
        got[:, coord] = True
        loss = 1.0 - got.mean(axis=0)
        # blocco più lungo (aggiornamenti consecutivi persi)
        worst = 0
        for n in range(self.N):
            run = best = 0
            for v in got[:, n]:
                run = 0 if v else run + 1
                best = max(best, run)
            worst = max(worst, best)
        return dict(loss_mean=float(loss[np.arange(self.N) != coord].mean()),
                    loss_max=float(loss.max()),
                    freeze_max_ms=worst * frame_us / 1000.0,
                    own_occupancy=busy_air / (frames * frame_us))


# --------------------------------------------------------------------------- scenari
def facade_scenarios():
    return {
        "Pulito": [],
        "Wi-Fi interno 30%": [Interferer("AP interno", (5, 5, -3), 20, 0.30, 3.0, wall_loss=3)],
        "Wi-Fi interno 60%": [Interferer("AP interno", (5, 5, -3), 20, 0.60, 3.0, wall_loss=3)],
        "Wi-Fi nascosto 40%": [Interferer("AP vicino, dietro l'angolo", (16, 5, 4), 20, 0.40, 3.0,
                                          shadow_rule=(0, 6.0, 30.0))],
        "Telecamera nascosta 85%": [Interferer("telecamera Wi-Fi", (16, 5, 4), 20, 0.85, 30.0,
                                               shadow_rule=(0, 6.0, 30.0))],
    }


def bridge_scenarios():
    return {
        "Pulito": [],
        "Telecamera a metà ponte 85%": [Interferer("telecamera su sponda", (150, 15, 3), 20, 0.85, 30.0)],
        "Wi-Fi su sponda 40%": [Interferer("AP bar su sponda", (60, 20, 2), 20, 0.40, 3.0, wall_loss=3)],
    }


def run_scene(topo, scen, rate, copies, runs, seed, refresh_s=1.0, deadline_ms=50.0, horizon_s=8.0,
              window_ms=30.0, relay=True):
    rng = np.random.default_rng(seed)
    all_ok = on_time_frac = 0.0
    lat_last = []
    consist = []
    hops_max = []
    for r in range(runs):
        intf = [Interferer(**{k: getattr(i, k) for k in
                              ("name", "pos", "ptx", "occupancy", "mean_on_ms", "wall_loss", "shadow_rule")})
                for i in scen]
        net = Network(topo, intf, rate, rng, horizon_s * 1e6)
        t0 = rng.uniform(0, 0.5e6)
        arr, hops = net.flood(t0, 48, copies, window_ms * 1000.0, relay=relay)
        others = np.arange(net.N) != topo.coord
        ok = arr[others] <= deadline_ms * 1000.0
        all_ok += ok.all()
        on_time_frac += ok.mean()
        fin = arr[others][np.isfinite(arr[others])]
        if len(fin) == others.sum():
            lat_last.append(fin.max() / 1000.0)
        hops_max.append(hops[others].max())
        # rinfresco dello stato
        missing = np.where(others & ~(arr <= deadline_ms * 1000.0))[0]
        t_cons = deadline_ms / 1000.0 if len(missing) == 0 else np.inf
        k = 1
        miss = set(missing.tolist())
        while miss and k * refresh_s < horizon_s - 0.5:
            tr = t0 + k * refresh_s * 1e6
            a2, _ = net.flood(tr, 48 + 5 * 2, 1, 0.0, relay=relay)
            got = {n for n in miss if a2[n] <= deadline_ms * 1000.0}
            miss -= got
            if not miss:
                t_cons = k * refresh_s + deadline_ms / 1000.0
            k += 1
        consist.append(t_cons)
    consist = np.array(consist)
    return dict(p_all_on_time=all_ok / runs, frac_on_time=on_time_frac / runs,
                lat_last_p95_ms=float(np.percentile(lat_last, 95)) if lat_last else None,
                consist_p99_s=float(np.percentile(consist, 99)) if np.isfinite(np.percentile(consist, 99)) else None,
                consist_max_s=float(consist.max()) if np.isfinite(consist.max()) else None,
                p_not_consistent=float(np.mean(~np.isfinite(consist))),
                hops_max=int(np.max(hops_max)))


def run_stream(n_side, bits, scen, runs, seed, rate=6):
    rng = np.random.default_rng(seed)
    topo = facade(n_side)
    res = []
    for r in range(runs):
        intf = [Interferer(**{k: getattr(i, k) for k in
                              ("name", "pos", "ptx", "occupancy", "mean_on_ms", "wall_loss", "shadow_rule")})
                for i in scen]
        net = Network(topo, intf, rate, rng, 5e6)
        res.append(net.stream(rng.uniform(0, 0.5e6), n_side * n_side, 5 * bits // 8))
    return {k: float(np.mean([x[k] for x in res])) if k != "freeze_max_ms" else float(np.max([x[k] for x in res]))
            for k in res[0]}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--runs", type=int, default=1000)
    ap.add_argument("--out", default="risultati")
    a = ap.parse_args()
    import os
    os.makedirs(a.out, exist_ok=True)
    out = {"scene_facciata": [], "scene_ponte": [], "streaming": [], "refresh": []}

    topo = facade(10)
    for sname, scen in facade_scenarios().items():
        for rate in (1, 6):
            for k in (1, 3, 5):
                r = run_scene(topo, scen, rate, k, a.runs, seed=zlib.crc32(repr((sname, rate, k)).encode()))
                r.update(scenario=sname, rate=rate, copies=k)
                out["scene_facciata"].append(r)
                print("facciata", sname, rate, k, r, flush=True)

    for refresh in (0.5, 1.0, 2.0):
        scen = facade_scenarios()["Telecamera nascosta 85%"]
        r = run_scene(topo, scen, 6, 3, a.runs, seed=7 + int(refresh * 10), refresh_s=refresh)
        r.update(refresh_s=refresh)
        out["refresh"].append(r)
        print("refresh", refresh, r, flush=True)

    for sname in ("Wi-Fi nascosto 40%", "Telecamera nascosta 85%"):
        for k in (1, 3, 5):
            r = run_scene(topo, facade_scenarios()[sname], 6, k, a.runs,
                          seed=zlib.crc32(repr(("nomesh", sname, k)).encode()), relay=False)
            r.update(scenario=sname, rate=6, copies=k, mesh=False)
            out.setdefault("senza_mesh", []).append(r)
            print("senza mesh", sname, k, r, flush=True)

    btopo = bridge()
    for sname, scen in bridge_scenarios().items():
        for rate in (1, 6):
            for k in (1, 3, 5):
                r = run_scene(btopo, scen, rate, k, a.runs, seed=zlib.crc32(repr(("b", sname, rate, k)).encode()))
                r.update(scenario=sname, rate=rate, copies=k)
                out["scene_ponte"].append(r)
                print("ponte", sname, rate, k, r, flush=True)

    for n_side in (5, 10, 20):
        for bits in (8, 16):
            for sname, scen in facade_scenarios().items():
                r = run_stream(n_side, bits, scen, max(20, a.runs // 10), seed=zlib.crc32(repr(("s", n_side, bits, sname)).encode()))
                r.update(scenario=sname, apparecchi=n_side * n_side, bit=bits)
                out["streaming"].append(r)
                print("stream", n_side * n_side, bits, sname, r, flush=True)

    with open(os.path.join(a.out, "risultati.json"), "w") as f:
        json.dump(out, f, indent=1, ensure_ascii=False)


if __name__ == "__main__":
    main()
