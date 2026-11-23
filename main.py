#!/usr/bin/env python3
"""Dad Joke Showdown.

Writes one original dad joke about a suitcase to /output/entry.txt.
Deterministic: the same bytes on every run. No network, stdlib only.
"""

import os

ENTRY = "I told my suitcase there would be no vacation this year. Now it's dealing with emotional baggage."


def main() -> None:
    assert 1 <= len(ENTRY) <= 199, f"entry must be 1-199 chars, got {len(ENTRY)}"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert ENTRY == ENTRY.strip(), "entry must have no leading/trailing whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
