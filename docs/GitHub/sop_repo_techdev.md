# GitHub Best Practices: TechDev Repository Management

Users should follow the [set-up]() information provided to learn more about where and how to create a new repository, before following the management best practices below.

## Security settings

- Two members of CCBR (creator and one manager) should be granted full administrative priveleges to the repository to ensure the source code can be accessed by other members, as needed
- Both the develop and master branch must be protected (IE have to have a PR to be changed) 

## CCBR Branch Strategy

### Branch Naming
- All repositories should follow the strategy outlined in the  [Creating your GitHub repo](https://ccbr.github.io/HowTos/GitHub/setup_repo/)

### Branch Overview

- All repositories should include a minimum of two branches at any time: 
    - main (master) 
    - dev
- Utilization of these branches should follow the documentation below.

### Branch Strategy
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