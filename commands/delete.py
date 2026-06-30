"""delete: remove a note by id."""
from storage import load, save


def cmd_delete(args):
    notes = load()
    remaining = [n for n in notes if n["id"] != args.id]
    if len(remaining) == len(notes):
        print(f"note #{args.id} not found")
        return
    save(remaining)
    print(f"deleted #{args.id}")


def register(subparsers):
    p = subparsers.add_parser("delete", help="delete a note")
    p.add_argument("id", type=int, help="note id")
    p.set_defaults(func=cmd_delete)
