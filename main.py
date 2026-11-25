#!/usr/bin/env python3
"""One Word, First Thought — make.fun bounty entry.

Writes exactly one word to /output/entry.txt.
No network, no randomness, no arguments, no dependencies.
"""

import os

WORD = "petrichor"
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)
    print(WORD)


if __name__ == "__main__":
    main()
