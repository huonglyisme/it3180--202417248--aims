# Lab 04 - Discussion Answers

## 1. Why is release/* not merged back into master?

In Lab 04, the release branch is created from master
after the release has been prepared and tested.

The release branch preserves a stable baseline,
while master continues to receive new development.

Since release/lab04 has no additional changes,
merging it back into master is unnecessary.

However, if a hotfix is made on the release branch,
it should also be integrated into the appropriate
development branch.

## 2. How does Release Flow differ from GitFlow?

The workflow in Lab 04 uses master as the main
development branch.

Release branches are created from master to preserve
specific software versions.

GitFlow normally uses separate develop and master
branches, with release branches created from develop.

Therefore, the Lab 04 workflow is simpler than GitFlow.

## 3. Why version 1.0.0 instead of 0.4.0?

Semantic Versioning follows MAJOR.MINOR.PATCH.

Versions 0.x.y represent initial development,
when the public API is not yet considered stable.

Version 1.0.0 marks the first stable release of
AIMS-mini according to the course convention.

The version number does not represent the number
of completed laboratory exercises.
