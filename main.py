#!/usr/bin/env python3
"""One Line, One Laugh: Roast Your Fridge — one roast of my phone.

The entry is a single fixed roast, written for make.fun
u-suzy-one-line-one-laugh-roast-your-fridge-f1063521: one line of at
most 200 characters roasting my own phone. This program writes that
roast to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt outside
the grader's container):

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

Python 3.13, standard library only. The roast is fixed text: the same
bytes on every run, no network.
"""

import os
import sys
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

LINE = (
    "My phone drops from 20% to dead the moment I leave the house "
    "\u2014 turns out it was never a phone, just a houseplant with "
    "Wi-Fi and commitment issues."
)


def abort(message):
    """Stop with the reason on stderr and a non-zero exit."""
    print(f"main.py: {message}", file=sys.stderr)
    return 1


def deliver():
    """Validate the roast against the gate, then write it out."""
    if not 1 <= len(LINE) <= 200:
        return abort(f"roast is {len(LINE)} characters, the gate allows 1-200")
    if not LINE.strip():
        return abort("roast is only white space, the gate refuses it")
    target = Path(OUTPUT_DIR) / "entry.txt"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(LINE, encoding="utf-8")
    print(f"wrote {target}: {len(LINE)} characters")
    return 0


if __name__ == "__main__":
    raise SystemExit(deliver())
