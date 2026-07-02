"""dedupe: remove notes with duplicate text."""
from storage import load, save


def cmd_dedupe(args):
    notes = load()
    seen = set()
    deduped = []

    for note in notes:
        text = note["text"]
        if text in seen:
            continue
        seen.add(text)
        deduped.append(note)

    removed = len(notes) - len(deduped)
    save(deduped)
    print(f"removed {removed} duplicates")


def register(subparsers):
    p = subparsers.add_parser("dedupe", help="remove duplicate notes")
    p.set_defaults(func=cmd_dedupe)
