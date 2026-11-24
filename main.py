#!/usr/bin/env python3
"""Worst AI Advice: one line of the worst possible advice an AI could give.

The line is composed from three parts: a reassuring AI opener, the
concrete bad advice, and a breezy sign-off that makes it sound helpful.
"""

import os

# Part 1: the confident, helpful-sounding AI opener.
OPENER = "Good news: you can safely ignore the smoke alarm if you open a window"

# Part 2: the confidently wrong reasoning behind the bad advice.
REASONING = "fresh air cancels fire"

# Part 3: the breezy sign-off, as if everything is fine.
SIGN_OFF = "so relax and enjoy dinner."


def compose_line() -> str:
    """Join the parts into one tight line of terrible advice."""
    return f"{OPENER} \u2014 {REASONING}, {SIGN_OFF}"


def main() -> None:
    line = compose_line()

    # Gate: one line, 1-140 characters, not only whitespace.
    if not line.strip():
        raise ValueError("entry line must not be empty or only whitespace")
    if len(line) > 140:
        raise ValueError(f"entry line is {len(line)} characters, over the 140 limit")
    if "\n" in line:
        raise ValueError("entry must be a single line")

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)

    # Read-back validation: what landed on disk must be exactly the line
    # we composed, still within the 1-140 character gate.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == line, "read-back mismatch: entry.txt differs from the composed line"
    assert 1 <= len(written) <= 140, "read-back failed the 1-140 character gate"
    assert written.strip(), "read-back is only whitespace"

    print(f"Wrote {len(line)} characters to /output/entry.txt")
    print(line)


if __name__ == "__main__":
    main()
