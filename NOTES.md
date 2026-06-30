# NOTES

This repository contains `noted`, a small Python command-line tool for adding and listing short notes. The main entry point is `noted.py`, notes are stored as JSON in `~/.noted.json` unless `NOTED_DB` overrides the path, and `test_noted.py` exercises the basic add-and-list workflow with `pytest`.

## Conventions

- Keep the command surface small and focused on simple note-management actions.
- Preserve the file-backed JSON storage model and use `NOTED_DB` when tests or alternate data files need isolation.
