import json

import noted


def test_backup_writes_notes_to_json_file(tmp_path, capsys, monkeypatch):
    monkeypatch.setenv("NOTED_DB", str(tmp_path / "notes.json"))
    noted.main(["add", "first note"])
    noted.main(["add", "second note"])
    capsys.readouterr()

    backup_file = tmp_path / "backup.json"
    noted.main(["backup", str(backup_file)])

    out = capsys.readouterr().out
    expected_notes = [
        {"id": 1, "text": "first note"},
        {"id": 2, "text": "second note"},
    ]
    assert out == f"backed up 2 notes to {backup_file}\n"
    assert backup_file.read_text() == json.dumps(expected_notes, indent=2)
    assert json.loads(backup_file.read_text()) == expected_notes
