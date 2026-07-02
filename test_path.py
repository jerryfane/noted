import noted


def test_path_prints_resolved_database_path(tmp_path, capsys, monkeypatch):
    db_file = tmp_path / "notes.json"
    monkeypatch.setenv("NOTED_DB", str(db_file))
    noted.main(["path"])
    out = capsys.readouterr().out
    assert out.strip() == str(db_file.resolve())
