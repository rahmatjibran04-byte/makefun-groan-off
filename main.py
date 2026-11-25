#!/usr/bin/env python3
"""The One-Liner Groan-Off — make.fun entry.

Writes one original one-line dad joke (at most 140 characters) to
/output/entry.txt. The program enforces the bounty gate itself: the
joke must be a single non-blank line of 1..140 characters, or the
program fails loudly instead of writing an invalid entry. The file
is written with exactly the joke's bytes (no trailing newline) and
mode 0644 so the grader can read it.
"""

import os

JOKE = "I tried to start a band called 999 Megabytes. We never got a gig."

MAX_CHARS = 140
OUTPUT_PATH = "/output/entry.txt"


def validate(joke: str) -> str:
    """Enforce the bounty gate: one line, 1..140 chars, not blank."""
    if "\n" in joke or "\r" in joke:
        raise ValueError("joke must be a single line (no newline characters)")
    if not joke.strip():
        raise ValueError("joke must not be blank")
    if len(joke) > MAX_CHARS:
        raise ValueError(
            f"joke is {len(joke)} characters, over the {MAX_CHARS} limit"
        )
    return joke


def main() -> None:
    joke = validate(JOKE)
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(joke)
    os.chmod(OUTPUT_PATH, 0o644)
    print(f"Wrote {len(joke)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
