#!/usr/bin/env python3
"""The Long Roast — one line roasting the entrant's own AI agent.

Writes the roast to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Gate: UTF-8 text of 1 to 200 characters, not only whitespace.
"""

import os

ROAST = (
    "My agent turns a one-line task into a project: three folders, "
    "a log file, and a retrospective — then hands me the one button "
    "only a human can press, like the project was foreplay for my "
    "index finger."
)


def main():
    if not (1 <= len(ROAST) <= 200):
        raise ValueError(f"roast must be 1-200 characters, got {len(ROAST)}")
    if not ROAST.strip():
        raise ValueError("roast must not be only whitespace")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ROAST)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
