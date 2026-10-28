#!/usr/bin/env python3
"""Build a relative-path manifest for frozen reference files."""

from __future__ import annotations

import csv
import hashlib
from pathlib import Path


def digest(path: Path):
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def main():
    root = Path(__file__).resolve().parents[1]
    reference = root / "results_reference"
    output = reference / "REFERENCE_MANIFEST.tsv"
    files = [
        path for path in sorted(reference.rglob("*"))
        if path.is_file() and path != output
    ]
    with output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["path", "bytes", "sha256"], delimiter="\t")
        writer.writeheader()
        for path in files:
            writer.writerow({
                "path": path.relative_to(reference).as_posix(),
                "bytes": path.stat().st_size,
                "sha256": digest(path),
            })
    print(f"wrote {len(files)} entries to {output}")


if __name__ == "__main__":
    main()

