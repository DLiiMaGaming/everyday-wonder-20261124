#!/usr/bin/env python3
"""Everyday Wonder, Two Days to Find the Line — entry program.

Writes one sentence (1-200 UTF-8 characters) about a small moment of
wonder in everyday life to /output/entry.txt.

Deterministic: the same bytes on every run, no network, no randomness,
no input read from anywhere.
"""

import os

ENTRY = (
    "At 6 a.m. the lift doors open on a stranger humming the song "
    "my grandmother used to sing while shelling peas, and for three "
    "floors the building forgets we are strangers."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
