import json

import noted


def test_rename_updates_note_text_and_persists(tmp_path, capsys, monkeypatch):
    db = tmp_path / "notes.json"
    monkeypatch.setenv("NOTED_DB", str(db))

    noted.main(["add", "first"])
    noted.main(["add", "second"])
    capsys.readouterr()

    noted.main(["rename", "2", "new text"])
    out = capsys.readouterr().out

    assert "renamed #2" in out
    assert json.loads(db.read_text()) == [
        {"id": 1, "text": "first"},
        {"id": 2, "text": "new text"},
    ]


def test_rename_missing_note_prints_message_without_changing_db(tmp_path, capsys, monkeypatch):
    db = tmp_path / "notes.json"
    monkeypatch.setenv("NOTED_DB", str(db))

    noted.main(["add", "first"])
    capsys.readouterr()

    noted.main(["rename", "2", "new text"])
    out = capsys.readouterr().out

    assert "no note #2" in out
    assert json.loads(db.read_text()) == [{"id": 1, "text": "first"}]
