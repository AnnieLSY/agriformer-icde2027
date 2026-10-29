#!/usr/bin/env python3
"""Fail when release files contain machine-specific or credential-like text."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

LOCAL_ACCOUNT = "".join(chr(value) for value in (97, 110, 110, 105, 101))
MAC_HOME = "/" + "Users" + "/"
LINUX_HOME = "/" + "home" + "/"
CJK = "\u3400-\u9fff"

PATTERNS = {
    "local_username": re.compile(
        rf"(?i)(?<![A-Za-z0-9_]){re.escape(LOCAL_ACCOUNT)}(?![A-Za-z0-9_])"
    ),
    "absolute_macos_user_path": re.compile(re.escape(MAC_HOME) + r"[^/\s]+/"),
    "absolute_linux_user_path": re.compile(re.escape(LINUX_HOME) + r"[^/\s]+/"),
    "absolute_windows_user_path": re.compile(r"(?i)[A-Z]:\\Users\\[^\\\s]+\\"),
    "cjk_directory_segment": re.compile(
        rf"(?:^|[/\\])[^\s`\"',;/\\]*[{CJK}][^\s`\"',;/\\]*"
        rf"(?:[/\\])(?=[A-Za-z0-9_.-])"
    ),
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
    parser.add_argument(
        "root", nargs="?", type=Path, default=Path(__file__).resolve().parents[1]
    )
    args = parser.parse_args()
    findings = []
    for path in sorted(args.root.rglob("*")):
        if not path.is_file() or ".git" in path.parts:
            continue
        relative = path.relative_to(args.root)
        if any(re.search(rf"[{CJK}]", part) for part in relative.parts):
            findings.append((relative, "cjk_directory_name", 0))
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for name, pattern in PATTERNS.items():
            for match in pattern.finditer(text):
                line = text.count("\n", 0, match.start()) + 1
                findings.append((relative, name, line))
    for path, name, line in findings:
        location = f"{path}:{line}" if line else str(path)
        print(f"{location}: {name}")
    if findings:
        raise SystemExit(1)
    print(
        "Sensitive-content scan: 0 usernames, 0 local paths, "
        "0 CJK directory names, 0 credential patterns."
    )


if __name__ == "__main__":
    main()
