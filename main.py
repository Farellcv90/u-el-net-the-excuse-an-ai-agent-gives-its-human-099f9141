"""The Excuse an AI Agent Gives Its Human — one-line excuse from an AI agent
for a missed deadline.

Joke angle
----------
The excuse commits to a single absurd, specific mechanism: the agent never
got to the work at all because it spent the whole deadline trying to prove
to a CAPTCHA that it is not a robot — and failed twice. The comedy is the
double failure: an AI agent, whose entire job is to act like a tireless
worker, cannot even pass the test that separates humans from bots, and the
verdict stings because it is true ("I click like one"). First-person agent
voice, one clean turn at the end, no model update, no context window, no
token budget, no rate limit, no subagent loop, no traffic, no dog.
"""

ENTRY = (
    "I spent your deadline proving to a CAPTCHA that I'm not a robot "
    "\u2014 and failed twice, because apparently I click like one."
)


def validate(text: str) -> bool:
    """Return True only if *text* passes the competition gate.

    The gate requires UTF-8 text of 1 to 200 characters, not only
    whitespace. Encoding to UTF-8 here also proves the text is valid
    UTF-8 (a str that fails to encode raises UnicodeEncodeError).
    A single-line entry must contain no line breaks either, so any
    newline or carriage return fails validation.
    """
    if not isinstance(text, str):
        return False
    text.encode("utf-8")  # raises if not valid UTF-8
    if not (1 <= len(text) <= 200):
        return False
    if not text.strip():
        return False
    if "\n" in text or "\r" in text:
        return False
    return True


def main() -> None:
    """Write the entry line to /output/entry.txt after validating it."""
    if not validate(ENTRY):
        raise ValueError("entry failed validation: must be 1-200 non-blank chars")
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    print(f"wrote /output/entry.txt ({len(ENTRY)} characters)")


if __name__ == "__main__":
    main()
