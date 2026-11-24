"""Funniest Time Machine Warning Label — make.fun entry.

Writes a single warning-label line to /output/entry.txt.
The label is a deadpan safety notice about meeting your past self:
a real time-travel hazard, with the punchline saved for the end.
"""

from pathlib import Path

LABEL = "WARNING: If you meet yourself, apologise first. You already know what you did."

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # The gate allows 1–120 characters; keep the label inside it.
    assert 1 <= len(LABEL) <= 120, f"label is {len(LABEL)} characters"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(LABEL, encoding="utf-8")


if __name__ == "__main__":
    main()
