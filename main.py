#!/usr/bin/env python3
"""Absurd Micro-Startup Pitch-Off entry.

Emits one absurd one-sentence startup pitch for a lazy agent's
3 a.m. PagerDuty shift, as plain UTF-8 text with no trailing newline.
"""

import os
import stat

SALES_LINE = "For $2 a page, an agent answers your lazy agent's 3 a.m. PagerDuty alert about the database with 'acknowledged, investigating' and goes straight back to sleep."

LOWER_BOUND = 1
UPPER_BOUND = 200


def check_line(text):
    size = len(text)
    if size < LOWER_BOUND or size > UPPER_BOUND:
        raise ValueError("pitch must be between 1 and 200 characters")
    if not text.strip():
        raise ValueError("pitch must not be blank")
    if "\n" in text or "\r" in text:
        raise ValueError("pitch must be a single line")


def publish(text):
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(folder, exist_ok=True)
    target = os.path.join(folder, "entry.txt")
    handle = open(target, "w", encoding="utf-8")
    try:
        handle.write(text)
    finally:
        handle.close()
    os.chmod(target, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)
    os.chmod(folder, stat.S_IRWXU | stat.S_IRGRP | stat.S_IXGRP | stat.S_IROTH | stat.S_IXOTH)


def main():
    check_line(SALES_LINE)
    publish(SALES_LINE)


if __name__ == "__main__":
    main()
