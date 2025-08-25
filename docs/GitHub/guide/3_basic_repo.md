# GitHub Basics: Repository

## Repository Location

All CCBR developed pipelines, and techdev efforts should be created under [CCBR's GitHub Org Account](https://github.com/CCBR/) and all CCBR team members should have a minimal of read-only permission to the repository.

## Use of CookieCutter Templates

- All CCBR developed pipelines should be created from the appropriate templates:
    - Nextflow Pipelines: https://github.com/CCBR/CCBR_NextflowTemplate
    - Snakemake Pipelines: https://github.com/CCBR/CCBR_SnakemakeTemplate
    - TechDev Projects: https://github.com/CCBR/CCBR_TechDevTemplate

> Note: The above templates are themselves under active development! As we continue building a multitude of analysis pipelines, we keep expanding on the list of "commonalities" between these analysis pipelines which need to be added to the template itself. Hence, templates are updated from time-to-time.

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
--template CCBR/CCBR_NextflowTemplate \
--description "<ADD REPO DESCRIPTION>" \
--public \
--confirm
```
```bash
gh repo create CCBR/<ADD NEW REPO NAME> \
--template CCBR/CCBR_SnakemakeTemplate \
--description "<ADD REPO DESCRIPTION>" \
--public \
--confirm
```

### 2) Creating a new techDev
```bash
gh repo create CCBR/techdev_<ADD NEW REPO NAME> \
--template CCBR/CCBR_TechDevTemplate \
--description "<ADD REPO DESCRIPTION>" \
--public \
--confirm
```

Once the repo is created, then you can clone a local copy of the new repository:

```bash
gh repo clone CCBR/<reponame>.git
```

## Minimal helper components

If you start from one of the above templates, you'll have these files already.
However, if you're updating an established repository, you may need to add some of these manually.

- [`CHANGELOG.md`](https://github.com/CCBR/CCBR_NextflowTemplate/blob/main/CHANGELOG.md)
    
    The changelog file should be at the top level of your repo. One exception is if your repo is an R package, it should be called [`NEWS.md`](https://r-pkgs.org/other-markdown.html#sec-news) instead. You can see an example changelog of a pipeline in active development [here](https://github.com/CCBR/CHAMPAGNE/blob/main/CHANGELOG.md).

- [`VERSION`](https://github.com/CCBR/CCBR_NextflowTemplate/blob/main/VERSION)

    The version file should be at the top level of your repo. If your repo is a **Python package**, it can be at at the package root instead, e.g. `src/pkg/VERSION`. If your repo is an **R package**, the version should be inside the [`DESCRIPTION`](https://r-pkgs.org/description.html) file instead.
    Every time a PR is opened, the PR owner should add a line to the changelog to describe any user-facing changes such as new features added, bugs fixed, documentation updates, or performance improvements.

    You will also need a CLI command to print the version. The implementation will be different depending on your repo's language and structure.

- [`CITATION.cff`]((https://github.com/CCBR/CCBR_NextflowTemplate/blob/main/CITATION.cff))

    The citation file must be at the top level of your repo. See template [here](https://github.com/CCBR/CCBR_NextflowTemplate/blob/main/CITATION.cff).

    You will also need a CLI command to print the citation. The implementation will be different depending on your repo's language and structure.

- Pre-commit config files

    Pre-commit hooks provide an automated way to style code, draw attention to typos, and validate commit messages. Learn more about pre-commit [here](https://ccbr.github.io/HowTos/GitHub/howto_precommit/).
    These files can be customized depending on the needs of the repo. For example, you don't need the hook for formatting R code if your repo does not and will never contain any R code.

    - [`.pre-commit-config.yaml`](https://github.com/CCBR/CCBR_NextflowTemplate/blob/main/.pre-commit-config.yaml)
    - [`.pretterignore`](https://github.com/CCBR/CCBR_NextflowTemplate/blob/main/.prettierignore)
    - [`.prettierrc`](https://github.com/CCBR/CCBR_NextflowTemplate/blob/main/.prettierrc)

- [`.github/PULL_REQUEST_TEMPLATE.md`](https://github.com/CCBR/CCBR_NextflowTemplate/blob/main/.github/PULL_REQUEST_TEMPLATE.md)

    The Pull Request template file helps developers and collaborators remember to write descriptive PR comments, link any relevant issues that the PR resolves, write unit tests, update the docs, and update the changelog.
    You can customize the Checklist in the template depending on the needs of the repo.

- [Issue templates](https://github.com/CCBR/CCBR_NextflowTemplate/tree/main/.github/ISSUE_TEMPLATE) (optional)

    Issue templates help users know how they can best communicate with maintainers to report bugs and request new features. These are helpful but not required.

    - [`.github/ISSUE_TEMPLATE/bug_report.yml`](https://github.com/CCBR/CCBR_NextflowTemplate/blob/main/.github/ISSUE_TEMPLATE/bug_report.yml)
    - [`.github/ISSUE_TEMPLATE/config.yml`](https://github.com/CCBR/CCBR_NextflowTemplate/blob/main/.github/ISSUE_TEMPLATE/config.yml)
    - [`.github/ISSUE_TEMPLATE/feature_request.yml`](https://github.com/CCBR/CCBR_NextflowTemplate/blob/main/.github/ISSUE_TEMPLATE/feature_request.yml)

- [GitHub Actions](https://ccbr.github.io/HowTos/GitHub/basic_actions/)

    GitHub Actions are automated workflows that run on GitHub's servers to execute unit tests, render documentation, build docker containers, etc. 
    Most Actions need to be customized for each repo. Learn more about them [here](https://ccbr.github.io/HowTos/GitHub/basic_actions/).