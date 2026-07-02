import noted


def test_longest_empty(tmp_path, capsys, monkeypatch):
    monkeypatch.setenv("NOTED_DB", str(tmp_path / "notes.json"))
    noted.main(["longest"])
    out = capsys.readouterr().out
    assert out == "no notes yet\n"


def test_longest_selects_longest_note(tmp_path, capsys, monkeypatch):
    monkeypatch.setenv("NOTED_DB", str(tmp_path / "notes.json"))
    noted.main(["add", "short"])
    noted.main(["add", "much longer note"])
    noted.main(["add", "mid"])
    capsys.readouterr()

    noted.main(["longest"])
    out = capsys.readouterr().out
    assert out == "#2\tmuch longer note\n"


def test_longest_keeps_first_note_when_tied(tmp_path, capsys, monkeypatch):
    monkeypatch.setenv("NOTED_DB", str(tmp_path / "notes.json"))
    noted.main(["add", "first tie"])
    noted.main(["add", "later tie"])
    capsys.readouterr()

    noted.main(["longest"])
    out = capsys.readouterr().out
    assert out == "#1\tfirst tie\n"
