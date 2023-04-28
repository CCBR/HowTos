# GitHub Best Practices: Pipeline Documentation

- Users should follow these links to learn more about setting up the repository, before reviewing the best practices below:
    - [Preparing your environment](https://ccbr.github.io/HowTos/GitHub/howto_setup/)
    - [Basic Commands](https://ccbr.github.io/HowTos/GitHub/howto_functions/)
    - [Creating your GitHub repo](https://ccbr.github.io/HowTos/GitHub/howto_setup/)
    - [Creating your Documentation](https://ccbr.github.io/HowTos/GitHub/setup_docs)
    - [GitHub Actions](https://ccbr.github.io/HowTos/GitHub/sop_actions/)
    - Repository Management:
        - [CCBR Projects, new Pipelines](https://ccbr.github.io/HowTos/GitHub/sop_repo_projpipes/)
- All pipelines should provide users with documentation for usage, test data, expected outputs, and troubleshooting information. [Mkdocs](https://www.mkdocs.org/) is the recommended tool to perform this action, however, other tools may be utilized. The cookiecutter template's ([NextFlow](https://github.com/CCBR/CCBR_NextflowPipelineCookiecutter), [Snakemake](https://github.com/CCBR/CCBR_SnakemakePipelineCookiecutter)) were written for mkdocs, and provide basic yaml markdown files provided for this use. They should be edited according to the pipelines function and user needs. Examples of the requirements for each page are provided in the cookiecutter templates.

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