#!/usr/bin/env python3
"""Quick-mode metric reconstruction from frozen per-sample predictions."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import pandas as pd

from agriformer.metrics import compute_metrics

OBSERVED = ("observed", "obs", "y_true", "actual")
PREDICTED = ("predicted", "prediction", "pred", "y_pred")


def find_column(frame, aliases):
    lookup = {str(c).lower(): c for c in frame.columns}
    return next((lookup[name] for name in aliases if name in lookup), None)


def column_pairs(frame):
    observed = find_column(frame, OBSERVED)
    predicted = find_column(frame, PREDICTED)
    if observed is not None and predicted is not None:
        return [("YLD", observed, predicted)]
    lookup = {str(c).lower(): c for c in frame.columns}
    pairs = []
    for column in frame.columns:
        lower = str(column).lower()
        if lower.startswith("observed_"):
            trait = str(column)[len("Observed_"):]
            match = lookup.get(f"predicted_{trait}".lower())
            if match is not None:
                pairs.append((trait, column, match))
    if pairs:
        return pairs
    observed_candidates = [c for c in frame.columns if str(c).lower().startswith("observed_")]
    if len(observed_candidates) == 1:
        observed = observed_candidates[0]
        trait = str(observed).split("_", 1)[1]
        for column in frame.columns:
            lower = str(column).lower()
            if "predicted" in lower or lower.endswith("_pred"):
                pairs.append((f"{trait}:{column}", observed, column))
    return pairs


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--reference-dir", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    rows, skipped = [], []
    for path in sorted(args.reference_dir.rglob("*.csv")):
        frame = pd.read_csv(path)
        pairs = column_pairs(frame)
        if not pairs:
            skipped.append({"file": str(path), "reason": "no observation/prediction pair"})
            continue
        for trait, observed, predicted in pairs:
            metrics = compute_metrics(frame[observed], frame[predicted])
            rows.append({
                "file": str(path.relative_to(args.reference_dir)),
                "trait_or_output": trait,
                "observed_column": observed,
                "predicted_column": predicted,
                **metrics,
            })
    args.out.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(rows).to_csv(args.out / "recomputed_metrics.csv", index=False)
    (args.out / "quick_mode_summary.json").write_text(
        json.dumps({"scored_files": len(rows), "skipped": skipped}, indent=2), encoding="utf-8"
    )


if __name__ == "__main__":
    main()

