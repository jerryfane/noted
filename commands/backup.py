"""backup: write notes to a JSON file."""
import json
from pathlib import Path

from storage import load


def cmd_backup(args):
    notes = load()
    output_path = Path(args.file)
    output_path.write_text(json.dumps(notes, indent=2))
    print(f"backed up {len(notes)} notes to {output_path}")


def register(subparsers):
    p = subparsers.add_parser("backup", help="back up notes to a JSON file")
    p.add_argument("file", help="backup output file")
    p.set_defaults(func=cmd_backup)
