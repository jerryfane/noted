"""longest: print the note with the longest text."""
from storage import load


def cmd_longest(args):
    notes = load()
    if not notes:
        print("no notes yet")
        return

    longest = max(notes, key=lambda n: len(n["text"]))
    print(f"#{longest['id']}\t{longest['text']}")


def register(subparsers):
    p = subparsers.add_parser("longest", help="show the longest note")
    p.set_defaults(func=cmd_longest)
