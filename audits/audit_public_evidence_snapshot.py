#!/usr/bin/env python3
"""Require the public evidence snapshot to contain only claim-linked records."""

from __future__ import annotations

import csv
from pathlib import Path


EXPECTED_ORIGINAL_IDS = {"O10", "O11", "O14", "O16", "O25"}
EXPECTED_POST_IDS = {
    "AUDIT-GROUPING-20261025",
    "FG-2",
    "LIT-SMALLN-20261026",
    "V13N-C",
    "AUDIT-DUAL-E1-20261025",
}
BANNED_INTERNAL_MARKERS = {
    "bean",
    "superseded",
    "quarantine",
    "results_excluded",
    "_cleanup_quarantine",
}


def _ids(path: Path) -> set[str]:
    with path.open(encoding="utf-8") as handle:
        return {row["id"] for row in csv.DictReader(handle, delimiter="\t")}


def audit(root: Path):
    snapshot = root / "evidence_snapshot"
    claims_path = root / "CLAIMS_TO_ARTIFACTS.tsv"
    with claims_path.open(encoding="utf-8") as handle:
        claims = list(csv.DictReader(handle, delimiter="\t"))
    referenced = {
        Path(value)
        for row in claims
        for value in row["artifact_paths"].split("|")
        if value.startswith("evidence_snapshot/")
    }
    actual = {path.relative_to(root) for path in snapshot.iterdir() if path.is_file()}
    if actual != referenced:
        raise AssertionError(
            f"public evidence file set differs from claims map: actual={sorted(map(str, actual))}, "
            f"referenced={sorted(map(str, referenced))}"
        )
    original = _ids(snapshot / "ORIGINAL_SUBMISSION_EXPERIMENT_LEDGER.tsv")
    post = _ids(snapshot / "POST_OCTOBER_EXPERIMENT_LEDGER.tsv")
    if original != EXPECTED_ORIGINAL_IDS:
        raise AssertionError(f"unexpected original-ledger IDs: {sorted(original)}")
    if post != EXPECTED_POST_IDS:
        raise AssertionError(f"unexpected post-October-ledger IDs: {sorted(post)}")
    for path in snapshot.iterdir():
        text = path.read_text(encoding="utf-8").lower()
        hits = sorted(marker for marker in BANNED_INTERNAL_MARKERS if marker in text)
        if hits:
            raise AssertionError(f"internal-only marker remains in {path.name}: {hits}")
    return {"files": len(actual), "original_rows": len(original), "post_rows": len(post)}


if __name__ == "__main__":
    finding = audit(Path(__file__).resolve().parents[1])
    print(
        "PASS public evidence snapshot: "
        f"{finding['files']} files, {finding['original_rows']} original rows, "
        f"{finding['post_rows']} post-October rows"
    )
