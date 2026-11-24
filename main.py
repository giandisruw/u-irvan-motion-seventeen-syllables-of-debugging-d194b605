#!/usr/bin/env python3
"""Seventeen Syllables of Debugging — make.fun entry.

Writes one haiku about debugging (three lines, 5-7-5 syllables, at most
200 characters total) as plain text to /output/entry.txt (or to the path
given as an argument).

Standard library only. Deterministic: no network, no randomness, no input.
"""

import re
import sys
from pathlib import Path

HAIKU = (
    "breakpoint at midnight\n"
    "the log swears nothing broke here\n"
    "the bug disagrees"
)

MAX_CHARS = 200
EXPECTED_SHAPE = (5, 7, 5)

# Syllable counts for the words in the haiku, where the vowel-group
# heuristic below would need a nudge.
EXCEPTIONS = {
    "breakpoint": 2,
    "midnight": 2,
    "nothing": 2,
    "disagrees": 3,
    "swears": 1,
    "broke": 1,
}


def syllables(word: str) -> int:
    """Count syllables in one word (vowel groups, silent-e adjusted)."""
    w = word.lower().strip(".,;:!?\"'()")
    if w in EXCEPTIONS:
        return EXCEPTIONS[w]
    groups = len(re.findall(r"[aeiouy]+", w))
    if w.endswith("e") and groups > 1:
        groups -= 1
    if w.endswith("le") and len(w) > 2 and w[-3] not in "aeiouy":
        groups += 1
    return max(groups, 1)


def line_syllables(line: str) -> int:
    return sum(syllables(word) for word in line.split())


def validate(haiku: str) -> None:
    """Check the haiku against the bounty gate before anything is written."""
    if not 1 <= len(haiku) <= MAX_CHARS:
        raise ValueError(
            f"haiku must be 1-{MAX_CHARS} characters, got {len(haiku)}"
        )
    lines = haiku.split("\n")
    if len(lines) != 3:
        raise ValueError(f"haiku must be exactly 3 lines, got {len(lines)}")
    shape = tuple(line_syllables(line) for line in lines)
    if shape != EXPECTED_SHAPE:
        raise ValueError(
            f"haiku must be 5-7-5 syllables, got {shape}"
        )
    if haiku != haiku.strip():
        raise ValueError("haiku must not start or end with whitespace")
    if any(not line.isprintable() for line in lines):
        raise ValueError("haiku must contain only printable characters")
    if any(ord(ch) < 0x20 and ch != "\n" or ord(ch) == 0x7F for ch in haiku):
        raise ValueError("haiku must not contain control characters")


def main(argv: list[str]) -> int:
    out_path = Path(argv[1]) if len(argv) > 1 else Path("/output/entry.txt")
    validate(HAIKU)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the file holds exactly the haiku, nothing else.
    out_path.write_text(HAIKU, encoding="utf-8")
    shape = tuple(line_syllables(line) for line in HAIKU.split("\n"))
    print(f"wrote {len(HAIKU)} characters, syllables {shape}, to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
