# Goal

Reject incorrect lengths in the existing public ISBN-10 and ISBN-13 validators.
The feature adds two length guards (four source lines), regressions in the
existing test file and the authorized pytest>=8.3.5 development dependency.
This follow-up only corrects one long-input fixture and updates this note;
no product source, API, dependency, workflow or support change.

# State

Origin `git@github.com:accessibleapps/isbn_utils.git`; open draft PR #1 is
published at 18081494e23071d5f429a1cf8f20e498f6b9cba5. Its base is landed CI
prerequisite #2 at 99ae1d0ef945fbf422d3aa0da2f2e4bc8f9c8cc2. That feature
head's hosted Python 3.8/3.13 tests and package builds passed in run
39517940869. No tracked lock exists; the pytest dev declaration is present.

This isolated follow-up branch repair/task6-isbn-utils-fixture starts from
that exact published head. Separate archive/task6-isbn-utils-fixture-local
and archive/task6-isbn-utils-fixture-published refs preserve it. Original
worktrees and the earlier note-only-ahead 47bf7690eea6fc2b05e36237e3caf2536613b440
tip/archive remain untouched, including canonical untracked uv.lock/caches.

# Decisions and why

README exposes both validators directly; existing direct validator tests reject
malformed text. isbn10_valid iterates without a length check and stops after ten
characters, accepting empty/short zero input and ignoring suffixes. isbn13_valid
indexes the last character without first establishing the required length.
Use existing exact valid README/test examples and malformed lengths; preserve
all valid inputs, normalization and checksum algorithms.
README documents uv run pytest, uv run pyright and uv run ruff check.
The hosted workflow now runs the existing pytest suite and package build on
Python 3.8 and 3.13/Linux; no tracked lock exists. Historical local checks below
were authorized before that CI prerequisite landed, not rerun for this follow-up.

Original supported-environment red proof: uv run pytest -q test_isbn_utils.py reproduced
7 failed / 5 passed before guards, using the newly declared pytest8.3.5.
After guards, full uv run pytest passes12 tests on Python3.8.20/pytest8.3.5
(0.04s) and Python3.13.15/pytest9.1.1 (0.14s). Full uv run pyright reports
0 errors/warnings; uv run ruff check passes. A prior strict-Pyright failure
on the new test parameters was fixed by annotating those two parameters.
Final dependency uses pytest>=8.3.5, with no upper/exact pin. A selective
uv lock --upgrade-package pytest on the task-generated untracked lock selected
8.3.5 for<3.9, 8.4.2 for3.9, and9.1.1 for>=3.10; other existing dev tools
resolved to pyright1.1.414 and ruff0.17.1 in that initial isolated environment.
No canonical manifest, lock or environment was synchronized.
Final manifest SHA256:961AD1580A7600FA6E8B73DA1531F5350E65F8AED3C3E1A458D75D51AF2F637A.
Generated untracked lock SHA256:20DBB24CE588A7EC52289A0F75D7068ACAF0F81142A2C8B13189D29CB5EA365B.
Whitespace check passes with per-command core.whitespace=cr-at-eol, preserving
the tracked source/test CRLF convention. No custom hook is configured.

# Surprises

Canonical venv lacks pytest; the first exact uv run pytest fell back to a
global pytest, and Pyright then failed to resolve the undeclared pytest import.
Earlier borrowed-runtime red/green runs are diagnostic only (7 failed/5 passed,
then 12 passed), not supported-command evidence. Coordinator authorized one
pytest dev declaration to make the existing README command reproducible.
Primary PyPI JSON metadata: pytest 8.3.5 requires Python >=3.8, 8.4.0 >=3.9,
9.0.1 >=3.10. Declare >=8.3.5 so uv retains older-Python compatibility while
allowing current pytest on newer interpreters. That manifest line is already
present; no tracked lock exists, so do not commit the generated local
lock or environment. Reverted only this worker's four guard lines before
reproducing red under the corrected supported test environment.
Pytest cannot update its task-generated cache due mixed sandbox/Q ownership;
test executions pass with cache-only PermissionError warnings. Do not change
permissions or security settings; retain that limitation in the private report.

# Next step

The prior 14-digit fixture 97807434885870 already returned False on the
baseline: its final 0 differs from the computed check digit 7. The corrected
97807434885877 is wrongly accepted by that baseline and rejected by the
existing exact-length guard, so it exercises the long-input regression.

On Python 3.12/pytest 8.3.5, baseline source loaded directly from 99ae1d0e
in memory returned False for the old fixture and True for the replacement.
The edited long-input test case failed against that baseline (1 failed in
0.42s), then the complete actively edited test file passed against unchanged
guarded source (12 passed in 0.05s). No full local CI or build was run.

Return this complete two-file diff/head for coordinator review before a
guarded update to the already-published PR. Fresh actual Claude review and
green hosted results must cover the final published head before merge.
No model calls, comments/descriptions, merge, full local CI or unrelated
changes are authorized here. The unchanged CI covers Linux on Python 3.8 and
3.13; other runtimes/platforms remain outside that hosted evidence.
