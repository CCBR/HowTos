# GitHub Best Practices: Project/Pipeline Repository Management

Users should follow these links to learn more about setting up the repository, before reviewing the best practices below:

    - [Preparing your environment](https://ccbr.github.io/HowTos/GitHub/howto_setup/)
    - [Basic Commands](https://ccbr.github.io/HowTos/GitHub/howto_functions/)
    - [Creating your GitHub repo](https://ccbr.github.io/HowTos/GitHub/howto_setup/)
    - [Creating your Documentation](https://ccbr.github.io/HowTos/GitHub/setup_docs)
    - [GitHub Actions](https://ccbr.github.io/HowTos/GitHub/sop_actions/)
    
## Security settings

- Two members of CCBR (creator and one manager) should be granted full administrative priveleges to the repository to ensure the source code can be accessed by other members, as needed
- Both the develop and master branch must be protected (IE have to have a PR to be changed) 

## CCBR Branch Strategy

### Branch Naming
- All repositories should follow the strategy outlined in the [Creating your GitHub repo](https://ccbr.github.io/HowTos/GitHub/basic_repo/)

### Branch Overview

- All repositories should include a minimum of two branches at any time: 
    - main (master) 
    - dev
- Additional branches should be created as needed. These would include feature branches, developed using individual, feature specific addition and hotfix branches, developed using individual, bug specific fixes. 
- Utilization of these branches should follow the documentation below.

### Strategy Outline
- We encourage the use of the [Git Flow tools](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow) for some actions, available on Biowulf. Our current branching strategy is based off of the Git Flow strategy shown below :

    ![Image title](https://github.com/CCBR/HowTos/blob/main/img/gitflow_workflow.svg?raw=true)

1.  Master (named main or master)
    - branch that contains the current release / tagged version of the pipeline
    - merges from Dev branch or hotfix branch allowed
    - merges require actions_master_branch `pass` from GitHub actions. See [GitHub actions](https://ccbr.github.io/HowTos/GitHub/sop_actions/) #4 for more information testing requirements for merge
2. Develop (named dev or activeDev)
    - branch that contains current dev
    - merges from feature branch allowed
    - merges require actions_dev_branch `pass` from GitHub actions. See [GitHub actions](https://ccbr.github.io/HowTos/GitHub/sop_actions/) #3 for more information testing requirements for merge
3. Feature (named feature/unique_feature_name)
    - branch to develop new features that branches off the develop branch
    - recommended usages of `git flow feature start unique_feature_name`
    - no merges into this branch are expected
4. Hotfix (named unique_hotfix_name)
    - branches arise from a bug that has been discovered and must be resolved; it enables developers to keep working on their own changes on the develop branch while the bug is being fixed
    - recommended usage of `git flow hotfix start unique_hotfix_name`
    - no merges into this branch are expected 
- Note
    - While the `git flow feature start` command is recommended for feature branch merging, the `git flow feature finish` is not. Using the `finish` command will automatically merge the `feature` branch into the `dev` branch, without any testing, and regardless of divergence that may have occured during feature development.

## Release, Tagged Nomenclature
- The following format of versioning should be followed:

    ```
    v.X.Y.Z
    ```

- The following rules should be applies when determining the version release:

    - X is major; non-backward compatible (dependent on the amount of changes; from dev) 
    - Y is minor; backwards compatible (dependent on the amount of changes; from dev) 
    - Z is patches; backwards compatible (bugs; hot fixes) 

- Other notes:

    - X,Y,Z must be numeric only
    - All updates to the main (master) branch must be tagged and versioned using the parameters above
    - Updates to the dev branch can be tagged, but should not be versioned
    - If the pipeline is available locally (IE on Biowulf), version changes should be added for use