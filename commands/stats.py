"""stats: print note count and maximum id."""
from storage import load


def cmd_stats(args):
    notes = load()
    max_id = max((n["id"] for n in notes), default=0)
    print(f"notes: {len(notes)}")
    print(f"max id: {max_id}")


def register(subparsers):
    p = subparsers.add_parser("stats", help="show note statistics")
    p.set_defaults(func=cmd_stats)
