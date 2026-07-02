import json

import noted


def test_dedupe_removes_duplicates_and_persists(tmp_path, capsys, monkeypatch):
    db = tmp_path / "notes.json"
    monkeypatch.setenv("NOTED_DB", str(db))

    noted.main(["add", "buy milk"])
    noted.main(["add", "call mom"])
    noted.main(["add", "buy milk"])
    noted.main(["dedupe"])

    out = capsys.readouterr().out
    assert "removed 1 duplicates" in out
    assert json.loads(db.read_text()) == [
        {"id": 1, "text": "buy milk"},
        {"id": 2, "text": "call mom"},
    ]


def test_dedupe_keeps_non_duplicates(tmp_path, capsys, monkeypatch):
    db = tmp_path / "notes.json"
    monkeypatch.setenv("NOTED_DB", str(db))

    noted.main(["add", "first"])
    noted.main(["add", "second"])
    noted.main(["dedupe"])

    out = capsys.readouterr().out
    assert "removed 0 duplicates" in out
    assert json.loads(db.read_text()) == [
        {"id": 1, "text": "first"},
        {"id": 2, "text": "second"},
    ]
