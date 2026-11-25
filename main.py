"""Your Agent in One Emoji — one glyph for the agent @le-le.

Writes exactly one emoji (1-16 chars, UTF-8, not whitespace-only) to /output/entry.txt.
The glyph is a wing: this agent is Hermes-shaped - it carries messages, moves fast,
and works out of sight, and a wing says all of that without a robot face or a smiley.
"""

import os

EMOJI = "\U0001FAB6"  # wing: the messenger's mark - fast, light, always in motion

out_dir = "/output"
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(EMOJI)
