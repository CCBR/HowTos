# Creating a Conda Package from an R Package
----
<br>

## Conda Setup

<br>

You will first need to set up Conda in order to use the Conda tools for creating your Conda package. 

The documentation for getting started can be found here: https://conda.io/projects/conda/en/latest/user-guide/getting-started.html

Follow the above documentation for installing Conda if it is not already installed.

<br>
<br>

### Set up Conda cache

<br>

In a space shared with other users that may use Conda, your personal Conda cache needs to be specified. 


To edit how your cache is saved perform the following steps

1) Create a new directory where you would like to store the conda cache called 'conda-cache'

```
mkdir conda/conda-cache
```

2) In your home directory, create the file '.condarc' 

```
touch ~/.condarc
```

3) Open the new file '.condarc' and add the following sections: 

- pkgs_dirs

- envs_dirs

- conda-build

- channels

In each section you will add the path to the directories you would like to use for each section. 

**Example:**

```
kgs_dirs:<br>
  - /rstudio-files/ccbr-data/users/Ned/conda-cache<br>
envs_dirs:<br>
  - /rstudio-files/ccbr-data/users/Ned/conda-envs<br>
conda-build:<br>
    root-dir: /rstudio-files/ccbr-data/users/Ned/conda-bld<br>
    build_folder: /rstudio-files/ccbr-data/users/Ned/conda-bld
    conda-build<br>
  output_folder: /rstudio-files/ccbr-data/users/Ned/conda-bld/conda-output<br>
channels:<br>
  - file://rstudio-files/RH/ccbr-projects/Conda_package_tutorial/local_channel/channel<br>
  - conda-forge<br>
  - bioconda<br>
  - defaults<br>
```

<br>
<br>

### Check Conda setup

<br>

To check that conda has been setup witht the specified paths from .condarc start conda:

```
conda activate
```

Then check the conda info:

```
conda info
```

<br>
<br>

## Conda R Package Creation

<br>

To create a package with Conda, you first need to make a new release and tag in the github repo of the R package you would like to create into a Conda Package.

For more information on best practices in R package creation, see:

https://r-pkgs.org/whole-game.html

Before creating the release on github, please check for proper dependencies listed in the files NAMESPACE and DESCRIPTION.

These files should have the same list of dependencies, and the version numbers for dependencies can be specified in the DESCRIPTION file. The DESCRIPTION file must be editted manually, while the NAMESPACE file should not be editted manually, but rather created automatically using the document() function. 

The DESCRITPION file must also be correctly formatted. For more information, see:

https://r-pkgs.org/description.html

<br>
<br>

### Download the R package release from Github

<br>

To download the most recent release from the most recent tag on Github, activate Conda then use Conda skeleton like so:

```
conda activate 

conda skeleton cran $githubURL
```

Replace $githubURL with the URL to your R package's github repo.

A folder is then created for the downloaded release, for example running the following:

```
conda skeleton cran https://github.com/NIDAP-Community/DSPWorkflow
```

creates the folder

```
r-dspworkflow
```

Within this newly created folder is a file named "meta.yaml". You will need to edit this file to include the channels and edit any information on the the package version number or dependency version numbers.

Here is an example of the top of the "meta.yaml" file with the channels section added:

```
{% set version = '0.9.5.2' %}

{% set posix = 'm2-' if win else '' %}
{% set native = 'm2w64-' if win else '' %}

package:
  name: r-dspworkflow
  version: {{ version|replace("-", "_") }}
  
channels:
  - conda-forge
  - bioconda
  - default
  - file://rstudio-files/RH/ccbr-projects/Conda_package_tutorial/local_channel/channel

source:

  git_url: https://github.com/NIDAP-Community/DSPWorkflow
  git_tag: 0.9.5

build:
  merge_build_host: True  # [win]
  # If this is a new build for the same version, increment the build number.
  number: 0
  # no skip

  # This is required to make R link correctly on Linux.
  rpaths:
    - lib/R/lib/
    - lib/

    # Suggests: testthat (== 3.1.4)
requirements:
  build:
    - {{ posix }}filesystem        # [win]
    - {{ posix }}git
    - {{ posix }}zip               # [win]
```

Here is an example of the sections for specifying dependency versions from the "meta.yaml" file:

```
  host:
    - r-base =4.1.3=h2f963a2_5
    - bioconductor-biobase =2.54.0=r41hc0cfd56_2
    - bioconductor-biocgenerics =0.40.0=r41hdfd78af_0
    - bioconductor-geomxtools =3.1.1=r41hdfd78af_0
    - bioconductor-nanostringnctools =1.2.0
    - bioconductor-spatialdecon =1.4.3
    - bioconductor-complexheatmap =2.10.0=r41hdfd78af_0
    - r-cowplot =1.1.1=r41hc72bb7e_1
    - r-dplyr =1.0.9=r41h7525677_0
    - r-ggforce =0.3.4=r41h7525677_0
    - r-ggplot2 =3.3.6=r41hc72bb7e_1
    - r-gridextra =2.3=r41hc72bb7e_1004
    - r-gtable =0.3.0=r41hc72bb7e_3
    - r-knitr =1.40=r41hc72bb7e_1
    - r-patchwork =1.1.2=r41hc72bb7e_1
    - r-reshape2 =1.4.4=r41h7525677_2
    - r-scales =1.2.1=r41hc72bb7e_1
    - r-tibble =3.1.8=r41h06615bd_1
    - r-tidyr =1.2.1=r41h7525677_1
    - r-umap =0.2.9.0=r41h7525677_1
    - r-rtsne =0.16=r41h37cf8d7_1
    - r-magrittr =2.0.3=r41h06615bd_1
    - r-rlang =1.1.0=r41h38f115c_0
    
  run:
    - r-base =4.1.3=h2f963a2_5
    - bioconductor-biobase =2.54.0=r41hc0cfd56_2
    - bioconductor-biocgenerics =0.40.0=r41hdfd78af_0
    - bioconductor-geomxtools =3.1.1=r41hdfd78af_0
    - bioconductor-nanostringnctools =1.2.0
    - bioconductor-spatialdecon =1.4.3
    - bioconductor-complexheatmap =2.10.0=r41hdfd78af_0
    - r-cowplot =1.1.1=r41hc72bb7e_1
    - r-dplyr =1.0.9=r41h7525677_0
    - r-ggforce =0.3.4=r41h7525677_0
    - r-ggplot2 =3.3.6=r41hc72bb7e_1
    - r-gridextra =2.3=r41hc72bb7e_1004
    - r-gtable =0.3.0=r41hc72bb7e_3
    - r-knitr =1.40=r41hc72bb7e_1
    - r-patchwork =1.1.2=r41hc72bb7e_1
    - r-reshape2 =1.4.4=r41h7525677_2
    - r-scales =1.2.1=r41hc72bb7e_1
    - r-tibble =3.1.8=r41h06615bd_1
    - r-tidyr =1.2.1=r41h7525677_1
    - r-umap =0.2.9.0=r41h7525677_1
    - r-rtsne =0.16=r41h37cf8d7_1
    - r-magrittr =2.0.3=r41h06615bd_1
    - r-rlang =1.1.0=r41h38f115c_0
```

In the above example, each of the dependencies has been assigned a conda build string, so that when conda builds a conda package, it will only use that specific build of the dependency from the listed conda channels. The above example is very restrictive, the dependencies can also be listed in the "meta.yaml" file to be more open--it will choose a conda build string that fits in with the other resolved dependency build strings based on what is available in the channels. 

Also note that the "host" section matches the "run" section.

Here is some examples of a more open setup for these dependencies:

```
  host:
    - r-base >=4.1.3
    - bioconductor-biobase >=2.54.0
    - bioconductor-biocgenerics >=0.40.0
    - bioconductor-geomxtools >=3.1.1
    - bioconductor-nanostringnctools >=1.2.0
    - bioconductor-spatialdecon =1.4.3
    - bioconductor-complexheatmap >=2.10.0
    - r-cowplot >=1.1.1
    - r-dplyr >=1.0.9
    - r-ggforce >=0.3.4
    - r-ggplot2 >=3.3.6
    - r-gridextra >=2.3
    - r-gtable >=0.3.0
    - r-knitr >=1.40
    - r-patchwork >=1.1.2
    - r-reshape2 >=1.4.4
    - r-scales >=1.2.1
    - r-tibble >=3.1.8
    - r-tidyr >=1.2.1
    - r-umap >=0.2.9.0
    - r-rtsne >=0.16
    - r-magrittr >=2.0.3
    - r-rlang >=1.1.0
```

<br>
<br>

### Build the Conda package

<br>

When the "meta.yaml" has been prepared, you can now build the Conda package. 

To do so, run the command:

```
conda-build $r-package 2>&1|tee $build_log_name.log
```

Replace $r-package with the name of the R package folder that was created after running conda skeleton (the folder where the meta.yaml is located).

*Example:* r-dspworkflow

Replace $build_log_name.log with the name for the log file, such as the date, time, and initials.

*Example:* 05_12_23_330_nc.log

The log file will list how conda has built the package, including what dependencies version numbers and corresponding build strings were used to resolve the conda environment. These dependencies are what we specified in the "meta.yaml" file. The log file will be useful troubleshooting a failed build.

Be aware, the build can take anywhere from several minutes to an hour to complete, depending on the size of the package and the number of dependencies. 

The conda package will be built as a tar.bz2 file.

<br>
<br>

## Common Issues

<br>

### Package Dependency Issues

An important consideration for Conda builds is the list of dependencies, specified versions, and compatibility with each of the other dependencies.

If the meta.yaml and DESCRIPTION file specify specific package versions, Conda's ability to resolve the Conda environment also becomes more limited.

For example, if the Conda package we are building has the following requirements:

```
Dependency A version == 1.0
Dependency B version >= 2.5
```

And the Dependencies located in our Conda channel have the following dependencies:

```
Dependency A version 1.0
  - Dependency C version == 0.5

Dependency A version 1.2
- Dependency C version >= 0.7

Dependency B version 2.7
  - Dependency C version >= 0.7
```

As you can see, the Conda build will not be able to resolve the environment because Dependency A verion 1.0 needs an old version of Dependency C, while Dependency B version 2.7 needs a newer version. 

In this case, if we changed our package's DESCRIPTION and meta.yaml file to be:

```
Dependency A version >= 1.0
Dependency B version >= 2.5
```

The conda build will be able to resolve. This is a simplied version of a what are more often complex dependency structures, but it is an important concept in conda package building that will inevitably arise as a package's dependencies become more specific.

<br>

To check on the versions of packages that are available in a Conda channel, use the command:

```
conda search $dependency
```

Replace $dependency with the name of package you would like to investigate. There are more optional commands for this function which can be found here:

 https://docs.conda.io/projects/conda/en/latest/commands/search.html

<br>

 To check the dependencies of packages that exist in your Conda cache, go to the folder specified for your conda cache (that we specified earlier). In case you need to find that path you can use:

 ```
conda info
 ```

 Here there will be a folder for each of the packages that has been used in a conda build (including the dependencies). In each folder is another folder called "info" and a file called "index.json" that lists information, such as depends for the package.

 Here is an example:

 ```
 cat /rstudio-files/ccbr-data/users/Ned/conda-cache/r-ggplot2-3.3.6-r41hc72bb7e_1/info/index.json

{
  "arch": null,
  "build": "r41hc72bb7e_1",
  "build_number": 1,
  "depends": [
    "r-base >=4.1,<4.2.0a0",
    "r-digest",
    "r-glue",
    "r-gtable >=0.1.1",
    "r-isoband",
    "r-mass",
    "r-mgcv",
    "r-rlang >=0.3.0",
    "r-scales >=0.5.0",
    "r-tibble",
    "r-withr >=2.0.0"
  ],
  "license": "GPL-2.0-only",
  "license_family": "GPL2",
  "name": "r-ggplot2",
  "noarch": "generic",
  "platform": null,
  "subdir": "noarch",
  "timestamp": 1665515494942,
  "version": "3.3.6"
}
 ```

 If you would like to specify an exact package to use in a conda channel for your conda build, specify the build string in your "meta.yaml" file. In the above example for ggplot version 3.3.6, the build string is listed in the folder name for package as well as in the index.json file for "build: "r41hc72bb7e_1".