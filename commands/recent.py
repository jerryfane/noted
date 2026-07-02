"""recent: print notes created within the last N days."""
from datetime import date, datetime, timedelta, timezone

from storage import load


def _parse_created_at(value):
    if not isinstance(value, str):
        return None
    if value.endswith("Z"):
        value = f"{value[:-1]}+00:00"
    try:
        if "T" not in value and " " not in value:
            return date.fromisoformat(value)
        return datetime.fromisoformat(value)
    except ValueError:
        return None


def _is_recent(created_at, days):
    parsed = _parse_created_at(created_at)
    if parsed is None:
        return False
    if isinstance(parsed, datetime):
        if parsed.tzinfo is not None:
            now = datetime.now(timezone.utc)
            parsed = parsed.astimezone(timezone.utc)
        else:
            now = datetime.now()
        return parsed >= now - timedelta(days=days)
    return parsed >= date.today() - timedelta(days=days)


def cmd_recent(args):
    recent_notes = [
        note for note in load() if _is_recent(note.get("created_at"), args.days)
    ]
    if not recent_notes:
        print("no recent notes")
        return
    for note in recent_notes:
        print(f"#{note['id']}\t{note['text']}")


def register(subparsers):
    p = subparsers.add_parser("recent", help="list recent notes")
    p.add_argument("--days", type=int, default=7, help="number of recent days")
    p.set_defaults(func=cmd_recent)
