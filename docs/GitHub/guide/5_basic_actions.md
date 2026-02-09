---
author: "[Samantha Sevilla](https://github.com/slsevilla) & [Vishal Koparde](https://github.com/kopardev)"
date: 2023-04-27
---

# GitHub Basics: GitHub Actions

The following describe the minimum GitHub actions that should be deployed with any production pipeline. The actions are automatically provided via the cookiecutter templates: [NextFlow](https://github.com/CCBR/CCBR_NextflowPipelineCookiecutter) and [Snakemake](https://github.com/CCBR/CCBR_SnakemakePipelineCookiecutter).

1. Documentation (assumes `mkdocs build`; required for all repos)

    - These rules will automatically update any documentation built with mkdocs for all PR's.
    - Rule Name(s): mkdocs_build --> pages-build-and-deployment

2. Lintr (required for CCBR projects and new pipelines)
    - This rule will automatically perform a lintr with the data provided in the .test folder of the pipeline. Review the [GitHub Best Practices - Test Data](https://ccbr.github.io/HowTos/GitHub/sop_testdata/) page for more information.

3. Dry-run with test sample data for any PR to dev branch (required for CCBR projects and new pipelines)

    - This rule will automatically perform a dry-run with the data provided in the .test folder of the pipeline. Review the [GitHub Best Practices - Test Data](https://ccbr.github.io/HowTos/GitHub/sop_testdata/) page for more information.

4. Full-run with full sample data for any PR to main branch (required for CCBR projects and new pipelines)
    - This rule will automatically perform a full-run with the data provided in the .test folder of the pipeline. Review the [GitHub Best Practices - Test Data](https://ccbr.github.io/HowTos/GitHub/sop_testdata/) page for more information.

5. Auto pull/push from source (if applicable for CCBR projects and new pipelines)
    - If the pipeline is forked from another location and updating this forked pipeline is required, an action will automatically perform a pull from the source location at least once a week.

6. Add assigned issues & PRs to user projects.

    When an issue or PR is assigned to a CCBR member, this action will automatically add it to their personal GitHub Project, if they have one.
    This file can be copy and pasted exactly as-is into any CCBR repo from [here](https://github.com/CCBR/CCBR_NextflowTemplate/blob/main/.github/workflows/projects.yml).

## Advanced

View the [GitHub Actions demo](/docs/GitHub/github-actions-demo.qmd) for an in-depth guide for creating your own GitHub Actions workflows.
