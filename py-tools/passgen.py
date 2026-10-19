#!/usr/bin/env python3
"""random password generator. usage: python3 passgen.py [length] [count]"""
import secrets
import string
import sys

ALPHABET = string.ascii_letters + string.digits + "!@#$%^&*-_=+?"


def make_password(length: int = 16) -> str:
    """cryptographically-random password of the given length."""
    if length < 4:
        length = 4
    # guarantee at least one of each class so it passes dumb validators
    pw = [
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.digits),
        secrets.choice("!@#$%^&*-_=+?"),
    ]
    pw += [secrets.choice(ALPHABET) for _ in range(length - 4)]
    # shuffle without a biased sort
    for i in range(len(pw) - 1, 0, -1):
        j = secrets.randbelow(i + 1)
        pw[i], pw[j] = pw[j], pw[i]
    return "".join(pw)


def main(argv):
    length = int(argv[1]) if len(argv) > 1 else 16
    count = int(argv[2]) if len(argv) > 2 else 5
    for _ in range(count):
        print(make_password(length))


if __name__ == "__main__":
    main(sys.argv)
