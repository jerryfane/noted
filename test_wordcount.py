import noted


def test_wordcount_empty_storage(tmp_path, capsys, monkeypatch):
    monkeypatch.setenv("NOTED_DB", str(tmp_path / "notes.json"))
    noted.main(["wordcount"])
    out = capsys.readouterr().out
    assert out == "words: 0\n"


def test_wordcount_counts_words_across_notes(tmp_path, capsys, monkeypatch):
    monkeypatch.setenv("NOTED_DB", str(tmp_path / "notes.json"))
    noted.main(["add", "alpha beta"])
    noted.main(["add", "gamma\tdelta\nepsilon"])
    capsys.readouterr()

    noted.main(["wordcount"])
    out = capsys.readouterr().out
    assert out == "words: 5\n"
