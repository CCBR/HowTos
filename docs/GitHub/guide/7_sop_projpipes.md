# GitHub Best Practices: Projects and Pipelines

- Users should follow these links to learn more about setting up the repository, before reviewing the best practices below:

    - [Preparing your environment](howto_setup.md)
    - [Basic Commands](howto_functions.md)
    - [Creating your GitHub repo](basic_repo.md)
    - [Creating your Documentation](setup_docs.md)
    - [GitHub Actions](basic_actions.md)

## Pipeline Documentation
- All pipelines should provide users with documentation for usage, test data, expected outputs, and troubleshooting information. [Mkdocs](https://www.mkdocs.org/) is the recommended tool to perform this action, however, other tools may be utilized. The template's ([NextFlow](https://github.com/CCBR/CCBR_NextflowTemplate), [Snakemake](https://github.com/CCBR/CCBR_SnakemakeTemplate)) were written for mkdocs, and provide basic yaml markdown files provided for this use. They should be edited according to the pipelines function and user needs. Examples of the requirements for each page are provided in the templates.

    1. Background
        - Information on who the pipeline was developed for, and a statement if it's only been tested on Biowulf. 
        - Also include a workflow image to summarize the pipeline.
    2. Getting Started
        - This should set the stage for all of the pipeline requirements. This should include the following pages:
            - Introduction
            - Setup Dependencies
            - Login to the cluster
            - Load an interactive session
    3. Preparing Files
        - This should include the following pages:
            - Configs
                - Cluster Config
                - Tools Config
                - Config YAML
                    - User Parameters
                    - References
            - Preparing Manifests
                - Samples Manifest
    4. Running the Pipeline
        - This should include all information about the various run commands provided within the pipeline. This should include the following pages:
            - Pipeline Overview
            - Commands explained
            - Typical Workflow
    5. Expected Output
        - This should include all pertinent information about output files, including extensions that differentiate files.
    6. Running Test Data
        - This should walk the user through the steps of running the pipeline using test data. This should include the following pages:
            - Getting Started
            - About the test data
            - Submit the test data
            - Review outputs

## Repository Management

### Security settings

- `AdminTeam` should have a minimum of `maintain` role to the repo
- Both the develop and master branch must be protected (IE have to have a PR to be changed)
- Repo visibility should be set to Private or Internal and made Public only when required.

### CCBR Branch Strategy

#### Branch Naming
- All repositories should follow the strategy outlined in the [Creating your GitHub repo](basic_repo.md)

#### Branch Overview

- All repositories should include a minimum of two branches at any time: 
    - main ( or master ) 
    - dev
- Additional branches should be created as needed. These would include feature branches, developed using individual, feature specific addition and hotfix branches, developed using individual, bug specific fixes. 
- Utilization of these branches should follow the documentation below.

#### Strategy Outline
- We encourage the use of the [Git Flow tools](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow) for some actions, available on Biowulf (module load gitflow). Our current branching strategy is based off of the Git Flow strategy shown below :

![](../images/gitmodel.png)
ref:https://nvie.com/posts/a-successful-git-branching-model/

1.  Master (named main or master)
    - branch that contains the current release / tagged version of the pipeline
    - merges from Dev branch or hotfix branch allowed
    - merges require actions_master_branch `pass` from GitHub actions. See [GitHub actions](basic_actions.md) #4 for more information testing requirements for merge
2. Develop (named dev or activeDev)
    - branch that contains current dev
    - merges from feature branch allowed
    - merges require actions_dev_branch `pass` from GitHub actions. See [GitHub actions](basic_actions.md) #3 for more information testing requirements for merge
3. Feature (named feature/unique_feature_name)
    - branch to develop new features that branches off the develop branch
    - recommended usages of `git flow feature start unique_feature_name` followed by `git flow feature publish unique_feature_name`
    - no merges into this branch are expected
4. Hotfix (named unique_hotfix_name)
    - branches arise from a bug that has been discovered and must be resolved; it enables developers to keep working on their own changes on the develop branch while the bug is being fixed
    - recommended usage of `git flow hotfix start unique_hotfix_name`
    - no merges into this branch are expected 

> 💡 **Note**  
> While the `git flow feature start` command is recommended for feature branch creation, the `git flow feature finish` command is not. Using the `finish` command will automatically merge the `feature` branch into the `dev` branch without any testing and regardless of any divergence that may have occurred during feature development.




#### General Workflow (Steps)
1. Assuming that you have already cloned the repo and initiated git flow with `git flow init`
2. Create a new feature and publish it `git flow feature start unique_feature_name` and then `git flow feature publish unique_feature_name`. The *unique_feature_name* will be created from the *develop* branch.
3. Code normally, make frequent commits, push frequently to remote. These commits are added to the *unique_feature_name* branch.
4. When you are ready to add your feature enhancements back to the *develop* branch, you may have to make sure that the *develop* branch has not marched forward while you were working on the *unique_feature_name* feature (This is possible as other may have added their PRs in the interim). If it has, then you may have to pull in changes made to *develop* branch into your *unique_feature_name* feature branch. This can be achieved using the GitHub web interface... **merge** **develop** <-- **unique_feature_name**. Resolve conflicts if any.
5. Retest your *unique_feature_name* branch.
6. Now send in a pull request using the GitHub web interface to pull your *unique_feature_name* into *develop* branch.
7. Occasionally, we may create a new *release* branch from the *develop* branch and perform thorough E2E testing with fixes. Once, everything is working as expected, we pull the *release* branch back into *develop* and also push it to *main* with a version tag.

#### Release, Tagged Nomenclature
- The following format of versioning should be followed:

    ```
    vX.Y.Z
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

### Pipelines Test Data

The following information is meant to outline test_data requirements for all pipelines, however, should be altered to fit the needs of the specific pipeline or project developed.

#### Requirements

1. Location of data
    - Test data sets should be stored within a `.test` directory, as found in all templates. 
2. Documentation
    - Review information on the [documentation](basic_docs.md) page, which will provide basic information on test data used within the project/pipeline.
    - A README file should be created under the `.test` directory, to include the following information:
        - Date of implementation
        - Information on species (IE Homo Sapiens) and data type (IE RNA-Seq)
        - Information on the references to be used (IE hg38)
        - Metadata manifests required by the pipeline
        - The source of the files
        - Link to scripts used in created the partial test data
3. Choosing a test data set
    - At a minimum three test sets are recommended to be available:         
        1) Should include sub-sampled inputs, to test the pipelines functionality, and to be used as the tutorial `test set`. 
        2) Should include full-sample inputs, of high quality, to test the robustness of the pipelines resources 
        3) Should include full-sample inputs, of expected project-level quality, to test the robustness of the pipelines error handling
    - Test data should come from a CCBR project or a publicly available source. Care should be taken when choosing test data sets, to ensure that the robustness of the pipeline will be tested, as well as the ability of the pipeline to handle both high and low quality data. Multiple test sets may need to be created to meet these goals. On BIOWULF, these test data files can be stored under `/data/CCBR_Pipeliner/testdata` for easy access by all users of the pipeline(s).