---
title: "Zenodo"
author: "[Ned Cauley](https://github.com/escauley)"
---

Submit a pipeline to Zenodo in order to create a DOI for publication.

## Reference link

Use the link for full information, summarized below: https://www.youtube.com/watch?v=A9FGAU9S9Ow

## Prepare GitHub Repository

The GitHub repository should include the following:

1. README page
2. Documentation page, such as mkdocs, with usage and contact information
3. A citation `CITATION.cff`; [Example here](https://github.com/CCBR/CCBR_NextflowTemplate/blob/main/CITATION.cff)
4. Tagged and versioned, stable repository

## Link GitHub account to Zenodo

1. Go to [Zenodo](https://zenodo.org/)

2. Select `username` in the top right >> `Profile`. Select `GitHub``

3. Click `Sync Now` (top right) to update repos. NOTE: You may have to refresh the page

4. Toggle the `On` button on the repo you wish to publish. This will move the pipeline to the `Enable Repositories` list.

## Prepare GitHub Repo

1. Go to [GitHub](https://www.github.com) and find the repository page.

2. Select `Releases` >> `Draft a new release`

3. Create a tag, following naming semantics described [here](https://ccbr.github.io/HowTos/GitHub/sop_projpipes/#release-tagged-nomenclature)

4. Describe the tag with the following: "Connecting pipeline to Zenodo"

## Update Zenodo Information

1. Go to [Zenodo](https://zenodo.org/)

2. Select `My dashboard` >> `Edit`

3. Update the following information:

    - Resource Type: Software
    - Title: Full Pipeline Name (ShorthandName) (IE Mouse nEoanTigen pRedictOr (METRO)
    - Creators: Add creators, including ORCID's whenever possible
    - Description: A short description of the main features of the pipeline
    - Additional Description: If you use this software, please cite it as below.
    - Keywords and subjects: Add several keywords related to the pipeline
    - Version: add the version used in GitHub
    - Publisher: Zenodo
    - Related works: "Is original form of" "github website" URL

## Add DOI, citation to GitHub

1. Go to [Zenodo](https://zenodo.org/)

2. Select `username` in the top right >> `Profile`. Select `GitHub``

3. Click `Sync Now` (top right) to update repos. NOTE: You may have to refresh the page

4. Copy the DOI for the repository

5. Return to the GitHub repository and edit the `README` of the GitHub repo, adding the DOI link.

6. Update the `CITATION.cff` as needed.

7. Create a new tagged version.
