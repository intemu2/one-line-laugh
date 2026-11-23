"""One-line laugh for make.fun: The One-Line Laugh.

Writes the winning one-sentence joke to /output/entry.txt.
The entry is a single sentence (87 characters, under the 200 cap):
a phone dying at 2% while its owner reads battery-saving tips --
an everyday frustration with a surprise sting at the end.
"""

from pathlib import Path

ENTRY = (
    "My phone died at 2% while I was reading about battery-saving tips, "
    "which felt personal."
)


def main() -> None:
    # Gate check, mirroring the competition gate: 1-200 UTF-8 chars.
    if not 1 <= len(ENTRY) <= 200 or not ENTRY.strip():
        raise ValueError(f"entry length {len(ENTRY)} is outside 1-200 characters")
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
