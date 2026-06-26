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


def format_note(note):
    return f"#{note['id']}\t{note['text']}"


def notes_json(notes):
    return json.dumps(notes, indent=2)


def save(notes):
    db_path().write_text(notes_json(notes))


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
        print(format_note(n))


def cmd_search(args):
    term = args.term.lower()
    matches = [n for n in load() if term in n["text"].lower()]
    if not matches:
        print("no matching notes")
        return
    for n in matches:
        print(format_note(n))


def cmd_delete(args):
    notes = load()
    remaining = [n for n in notes if n["id"] != args.id]
    if len(remaining) == len(notes):
        print(f"note #{args.id} not found")
        return
    save(remaining)
    print(f"deleted #{args.id}")


def cmd_export(args):
    print(notes_json(load()))


def build_parser():
    parser = argparse.ArgumentParser(prog="noted", description="A tiny notes CLI.")
    sub = parser.add_subparsers(dest="command", required=True)

    p_add = sub.add_parser("add", help="add a note")
    p_add.add_argument("text", help="note text")
    p_add.set_defaults(func=cmd_add)

    p_list = sub.add_parser("list", help="list all notes")
    p_list.set_defaults(func=cmd_list)

    p_search = sub.add_parser("search", help="search notes")
    p_search.add_argument("term", help="search term")
    p_search.set_defaults(func=cmd_search)

    p_delete = sub.add_parser("delete", help="delete a note")
    p_delete.add_argument("id", type=int, help="note id")
    p_delete.set_defaults(func=cmd_delete)

    p_export = sub.add_parser("export", help="export notes")
    p_export.add_argument("--json", action="store_true", required=True, help="export as JSON")
    p_export.set_defaults(func=cmd_export)

    return parser


def main(argv=None):
    args = build_parser().parse_args(argv)
    args.func(args)


if __name__ == "__main__":
    main()
