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

## Documentation

- All pipelines should provide users with documentation for usage, test data, expected outputs, and troubleshooting information. [Mkdocs](https://www.mkdocs.org/) is the recommended tool to perform this action, however, other tools may be utilized. The cookiecutter templates ([TechDev](https://github.com/CCBR/CCBR_CCBRTechDevCookieCutter)) template's (written for mkdocs) provided have basic yaml markdown files provided for this use, and should be edited according to the pipelines function and user needs.

1. Overview
- This TechDev project was developed to [provide summary of the scope, key objectives].

2. Analysis
    - This will include several sections discussing the details of the development project.
   
    A. Background
    - Provide any relavant background to the project to be completed. This might include information on: - problem that was encountered leadings to this techdev - new feature or tool developed to be benchmarked - relevant biological or statistical information needed to perform this analysis

    B. Resources
    - This page should include any relevant tools that were used for testing. If these tools were loaded via Biowulf, include all version numbers. If they were installed locally, provide information on installation, source location, and any reference documents used.
    
    C. Analysis Plan
    - Provide a summary of the plan of action.
    - If benchmarking tools, include the dataset used, where the source material was obtained, and all relevant metadata.
    - Include the location of any relevant config / data files used in this analysis
    - Provide information on the limits of the analysis - IE this was only tested on Biowulf, this was only performed in human samples, etc.

    D. Results
    - Provide brief descriptions of the results obtained. Include links to where intermediate files may be locatedd.
    
    E. Conclusions
    - Provide brief, concise conclusion drawn from the analysis, including any alterations being made to pipelines or analysis.

3. Contributions
    - Provide any names that contributed to this work.

