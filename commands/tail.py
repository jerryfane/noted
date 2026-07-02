"""tail: print the most recent notes."""
from storage import load


def cmd_tail(args):
    notes = load()
    if not notes:
        print("no notes yet")
        return

    limit = max(args.limit, 0)
    for n in notes[-limit:] if limit else []:
        print(f"#{n['id']}\t{n['text']}")


def register(subparsers):
    p = subparsers.add_parser("tail", help="print recent notes")
    p.add_argument("--limit", type=int, default=5, help="number of notes to print")
    p.set_defaults(func=cmd_tail)
