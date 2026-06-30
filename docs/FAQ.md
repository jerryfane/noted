# FAQ

## What is noted?

`noted` is a tiny command-line notes app. It lets you add short notes and list
them later from a simple local JSON file.

## How do I add and view notes?

Run `python noted.py add "your note"` to save a note. Run `python noted.py list`
to print all saved notes in the order they were added.

## Where does noted store data?

By default, notes are stored in `~/.noted.json`. You can override that location
by setting the `NOTED_DB` environment variable before running the CLI.
