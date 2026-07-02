"""move: reorder an existing note."""
from storage import load, save


def cmd_move(args):
    notes = load()
    note = next((n for n in notes if n["id"] == args.id), None)
    if note is None:
        print(f"no note #{args.id}")
        return

    position = max(1, min(args.position, len(notes)))
    notes.remove(note)
    notes.insert(position - 1, note)
    save(notes)
    print(f"moved #{args.id} to {position}")


def register(subparsers):
    p = subparsers.add_parser("move", help="move a note")
    p.add_argument("id", type=int, help="note id")
    p.add_argument("position", type=int, help="1-based target position")
    p.set_defaults(func=cmd_move)
