# GitHub Setup: Repository!

## Repository Location

- All CCBR developed pipelines should be created under [CCBR's GitHub Org Account](https://github.com/CCBR/).

## Use of CookieCutter Templates

- All CCBR developed pipelines should be created from the appropriate cookiecutter template:
    - NextFlow Pipelines: https://github.com/CCBR/CCBR_NextflowPipelineCookiecutter
    - Snakemake Pipelines: https://github.com/CCBR/CCBR_SnakemakePipelineCookiecutter
    - TechDev Projects: https://github.com/CCBR/CCBR_CCBRTechDevCookieCutter

## Creating a new repository
To create a new repository on Github using [gh cli](https://cli.github.com/), you can run the following command on [Biowulf](https://hpc.nih.gov) after you update the new repository name (`<ADD NEW REPO NAME>`) and the repository description (`<ADD REPO DESCRIPTION>`) commands below. 

Naming Nomenclature:
- All Repositories: Do not remove the `CCBR/` leading the repository name, as this will correctly place the repository under the CCBR organization account.
- CCBR Projects: These should be named with the CCBR#. IE `CCBR/CCBR1155`
- CCBR Pipelines: These should be descriptive of the pipelines main process; acronyms are encouraged. IE `CCBR/CARLISLE`
- TechDev projects: These should be descriptive of the techDev project to be performed and should begin with `techdev_`. IE `CCBR/techdev_peakcall_benchmarking`


### 1) Creating a new project OR new pipeline repository
```bash
gh repo create CCBR/<ADD NEW REPO NAME> \
--template CCBR/CCBR_SnakemakePipelineCookiecutter \
--description "<ADD REPO DESCRIPTION>" \
--public \
--confirm
```

### 2) Creating a new techDev
```bash
gh repo create CCBR/techdev_<ADD NEW REPO NAME> \
--template CCBR/CCBR_CCBRTechDevCookieCutter \
--description "<ADD REPO DESCRIPTION>" \
--public \
--confirm
```


Once the repo is created, then you can clone a local copy of the new repository:

```bash
gh repo clone CCBR/<reponame>.git
```

## GitHub Functions
- The following outlines basic GitHub function to `push` and `pull` from your repository. It also includes information on creating a new branch and deleting a branch. These commands should be used in line with guidance on [GitHub Repo Management](https://ccbr.github.io/HowTos/GitHub/sop_repo/).

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

If you have non-compatable changes in the `old_feature` branch, there are two options:
1) ignore local changes and pull remote anyways. This will delete the changes you've made to your remote respository.
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