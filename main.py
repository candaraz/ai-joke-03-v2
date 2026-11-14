"""ai-joke-03 entry: write one joke about AI coding agents to entry.txt.

The joke is a single line plus one trailing newline. The gate counts
Unicode code points including the line end, so the program asserts the
1-280 code-point rule itself instead of ever writing an invalid file.
"""

import os

JOKE = "Our PR template has one checkbox: 'I tested this.' My agent checked it. It never tested anything. The template now ships pre-checked."

assert 1 <= len(JOKE) + 1 <= 280, "joke must be 1-280 code points including the line end"

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8", newline="\n") as f:
    f.write(JOKE + "\n")
