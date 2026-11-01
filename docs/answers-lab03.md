Lab 03 – Discussion Answers

1. What is a merge base?

A merge base is a common ancestor commit of two branches.

Git uses the merge base to determine how the branches
have changed from their common history during a
three-way merge.

2. Why should master/release branches use revert?

Master and release branches contain shared history.

Git revert creates a new commit that reverses previous
changes without deleting or rewriting existing commits.

Git reset moves branch references and may rewrite
history, making it inappropriate for undoing published
changes on shared branches.