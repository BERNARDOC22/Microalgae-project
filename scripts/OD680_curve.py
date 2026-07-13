"""
Growth curve plotting for OD680 measurements.

Author: Bernardo Cintra
"""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

DATA_FILE = Path("data/")
OUTPUT_FILE = Path("results/growth_curve_chlorella.png")
OUTPUT_FILE.parent.mkdir(exist_ok=True)

df = pd.read_excel(DATA_FILE, index_col=0)
df = df.dropna(axis=1, how="all")

fig, ax = plt.subplots(figsize=(8, 5.5))

colors = plt.cm.tab10.colors

for i, (label, row) in enumerate(df.iterrows()):
    row = row.dropna()

    x = row.index.str.replace("DAY ", "", regex=False).astype(int)
    y = row.values

    marker = "o" if "control" in label.lower() else "s"
    linestyle = "-" if marker == "o" else "--"

    ax.plot(
        x, y,
        marker=marker,
        linestyle=linestyle,
        color=colors[i % len(colors)],
        label=label
    )

ax.set_xlabel("Dia de cultivo")
ax.set_ylabel("Densidade óptica (OD680)")
ax.set_title("Curva de crescimento")
ax.xaxis.set_major_locator(ticker.MaxNLocator(integer=True))

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

ax.legend(frameon=False)
plt.tight_layout()
plt.savefig(OUTPUT_FILE, dpi=300)
print(f"Saved: {OUTPUT_FILE}")
