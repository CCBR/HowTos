# GitHub Best Practices: TechDev Test Data

The following information is meant to outline test_data requirements, however, should be altered to fit the needs of the specific techdev developed.
- [Preparing your environment](https://ccbr.github.io/HowTos/GitHub/howto_setup/)
- [Basic Commands](https://ccbr.github.io/HowTos/GitHub/howto_functions/)
- [Creating your GitHub repo](https://ccbr.github.io/HowTos/GitHub/howto_setup/)
- [Creating your Documentation](https://ccbr.github.io/HowTos/GitHub/setup_docs)
- [GitHub Actions](https://ccbr.github.io/HowTos/GitHub/sop_actions/)
- Repository Management:
    - [TechDev](https://ccbr.github.io/HowTos/GitHub/sop_repo_techdev/)
- Documentation:
    - [TechDev](https://ccbr.github.io/HowTos/GitHub/sop_doc_techdev/)

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
    - Test data should come from a CCBR project or a a publicly available source. Care should be taken when choosing test data sets, to ensure that the data matches the goals of the techdev effort.