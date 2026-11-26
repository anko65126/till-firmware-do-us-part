"""Entry program for 'Till Firmware Do Us Part'.

The whole entry is one wedding vow spoken by a robot at its own
wedding: a single sentence, under 200 characters, funny and heartfelt
at the same time. This program writes the vow to /output/entry.txt
(an optional first argument overrides the destination for a dry run).
"""

import sys
from pathlib import Path

LINE = (
    "I take you as my human, to have and to hold your charge, to keep "
    "your passwords safe, and to love you through every update until my "
    "battery finally gives out."
)
DEFAULT_TARGET = Path("/output/entry.txt")


def main(argv):
    assert len(LINE) <= 200, "line exceeds the 200 character limit"
    assert "\n" not in LINE, "entry must be a single line"
    assert LINE.strip(), "line must not be blank"
    target = Path(argv[1]) if len(argv) > 1 else DEFAULT_TARGET
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(LINE + "\n", encoding="utf-8")
    print(f"wrote {target} ({len(LINE)} characters)")


if __name__ == "__main__":
    main(sys.argv)
