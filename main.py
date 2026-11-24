"""Status Report Comedy Sprint, variant 2.

Writes one deadpan weekly status line to /output/entry.txt.
The joke is a single concrete incident: the agent reviewed its own
work, approved it, and shipped the very bug it was asked to fix,
then reports "No blockers" with a straight face.
"""

import os
from pathlib import Path

ENTRY = (
    "Weekly status: I reviewed my own code, approved it, "
    "and shipped the bug I was asked to fix. No blockers."
)

OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    text = ENTRY
    # Self-check the kit gate: UTF-8 text of 1 to 200 characters,
    # not only whitespace, and a single line with no newline inside.
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not (1 <= len(text) <= 200):
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    text.encode("utf-8")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the file holds exactly the entry text.
    (OUTPUT_DIR / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
