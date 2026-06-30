import noted


def test_search_prints_matching_notes(tmp_path, capsys, monkeypatch):
    monkeypatch.setenv("NOTED_DB", str(tmp_path / "notes.json"))
    noted.main(["add", "buy milk"])
    noted.main(["add", "walk dog"])
    capsys.readouterr()

    noted.main(["search", "milk"])
    out = capsys.readouterr().out

    assert "#1\tbuy milk" in out
    assert "walk dog" not in out


def test_search_is_case_insensitive(tmp_path, capsys, monkeypatch):
    monkeypatch.setenv("NOTED_DB", str(tmp_path / "notes.json"))
    noted.main(["add", "Buy Milk"])
    capsys.readouterr()

    noted.main(["search", "milk"])
    out = capsys.readouterr().out

    assert "#1\tBuy Milk" in out


def test_search_prints_no_matching_notes(tmp_path, capsys, monkeypatch):
    monkeypatch.setenv("NOTED_DB", str(tmp_path / "notes.json"))
    noted.main(["add", "buy milk"])
    capsys.readouterr()

    noted.main(["search", "coffee"])
    out = capsys.readouterr().out

    assert "no matching notes" in out
