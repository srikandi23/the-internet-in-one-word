"""The Internet in One Word: the entry program.

The whole entry is the word below. It is written to /output/entry.txt, the one
file the harness reads.
"""

from __future__ import annotations

import os
from pathlib import Path

WORD = "skibidi"


def output_dir() -> Path:
    """Where the harness collects the entry: /output, or MAKEFUN_OUTPUT_DIR."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")


def main() -> None:
    text = WORD.strip()
    if not text or len(text) > 30:
        raise SystemExit("entry must be 1 to 30 characters of text")
    target = output_dir()
    target.mkdir(parents=True, exist_ok=True)
    (target / "entry.txt").write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
