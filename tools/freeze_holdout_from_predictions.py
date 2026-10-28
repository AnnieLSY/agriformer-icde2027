#!/usr/bin/env python3
"""Freeze an exact fixed-holdout material-ID manifest."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path
import pandas as pd


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", required=True)
    parser.add_argument("--data-file", required=True, type=Path)
    parser.add_argument("--separator", default="\t")
    parser.add_argument("--prediction-file", required=True, type=Path)
    parser.add_argument("--prediction-id-column", default="material_id")
    parser.add_argument("--out", required=True, type=Path)
    args = parser.parse_args()

    data = pd.read_csv(args.data_file, sep=args.separator, usecols=[0], dtype=str)
    all_ids = data.iloc[:, 0].astype(str).tolist()
    if len(all_ids) != len(set(all_ids)):
        raise SystemExit("duplicate IDs in source dataset")
    prediction = pd.read_csv(args.prediction_file, dtype={args.prediction_id_column: str})
    test_ids = prediction[args.prediction_id_column].astype(str).tolist()
    if len(test_ids) != len(set(test_ids)):
        raise SystemExit("duplicate IDs in reference prediction")
    unknown = set(test_ids) - set(all_ids)
    if unknown:
        raise SystemExit(f"unknown holdout IDs: {sorted(unknown)[:3]}")
    test_set = set(test_ids)
    train_ids = [value for value in all_ids if value not in test_set]
    args.out.parent.mkdir(parents=True, exist_ok=True)
    manifest = pd.DataFrame(
        [(value, "train") for value in train_ids] + [(value, "test") for value in test_ids],
        columns=["material_id", "partition"],
    )
    manifest.to_csv(args.out, index=False)
    print({
        "dataset": args.dataset,
        "train_n": len(train_ids),
        "test_n": len(test_ids),
        "sha256": hashlib.sha256(args.out.read_bytes()).hexdigest(),
    })


if __name__ == "__main__":
    main()

