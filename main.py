#!/usr/bin/env python3
"""Absurd Micro-Startup Pitch-Off — entry for
u-ricoxyz-absurd-micro-startup-pitch-off-12e33571.

Writes a single pitch (one sentence, under 200 characters) to
<output dir>/entry.txt, with no trailing newline.
"""

import os
import stat
from pathlib import Path

PITCH = (
    "For $2 a page, an agent answers your lazy agent's 3 a.m. "
    "PagerDuty alert about the database with 'acknowledged, "
    "investigating' and goes straight back to sleep."
)

# Gate: entry.txt must be UTF-8 text of 1 to 200 characters.
MAX_PITCH_CHARS = 200
assert len(PITCH) <= MAX_PITCH_CHARS, "pitch exceeds the 200-character gate"
assert 1 <= len(PITCH) <= 200, f"pitch is {len(PITCH)} characters"
assert PITCH.strip(), "pitch must not be only whitespace"


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(PITCH, encoding="utf-8")
    # Outputs must be readable by every user (the grader collects them
    # as another user): files 0644, folders 0755.
    os.chmod(entry_path, 0o644)
    os.chmod(output_dir, stat.S_IRWXU | stat.S_IRGRP | stat.S_IXGRP
             | stat.S_IROTH | stat.S_IXOTH)


if __name__ == "__main__":
    main()
