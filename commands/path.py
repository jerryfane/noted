"""path: print the notes database path."""
from storage import db_path


def cmd_path(_args):
    print(db_path().resolve())


def register(subparsers):
    p = subparsers.add_parser("path", help="print the notes database path")
    p.set_defaults(func=cmd_path)
