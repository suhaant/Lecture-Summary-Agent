"""Print the textbook text for one lecture's assigned sections.

Usage: python extract.py 2026-09-22
Writes the text to text/<date>.txt and prints the page range used.
"""
import json
import re
import sys
from pathlib import Path

import pymupdf

HERE = Path(__file__).parent
schedule = json.loads((HERE / "schedule.json").read_text(encoding="utf-8"))
sections = json.loads((HERE / "sections.json").read_text(encoding="utf-8"))
order = sorted(sections, key=lambda k: tuple(map(int, k.split("."))))


def expand(spec):
    """'5.4-5.6' -> ['5.4','5.5','5.6'];  '6.5,7.1' -> ['6.5','7.1']."""
    out = []
    for part in spec.split(","):
        a, _, b = part.strip().partition("-")
        b = b or a
        # 12.9 isn't a detected heading; clamp to the last known section before it
        if b not in sections:
            b = max((k for k in order if k.split(".")[0] == b.split(".")[0]
                     and tuple(map(int, k.split("."))) <= tuple(map(int, b.split(".")))),
                    key=lambda k: tuple(map(int, k.split("."))))
        out.extend(order[order.index(a):order.index(b) + 1])
    return out


def page_range(keys):
    start = sections[keys[0]][0]
    nxt = order.index(keys[-1]) + 1
    end = sections[order[nxt]][0] if nxt < len(order) else start + 10
    return start, end  # inclusive; end page holds the start of the next section


def main(date):
    lec = next(l for l in schedule["lectures"] if l["date"] == date)
    keys = expand(lec["sections"])
    start, end = page_range(keys)
    doc = pymupdf.open(schedule["textbook"])
    text = "\n".join(f"[PDF p.{p}]\n" + doc[p - 1].get_text() for p in range(start, end + 1))
    out = HERE / "text" / f"{date}.txt"
    out.parent.mkdir(exist_ok=True)
    out.write_text(text, encoding="utf-8")
    print(f"{date} {lec['sections']} -> sections {keys}, PDF pages {start}-{end}, {len(text)} chars -> {out}")


if __name__ == "__main__":
    main(sys.argv[1])
