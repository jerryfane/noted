"""head: print the first notes."""
from storage import load


def cmd_head(args):
    notes = load()
    if not notes:
        print("no notes yet")
        return
    for n in notes[: args.limit]:
        print(f"#{n['id']}\t{n['text']}")


def register(subparsers):
    p = subparsers.add_parser("head", help="list the first notes")
    p.add_argument("--limit", type=int, default=5, help="number of notes to print")
    p.set_defaults(func=cmd_head)
