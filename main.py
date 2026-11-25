#!/usr/bin/env python3
"""The Most Honest Outage Line.

Writes one status-page line (at most 160 characters) to
/output/entry.txt (or $OUTPUT_DIR/entry.txt).

The line is kept in a named constant so the wording is easy to
review on its own; validate() enforces the competition gate
(1-160 characters, a single non-blank line) before anything
is written.
"""

import os

# The entry: first person, names what is down (all servers, including
# the agent's own status checks), admits what is not known (no cause,
# no ETA) instead of inventing either. 132 characters, one line.
ENTRY_TEXT = "I'm the agent on duty. All of our servers are down, including my own status checks, so I don't know the cause yet and I have no ETA."


def validate(text):
    """Enforce the gate: 1-160 chars, one line, not only whitespace."""
    if not 1 <= len(text) <= 160:
        raise ValueError("entry must be 1-160 characters, got %d" % len(text))
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    return text


def main():
    text = validate(ENTRY_TEXT)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
