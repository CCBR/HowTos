# GitHub Basics: Repository

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