#!/usr/bin/env python3
"""
random_stuff.py — a single file crammed with pointless harmless junk.
run `python3 random_stuff.py` and it just spits out a bunch of random shi.
"""
import datetime as dt
import random
import string

FACTS = [
    "honey never spoils.",
    "octopuses have three hearts.",
    "bananas are berries but strawberries aren't.",
    "a group of flamingos is called a flamboyance.",
    "wombat poop is cube-shaped.",
    "there are more stars than grains of sand on all beaches.",
]

KAOMOJI = ["(づ｡◕‿‿◕｡)づ", "ʕ•ᴥ•ʔ", "(ノ◕ヮ◕)ノ*:･ﾟ✧", "¯\\_(ツ)_/¯", "(╯°□°)╯︵ ┻━┻"]


def random_hex_color() -> str:
    return "#" + "".join(random.choice("0123456789abcdef") for _ in range(6))


def random_string(n: int = 12) -> str:
    return "".join(random.choice(string.ascii_letters + string.digits) for _ in range(n))


def random_fact() -> str:
    return random.choice(FACTS)


def random_kaomoji() -> str:
    return random.choice(KAOMOJI)


def days_until_new_year() -> int:
    today = dt.date.today()
    ny = dt.date(today.year + 1, 1, 1)
    return (ny - today).days


def lucky_numbers(count: int = 6, hi: int = 49):
    return sorted(random.sample(range(1, hi + 1), count))


def main():
    print("=== random stuff ===")
    print("color:  ", random_hex_color())
    print("string: ", random_string())
    print("fact:   ", random_fact())
    print("mood:   ", random_kaomoji())
    print("lucky:  ", lucky_numbers())
    print(f"days until new year: {days_until_new_year()}")


if __name__ == "__main__":
    main()
