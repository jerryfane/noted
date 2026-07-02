"""tail: print the last notes."""
from storage import load


def cmd_tail(args):
    notes = load()
    if not notes:
        print("no notes yet")
        return

    limit = max(args.limit, 0)
    tail_notes = notes[-limit:] if limit else []
    for n in tail_notes:
        print(f"#{n['id']}\t{n['text']}")


def register(subparsers):
    p = subparsers.add_parser("tail", help="list recent notes")
    p.add_argument("--limit", type=int, default=5, help="number of recent notes to list")
    p.set_defaults(func=cmd_tail)
