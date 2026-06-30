# noted Usage Guide

`noted` is a small command-line tool for saving and listing short notes.

## Add a Note

Run the `add` command with the note text:

```bash
python noted.py add "buy milk"
```

This stores the note and prints the new note ID.

## List Notes

Run the `list` command to show every saved note:

```bash
python noted.py list
```

If no notes have been saved yet, the command prints `no notes yet`.

## Storage Location

By default, notes are stored as JSON in `~/.noted.json`. Set `NOTED_DB` to use a different file:

```bash
NOTED_DB=/tmp/notes.json python noted.py add "draft release notes"
```
