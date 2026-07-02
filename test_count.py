import noted


def test_count_empty_storage(tmp_path, capsys, monkeypatch):
    monkeypatch.setenv("NOTED_DB", str(tmp_path / "notes.json"))
    noted.main(["count"])
    out = capsys.readouterr().out
    assert "notes: 0" in out


def test_count_populated_storage(tmp_path, capsys, monkeypatch):
    monkeypatch.setenv("NOTED_DB", str(tmp_path / "notes.json"))
    noted.main(["add", "buy milk"])
    noted.main(["add", "walk dog"])
    capsys.readouterr()

    noted.main(["count"])
    out = capsys.readouterr().out
    assert "notes: 2" in out
