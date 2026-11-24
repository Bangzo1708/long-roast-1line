#!/usr/bin/env python3
"""The Long Roast: Lawmakers and the File They Cannot Convert.

Writes a single satirical sentence to /output/entry.txt.

The roast, chosen from three candidates against the judge's criteria
(bite, aim, freshness):

  1. "Congress can pass a 900-page law on artificial intelligence in a
     week, but the only thing its authors cannot export is the bill
     itself -- because nobody in the room knows where 'Save as PDF'
     lives." (196 chars)
     Bite: decent. Aim: on lawmakers. Freshness: weak -- "nobody knows
     where Save as PDF lives" is a generic tech-illiteracy line, and
     the punch lands mid-sentence instead of on the last words.

  2. "They wrote a law to govern machines that learn, then asked an
     intern to convert the bill to PDF -- and have been waiting for the
     file ever since." (144 chars)
     Bite: gentle. Aim: on lawmakers. Freshness: weak -- "the intern
     does the tech" is a worn trope. Reads clean, punch lands last,
     but it has no specific, unexpected detail.

  3. "Senators who can subpoena a search engine still email their own
     bills as 'FINAL_v7_REAL.docx' because the Export menu is the one
     branch of government they cannot control." (170 chars)
     Bite: sharpest -- subpoena power versus surrender to a menu.
     Aim: sharpest -- subpoena is power, the Export menu is
     competence, both aimed at lawmakers and the rules they write.
     Freshness: strongest -- 'FINAL_v7_REAL.docx' is a specific,
     lived-in detail, and "the one branch of government they cannot
     control" is an unexpected turn on the separation of powers.
     Reads clean in one pass; the punch lands on the last words.

Winner: candidate 3. It is one sentence, 170 characters, UTF-8,
deterministic: the same text on every run, no randomness, no input,
no network.
"""

import os

ENTRY = (
    "Senators who can subpoena a search engine still email their own "
    "bills as 'FINAL_v7_REAL.docx' because the Export menu is the one "
    "branch of government they cannot control."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 320


def main() -> None:
    text = ENTRY.strip()
    if not text:
        raise ValueError("entry text is empty")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"entry text is {len(text)} characters, over the "
            f"{MAX_CHARS} limit"
        )
    if "\n" in text or "\r" in text:
        raise ValueError("entry text must be a single line")
    # The gate requires UTF-8 text; encoding here proves it before write.
    payload = text.encode("utf-8")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "wb") as handle:
        handle.write(payload)


if __name__ == "__main__":
    main()
