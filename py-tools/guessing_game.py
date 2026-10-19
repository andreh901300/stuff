#!/usr/bin/env python3
"""classic guess-the-number game. python3 guessing_game.py"""
import random


def play(low: int = 1, high: int = 100) -> int:
    secret = random.randint(low, high)
    tries = 0
    print(f"i'm thinking of a number between {low} and {high}.")
    while True:
        raw = input("your guess (or 'q' to quit): ").strip().lower()
        if raw in ("q", "quit", "exit"):
            print(f"coward. it was {secret}.")
            return tries
        try:
            guess = int(raw)
        except ValueError:
            print("that's not a number lol")
            continue
        tries += 1
        if guess < secret:
            print("higher ⬆️")
        elif guess > secret:
            print("lower ⬇️")
        else:
            print(f"🎉 got it in {tries} tries!")
            return tries


if __name__ == "__main__":
    try:
        play()
    except (KeyboardInterrupt, EOFError):
        print("\nbye")
