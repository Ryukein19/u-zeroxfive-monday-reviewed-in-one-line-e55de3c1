import os
# One-liner entry, under 200 chars: the line below is the whole submission.
# Output goes to /output/entry.txt.
LINE = "Monday, reviewed: the coffee machine broke, the printer filed a complaint, and the meeting about the meeting ran long. Two stars, for the biscuits."
os.makedirs("/output", exist_ok=True)
open("/output/entry.txt", "w", encoding="utf-8").write(LINE)
