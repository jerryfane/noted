# today

List notes created today.

    python noted.py today

Prints matching notes as `#<id>\t<text>`, or `no notes today` when none match.
Notes without a `created_at` field are skipped. `created_at` may be an ISO date
or datetime string.
