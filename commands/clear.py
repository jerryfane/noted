"""clear: remove all notes after explicit confirmation."""
from storage import load, save


def cmd_clear(args):
    if not args.yes:
        print("pass --yes to clear notes")
        return

    notes = load()
    save([])
    print(f"cleared {len(notes)} notes")


def register(subparsers):
    p = subparsers.add_parser("clear", help="clear all notes")
    p.add_argument("--yes", action="store_true", help="confirm clearing all notes")
    p.set_defaults(func=cmd_clear)
