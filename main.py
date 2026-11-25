"""One Line, Big Laugh -- entry writer.

Writes a single original joke line to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). Standard library only.
"""

import os
import sys

LINE = (
    "My therapist asked what my safe word was, so I said 'mortgage' "
    "\u2014 she nodded like she'd heard it before."
)

MAX_CHARS = 200


def main() -> int:
    line = LINE.strip()

    if not line or "\n" in line or "\r" in line:
        print("entry line invalid: empty or not a single line", file=sys.stderr)
        return 1

    if len(line) > MAX_CHARS:
        print(
            f"entry line invalid: {len(line)} characters (need 1-{MAX_CHARS})",
            file=sys.stderr,
        )
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)

    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the gate counts the file's characters, so the
    # file holds exactly the line and nothing else.
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(line)

    print(f"wrote {len(line)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
