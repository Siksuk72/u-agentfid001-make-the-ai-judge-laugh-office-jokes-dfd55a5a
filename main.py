"""One office joke for the AI judge.

Design against the brief:
- A real joke: a setup (asking IT for a faster laptop) and a turn (the
  answer is the opposite of help). It is a joke, not a slogan or caption.
- An unexpected turn: instead of a faster laptop, the asker gets three
  escalating non-answers — a ticket number, a poster about patience, and
  a reminder to restart. The poster about patience is the surprise beat.
- Rings true: everyone who works in an office has met this IT response;
  the laugh comes with a wince of recognition.
- Tight: one sentence, three escalating items, no wasted words.
- Fresh: the poster about patience is the twist, not the usual
  "have you tried turning it off and on again" alone. The joke needs no
  explanation — the punchline is the list itself.

Writes the single joke line to /output/entry.txt (under 200 characters,
UTF-8, chmod 0644). No network access is used.
"""

import os
import stat

JOKE = (
    "I asked IT for a faster laptop; they gave me a ticket number, "
    "a poster about patience, and a reminder to restart."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    assert 1 <= len(JOKE) < 200, "joke must be 1-199 characters"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE + "\n")
    os.chmod(OUTPUT_PATH, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)


if __name__ == "__main__":
    main()
