"""count: print the number of notes."""
from storage import load


def cmd_count(args):
    notes = load()
    print(f"notes: {len(notes)}")


def register(subparsers):
    p = subparsers.add_parser("count", help="count notes")
    p.set_defaults(func=cmd_count)
