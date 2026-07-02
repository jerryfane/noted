import json

import noted


def test_pin_sets_pinned_and_persists(tmp_path, capsys, monkeypatch):
    db = tmp_path / "notes.json"
    db.write_text(json.dumps([
        {"id": 2, "text": "keep sorted"},
        {"id": 3, "text": "ship pin command"},
    ]))
    monkeypatch.setenv("NOTED_DB", str(db))

    noted.main(["pin", "3"])

    out = capsys.readouterr().out
    assert out == "pinned #3\n"
    notes = json.loads(db.read_text())
    assert notes == [
        {"id": 2, "text": "keep sorted"},
        {"id": 3, "text": "ship pin command", "pinned": True},
    ]


def test_pin_missing_id_prints_message_without_raising(tmp_path, capsys, monkeypatch):
    db = tmp_path / "notes.json"
    original_notes = [{"id": 1, "text": "existing"}]
    db.write_text(json.dumps(original_notes))
    monkeypatch.setenv("NOTED_DB", str(db))

    noted.main(["pin", "3"])

    out = capsys.readouterr().out
    assert out == "no note #3\n"
    assert json.loads(db.read_text()) == original_notes
