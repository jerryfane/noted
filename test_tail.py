import noted


def add_notes(count):
    for i in range(1, count + 1):
        noted.main(["add", f"note {i}"])


def test_tail_defaults_to_last_five(tmp_path, capsys, monkeypatch):
    monkeypatch.setenv("NOTED_DB", str(tmp_path / "notes.json"))
    add_notes(7)
    capsys.readouterr()

    noted.main(["tail"])
    out = capsys.readouterr().out

    assert out == "#3\tnote 3\n#4\tnote 4\n#5\tnote 5\n#6\tnote 6\n#7\tnote 7\n"


def test_tail_custom_limit(tmp_path, capsys, monkeypatch):
    monkeypatch.setenv("NOTED_DB", str(tmp_path / "notes.json"))
    add_notes(5)
    capsys.readouterr()

    noted.main(["tail", "--limit", "2"])
    out = capsys.readouterr().out

    assert out == "#4\tnote 4\n#5\tnote 5\n"


def test_tail_empty(tmp_path, capsys, monkeypatch):
    monkeypatch.setenv("NOTED_DB", str(tmp_path / "notes.json"))

    noted.main(["tail"])
    out = capsys.readouterr().out

    assert out == "no notes yet\n"
