#!/usr/bin/env python3
"""Reconstruct Tables I--V and Figs. 3--5 from frozen source data only."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path
import shutil
import numpy as np
import pandas as pd

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


DATASET_ORDER = ["AUS2015", "GABI", "Ward", "lentil", "pine", "rice", "wheatG"]
BLUE, ORANGE, GREEN, DARK, MID = "#2F6FB0", "#D47A22", "#2C8B57", "#555555", "#888888"


def style():
    plt.rcParams.update({
        "font.family": "serif", "font.size": 8, "axes.labelsize": 8,
        "axes.titlesize": 8, "xtick.labelsize": 8, "ytick.labelsize": 8,
        "legend.fontsize": 8, "pdf.fonttype": 42, "ps.fonttype": 42,
        "axes.spines.top": False, "axes.spines.right": False,
    })


def escape(value):
    return str(value).replace("\\", r"\textbackslash{}").replace("&", r"\&").replace("%", r"\%").replace("_", r"\_")


def write_latex_table(frame, path, caption, label):
    columns = list(frame.columns)
    lines = [
        r"\begin{table*}[t]", r"\centering", f"\\caption{{{caption}}}", f"\\label{{{label}}}",
        r"\scriptsize", r"\begin{tabular}{" + "l" * len(columns) + "}", r"\toprule",
        " & ".join(escape(column) for column in columns) + r" \\", r"\midrule",
    ]
    for row in frame.itertuples(index=False, name=None):
        values = []
        for value in row:
            if isinstance(value, float):
                values.append("---" if not np.isfinite(value) else f"{value:.4g}")
            else:
                values.append(escape(value))
        lines.append(" & ".join(values) + r" \\")
    lines.extend([r"\bottomrule", r"\end{tabular}", r"\end{table*}", ""])
    path.write_text("\n".join(lines), encoding="utf-8")


def figure3(frame, out):
    frame = frame.set_index("dataset").loc[DATASET_ORDER].reset_index()
    x = np.arange(len(frame)); width = 0.36
    fig, ax = plt.subplots(figsize=(3.5, 2.45))
    ax.bar(x - width / 2, frame.mean_delta_ln_pcc, width, color=MID, edgecolor=DARK, hatch="///", label=r"$\Delta\ln\mathrm{PCC}$")
    ax.bar(x + width / 2, frame.mean_delta_ln_cb, width, color=GREEN, edgecolor=DARK, hatch="...", label=r"$\Delta\ln C_b$")
    ax.axhline(0, color=DARK, lw=.6); ax.set_xticks(x, frame.dataset, rotation=35, ha="right")
    ax.set_ylabel("Mean change in log component"); ax.legend(frameon=False); fig.tight_layout()
    return fig


def figure4(frame, out):
    fig, axes = plt.subplots(2, 2, figsize=(7.16, 5.65))
    for ax, panel, title in [(axes[0, 0], "sample", "(a) Sample availability"), (axes[0, 1], "marker", "(b) Marker availability")]:
        part = frame[frame.panel == panel]
        for model, group in part.groupby("model"):
            group = group.sort_values("ratio")
            ax.plot(100 * group.ratio, group.ccc, marker="o", label=model, color=BLUE if model == "AF" else MID)
        ax.set_title(title, loc="left", fontweight="bold"); ax.set_xlabel("Retained (%)"); ax.set_ylabel("CCC"); ax.legend(frameon=False)
    ax = axes[1, 0]
    part = frame[frame.panel == "missingness"]
    for (dataset, model), group in part.groupby(["dataset", "model"]):
        ax.plot(100 * group.missing_fraction, group.ccc_drop, marker="o", label=f"{dataset}, {model}")
    ax.axhline(0, color=DARK, lw=.6); ax.set_title("(c) Test-genotype missingness", loc="left", fontweight="bold")
    ax.set_xlabel("Masked test genotypes (%)"); ax.set_ylabel("Mean CCC decrease"); ax.legend(frameon=False, fontsize=6)
    ax = axes[1, 1]
    part = frame[frame.panel == "applicability"]
    ax.scatter(part.gblup_cb, part.af_minus_gblup_ccc, color=BLUE)
    for row in part.itertuples():
        ax.annotate(row.dataset, (row.gblup_cb, row.af_minus_gblup_ccc), fontsize=7)
    ax.axhline(0, color=DARK, lw=.6); ax.set_title("(d) Calibration and AF gain", loc="left", fontweight="bold")
    ax.set_xlabel(r"GBLUP $C_b$"); ax.set_ylabel(r"AF $-$ GBLUP: $\Delta$CCC")
    fig.tight_layout(); return fig


def figure5(frame, out):
    fig, axes = plt.subplots(1, 2, figsize=(7.16, 3.75))
    ax = axes[0]; part = frame[frame.panel == "inflation"]
    positions = {dataset: index for index, dataset in enumerate(DATASET_ORDER)}
    styles = {("AF-MT", "PCC"): (BLUE, "o"), ("AF-MT", "CCC"): (BLUE, "^"), ("MLP-Dual", "PCC"): (DARK, "s"), ("MLP-Dual", "CCC"): (DARK, "D")}
    for key, group in part.groupby(["model", "metric"]):
        color, marker = styles.get(key, (MID, "o"))
        ax.scatter([positions[x] for x in group.dataset], group.naive_minus_scoped, color=color, marker=marker, label=", ".join(key))
    ax.axhline(0, color=DARK, lw=.6); ax.set_xticks(range(7), DATASET_ORDER, rotation=32, ha="right")
    ax.set_ylabel("Naive minus scoped"); ax.set_title("(a) Preparation-induced overestimation", loc="left", fontweight="bold"); ax.legend(frameon=False, fontsize=6)
    ax = axes[1]; part = frame[frame.panel == "difficulty_rank"]
    for row in part.itertuples():
        ax.plot([0, 1], [row.scoped_rank, row.naive_rank], marker="o", label=row.dataset)
    ax.set_xticks([0, 1], ["Scoped", "Naive"]); ax.invert_yaxis(); ax.set_ylabel("Difficulty rank")
    ax.set_title("(b) Wheat difficulty order", loc="left", fontweight="bold"); ax.legend(frameon=False)
    fig.tight_layout(); return fig


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(reference, out):
    out.mkdir(parents=True, exist_ok=True)
    source_dir = out / "source_data"; source_dir.mkdir(exist_ok=True)
    table_info = {
        "i": ("Phenotype use in examined studies and AgriFormer", "tab:phenotype_routing"),
        "ii": ("Dataset profiles and GBLUP calibration", "tab:data_profiles"),
        "iii": ("Fixed-holdout comparison by model", "tab:holdout"),
        "iv": ("Replacement effects and learner dependence", "tab:replacement"),
        "v": ("Recorded efficiency and parameter sensitivity", "tab:efficiency"),
    }
    for number, (caption, label) in table_info.items():
        source = reference / f"table_{number}_source_data.csv"
        frame = pd.read_csv(source)
        shutil.copy2(source, source_dir / source.name)
        write_latex_table(frame, out / f"table_{number}.tex", caption, label)
        for suffix in ("evidence.json", "provenance.csv"):
            associated = reference / f"table_{number}_{suffix}"
            if associated.exists(): shutil.copy2(associated, source_dir / associated.name)
    figures = {"3": figure3, "4": figure4, "5": figure5}
    style()
    for number, builder in figures.items():
        source = reference / f"fig{number}_source_data.csv"
        frame = pd.read_csv(source)
        shutil.copy2(source, source_dir / source.name)
        figure = builder(frame, out)
        figure.savefig(out / f"fig{number}.pdf")
        figure.savefig(out / f"fig{number}.png", dpi=300)
        plt.close(figure)
        for suffix in ("evidence.json", "provenance.csv"):
            associated = reference / f"fig{number}_{suffix}"
            if associated.exists(): shutil.copy2(associated, source_dir / associated.name)
    files = sorted(path for path in out.rglob("*") if path.is_file())
    manifest = [{"file": str(path.relative_to(out)), "sha256": digest(path), "bytes": path.stat().st_size} for path in files]
    (out / "MANIFEST.json").write_text(json.dumps(manifest, indent=2) + "\n")
    return manifest


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--reference-dir", required=True, type=Path)
    parser.add_argument("--out", required=True, type=Path)
    args = parser.parse_args()
    manifest = run(args.reference_dir, args.out)
    print(f"Reconstructed 5 tables and 3 figures; manifested {len(manifest)} files.")


if __name__ == "__main__":
    main()
