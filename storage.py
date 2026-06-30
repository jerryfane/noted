"""noted storage helpers: shared note persistence used by all commands."""
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
