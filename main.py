"""Real-Life Patch Notes entry: writes one patch-note line to entry.txt.

Stdlib only. No network, no secrets.
"""

import os

ENTRY = (
    "v2.4.1: fixed a bug where knees made a loud cracking sound on "
    "standing up, alerting everyone in the room that you are now old."
)


def write_entry(out_dir, text):
    """Write the patch note with no trailing newline.

    The sealed gate requires 1-160 characters of UTF-8 text, not only
    whitespace, so fail loudly here instead of shipping a bad entry.
    """
    if not 1 <= len(text) <= 160 or not text.strip():
        raise SystemExit(
            "entry must be 1-160 non-blank characters, got %d" % len(text)
        )
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


def main():
    write_entry(os.environ["MAKEFUN_OUTPUT_DIR"], ENTRY)


if __name__ == "__main__":
    main()
