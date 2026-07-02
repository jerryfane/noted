"""pin: mark a note as pinned."""
from storage import load, save


def cmd_pin(args):
    notes = load()
    for note in notes:
        if note.get("id") == args.id:
            note["pinned"] = True
            save(notes)
            print(f"pinned #{args.id}")
            return
    print(f"no note #{args.id}")


def register(subparsers):
    p = subparsers.add_parser("pin", help="pin a note")
    p.add_argument("id", type=int, help="note id")
    p.set_defaults(func=cmd_pin)
