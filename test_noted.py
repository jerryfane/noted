import json

import noted


def use_tmp_db(tmp_path, monkeypatch):
    monkeypatch.setenv("NOTED_DB", str(tmp_path / "notes.json"))


def test_add_then_list(tmp_path, capsys, monkeypatch):
    use_tmp_db(tmp_path, monkeypatch)
    noted.main(["add", "buy milk"])
    noted.main(["list"])
    out = capsys.readouterr().out
    assert "added #1" in out
    assert "buy milk" in out


def test_search_matches_case_insensitive_and_reports_empty(tmp_path, capsys, monkeypatch):
    use_tmp_db(tmp_path, monkeypatch)
    noted.main(["add", "buy milk"])
    noted.main(["add", "call mom"])
    capsys.readouterr()

    noted.main(["search", "MILK"])
    found = capsys.readouterr().out
    assert "#1\tbuy milk" in found
    assert "call mom" not in found

    noted.main(["search", "tea"])
    assert capsys.readouterr().out.strip() == "no matching notes"


def test_delete_removes_note_by_id_and_reports_not_found(tmp_path, capsys, monkeypatch):
    use_tmp_db(tmp_path, monkeypatch)
    noted.main(["add", "buy milk"])
    noted.main(["add", "walk dog"])
    capsys.readouterr()

    noted.main(["delete", "1"])
    assert capsys.readouterr().out.strip() == "deleted #1"

    noted.main(["delete", "99"])
    assert capsys.readouterr().out.strip() == "note #99 not found"

    noted.main(["list"])
    out = capsys.readouterr().out
    assert "buy milk" not in out
    assert "#2\twalk dog" in out


def test_export_json_prints_all_notes(tmp_path, capsys, monkeypatch):
    use_tmp_db(tmp_path, monkeypatch)
    noted.main(["add", "buy milk"])
    noted.main(["add", "write tests"])
    capsys.readouterr()

    noted.main(["export", "--json"])
    exported = json.loads(capsys.readouterr().out)

    assert exported == [
        {"id": 1, "text": "buy milk"},
        {"id": 2, "text": "write tests"},
    ]
