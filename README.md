# CCBR How-Tos

[![docs](https://github.com/CCBR/HowTos/actions/workflows/docs-quarto.yml/badge.svg)](https://ccbr.github.io/HowTos/)
[![CodeQL](https://github.com/CCBR/HowTos/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/CCBR/HowTos/actions/workflows/github-code-scanning/codeql)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18038599.svg)](https://doi.org/10.5281/zenodo.18038599)

This page is designed to share knowledge between analysts within [CCBR](https://bioinformatics.ccr.cancer.gov/ccbr/).
You'll find how-to guides, best practices, and tutorials on the website:
<https://ccbr.github.io/HowTos/>

To render locally on a system with the `ccbrpipeliner` module available, run:

```bash
bash render.sh
```

The script loads `ccbrpipeliner` and `python/3.11`, creates `.venv-quarto` on first use, installs any
missing Jupyter dependencies, and renders the site into `_site/`. Later runs
reuse the environment. The first setup requires access to the Python package
index. Additional Quarto render arguments can be passed through, for example
`bash render.sh contributors.qmd`.

If you come across a **bug**, would like to **suggest an improvement**,
or have an **idea** for a new how-to guide,
please [**open an issue**](https://github.com/CCBR/HowTos/issues).

This page was created through the [contributions](https://ccbr.github.io/HowTos/contributors)
of several members within [CCBR](https://bioinformatics.ccr.cancer.gov/ccbr/).
If you would like to contribute, please reach out to
[Vishal Koparde](https://teams.microsoft.com/l/chat/0/0?users=vishal.koparde@nih.gov).
