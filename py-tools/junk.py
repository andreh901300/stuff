#!/usr/bin/env python3
"""the official junk drawer. a pile of pointless but harmless functions.
run it with no args to see a random demo, or `python3 junk.py all`.
"""
import random
import sys

COMPLIMENTS = [
    "you're doing great, probably",
    "your code compiles in spirit",
    "statistically, you're a 10/10",
    "big brain energy detected",
    "certified epic gamer moment",
]

EIGHT_BALL = [
    "yes", "no", "maybe", "absolutely", "lmao no", "ask again later",
    "the signs point to yes", "doubt it", "100%", "outlook not so good",
]


def shout(s: str) -> str:
    return s.upper() + "!!!"


def owoify(s: str) -> str:
    return s.replace("r", "w").replace("l", "w").replace("R", "W").replace("L", "W")


def roman(n: int) -> str:
    vals = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"),
            (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"),
            (5, "V"), (4, "IV"), (1, "I")]
    out = []
    for v, sym in vals:
        while n >= v:
            out.append(sym)
            n -= v
    return "".join(out) or "nulla"


def is_palindrome(s: str) -> bool:
    cleaned = "".join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]


def random_compliment() -> str:
    return random.choice(COMPLIMENTS)


def magic_eight_ball() -> str:
    return random.choice(EIGHT_BALL)


def demo():
    print("shout:", shout("hello"))
    print("owo:", owoify("really lovely railroad"))
    print("roman 2026:", roman(2026))
    print("palindrome 'Taco cat':", is_palindrome("Taco cat"))
    print("compliment:", random_compliment())
    print("8ball:", magic_eight_ball())


if __name__ == "__main__":
    demo()
