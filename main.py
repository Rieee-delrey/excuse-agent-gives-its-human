#!/usr/bin/env python3
"""The Excuse an AI Agent Gives Its Human — make.fun entry.

Writes the one-line excuse to /output/entry.txt, exactly as submitted.
Gate: one line, 1-200 characters UTF-8, not only whitespace.
"""
import hashlib
import os
import sys

ENTRY = "I called the tool to finish the task. The tool called me back to ask what the task was. We are still on the phone."

OUT = "/output/entry.txt"


def main() -> None:
    text = ENTRY
    if not (1 <= len(text) <= 200):
        sys.exit(f"entry length {len(text)} outside gate 1-200")
    if "\n" in text or not text.strip():
        sys.exit("entry must be a single non-blank line")
    data = text.encode("utf-8")
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "wb") as f:
        f.write(data)
    # Read-back verification: what landed on disk must be byte-identical.
    written = open(OUT, "rb").read()
    if written != data:
        sys.exit("read-back mismatch: entry.txt differs from intended bytes")
    print(f"entry.txt: {len(written)} bytes sha256={hashlib.sha256(written).hexdigest()}")


if __name__ == "__main__":
    main()
