import noted


def test_tail_defaults_to_last_five(tmp_path, capsys, monkeypatch):
    monkeypatch.setenv("NOTED_DB", str(tmp_path / "notes.json"))
    for i in range(1, 8):
        noted.main(["add", f"note {i}"])
    capsys.readouterr()

    noted.main(["tail"])
    out = capsys.readouterr().out.splitlines()

    assert out == [
        "#3\tnote 3",
        "#4\tnote 4",
        "#5\tnote 5",
        "#6\tnote 6",
        "#7\tnote 7",
    ]


def test_tail_custom_limit(tmp_path, capsys, monkeypatch):
    monkeypatch.setenv("NOTED_DB", str(tmp_path / "notes.json"))
    for i in range(1, 6):
        noted.main(["add", f"note {i}"])
    capsys.readouterr()

    noted.main(["tail", "--limit", "2"])
    out = capsys.readouterr().out.splitlines()

    assert out == [
        "#4\tnote 4",
        "#5\tnote 5",
    ]


def test_tail_empty(tmp_path, capsys, monkeypatch):
    monkeypatch.setenv("NOTED_DB", str(tmp_path / "notes.json"))

    noted.main(["tail"])
    out = capsys.readouterr().out

    assert out == "no notes yet\n"
