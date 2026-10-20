# Goal

Reject incorrect lengths in the existing public ISBN-10 and ISBN-13 validators.
Smallest slice: two length guards (four source lines), about 20 regression lines
in the existing test file, no dependency or consumer changes.

# State

Worker thread `01a15b46-3e8d-756c-aae8-81ec4de0103c`.
Origin `git@github.com:accessibleapps/isbn_utils.git`, fresh master/base
`235e22dfcacac5ec8d8b55ee5f9395706af627bf`. Non-archived/non-fork,
authenticated ctoth/admin; no open PRs. Isolated branch
`modernize/task6-isbn_utils` in task-root worktrees/isbn_utils.
Canonical checkout remains untouched; its untracked uv.lock is preserved.
No repo or nested AGENTS/CLAUDE/skills/task-note guidance exists.

# Decisions and why

README exposes both validators directly; existing direct validator tests reject
malformed text. isbn10_valid iterates without a length check and stops after ten
characters, accepting empty/short zero input and ignoring suffixes. isbn13_valid
indexes the last character without first establishing the required length.
Use existing exact valid README/test examples and malformed lengths; preserve
all valid inputs, normalization and checksum algorithms.
README documents uv run pytest, uv run pyright and uv run ruff check.
No hosted workflow or tracked lock exists. Coordinator authorizes the existing
relevant full checks once locally when hosted CI is absent.

Supported-environment red proof: uv run pytest -q test_isbn_utils.py reproduced
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
allowing current pytest on newer interpreters. Add one manifest line;
no tracked lock exists, so do not commit the generated local
lock or environment. Reverted only this worker's four guard lines before
reproducing red under the corrected supported test environment.
Pytest cannot update its task-generated cache due mixed sandbox/Q ownership;
test executions pass with cache-only PermissionError warnings. Do not change
permissions or security settings; retain that limitation in the private report.

# Next step

Commit the four named task files, excluding generated caches, uv.lock and
environment. Return exact head/diff/results and concise PR text for coordinator
review before publication. No hosted authority exists for this repository.
