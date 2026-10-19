#!/usr/bin/env python3
"""flip a coin a bunch of times and show the stats.
usage: python3 coinflip.py [count]
"""
import random
import sys


def flip_many(n: int):
    heads = sum(1 for _ in range(n) if random.random() < 0.5)
    return heads, n - heads


def bar(value: int, total: int, width: int = 30) -> str:
    if total == 0:
        return ""
    filled = round(width * value / total)
    return "█" * filled + "·" * (width - filled)


def main(argv):
    n = int(argv[1]) if len(argv) > 1 else 1000
    heads, tails = flip_many(n)
    print(f"flipped {n} times")
    print(f"  heads: {heads:>6}  {bar(heads, n)}  {heads / n:.1%}")
    print(f"  tails: {tails:>6}  {bar(tails, n)}  {tails / n:.1%}")


if __name__ == "__main__":
    main(sys.argv)
