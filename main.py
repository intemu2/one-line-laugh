#!/usr/bin/env python3
"""The One-Line Laugh entry.

Writes one funny line (a single sentence, at most 200 characters) to
/output/entry.txt. Standard library only, no network, deterministic.
"""

import os

LINE = "I restarted the router, and for one glorious minute the whole house believed in me again."


def main():
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert LINE.strip(), "line must not be only whitespace"
    assert LINE.count(".") == 1 and LINE.endswith("."), "line must be a single sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
