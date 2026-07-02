import noted


def test_path_prints_database_path(tmp_path, capsys, monkeypatch):
    db_file = tmp_path / "notes.json"
    monkeypatch.setenv("NOTED_DB", str(db_file))
    noted.main(["path"])
    out = capsys.readouterr().out
    assert out == f"{db_file.resolve()}\n"
