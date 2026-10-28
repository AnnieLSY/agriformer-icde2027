#!/usr/bin/env python3
"""Freeze exact train/test material-ID manifests from authoritative predictions."""

from __future__ import annotations

import argparse
import hashlib
import re
from pathlib import Path
import pandas as pd


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", required=True)
    parser.add_argument("--data-file", required=True, type=Path)
    parser.add_argument("--separator", default="\t")
    parser.add_argument("--prediction-dir", required=True, type=Path)
    parser.add_argument("--pattern", required=True)
    parser.add_argument("--out", required=True, type=Path)
    args = parser.parse_args()

    data = pd.read_csv(args.data_file, sep=args.separator, usecols=[0], dtype=str)
    id_column = data.columns[0]
    all_ids = data[id_column].astype(str).tolist()
    if len(all_ids) != len(set(all_ids)):
        raise SystemExit(f"duplicate material IDs in {args.data_file}")
    all_id_set = set(all_ids)
    args.out.mkdir(parents=True, exist_ok=True)
    rows = []
    files = sorted(args.prediction_dir.glob(args.pattern))
    if not files:
        raise SystemExit("no authoritative prediction files matched")
    for prediction_file in files:
        match = re.search(r"_r(\d+)_f(\d+)_", prediction_file.name)
        if not match:
            raise SystemExit(f"cannot infer repeat/fold: {prediction_file.name}")
        repeat, fold = map(int, match.groups())
        prediction = pd.read_csv(prediction_file, dtype={"material_id": str})
        test_ids = prediction["material_id"].astype(str).tolist()
        if len(test_ids) != len(set(test_ids)):
            raise SystemExit(f"duplicate test IDs: {prediction_file}")
        unknown = set(test_ids) - all_id_set
        if unknown:
            raise SystemExit(f"unknown test IDs in {prediction_file}: {sorted(unknown)[:3]}")
        test_set = set(test_ids)
        train_ids = [value for value in all_ids if value not in test_set]
        manifest = pd.DataFrame(
            [(value, "train") for value in train_ids] + [(value, "test") for value in test_ids],
            columns=["material_id", "partition"],
        )
        output = args.out / f"repeat_{repeat}_fold_{fold}.csv"
        manifest.to_csv(output, index=False)
        rows.append({
            "dataset": args.dataset,
            "repeat": repeat,
            "fold": fold,
            "train_n": len(train_ids),
            "test_n": len(test_ids),
            "manifest": output.name,
            "sha256": hashlib.sha256(output.read_bytes()).hexdigest(),
        })
    pd.DataFrame(rows).sort_values(["repeat", "fold"]).to_csv(args.out / "SPLIT_INDEX.csv", index=False)
    print(f"froze {len(rows)} split manifests for {args.dataset}")


if __name__ == "__main__":
    main()

