import json

import noted


def test_export_json_empty(tmp_path, capsys, monkeypatch):
    monkeypatch.setenv("NOTED_DB", str(tmp_path / "notes.json"))
    noted.main(["export", "--json"])
    out = capsys.readouterr().out
    assert json.loads(out) == []


def test_export_json_includes_all_notes(tmp_path, capsys, monkeypatch):
    monkeypatch.setenv("NOTED_DB", str(tmp_path / "notes.json"))
    noted.main(["add", "first"])
    noted.main(["add", "second"])
    capsys.readouterr()

    noted.main(["export", "--json"])
    out = capsys.readouterr().out

    assert json.loads(out) == [
        {"id": 1, "text": "first"},
        {"id": 2, "text": "second"},
    ]
