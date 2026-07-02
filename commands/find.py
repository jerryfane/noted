"""find: print notes containing a search term."""
from storage import load


def cmd_find(args):
    term = args.term.lower()
    matches = [n for n in load() if term in n["text"].lower()]
    if not matches:
        print("no matches")
        return
    for n in matches:
        print(f"#{n['id']}\t{n['text']}")


def register(subparsers):
    p = subparsers.add_parser("find", help="find notes")
    p.add_argument("term", help="search term")
    p.set_defaults(func=cmd_find)
