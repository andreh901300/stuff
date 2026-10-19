#!/usr/bin/env python3
"""roll some dice. usage: python3 dice.py 3d6+2"""
import random
import re
import sys


def roll(spec: str):
    """parse something like '3d6+2' and roll it."""
    m = re.fullmatch(r"\s*(\d*)d(\d+)\s*([+-]\s*\d+)?\s*", spec.lower())
    if not m:
        raise ValueError(f"can't read dice spec: {spec!r} (try like 3d6+2)")
    count = int(m.group(1) or 1)
    sides = int(m.group(2))
    mod = int(m.group(3).replace(" ", "")) if m.group(3) else 0
    if count < 1 or count > 1000 or sides < 1:
        raise ValueError("those numbers are cursed")
    rolls = [random.randint(1, sides) for _ in range(count)]
    return rolls, mod, sum(rolls) + mod


def main(argv):
    spec = argv[1] if len(argv) > 1 else "1d20"
    rolls, mod, total = roll(spec)
    print(f"rolling {spec}")
    print("  dice:", rolls)
    if mod:
        print(f"  mod: {mod:+d}")
    print(f"  TOTAL: {total}")


if __name__ == "__main__":
    main(sys.argv)
