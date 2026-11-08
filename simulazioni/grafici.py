"""Grafici dei risultati di coesistenza_24ghz.py (sfondo bianco, palette fissa)."""
import json
import os
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

BASE = os.path.dirname(os.path.abspath(__file__))
RES = os.path.join(BASE, "risultati")
d = json.load(open(os.path.join(RES, "risultati.json")))

INK, INK2, MUTED, GRID = "#0b0b0b", "#52514e", "#898781", "#e1e0d9"
BLUE = ["#86b6ef", "#2a78d6", "#184f95"]   # rampa sequenziale (1, 3, 5 copie)
ORANGE, AQUA = "#eb6834", "#1baf7a"

plt.rcParams.update({
    "figure.facecolor": "white", "axes.facecolor": "white", "savefig.facecolor": "white",
    "axes.edgecolor": MUTED, "axes.labelcolor": INK2, "xtick.color": INK2, "ytick.color": INK2,
    "axes.spines.top": False, "axes.spines.right": False, "font.size": 10,
    "axes.titlesize": 12, "axes.titleweight": "bold", "axes.titlecolor": INK,
    "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.8, "axes.axisbelow": True,
    "axes.grid.axis": "y", "legend.frameon": False,
})


def bars(ax, cats, series, colors, labels, fmt="{:.0f}%", ylim=(0, 105), scale=100):
    n = len(series)
    w = 0.8 / n
    x = np.arange(len(cats))
    for i, (vals, c, lab) in enumerate(zip(series, colors, labels)):
        xs = x - 0.4 + w * (i + 0.5)
        v = np.array(vals, float) * scale
        ax.bar(xs, v, w * 0.9, color=c, label=lab, edgecolor="white", linewidth=1)
        for xx, vv in zip(xs, v):
            ax.text(xx, vv + ylim[1] * 0.015, fmt.format(vv).replace(".", ","), ha="center", va="bottom", fontsize=8, color=INK2)
    ax.set_xticks(x, cats)
    ax.set_ylim(*ylim)


def pick(rows, **kw):
    return [r for r in rows if all(r.get(k) == v for k, v in kw.items())]


# 1. mesh contro ripetizioni del coordinatore (sorgenti nascoste)
fig, ax = plt.subplots(figsize=(8, 4.2))
cats = ["Wi-Fi nascosto 40%", "Telecamera nascosta 85%"]
series, labels, colors = [], [], []
for i, k in enumerate((1, 3, 5)):
    series.append([pick(d["senza_mesh"], scenario=c, copies=k)[0]["p_all_on_time"] for c in cats])
    labels.append(f"senza mesh, {k} cop{'ia' if k == 1 else 'ie'}")
    colors.append(BLUE[i])
series.append([pick(d["scene_facciata"], scenario=c, rate=6, copies=3)[0]["p_all_on_time"] for c in cats])
labels.append("con mesh, 3 copie")
colors.append(ORANGE)
bars(ax, cats, series, colors, labels)
ax.set_ylabel("comandi arrivati a tutti entro 50 ms")
ax.set_title("Facciata 100 apparecchi: l'inoltro mesh vale più delle ripetizioni")
ax.legend(loc="upper right", ncol=2, fontsize=8)
fig.tight_layout()
fig.savefig(os.path.join(RES, "1_mesh_contro_ripetizioni.png"), dpi=160)

# 2. scenari facciata, 1 contro 6 Mbps (mesh, 3 copie)
fig, ax = plt.subplots(figsize=(9, 4.2))
cats = list(dict.fromkeys(r["scenario"] for r in d["scene_facciata"]))
s1 = [pick(d["scene_facciata"], scenario=c, rate=1, copies=3)[0]["p_all_on_time"] for c in cats]
s6 = [pick(d["scene_facciata"], scenario=c, rate=6, copies=3)[0]["p_all_on_time"] for c in cats]
bars(ax, [c.replace(" ", "\n", 1) for c in cats], [s1, s6], [BLUE[1], ORANGE], ["1 Mbps", "6 Mbps"])
ax.set_ylabel("comandi arrivati a tutti entro 50 ms")
ax.set_title("Facciata: solo una sorgente nascosta e continua fa perdere comandi")
ax.legend(loc="lower left", fontsize=8)
fig.tight_layout()
fig.savefig(os.path.join(RES, "2_scenari_facciata.png"), dpi=160)

# 3. tempo di riallineamento contro intervallo di rinfresco
fig, ax = plt.subplots(figsize=(6, 3.8))
rows = sorted(d["refresh"], key=lambda r: r["refresh_s"])
cats = [f"ogni {r['refresh_s']:g} s".replace(".", ",") for r in rows]
vals = [r["consist_p99_s"] for r in rows]
bars(ax, cats, [vals], [BLUE[1]], ["99° percentile"], fmt="{:.1f} s", ylim=(0, max(vals) * 1.25), scale=1)
ax.set_ylabel("tempo per riallineare tutti (s)")
ax.set_xlabel("rinfresco dello stato completo")
ax.set_title("Telecamera nascosta: il rinfresco fissa il ritardo massimo")
fig.tight_layout()
fig.savefig(os.path.join(RES, "3_rinfresco.png"), dpi=160)

# 4. controllo dal vivo
fig, ax = plt.subplots(figsize=(9, 4.2))
cats = list(dict.fromkeys(r["scenario"] for r in d["streaming"]))
s100 = [pick(d["streaming"], scenario=c, apparecchi=100, bit=16)[0]["loss_mean"] for c in cats]
s400 = [pick(d["streaming"], scenario=c, apparecchi=400, bit=16)[0]["loss_mean"] for c in cats]
bars(ax, [c.replace(" ", "\n", 1) for c in cats], [s100, s400], [BLUE[1], ORANGE],
     ["100 apparecchi, 16 bit", "400 apparecchi, 16 bit"], fmt="{:.1f}%", ylim=(0, 50))
ax.set_ylabel("aggiornamenti persi (media per apparecchio)")
ax.set_title("Controllo dal vivo a 30 fps senza ripetizioni: vulnerabile alle sorgenti nascoste")
ax.legend(loc="upper left", fontsize=8)
fig.tight_layout()
fig.savefig(os.path.join(RES, "4_controllo_dal_vivo.png"), dpi=160)

# 5. ponte
fig, ax = plt.subplots(figsize=(8, 4.2))
cats = list(dict.fromkeys(r["scenario"] for r in d["scene_ponte"]))
s1 = [pick(d["scene_ponte"], scenario=c, rate=1, copies=3)[0]["p_all_on_time"] for c in cats]
s6 = [pick(d["scene_ponte"], scenario=c, rate=6, copies=3)[0]["p_all_on_time"] for c in cats]
bars(ax, [c.replace(" ", "\n", 1) for c in cats], [s1, s6], [BLUE[1], ORANGE], ["1 Mbps", "6 Mbps"])
ax.set_ylabel("comandi arrivati a tutti entro 50 ms")
ax.set_title("Ponte 300 m, 31 apparecchi: la telecamera spezza la catena")
ax.legend(loc="lower left", fontsize=8)
fig.tight_layout()
fig.savefig(os.path.join(RES, "5_ponte.png"), dpi=160)
print("ok")
