"""search: print notes containing a term."""
from storage import load


def cmd_search(args):
    term = args.term.lower()
    matches = [n for n in load() if term in n["text"].lower()]
    if not matches:
        print("no matching notes")
        return
    for n in matches:
        print(f"#{n['id']}\t{n['text']}")


def register(subparsers):
    p = subparsers.add_parser("search", help="search notes")
    p.add_argument("term", help="term to search for")
    p.set_defaults(func=cmd_search)
