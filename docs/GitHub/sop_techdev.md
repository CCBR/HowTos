# GitHub Best Practices
- Users should follow these links to learn more about setting up the repository, before reviewing the best practices below:

    - [Preparing your environment](https://ccbr.github.io/HowTos/GitHub/howto_setup/)
    - [Basic Commands](https://ccbr.github.io/HowTos/GitHub/howto_functions/)
    - [Creating your GitHub repo](https://ccbr.github.io/HowTos/GitHub/basic_repo/)
    - [Creating your Documentation](https://ccbr.github.io/HowTos/GitHub/setup_docs)
    - [GitHub Actions](https://ccbr.github.io/HowTos/GitHub/basic_actions/)

## TechDev Documentation

- All pipelines should provide users with:
    -  documentation for usage
    -  test data 
    -  expected outputs and reports  
    -  troubleshooting information 
   
    Markdown pages can be hosted directly within the repo using GH Pages. [Mkdocs](https://www.mkdocs.org/) is the recommended tool to perform this action, however, other tools may be utilized. The templates ([TechDev](https://github.com/CCBR/CCBR_CCBRTechDevTemplate)) template's (written for mkdocs) provided have basic yaml markdown files provided for this use, and should be edited according to the pipelines function and user needs. Also, track blockers/hurdles using GitHub Issues.

    1. **Overview**
        - Information on the goal of the TechDev project.
    2. **Analysis**            
        ***2.1. Background*** - Provide any relevant background to the project to be completed. This might include information on: - problem that was encountered leadings to this techdev - new feature or tool developed to be benchmarked - relevant biological or statistical information needed to perform this analysis
        
        ***2.2. Resources***
        - This page should include any relevant tools that were used for testing. If these tools were loaded via Biowulf, include all version numbers. If they were installed locally, provide information on installation, source location, and any reference documents used. 
            
        ***2.3. Test Data***
        - This will include information on the test data included within the project. Species information, source information, and references should be included. Any manipulation performed on the source samples should also be included. Manifest information should also be outlined. Provide location to toy dataset or real dataset or both. It is best to park these datasets at a commonly accessible location on Biowulf and share that location here. Also, make the location read-only to prevent accidental edits by other users.
            
        ***2.4. Analysis Plan***
        - Provide a summary of the plan of action.
        - If benchmarking tools, include the dataset used, where the source material was obtained, and all relevant metadata.
        - Include the location of any relevant config / data files used in this analysis
        - Provide information on the limits of the analysis - IE this was only tested on Biowulf, this was only performed in human samples, etc.

        ***2.5. Results***
        - What were the findings of this TechDev exercise? Include links to where intermediate files may be located.  Include tables, plots, etc. This will serve as a permanent record of the TechDev efforts to be shared within the team and beyond.
            
        ***2.6 Conclusions***
        - Provide brief, concise conclusion drawn from the analysis, including any alterations being made to pipelines or analysis.

    3. ***Contributions***
        - Provide any names that contributed to this work.

## TechDev Repository Management

### Security settings

- Two members of CCBR (creator and one manager) should be granted full administrative privileges to the repository to ensure the source code can be accessed by other members, as needed
- Both the develop and master branch must be protected (IE have to have a PR to be changed) 

### CCBR Branch Strategy

#### Branch Naming
- All repositories should follow the strategy outlined in the [Creating your GitHub repo](https://ccbr.github.io/HowTos/GitHub/basic_repo/)

#### Branch Overview

- All repositories should include a minimum of two branches at any time: 
    - main (master) 
    - dev
- Utilization of these branches should follow the documentation below.

#### Branch Strategy
- We encourage the use of the [Git Flow tools](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow) for some actions, available on Biowulf. Our current branching strategy is based off of the Git Flow strategy shown below :

    ![Image title](https://github.com/CCBR/HowTos/blob/main/img/gitflow_workflow.svg?raw=true)

1.  Master (named main or master)
    - branch that contains the current release / tagged version of the pipeline
    - merges from Dev branch or hotfix branch allowed
    - merges require actions_master_branch `pass` from GitHub actions. See [GitHub actions](https://ccbr.github.io/HowTos/GitHub/basic_actions/) #4 for more information testing requirements for merge
2. Develop (named dev or activeDev)
    - branch that contains current dev
    - merges from feature branch allowed
    - merges require actions_dev_branch `pass` from GitHub actions. See [GitHub actions](https://ccbr.github.io/HowTos/GitHub/basic_actions/) #3 for more information testing requirements for merge

## TechDev Test Data

### Requirements

1. Location of data
    - Test data sets should be stored within a `.test` directory, as found in all templates. 
2. Documentation
    - Review information on the [documentation](https://ccbr.github.io/HowTos/GitHub/basic_docs/) page, which will provide basic information on test data used within the project/pipeline.
    - A README file should be created under the `.test` directory, to include the following information:
        - Date of implementation
        - Information on species (IE Homo Sapiens) and data type (IE RNA-Seq)
        - Information on the references to be used (IE hg38)
        - Metadata manifests required by the pipeline
        - The source of the files
        - Link to scripts used in created the partial test data
3. Choosing a test data set
    - Test data should come from a CCBR project or a a publicly available source. Care should be taken when choosing test data sets, to ensure that the data matches the goals of the techdev effort.