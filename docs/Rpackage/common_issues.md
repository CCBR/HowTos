# Creating a Conda Package from an R Package

## Common Issues

### Package Dependency Issues

An important consideration for Conda builds is the list of dependencies, specified versions, and compatibility with each of the other dependencies.

If the `meta.yaml` and `DESCRIPTION` file specify specific package versions, Conda's ability to resolve the Conda environment also becomes more limited.

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

As you can see, the Conda build will not be able to resolve the environment because Dependency A version 1.0 needs an old version of Dependency C, while Dependency B version 2.7 needs a newer version. 

In this case, if we changed our package's `DESCRIPTION` and `meta.yaml ` file to be:

```
Dependency A version >= 1.0
Dependency B version >= 2.5
```

The conda build will be able to resolve. This is a simplified version of a what are more often complex dependency structures, but it is an important concept in conda package building that will inevitably arise as a package's dependencies become more specific.

To check on the versions of packages that are available in a Conda channel, use the command:

```
conda search $dependency
```

Replace $dependency with the name of package you would like to investigate. There are more optional commands for this function which can be found [here](https://docs.conda.io/projects/conda/en/latest/commands/search.html)

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