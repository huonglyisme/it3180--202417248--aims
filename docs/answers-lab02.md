Lab 02 - Discussion Answers

1. Why synchronize with master before a PR?

To integrate the latest changes from master into the
feature branch, detect conflicts, and verify compatibility
before merging the feature into master.

2. When should we avoid rebase?

Avoid rebasing commits that have already been shared
and are being used by other developers, because rebase
rewrites commit history and changes commit SHA values.

3. Feature branch vs Topic branch

- feature/*: Used to develop new software functionality.
- topic/*: Used for a specific task such as documentation
  or repository configuration.