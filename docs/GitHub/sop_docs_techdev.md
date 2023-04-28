# GitHub Best Practices: TechDev Documentation

- All pipelines should provide users with documentation for usage, test data, expected outputs, and troubleshooting information. [Mkdocs](https://www.mkdocs.org/) is the recommended tool to perform this action, however, other tools may be utilized. The cookiecutter templates ([TechDev](https://github.com/CCBR/CCBR_CCBRTechDevCookieCutter)) template's (written for mkdocs) provided have basic yaml markdown files provided for this use, and should be edited according to the pipelines function and user needs.

1. Overview
- This TechDev project was developed to [provide summary of the scope, key objectives].

2. Analysis
    - This will include several sections discussing the details of the development project.
   
    A. Background
    - Provide any relavant background to the project to be completed. This might include information on: - problem that was encountered leadings to this techdev - new feature or tool developed to be benchmarked - relevant biological or statistical information needed to perform this analysis

    B. Resources
    - This page should include any relevant tools that were used for testing. If these tools were loaded via Biowulf, include all version numbers. If they were installed locally, provide information on installation, source location, and any reference documents used.
    
    C. Test Data
    - This will include information on the test data included within the project. Species information, source information, and references should be included. Any manipulation performed on the source samples should also be included. Manifest information should also be outlined.
    
    D. Analysis Plan
    - Provide a summary of the plan of action.
    - If benchmarking tools, include the dataset used, where the source material was obtained, and all relevant metadata.
    - Include the location of any relevant config / data files used in this analysis
    - Provide information on the limits of the analysis - IE this was only tested on Biowulf, this was only performed in human samples, etc.

    E. Results
    - Provide brief descriptions of the results obtained. Include links to where intermediate files may be locatedd.
    
    F. Conclusions
    - Provide brief, concise conclusion drawn from the analysis, including any alterations being made to pipelines or analysis.

3. Contributions
    - Provide any names that contributed to this work.

