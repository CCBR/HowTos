# Creating a Conda Package from an R Package

## Set up Conda Tools, installation (if needed)

- You will first need to set up Conda in order to use the Conda tools for creating your Conda package. 

- The documentation for getting started can be found [here](https://conda.io/projects/conda/en/latest/user-guide/getting-started.html), including installation guidelines.

## Set up Conda cache

In a space shared with other users that may use Conda, your personal Conda cache needs to be specified. To edit how your cache is saved perform the following steps:

1) Create a new directory where you would like to store the conda cache called 'conda-cache'

  ```
  mkdir conda/conda-cache
  ```

2) In your home directory, create the file `.condarc`

```
touch ~/.condarc
```

3) Open the new file `.condarc` and add the following sections: 

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

## Check Conda setup

To check that conda has been setup with the specified paths from `.condarc` start conda:

```
conda activate
```

Then check the conda info:

```
conda info
```