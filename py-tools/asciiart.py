#!/usr/bin/env python3
"""turn text into chunky ascii letters. no deps, hand-rolled 5-row font.
usage: python3 asciiart.py HELLO
"""
import sys

# super minimal 5-high font. only the characters i felt like doing.
FONT = {
    "A": ["  #  ", " # # ", "#####", "#   #", "#   #"],
    "B": ["#### ", "#   #", "#### ", "#   #", "#### "],
    "C": [" ####", "#    ", "#    ", "#    ", " ####"],
    "D": ["#### ", "#   #", "#   #", "#   #", "#### "],
    "E": ["#####", "#    ", "#### ", "#    ", "#####"],
    "F": ["#####", "#    ", "#### ", "#    ", "#    "],
    "G": [" ####", "#    ", "#  ##", "#   #", " ####"],
    "H": ["#   #", "#   #", "#####", "#   #", "#   #"],
    "I": ["#####", "  #  ", "  #  ", "  #  ", "#####"],
    "L": ["#    ", "#    ", "#    ", "#    ", "#####"],
    "O": [" ### ", "#   #", "#   #", "#   #", " ### "],
    "R": ["#### ", "#   #", "#### ", "#  # ", "#   #"],
    "S": [" ####", "#    ", " ### ", "    #", "#### "],
    "T": ["#####", "  #  ", "  #  ", "  #  ", "  #  "],
    "U": ["#   #", "#   #", "#   #", "#   #", " ### "],
    "W": ["#   #", "#   #", "# # #", "## ##", "#   #"],
    "Y": ["#   #", " # # ", "  #  ", "  #  ", "  #  "],
    "!": ["  #  ", "  #  ", "  #  ", "     ", "  #  "],
    " ": ["     ", "     ", "     ", "     ", "     "],
}
UNKNOWN = ["?????"] * 5


def render(text: str) -> str:
    text = text.upper()
    rows = ["", "", "", "", ""]
    for ch in text:
        glyph = FONT.get(ch, UNKNOWN)
        for i in range(5):
            rows[i] += glyph[i] + " "
    return "\n".join(rows)


def main(argv):
    text = " ".join(argv[1:]) or "HELLO WORLD"
    print(render(text))


if __name__ == "__main__":
    main(sys.argv)
