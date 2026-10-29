#!/usr/bin/env python3
"""Audit the 30 AUS2015-only regressors promised in the Table III note."""

from __future__ import annotations

import hashlib
from pathlib import Path
import pandas as pd


def audit(root: Path):
    folder = root / "results_reference/table_iii"
    results = pd.read_csv(folder / "aus2015_only_30_regressors.csv")
    manifest = pd.read_csv(folder / "aus2015_only_30_prediction_manifest.csv")
    if len(results) != 30 or results["model"].nunique() != 30:
        raise AssertionError("Table III supplement must contain 30 unique regressors")
    if not ((results["n_materials"] == 75).all()):
        raise AssertionError("AUS2015 holdout result has an unexpected sample count")
    if set(results["model"]) != set(manifest["model"]):
        raise AssertionError("prediction manifest does not cover all 30 regressors")
    for row in manifest.to_dict("records"):
        path = root / row["prediction_file"]
        if not path.is_file():
            raise AssertionError(f"missing prediction file: {path}")
        if hashlib.sha256(path.read_bytes()).hexdigest() != row["sha256"]:
            raise AssertionError(f"prediction hash mismatch: {path}")
    return {"models": len(results), "prediction_files": len(manifest)}


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    finding = audit(root)
    print(f"PASS AUS2015-only regressors: {finding['models']} models, {finding['prediction_files']} files")
