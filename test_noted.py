import noted


def test_add_then_list(tmp_path, capsys, monkeypatch):
    monkeypatch.setenv("NOTED_DB", str(tmp_path / "notes.json"))
    noted.main(["add", "buy milk"])
    noted.main(["list"])
    out = capsys.readouterr().out
    assert "added #1" in out
    assert "buy milk" in out
