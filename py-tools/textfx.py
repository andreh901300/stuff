#!/usr/bin/env python3
"""mess with text in dumb ways.
usage: python3 textfx.py <effect> <text...>
effects: leet  mock  reverse  clap  space  vapor
"""
import sys

_LEET = str.maketrans({"a": "4", "e": "3", "i": "1", "o": "0", "s": "5", "t": "7"})


def leet(s):
    return s.lower().translate(_LEET)


def mock(s):
    return "".join(c.upper() if i % 2 else c.lower() for i, c in enumerate(s))


def reverse(s):
    return s[::-1]


def clap(s):
    return " 👏 ".join(s.split())


def space(s):
    return " ".join(s)


def vapor(s):
    # fullwidth aesthetic
    out = []
    for c in s:
        o = ord(c)
        if 0x21 <= o <= 0x7E:
            out.append(chr(o + 0xFEE0))
        elif c == " ":
            out.append("　")
        else:
            out.append(c)
    return "".join(out)


EFFECTS = {
    "leet": leet,
    "mock": mock,
    "reverse": reverse,
    "clap": clap,
    "space": space,
    "vapor": vapor,
}


def main(argv):
    if len(argv) < 3:
        print(__doc__.strip())
        print("effects:", ", ".join(EFFECTS))
        return
    effect = argv[1].lower()
    text = " ".join(argv[2:])
    fn = EFFECTS.get(effect)
    if not fn:
        print(f"no such effect: {effect}. pick from {', '.join(EFFECTS)}")
        return
    print(fn(text))


if __name__ == "__main__":
    main(sys.argv)
