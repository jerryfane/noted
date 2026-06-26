#!/usr/bin/env python3
"""noted: a tiny notes CLI."""
import argparse
import json
import os
from pathlib import Path


def db_path():
    return Path(os.environ.get("NOTED_DB", str(Path.home() / ".noted.json")))


def load():
    p = db_path()
    if p.exists():
        return json.loads(p.read_text() or "[]")
    return []


def save(notes):
    db_path().write_text(json.dumps(notes, indent=2))


def cmd_add(args):
    notes = load()
    next_id = max((n["id"] for n in notes), default=0) + 1
    notes.append({"id": next_id, "text": args.text})
    save(notes)
    print(f"added #{next_id}")


def cmd_list(args):
    notes = load()
    if not notes:
        print("no notes yet")
        return
    for n in notes:
        print(f"#{n['id']}\t{n['text']}")


def build_parser():
    parser = argparse.ArgumentParser(prog="noted", description="A tiny notes CLI.")
    sub = parser.add_subparsers(dest="command", required=True)

    p_add = sub.add_parser("add", help="add a note")
    p_add.add_argument("text", help="note text")
    p_add.set_defaults(func=cmd_add)

    p_list = sub.add_parser("list", help="list all notes")
    p_list.set_defaults(func=cmd_list)

    return parser


def main(argv=None):
    args = build_parser().parse_args(argv)
    args.func(args)


if __name__ == "__main__":
    main()
