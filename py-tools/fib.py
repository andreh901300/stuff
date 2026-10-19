#!/usr/bin/env python3
"""number toys: fibonacci, primes, factorial.
usage:
  python3 fib.py fib 15
  python3 fib.py primes 50
  python3 fib.py fact 6
"""
import sys


def fib(n: int):
    a, b = 0, 1
    out = []
    for _ in range(n):
        out.append(a)
        a, b = b, a + b
    return out


def primes_up_to(n: int):
    """sieve of eratosthenes."""
    if n < 2:
        return []
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return [i for i, p in enumerate(sieve) if p]


def factorial(n: int) -> int:
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def main(argv):
    if len(argv) < 3:
        print(__doc__.strip())
        return
    cmd, n = argv[1], int(argv[2])
    if cmd == "fib":
        print(fib(n))
    elif cmd == "primes":
        print(primes_up_to(n))
    elif cmd == "fact":
        print(f"{n}! = {factorial(n)}")
    else:
        print(f"unknown command: {cmd}")


if __name__ == "__main__":
    main(sys.argv)
