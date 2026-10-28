#!/usr/bin/env python3
"""Fail when release files contain machine-specific or credential-like text."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

PATTERNS = {
    "absolute_user_path": re.compile(r"/Users/[^/\s]+/"),
    "private_key": re.compile(r"BEGIN (?:RSA |OPENSSH )?PRIVATE KEY"),
    "ipv4_private": re.compile(
        r"\b(?:10\.\d{1,3}\.\d{1,3}\.\d{1,3}|"
        r"172\.(?:1[6-9]|2\d|3[01])\.\d{1,3}\.\d{1,3}|"
        r"192\.168\.\d{1,3}\.\d{1,3})\b"
    ),
    "password_assignment": re.compile(r"(?i)password\s*[:=]"),
}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    findings = []
    for path in sorted(args.root.rglob("*")):
        if not path.is_file() or ".git" in path.parts or path.resolve() == Path(__file__).resolve():
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for name, pattern in PATTERNS.items():
            for match in pattern.finditer(text):
                findings.append((path.relative_to(args.root), name, text.count("\n", 0, match.start()) + 1))
    for path, name, line in findings:
        print(f"{path}:{line}: {name}")
    if findings:
        raise SystemExit(1)
    print("No sensitive-content patterns detected.")


if __name__ == "__main__":
    main()

