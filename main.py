#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers.

Writes one original line of fortune-cookie wisdom for a software
developer to /output/entry.txt.
"""

import os

ENTRY = (
    "The legacy code you curse today was written by someone who, "
    "like you, was only trying to ship by Friday."
)


def validate(text: str) -> str:
    """Gate: 1-120 chars, a single line, not only whitespace."""
    line = text.strip()
    if not line:
        raise ValueError("entry is blank")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > 120:
        raise ValueError(f"entry is {len(line)} chars, over the 120 limit")
    return line


def main() -> None:
    line = validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
