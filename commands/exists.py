"""exists: check whether a note id exists."""
from storage import load


def cmd_exists(args):
    notes = load()
    prefix = "yes" if any(n.get("id") == args.id for n in notes) else "no"
    print(f"{prefix} #{args.id}")


def register(subparsers):
    p = subparsers.add_parser("exists", help="check whether a note exists")
    p.add_argument("id", type=int, help="note id")
    p.set_defaults(func=cmd_exists)
