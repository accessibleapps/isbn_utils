# Hosted test and package-build prerequisite

## Goal
Provide the existing ISBN tests and package build as a hosted gate before the feature PR can merge.

## State
Isolated branch from fresh origin/master 235e22dfcacac5ec8d8b55ee5f9395706af627bf. No feature source copied; canonical untracked uv.lock and feature worktree preserved. CI uses one Linux runner and Python 3.12, pinned actions, read-only token permissions, and no persisted checkout credentials. Actions enabled was verified through the read-only permissions API. Official latest releases checkout v7.0.1 and setup-uv v10.3.0 were resolved to their immutable commits through the GitHub API.

## Decisions and why
README declares pytest; the default manifest omits it and owns no lock. A pinned pytest tool environment runs the entire existing suite without changing project dependencies or duplicating feature #1's pytest declaration. uv build uses the existing Hatchling backend and both exact package outputs are required. Actions Dependabot maintains immutable action pins. No live services or release actions are used.

## Surprises
The four small libraries are absent from the committed product topology; the explicit task authorizes their narrow existing-test and package-build CI prerequisites. Hosted execution remains unverified until coordinator-authorized publication.

## Next step
Local Python 3.12 validation: all four existing tests passed; uv build produced dist/isbn_utils-0.1.tar.gz and dist/isbn_utils-0.1-py3-none-any.whl. actionlint 1.7.12 passed; zizmor 1.31.1 offline reported no findings (one default suppression). Return the committed local patch for coordinator review before publication. Actual Claude review and green checks on the final published head are required before a coordinator-directed merge.
