# recent

List notes created within the last N days.

    python noted.py recent
    python noted.py recent --days 14

Prints each matching note as `#<id>\t<text>`, or `no recent notes` when none
match. The default window is 7 days. Notes without a `created_at` value are
skipped. `created_at` may be an ISO date or datetime string.
