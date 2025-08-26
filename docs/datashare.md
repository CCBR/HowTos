---
title: Datashare
description: "Host data on helix & biowulf with"
author: "[Ned Cauley](https://github.com/escauley)"
---

Host data on [Helix](https://hpc.nih.gov/systems/) or [Biowulf](https://hpc.nih.gov/systems/), that is publicly accessible through a URL

## Setup

### Access Login

```
# Helix
ssh -Y username@helix.nih.gov

# Biowulf
ssh -Y username@biowulf.nih.gov
```

Create a new dir (`tutorial`) in the datashare path:

```
cd /data/CCBR/datashare/
mkdir tutorial
```

## Processing

### Make a directory in the datashare folder

**NOTE: For all steps below, an example is shown for Helix, but the same process is applicable for Biowulf, after changing the `helix.nih.gov` to `biowulf.nih.gov`**

Now you can transfer your data to the new directory. One method is to use `scp` to copy data from your local machine to Helix. 

Here is an example of using `scp` to copy the file `file.txt` from a local directory to Helix. 

```
scp /data/$USER/file.txt username@helix.nih.gov:/data/CCBR/datashare/tutorial/
```

To copy multiple directories recursively, you can also include the `-r` command with `scp` and from the top level directory:

```
scp -r /data/$USER/ username@helix.nih.gov:/data/CCBR/datashare/tutorial/
```

### Create public permissions for data

When the data has been successully copied, we need to open the permissions. 

**NOTE: This will give open access to anyone with the link. Ensure this is appropriate for the data type**

```
# cd to the shared dir
cd /data/CCBR/datashare/

# run CHMOD, twice
chmod -R 777 tutorial
chmod -R 777 tutorial/*

# run SETFACL
setfacl -m u:webcpu:r-x tutorial/*
```

## Public Access

**NOTE: You must be logged into [HPC](https://hpc.nih.gov/) in order to access these files from a web browser.**

Files will be available for access through a browser, via tools like `wget` and `UCSC genome track browser` via the following format:

http://hpc.nih.gov/~CCBR/tutorial/file.txt

For more information and a tutorial for creating [UCSC tracks](https://ccbr.github.io/HowTos/UCSC/overview/), visit the [CCBR HowTo Page](https://ccbr.github.io/HowTos/).