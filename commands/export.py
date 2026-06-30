"""export: write notes in machine-readable formats."""
import json

from storage import load


def cmd_export(args):
    notes = load()
    print(json.dumps(notes, indent=2))


def register(subparsers):
    p = subparsers.add_parser("export", help="export notes")
    p.add_argument("--json", action="store_true", required=True, help="export notes as JSON")
    p.set_defaults(func=cmd_export)
