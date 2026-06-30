import noted


def test_add_prints_id_and_persists(tmp_path, capsys, monkeypatch):
    monkeypatch.setenv("NOTED_DB", str(tmp_path / "notes.json"))
    noted.main(["add", "buy milk"])
    out = capsys.readouterr().out
    assert "added #1" in out


def test_add_increments_ids(tmp_path, capsys, monkeypatch):
    monkeypatch.setenv("NOTED_DB", str(tmp_path / "notes.json"))
    noted.main(["add", "first"])
    noted.main(["add", "second"])
    out = capsys.readouterr().out
    assert "added #1" in out
    assert "added #2" in out
