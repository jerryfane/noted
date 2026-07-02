"""today: print notes created today."""
from datetime import date, datetime

from storage import load


def _created_date(value):
    if not isinstance(value, str):
        return None

    normalized = value.replace("Z", "+00:00")
    try:
        dt = datetime.fromisoformat(normalized)
    except ValueError:
        try:
            return date.fromisoformat(value)
        except ValueError:
            return None

    if dt.tzinfo is not None:
        return dt.astimezone().date()
    return dt.date()


def cmd_today(args):
    today = date.today()
    matches = [
        note
        for note in load()
        if _created_date(note.get("created_at")) == today
    ]

    if not matches:
        print("no notes today")
        return

    for note in matches:
        print(f"#{note['id']}\t{note['text']}")


def register(subparsers):
    p = subparsers.add_parser("today", help="list notes created today")
    p.set_defaults(func=cmd_today)
