import noted


def test_head_empty(tmp_path, capsys, monkeypatch):
    monkeypatch.setenv("NOTED_DB", str(tmp_path / "notes.json"))
    noted.main(["head"])
    out = capsys.readouterr().out
    assert "no notes yet" in out


def test_head_default_limit(tmp_path, capsys, monkeypatch):
    monkeypatch.setenv("NOTED_DB", str(tmp_path / "notes.json"))
    for text in ["one", "two", "three", "four", "five", "six"]:
        noted.main(["add", text])
    capsys.readouterr()

    noted.main(["head"])
    out = capsys.readouterr().out

    assert out.splitlines() == [
        "#1\tone",
        "#2\ttwo",
        "#3\tthree",
        "#4\tfour",
        "#5\tfive",
    ]


def test_head_custom_limit(tmp_path, capsys, monkeypatch):
    monkeypatch.setenv("NOTED_DB", str(tmp_path / "notes.json"))
    for text in ["one", "two", "three"]:
        noted.main(["add", text])
    capsys.readouterr()

    noted.main(["head", "--limit", "2"])
    out = capsys.readouterr().out

    assert out.splitlines() == [
        "#1\tone",
        "#2\ttwo",
    ]
