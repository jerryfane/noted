import json
from datetime import date, datetime, timedelta, timezone

import noted


def write_notes(path, notes):
    path.write_text(json.dumps(notes))


def test_recent_lists_notes_within_default_window(tmp_path, capsys, monkeypatch):
    db = tmp_path / "notes.json"
    monkeypatch.setenv("NOTED_DB", str(db))
    write_notes(
        db,
        [
            {
                "id": 1,
                "text": "fresh",
                "created_at": (datetime.now() - timedelta(days=2)).isoformat(),
            },
            {
                "id": 2,
                "text": "old",
                "created_at": (datetime.now() - timedelta(days=9)).isoformat(),
            },
            {"id": 3, "text": "missing timestamp"},
        ],
    )

    noted.main(["recent"])

    out = capsys.readouterr().out
    assert "#1\tfresh" in out
    assert "old" not in out
    assert "missing timestamp" not in out


def test_recent_accepts_days_argument_and_date_strings(tmp_path, capsys, monkeypatch):
    db = tmp_path / "notes.json"
    monkeypatch.setenv("NOTED_DB", str(db))
    write_notes(
        db,
        [
            {
                "id": 1,
                "text": "inside",
                "created_at": (date.today() - timedelta(days=2)).isoformat(),
            },
            {
                "id": 2,
                "text": "outside",
                "created_at": (date.today() - timedelta(days=4)).isoformat(),
            },
        ],
    )

    noted.main(["recent", "--days", "3"])

    out = capsys.readouterr().out
    assert out == "#1\tinside\n"


def test_recent_accepts_timezone_datetime_strings(tmp_path, capsys, monkeypatch):
    db = tmp_path / "notes.json"
    monkeypatch.setenv("NOTED_DB", str(db))
    write_notes(
        db,
        [
            {
                "id": 1,
                "text": "aware",
                "created_at": (
                    datetime.now(timezone.utc) - timedelta(days=1)
                ).isoformat(),
            }
        ],
    )

    noted.main(["recent", "--days", "2"])

    out = capsys.readouterr().out
    assert out == "#1\taware\n"


def test_recent_prints_message_when_none_match(tmp_path, capsys, monkeypatch):
    db = tmp_path / "notes.json"
    monkeypatch.setenv("NOTED_DB", str(db))
    write_notes(
        db,
        [
            {
                "id": 1,
                "text": "old",
                "created_at": (datetime.now() - timedelta(days=10)).isoformat(),
            },
            {"id": 2, "text": "missing timestamp"},
        ],
    )

    noted.main(["recent", "--days", "1"])

    out = capsys.readouterr().out
    assert out == "no recent notes\n"
