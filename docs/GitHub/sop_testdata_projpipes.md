# GitHub Best Practices: Pipelines Test Data

The following information is meant to outline test_data requirements for all pipelines, however, should be altered to fit the needs of the specific pipeline or project developed.
- [Preparing your environment](https://ccbr.github.io/HowTos/GitHub/howto_setup/)
- [Basic Commands](https://ccbr.github.io/HowTos/GitHub/howto_functions/)
- [Creating your GitHub repo](https://ccbr.github.io/HowTos/GitHub/howto_setup/)
- [Creating your Documentation](https://ccbr.github.io/HowTos/GitHub/setup_docs)
- [GitHub Actions](https://ccbr.github.io/HowTos/GitHub/sop_actions/)
- Repository Management:
    - [CCBR Projects, new Pipelines](https://ccbr.github.io/HowTos/GitHub/sop_repo_projpipes/)
- Documentation:
    - [new Pipelines](https://ccbr.github.io/HowTos/GitHub/sop_doc_projpipes/)

## Requirements

1. Location of data
    - Test data sets should be stored within a `.test` directory, as found in all cookiecutter templates. 
2. Documentation
    - Review information on the [documentation](https://ccbr.github.io/HowTos/GitHub/sop_docs_techdev/) page, which will provide basic information on test data used within the project/pipeline.
    - A README file should be created under the `.test` directory, to include the following information:
        - Date of implementation
        - Information on species (IE Homo Sapiens) and data type (IE RNA-Seq)
        - Information on the references to be used (IE hg38)
        - Metadata manifests required by the pipeline
        - The source of the files
        - Link to scripts used in created the partial test data
3. Choosing a test data set
    - At a minimum three test sets should be available: 1) Should include sub-sampled inputs, to test the pipelines functionality, and to be used as the tutorial `test set`. 2) Should include full-sample inputs, of high quality, to test the robustness of the pipelines resources 3) Should include full-sample inputs, of expected project-level quality, to test the robustness of the pipelines error handling
    - Test data should come from a CCBR project or a a publicly available source. Care should be taken when choosing test data sets, to ensure that the robustness of the pipeline will be tested, as well as the ability of the pipeline to handle both high and low quality data. Multiple test sets may need to be created to meet these goals.