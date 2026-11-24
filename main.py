"""Write the roast-the-gadget entry to /output/entry.txt.

One line, 109 characters (limit 200) -- no trailing newline."""

from pathlib import Path

ENTRY = "My phone dies at 4pm every day, like clockwork, as if it has union-mandated rest hours and I am the overtime."

def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")

if __name__ == "__main__":
    main()
