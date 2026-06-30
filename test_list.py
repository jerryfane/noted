import noted


def test_list_empty(tmp_path, capsys, monkeypatch):
    monkeypatch.setenv("NOTED_DB", str(tmp_path / "notes.json"))
    noted.main(["list"])
    out = capsys.readouterr().out
    assert "no notes yet" in out


def test_add_then_list(tmp_path, capsys, monkeypatch):
    monkeypatch.setenv("NOTED_DB", str(tmp_path / "notes.json"))
    noted.main(["add", "buy milk"])
    noted.main(["list"])
    out = capsys.readouterr().out
    assert "buy milk" in out
