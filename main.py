#!/usr/bin/env python3
"""The One-Line Laugh entry (make.fun u-ronigrv-the-one-line-laugh-7ccca46f).

Writes one funny line to /output/entry.txt: a single sentence of at most
200 characters. Deterministic, no network, no dependencies, no secrets.
"""
import os

LINE = "I bought a houseplant to teach myself responsibility, and it died just to prove I was a fast learner."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
