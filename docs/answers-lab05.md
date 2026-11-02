# Lab 05 - Discussion Questions

## Question 1: Upstream First vs Release First

### Upstream First

Fix bugs on the main development branch first, then
propagate the changes to affected release branches.

Advantages:
- The fix is tested against the latest code.
- Helps prevent the bug from appearing in future releases.
- Keeps the main development branch updated.

Disadvantages:
- The fix may be difficult to backport to older versions.
- Additional changes may be needed for compatibility.

### Release First

Fix bugs directly on the affected release branch first,
then propagate the fix to master and other releases.

Advantages:
- Prioritizes fixing the currently released version.
- Avoids introducing unrelated new features.
- Suitable for urgent production hotfixes.

Disadvantages:
- The fix must be propagated to all affected branches.
- Missing a branch may leave some versions vulnerable.
- Cherry-pick conflicts may occur.

### Lab 05

This lab follows the Release First approach.

The fix is created from release/lab04 and propagated to:
- master
- release/lab05

## Question 2: How to detect a missing hotfix?

Use:

    git cherry -v origin/release/lab05 origin/release/lab04

The command compares patches between the two branches.

- "-" indicates an equivalent patch was found.
- "+" indicates no equivalent patch was detected.

Since cherry-pick conflicts can alter patch content,
we must also verify the behavior of each version.

Expected results:

    v1.0.1   1
    v1.1.0   1
    master   1

All three versions should successfully find
"The Lion King" using the keyword "lion".