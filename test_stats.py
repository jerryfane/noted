import noted


def test_stats_empty(tmp_path, capsys, monkeypatch):
    monkeypatch.setenv("NOTED_DB", str(tmp_path / "notes.json"))
    noted.main(["stats"])
    out = capsys.readouterr().out
    assert out == "notes: 0\nmax id: 0\n"


def test_stats_counts_notes_and_reports_max_id(tmp_path, capsys, monkeypatch):
    monkeypatch.setenv("NOTED_DB", str(tmp_path / "notes.json"))
    noted.main(["add", "first"])
    noted.main(["add", "second"])
    capsys.readouterr()

    noted.main(["stats"])
    out = capsys.readouterr().out
    assert out == "notes: 2\nmax id: 2\n"
