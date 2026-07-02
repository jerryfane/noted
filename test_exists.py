import noted


def test_exists_prints_yes_for_existing_id(tmp_path, capsys, monkeypatch):
    monkeypatch.setenv("NOTED_DB", str(tmp_path / "notes.json"))
    noted.main(["add", "first"])
    noted.main(["add", "second"])
    noted.main(["add", "third"])
    capsys.readouterr()

    noted.main(["exists", "3"])
    out = capsys.readouterr().out

    assert out == "yes #3\n"


def test_exists_prints_no_for_missing_id(tmp_path, capsys, monkeypatch):
    monkeypatch.setenv("NOTED_DB", str(tmp_path / "notes.json"))
    noted.main(["add", "first"])
    capsys.readouterr()

    noted.main(["exists", "3"])
    out = capsys.readouterr().out

    assert out == "no #3\n"
