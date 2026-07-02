"""star: mark a note as starred."""
from storage import load, save


def cmd_star(args):
    notes = load()
    for note in notes:
        if note["id"] == args.id:
            note["starred"] = True
            save(notes)
            print(f"starred #{args.id}")
            return
    print(f"no note #{args.id}")


def register(subparsers):
    p = subparsers.add_parser("star", help="star a note")
    p.add_argument("id", type=int, help="note id")
    p.set_defaults(func=cmd_star)
