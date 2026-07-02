import json

import noted


def test_star_marks_note_and_persists(tmp_path, capsys, monkeypatch):
    db = tmp_path / "notes.json"
    db.write_text(json.dumps([{"id": 3, "text": "buy milk"}]))
    monkeypatch.setenv("NOTED_DB", str(db))

    noted.main(["star", "3"])

    out = capsys.readouterr().out
    assert "starred #3" in out
    assert json.loads(db.read_text()) == [
        {"id": 3, "text": "buy milk", "starred": True}
    ]


def test_star_missing_note_prints_message(tmp_path, capsys, monkeypatch):
    db = tmp_path / "notes.json"
    db.write_text(json.dumps([{"id": 1, "text": "buy milk"}]))
    monkeypatch.setenv("NOTED_DB", str(db))

    noted.main(["star", "3"])

    out = capsys.readouterr().out
    assert "no note #3" in out
    assert json.loads(db.read_text()) == [{"id": 1, "text": "buy milk"}]
