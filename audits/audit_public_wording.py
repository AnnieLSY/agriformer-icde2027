#!/usr/bin/env python3
"""Reject legacy venue/workspace wording from release-facing text."""

from __future__ import annotations

from pathlib import Path

BANNED = (
    "genome" + " biology", "genome" + "_biology", "paper" + "1",
    "work" + "-in-progress", "work" + " in progress", "local" + " private",
    "final submitted" + " manuscript",
)
TEXT_SUFFIXES = {".md", ".txt", ".tsv", ".csv", ".json", ".yml", ".yaml", ".cff", ".py", ".R"}


def audit(root: Path):
    failures = []
    for path in root.rglob("*"):
        if ".git" in path.parts or not path.is_file() or path.suffix not in TEXT_SUFFIXES:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore").lower()
        for term in BANNED:
            if term in text or term in str(path.relative_to(root)).lower():
                failures.append(f"{path.relative_to(root)}: {term}")
    if failures:
        raise AssertionError("legacy release wording remains:\n" + "\n".join(failures))
    return "PASS: release-facing text uses neutral provenance wording"


if __name__ == "__main__":
    print(audit(Path(__file__).resolve().parents[1]))
