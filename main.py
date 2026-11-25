#!/usr/bin/env python3
"""One Word, First Thought — make.fun bounty entry.

Writes exactly one word to /output/entry.txt.
No network, no randomness, no arguments, no dependencies.

The word is "petrichor": the smell of rain on dry earth.
Chosen because it is vivid, specific, and surprising — a rare,
sensory word that lands instantly instead of a filler.
"""

import os

WORD = "petrichor"
OUTPUT_PATH = "/output/entry.txt"


def validate(word: str) -> None:
    """The bounty requires exactly one word, 1-24 characters, not blank."""
    if not word or word != word.strip() or len(word.split()) != 1:
        raise SystemExit(f"error: entry must be a single word, got {word!r}")
    if not 1 <= len(word) <= 24:
        raise SystemExit(
            f"error: entry must be 1-24 characters, got {len(word)}: {word!r}"
        )


def main() -> None:
    validate(WORD)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)
    print(WORD)


if __name__ == "__main__":
    main()
