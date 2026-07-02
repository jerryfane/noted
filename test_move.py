import json

import noted


def read_notes(path):
    return json.loads(path.read_text())


def test_move_reorders_persisted_notes(tmp_path, capsys, monkeypatch):
    db = tmp_path / "notes.json"
    monkeypatch.setenv("NOTED_DB", str(db))
    noted.main(["add", "first"])
    noted.main(["add", "second"])
    noted.main(["add", "third"])
    capsys.readouterr()

    noted.main(["move", "3", "1"])

    out = capsys.readouterr().out
    assert "moved #3 to 1" in out
    assert [n["id"] for n in read_notes(db)] == [3, 1, 2]


def test_move_clamps_positions(tmp_path, capsys, monkeypatch):
    db = tmp_path / "notes.json"
    monkeypatch.setenv("NOTED_DB", str(db))
    noted.main(["add", "first"])
    noted.main(["add", "second"])
    noted.main(["add", "third"])
    capsys.readouterr()

    noted.main(["move", "2", "99"])
    noted.main(["move", "3", "0"])

    out = capsys.readouterr().out
    assert "moved #2 to 3" in out
    assert "moved #3 to 1" in out
    assert [n["id"] for n in read_notes(db)] == [3, 1, 2]


def test_move_missing_id_does_not_raise_or_change_order(tmp_path, capsys, monkeypatch):
    db = tmp_path / "notes.json"
    monkeypatch.setenv("NOTED_DB", str(db))
    noted.main(["add", "first"])
    noted.main(["add", "second"])
    capsys.readouterr()

    noted.main(["move", "3", "1"])

    out = capsys.readouterr().out
    assert "no note #3" in out
    assert [n["id"] for n in read_notes(db)] == [1, 2]
