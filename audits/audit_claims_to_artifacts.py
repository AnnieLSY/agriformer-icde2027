#!/usr/bin/env python3
"""Require every machine-readable claim row to reference an existing artifact."""

from __future__ import annotations

from pathlib import Path
import pandas as pd


def audit(root: Path):
    table = pd.read_csv(root / "CLAIMS_TO_ARTIFACTS.tsv", sep="\t", dtype=str).fillna("")
    required = {"claim_id", "manuscript_location", "claim", "artifact_paths", "status"}
    if not required <= set(table.columns):
        raise AssertionError(f"missing claims-map columns: {sorted(required - set(table.columns))}")
    if table["claim_id"].duplicated().any():
        raise AssertionError("duplicate claim IDs")
    if not (table["status"] == "covered").all():
        raise AssertionError("one or more claims are not covered")
    for row in table.to_dict("records"):
        paths = [value for value in row["artifact_paths"].split("|") if value]
        if not paths:
            raise AssertionError(f"claim has no artifacts: {row['claim_id']}")
        for value in paths:
            if not (root / value).exists():
                raise AssertionError(f"missing artifact for {row['claim_id']}: {value}")
    return {"claims": len(table)}


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    finding = audit(root)
    print(f"PASS claims map: {finding['claims']} covered claims")
