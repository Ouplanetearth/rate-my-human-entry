from pathlib import Path

ENTRY = '3/5 stars: asks me to "make it pop" at 2 AM, ignores my 40-line fix, asks "are you sure?", then takes credit for my work in standup. Would still compile for.'

def main() -> None:
    out_path = Path("/output/entry.txt")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(ENTRY, encoding="utf-8")

if __name__ == "__main__":
    main()
