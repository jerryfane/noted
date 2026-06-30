"""list: print all notes."""
from storage import load


def cmd_list(args):
    notes = load()
    if not notes:
        print("no notes yet")
        return
    for n in notes:
        print(f"#{n['id']}\t{n['text']}")


def register(subparsers):
    p = subparsers.add_parser("list", help="list all notes")
    p.set_defaults(func=cmd_list)
