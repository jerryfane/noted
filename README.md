# noted

A tiny notes CLI.

## Usage

    python noted.py <command> [args]

Each subcommand lives in its own file under `commands/` and is auto-discovered,
and each is documented in its own file under [`docs/commands/`](docs/commands/).

Notes are stored as JSON at `~/.noted.json` (override with the `NOTED_DB` env var).

## Architecture

- `noted.py` — entry point; builds the parser by discovering `commands/*`.
- `storage.py` — shared note persistence (`load` / `save` / `db_path`).
- `commands/<name>.py` — one self-contained subcommand exposing `register(subparsers)`.
- `docs/commands/<name>.md` — usage for that subcommand.

Adding a subcommand means adding those files — no edits to any shared file.

## Develop

    pip install pytest
    pytest
