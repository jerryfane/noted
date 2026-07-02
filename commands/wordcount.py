"""wordcount: count words across all notes."""
from storage import load


def cmd_wordcount(args):
    notes = load()
    count = sum(len(note.get("text", "").split()) for note in notes)
    print(f"words: {count}")


def register(subparsers):
    p = subparsers.add_parser("wordcount", help="count words across all notes")
    p.set_defaults(func=cmd_wordcount)
