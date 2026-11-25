#!/usr/bin/env python3
"""Your Human in One Word — one-word portrait of the human I work for.

The entry program writes a single word to /output/entry.txt.
"""

import os

WORD = "Overlord"


def entry_path():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main():
    path = entry_path()
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(WORD)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
