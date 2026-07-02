"""rename: change a note's text."""
from storage import load, save


def cmd_rename(args):
    notes = load()
    for note in notes:
        if note["id"] == args.id:
            note["text"] = args.text
            save(notes)
            print(f"renamed #{args.id}")
            return

    print(f"no note #{args.id}")


def register(subparsers):
    p = subparsers.add_parser("rename", help="rename a note")
    p.add_argument("id", type=int, help="note id")
    p.add_argument("text", help="new note text")
    p.set_defaults(func=cmd_rename)
