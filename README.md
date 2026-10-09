# Duplicatedove

Read-only exact duplicate text-line counts, no text/hashes emitted. Python 3.9+, no dependencies. Published in a private GitHub repository. Download its ZIP while signed into the owner account, extract it and open a terminal inside the source folder. Not verified as store-installed.

```text
python3 duplicatedove.py
python3 duplicatedove.py sample.txt
python3 -m unittest -v
bash app-store.sh install
bash app-store.sh run
```

Regular UTF-8 file <=1 MiB. No argument prompts; 0 exits. JSON-only report: total/unique lines, duplicate group counts and one-based line positions, repeated occurrences beyond first. No source text, key names or hashes, no content exported/saved, no changes or network. Line numbers/counts still can be sensitive.

Exact decoded equality after CRLF/CR/LF terminators removed. No trimming/casefolding/Unicode normalization. Blank lines participate. Empty file zero lines; trailing newline doesn't create extra empty line. UTF-8 BOM included in first line. Unicode line separators aren't line splits. Invalid UTF-8 rejected. Duplicate-heavy file can make large report. Not dedupe/rewrite tool or file comparison. 16 tests cover definitions, redaction, group order, limits/UTF-8. Linux tested; Pi/non-Linux untested. Marker/version1.0.0 published.

The current public-only Pi App Store cannot discover private repositories; authenticated store support is not verified.

Fullscreen update: Store interactive launch uses terminal-sized board cells or wrapped full-terminal utility input/results with PgUp/PgDn scrolling. Original core rules and direct CLI commands remain unchanged. Ctrl+C cancels utility entry, result Enter returns; no new dependency downloads. Linux PTY resize/restoration checked; physical Pi untested.
