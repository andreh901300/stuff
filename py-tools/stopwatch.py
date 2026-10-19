#!/usr/bin/env python3
"""dumb terminal stopwatch. enter = lap, q = quit. python3 stopwatch.py"""
import time


def fmt(seconds: float) -> str:
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    return f"{int(h):02d}:{int(m):02d}:{s:06.3f}"


def main():
    start = time.monotonic()
    laps = []
    print("stopwatch started. press enter for a lap, type q then enter to stop.")
    try:
        while True:
            cmd = input()
            now = time.monotonic() - start
            if cmd.strip().lower() == "q":
                break
            laps.append(now)
            print(f"  lap {len(laps)}: {fmt(now)}")
    except (KeyboardInterrupt, EOFError):
        pass
    total = time.monotonic() - start
    print(f"\ntotal: {fmt(total)} over {len(laps)} lap(s)")


if __name__ == "__main__":
    main()
