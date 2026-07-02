import noted


def test_find_prints_matching_notes(tmp_path, capsys, monkeypatch):
    monkeypatch.setenv("NOTED_DB", str(tmp_path / "notes.json"))
    noted.main(["add", "buy milk"])
    noted.main(["add", "call mom"])
    noted.main(["add", "milk carton"])
    capsys.readouterr()

    noted.main(["find", "milk"])
    out = capsys.readouterr().out

    assert out == "#1\tbuy milk\n#3\tmilk carton\n"


def test_find_is_case_insensitive(tmp_path, capsys, monkeypatch):
    monkeypatch.setenv("NOTED_DB", str(tmp_path / "notes.json"))
    noted.main(["add", "Buy MILK"])
    capsys.readouterr()

    noted.main(["find", "milk"])
    out = capsys.readouterr().out

    assert out == "#1\tBuy MILK\n"


def test_find_no_match(tmp_path, capsys, monkeypatch):
    monkeypatch.setenv("NOTED_DB", str(tmp_path / "notes.json"))
    noted.main(["add", "buy milk"])
    capsys.readouterr()

    noted.main(["find", "eggs"])
    out = capsys.readouterr().out

    assert out == "no matches\n"
