#!/usr/bin/env python3
"""Fail when the active Python or R environment differs from the tested lock."""

from __future__ import annotations

import importlib.metadata
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def python_lock():
    rows = {}
    for line in (ROOT / "environment/requirements-lock.txt").read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            name, version = line.split("==", 1)
            rows[name] = version
    return rows


def main():
    failures = []
    expected_python = (ROOT / "environment/python-version.txt").read_text().strip()
    actual_python = ".".join(str(value) for value in sys.version_info[:3])
    if actual_python != expected_python:
        failures.append(f"Python: expected {expected_python}, found {actual_python}")
    for name, expected in python_lock().items():
        try:
            actual = importlib.metadata.version(name)
        except importlib.metadata.PackageNotFoundError:
            failures.append(f"Python package missing: {name}=={expected}")
            continue
        if actual != expected:
            failures.append(f"Python {name}: expected {expected}, found {actual}")
    lock = json.loads((ROOT / "environment/renv.lock").read_text())
    expression = "cat(as.character(getRversion()), '\\n'); for (p in c('BGLR','rrBLUP','truncnorm','MASS')) cat(p, as.character(packageVersion(p)), '\\n')"
    try:
        completed = subprocess.run(["Rscript", "-e", expression], check=True, capture_output=True, text=True)
        lines = [line.strip() for line in completed.stdout.strip().splitlines()]
        actual_r = lines[0] if lines else "unknown"
        if actual_r != lock["R"]["Version"]:
            failures.append(f"R: expected {lock['R']['Version']}, found {actual_r}")
        found = dict(line.split(maxsplit=1) for line in lines[1:])
        for name, record in lock["Packages"].items():
            actual = found.get(name, "missing")
            if actual != record["Version"]:
                failures.append(f"R {name}: expected {record['Version']}, found {actual}")
    except (OSError, subprocess.CalledProcessError) as error:
        failures.append(f"R lock check could not run: {error}")
    if failures:
        raise SystemExit("\n".join(failures))
    print("Environment matches the tested Python/R lock.")


if __name__ == "__main__":
    main()
