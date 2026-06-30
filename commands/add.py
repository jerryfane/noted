"""add: append a new note."""
from storage import load, save


def cmd_add(args):
    notes = load()
    next_id = max((n["id"] for n in notes), default=0) + 1
    notes.append({"id": next_id, "text": args.text})
    save(notes)
    print(f"added #{next_id}")


def register(subparsers):
    p = subparsers.add_parser("add", help="add a note")
    p.add_argument("text", help="note text")
    p.set_defaults(func=cmd_add)
