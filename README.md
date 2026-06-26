# noted

A tiny notes CLI.

## Usage

    python noted.py add "buy milk"
    python noted.py list
    python noted.py search "milk"
    python noted.py delete 1
    python noted.py export --json

Notes are stored as JSON at `~/.noted.json` (override with the `NOTED_DB` env var).

## Develop

    pip install pytest
    pytest
