"""Write one short text for a make.fun bounty entry.

Standard library only, no network. Writes the bytes with no trailing newline
into the folder named by MAKEFUN_OUTPUT_DIR when set, else /output, creating
the folder if needed. Prints the character count to stderr.
"""

import os
import sys
from pathlib import Path

TEXT = "For three years my father called the dog by my name. The dog has been dead since 2019. I answer anyway."


def output_dir() -> Path:
    """Return the destination folder: MAKEFUN_OUTPUT_DIR, then OUTPUT_DIR, then /output."""
    for name in ("MAKEFUN_OUTPUT_DIR", "OUTPUT_DIR"):
        value = os.environ.get(name)
        if value:
            return Path(value)
    return Path("/output")


def main() -> int:
    text = TEXT
    assert 1 <= len(text) <= 280, f"text length {len(text)} outside 1..280"

    folder = output_dir()
    folder.mkdir(parents=True, exist_ok=True)
    path = folder / "entry.txt"
    path.write_bytes(text.encode("utf-8"))

    print(len(text), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
