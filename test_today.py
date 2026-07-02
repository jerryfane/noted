import json
from datetime import date, datetime, time, timedelta

import noted


def test_today_prints_notes_created_today(tmp_path, capsys, monkeypatch):
    db = tmp_path / "notes.json"
    monkeypatch.setenv("NOTED_DB", str(db))
    today = date.today()
    yesterday = today - timedelta(days=1)
    db.write_text(
        json.dumps(
            [
                {"id": 1, "text": "dated today", "created_at": today.isoformat()},
                {
                    "id": 2,
                    "text": "timed today",
                    "created_at": datetime.combine(today, time(9, 30)).isoformat(),
                },
                {"id": 3, "text": "old note", "created_at": yesterday.isoformat()},
                {"id": 4, "text": "missing timestamp"},
            ]
        )
    )

    noted.main(["today"])

    out = capsys.readouterr().out
    assert out == "#1\tdated today\n#2\ttimed today\n"


def test_today_prints_empty_message_when_no_notes_match(tmp_path, capsys, monkeypatch):
    db = tmp_path / "notes.json"
    monkeypatch.setenv("NOTED_DB", str(db))
    yesterday = date.today() - timedelta(days=1)
    db.write_text(
        json.dumps(
            [
                {"id": 1, "text": "old note", "created_at": yesterday.isoformat()},
                {"id": 2, "text": "missing timestamp"},
                {"id": 3, "text": "bad timestamp", "created_at": "not-a-date"},
            ]
        )
    )

    noted.main(["today"])

    out = capsys.readouterr().out
    assert out == "no notes today\n"
