# move

Move a note to a 1-based position.

    python noted.py move 3 1

Prints `moved #3 to 1` when the note exists. Positions below 1 move to the
start, and positions past the list length move to the end.

Prints `no note #3` when the note does not exist.
