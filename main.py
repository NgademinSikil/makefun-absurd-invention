"""The ShowerTax absurd-invention pitch.

Writes the single-sentence pitch to /output/entry.txt, exactly as
specified, using only the Python standard library.
"""

from pathlib import Path

ENTRY = (
    "The ShowerTax: a showerhead that fines you 10 cents for every "
    "off-key note, then spends the takings hiring a professional "
    "singer to sing your morning shower for you."
)


def main() -> None:
    # The gate requires 1-220 characters of non-blank UTF-8 text,
    # so fail loudly here instead of writing an invalid entry.
    if not 1 <= len(ENTRY) <= 220 or not ENTRY.strip():
        raise ValueError(f"entry is {len(ENTRY)} characters, outside 1-220")
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(ENTRY, encoding="utf-8")
    print(ENTRY)


if __name__ == "__main__":
    main()
