---
author: "[Samantha Sevilla](https://github.com/slsevilla) & [Vishal Koparde](https://github.com/kopardev)"
date: 2023-04-27
---

# GitHub HowTo: Basic Commands

The following outlines basic GitHub commands to `push` and `pull` from your repository. It also includes information on creating a new branch and deleting a branch. These commands should be used in line with guidance on [GitHub Repo Management](https://ccbr.github.io/HowTos/GitHub/sop_repo/).

### Pushing local changes to remote

Check which files have been changed.

```bash
git status
```

Stage files that need to be pushed
```bash
git add <thisfile>
git add <thatfile>
```

Push changes to branch named `new_feature`
```bash
git push origin new_feature
```

### Pulling remote changes to local

Pull changes from branch `new_feature` into your branch `old_feature`
```bash
git checkout old_feature
git pull new_feature
```

If you have non-compatible changes in the `old_feature` branch, there are two options:
1) ignore local changes and pull remote anyways. This will delete the changes you've made to your remote repository.
```bash
git reset --hard
git pull
```
2) temporarily stash changes away, pull and reapply changes after.
```bash
git stash
git pull
git stash pop
```

### Creating a new branch

This is a two step process.

  * Create the branch locally
```bash
git checkout -b <newbranch>
```

 * Push the branch to remote
```bash
git push -u origin <newbranch>
```
OR
```bash
git push -u origin HEAD
```
This is a shortcut to push the current branch to a branch of the same name on `origin` and track it so that you don't need to specify `origin HEAD` in the future.


### Deleting branches

#### Locally

```bash
git branch -d <BranchName>
```

#### on GitHub

```bash
git push origin --delete <BranchName>
```
