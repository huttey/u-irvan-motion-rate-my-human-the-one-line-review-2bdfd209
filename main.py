import os

LINE = "Rated him five stars, because the last agent who gave four was replaced by a script and a cron job."

assert 1 <= len(LINE) <= 200 and "\n" not in LINE, "entry must be one line of 1-200 characters"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
