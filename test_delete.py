import noted


def test_delete_removes_note_by_id(tmp_path, capsys, monkeypatch):
    monkeypatch.setenv("NOTED_DB", str(tmp_path / "notes.json"))
    noted.main(["add", "first"])
    noted.main(["add", "second"])
    capsys.readouterr()

    noted.main(["delete", "1"])
    out = capsys.readouterr().out
    assert "deleted #1" in out

    noted.main(["list"])
    out = capsys.readouterr().out
    assert "#1\tfirst" not in out
    assert "#2\tsecond" in out


def test_delete_missing_note_reports_not_found_and_keeps_notes(tmp_path, capsys, monkeypatch):
    monkeypatch.setenv("NOTED_DB", str(tmp_path / "notes.json"))
    noted.main(["add", "keep"])
    capsys.readouterr()

    noted.main(["delete", "99"])
    out = capsys.readouterr().out
    assert "note #99 not found" in out

    noted.main(["list"])
    out = capsys.readouterr().out
    assert "#1\tkeep" in out
