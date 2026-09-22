# CH 101 Pre-Reader — generation instructions

Folder: `C:\Users\suhaa\Downloads\PreReads\`
- `schedule.json` — lecture dates → textbook sections (edit this if the schedule changes)
- `sections.json` — section → [starting PDF page, title]
- `extract.py` — `python -X utf8 extract.py YYYY-MM-DD` writes `text/YYYY-MM-DD.txt`
- `briefs/` — local copy of each brief
- `state.json` — Drive folder id, calendar id, and briefs already delivered (`done`)
- `briefs/2026-09-22.txt` — the reference brief; match its format, tone and depth

## Procedure (run for each lecture that needs a brief)

A lecture needs a brief if its date is within the next 4 days (today included, but only if it is before 07:00 local
time) and it is not in `state.json` → `done`.

1. `python -X utf8 extract.py <date>` and read `text/<date>.txt` in full.
2. Write the brief to `briefs/<date>.txt`, 500–800 words of prose (go to ~900 only for dense multi-section days),
   under 7,500 characters total. Sections, in order:
   - Header: `CH 101 · Sections X–Y · <topic>`, `Class: <Day Mon D>, 3:00 PM · 222 Dabney Hall`,
     `Reading: textbook pages A–B (PDF pages C–D) · ~N min read`. Printed page = PDF page − 6.
   - THE BIG IDEA (2–3 sentences)
   - KEY CONCEPTS (3–5, numbered, each tagged with its section, explained for a first-time reader)
   - KEY TERMS (term: one-line definition)
   - WORKED EXAMPLE 1 and 2 — use exercises or examples from the reading and solve them step by step,
     with a check line. Verify every number twice; wrong chemistry is worse than no brief.
   - QUICK SELF-CHECK (one short problem with answer, plus which book exercises to try)
   - If the lecture topic covers material outside the assigned sections, add a short clearly-labelled note.
   - WHAT TO WATCH FOR IN LECTURE (2–3 likely confusion points; link to the next lecture if relevant)
   Plain text only: no markdown, no LaTeX. Use Unicode for subscripts/superscripts/arrows where helpful (CO₃²⁻, ⇌, Δ).
3. Create a Google Doc in the Drive folder (`state.json` → `drive_folder_id`), title
   `<date> · CH 101 · <sections> <short topic>`, textContent = the brief, contentMimeType `text/plain`.
4. Create a Google Calendar event on `calendar_id`:
   - summary `📘 CH 101 Pre-Read: <sections> <short topic>`
   - start `<date>T07:00:00`, end `<date>T07:15:00`, timeZone `America/New_York`
   - availability FREE
   - overrideReminders: `[{"method":"email","minutes":0},{"method":"popup","minutes":0}]`
   - description: `Full brief (Drive): <doc url>` + blank line + the full brief
5. Add `{ "<date>": {"doc_id": ..., "event_id": ...} }` to `state.json` → `done`.

## Rules
- Dates in `schedule.json` → `skipped` never get a brief.
- Never create a second event/doc for a date already in `done`. To regenerate (schedule change), the user will ask:
  update the existing doc and event instead of creating new ones.
- If the textbook PDF or extraction fails, stop and report — do not write a brief from memory.
- Do not send email any other way; the calendar email reminder is the delivery.
