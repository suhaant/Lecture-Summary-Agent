# Lecture-Summary-Agent

AI agent that reads your textbook and sends you an overview of what will be covered in lecture today.

Currently piloting on NC State **CH 101-010** (Fall 2026). Each lecture day at 7:00 AM a brief lands in your inbox covering the assigned textbook sections: the big idea, key concepts and terms, two worked examples, a self-check, and what to watch for in lecture.

## How it works

1. **Map**: `sections.json` maps every textbook section to its starting PDF page. `schedule.json` maps lecture dates to sections and lists skipped days (exams, holidays).
2. **Extract**: `python -X utf8 extract.py 2026-09-24` pulls the text for that lecture's sections into `text/<date>.txt`.
3. **Generate**: a Claude scheduled task runs daily at 8 PM, following [`INSTRUCTIONS.md`](INSTRUCTIONS.md). For any lecture within 4 days that has no brief yet, it writes one to `briefs/<date>.txt`.
4. **Deliver**: each brief is saved as a Google Doc and placed in a 7:00–7:15 AM Google Calendar event with an email reminder, so Google sends the email even when the laptop is off.

`state.json` (gitignored; see `state.example.json`) records the Drive folder, calendar, and briefs already delivered so nothing is sent twice.

## Setup

- Python 3 with `pymupdf` (`pip install pymupdf`)
- The course textbook PDF; set its path in `schedule.json` → `textbook`
- Claude desktop app with the Google Drive and Google Calendar connectors
- Copy `state.example.json` to `state.json` and fill in your Drive folder and calendar IDs
- Create a daily scheduled task that follows `INSTRUCTIONS.md`

## Adapting to another course

Rebuild `sections.json` for the new textbook, replace the lecture list in `schedule.json`, and update the header line in `INSTRUCTIONS.md` (class time, room).

## Not in this repo

The textbook and raw extracted pages are copyrighted and never committed. `briefs/` contains only original summaries.
