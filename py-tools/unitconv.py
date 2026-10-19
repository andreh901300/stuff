#!/usr/bin/env python3
"""convert some units.
usage:
  python3 unitconv.py c2f 100
  python3 unitconv.py f2c 32
  python3 unitconv.py km2mi 42
  python3 unitconv.py mi2km 26
  python3 unitconv.py kg2lb 70
  python3 unitconv.py lb2kg 154
"""
import sys

CONVERSIONS = {
    "c2f": lambda c: c * 9 / 5 + 32,
    "f2c": lambda f: (f - 32) * 5 / 9,
    "km2mi": lambda km: km * 0.621371,
    "mi2km": lambda mi: mi / 0.621371,
    "kg2lb": lambda kg: kg * 2.20462,
    "lb2kg": lambda lb: lb / 2.20462,
}


def main(argv):
    if len(argv) < 3:
        print(__doc__.strip())
        print("available:", ", ".join(CONVERSIONS))
        return
    key, value = argv[1].lower(), float(argv[2])
    fn = CONVERSIONS.get(key)
    if not fn:
        print(f"no conversion {key!r}. try one of: {', '.join(CONVERSIONS)}")
        return
    print(f"{value:g} -> {fn(value):.4g}")


if __name__ == "__main__":
    main(sys.argv)
