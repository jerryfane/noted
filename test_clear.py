import json

import noted


def read_notes(path):
    return json.loads(path.read_text())


def test_clear_requires_yes_and_preserves_notes(tmp_path, capsys, monkeypatch):
    db = tmp_path / "notes.json"
    monkeypatch.setenv("NOTED_DB", str(db))
    noted.main(["add", "first"])
    noted.main(["add", "second"])
    capsys.readouterr()

    noted.main(["clear"])

    out = capsys.readouterr().out
    assert out == "pass --yes to clear notes\n"
    assert read_notes(db) == [
        {"id": 1, "text": "first"},
        {"id": 2, "text": "second"},
    ]


def test_clear_yes_removes_notes_and_reports_count(tmp_path, capsys, monkeypatch):
    db = tmp_path / "notes.json"
    monkeypatch.setenv("NOTED_DB", str(db))
    noted.main(["add", "first"])
    noted.main(["add", "second"])
    capsys.readouterr()

    noted.main(["clear", "--yes"])

    out = capsys.readouterr().out
    assert out == "cleared 2 notes\n"
    assert read_notes(db) == []
