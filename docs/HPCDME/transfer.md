### Background

Rawdata or Project folders from Biowulf can be parked at a secure location after the analysis has reached a endpoint. Traditionally, CCBR analysts had access to the GridFTP Globus Archive for doing this. But, this Globus Archive has been running past 95% full lately.

This document outlines how a projects folder can be directly parked on HPCDME as a single "tar.gz" ball. It is assumed that HPC DME API CLUs are already setup as per [these](https://ccbr.github.io/HowTos/HPCDME/setup/) instructions.

Here are the steps:

#### Create tarball

Once you have a list of files that you want to include in the tarball, create the tarball. This may take a while and should be submitted as a slurm job.

```bash
% cd /data/CCBR/projects
% du -hs /data/CCBR/projects/ccbr796
440G	/data/CCBR/projects/ccbr796
% echo "tar czvf ccbr796.tar.gz /data/CCBR/projects/ccbr796" > do_tar_gz
% swarm -f do_tar_gz --partition=ccr,norm --time=24:00:00 -t 2 -g 100
41985209
```

#### Create filelist

Sometime you just want to know what files are in the tarball. Hence, it is important to upload a filelist along with the tarball.

```bash
% tar tzvf ccbr796.tar.gz > ccbr796.tar.gz.filelist
```

#### Create Project

If the Project collection does not exist in HPCDME (verify using the web interface), then you may need to create it.

```bash
% cd /data/kopardevn/SandBox/parkit
% bash create_empty_project_collection.sh /CCBR_Archive/GRIDFTP/Project_CCBR-796 CCBR-796 CCBR-796
{
    "metadataEntries": [
        {
         "attribute": "collection_type",
         "value": "Project"
        },
        {
         "attribute": "project_start_date",
         "value": "20220616",
         "dateFormat": "yyyyMMdd"
        },
        {
         "attribute": "access",
         "value": "Open Access"
        },
        {
         "attribute": "method",
         "value": "NGS"
        },
        {
         "attribute": "origin",
         "value": "CCBR"
        },
        {
         "attribute": "project_affiliation",
         "value": "CCBR"
        },
        {
         "attribute": "project_description",
         "value": "CCBR-796"
        },
        {
         "attribute": "project_status",
         "value": "Completed"
        },
        {
         "attribute": "retention_years",
         "value": "7"
        },
        {
         "attribute": "project_title",
         "value": "CCBR-796"
        },
        {
         "attribute": "summary_of_samples",
         "value": "Unknown"
        },
        {
         "attribute": "organism",
         "value": "Unknown"
        }
    ]
}
dm_register_collection /dev/shm/Project_CCBR-796.metadata.json /CCBR_Archive/GRIDFTP/Project_CCBR-796
```

> **Error**: Have encountered this error message:
> ```bash
> Error during registration, HTTP_CODE: 503
> Cannot find the response message file
> collection-registration-response-message.json.tmp
> ```
> 503 error means that the API is down!

#### Create Analysis

If the Analysis collection does not exist in HPCDME (verify using the web interface) under the Project collection, then you may need to create it.

```bash
% cd /data/kopardevn/SandBox/parkit
% bash create_empty_analysis_collection.sh /CCBR_Archive/GRIDFTP/Project_CCBR-796/Analysis
dm_register_collection /dev/shm/Analysis.metadata.json /CCBR_Archive/GRIDFTP/Project_CCBR-796/Analysis
```

Done! Now you have a location ready for the the tarball to be parked.

#### Create metadata

Using `meta` script from [`pyrkit`](https://github.com/CCBR/pyrkit), we can then generate the required `.metadata.json` file for the tarball. Analysis collection `/CCBR_Archive/GRIDFTP/Project_CCBR-796/Analysis` should already exist in the HPCDME vault.

```bash
% echo "/data/kopardevn/SandBox/pyrkit/src/meta combined --input /data/CCBR/projects/ccbr796.tar.gz --output /CCBR_Archive/GRIDFTP/Project_CCBR-796/Analysis" > do_get_metadata
% swarm -f do_get_metadata --partition=ccr,norm --time=24:00:00 -t 2 -g 100
```

If the file is large (100s of GB), then this may take a while as the md5sum of the file is being calculated. Hence, this should be submitted to the slurm. 

Metadata also needs to be created for the filelist file. These files are generally small (few MBs) and the following command can be directly run on an interactive node.

```bash
% /data/kopardevn/SandBox/pyrkit/src/meta combined --input /data/CCBR/projects/ccbr796.tar.gz.filelist --output /CCBR_Archive/GRIDFTP/Project_CCBR-796/Analysis
```

The above command, when run sucessfully, will create `/data/CCBR/projects/ccbr796.tar.gz.filelist.metadata.json`

#### Transfer

`dm_register_dataobject` cannot be used for large files (>10GB), but it can be replaced by `dm_register_dataobject_multipart`

```bash
% dm_register_dataobject_multipart /data/CCBR/projects/ccbr796.tar.gz.metadata.json /CCBR_Archive/GRIDFTP/Project_CCBR-796/Analysis/ccbr796.tar.gz /data/CCBR/projects/ccbr796.tar.gz
Reading properties from /data/kopardevn/SandBox/HPC_DME_APIs/utils/hpcdme.properties
Registering file: /data/CCBR/projects/ccbr796.tar.gz
Destination archive path: /CCBR_Archive/GRIDFTP/Project_CCBR-796/Analysis/ccbr796.tar.gz
Cmd process Completed
Jun 16, 2022 10:55:25 AM org.springframework.shell.core.AbstractShell handleExecutionResult
INFO: CLI_SUCCESS
```

Depending on the size of the file, this step can be done in a reasonable amount of time (<1hr) and can be run in an interactive node.

Remember, the filelist file also needs to be registered separately like this:

```bash
% dm_register_dataobject /data/CCBR/projects/ccbr796.tar.gz.filelist.metadata.json /CCBR_Archive/GRIDFTP/Project_CCBR-796/Analysis/ccbr796.tar.gz.filelist /data/CCBR/projects/ccbr796.tar.gz.filelist
```

As filelist files are smaller (few MBs), we can run `dm_register_dataobject` in place of `dm_register_dataobject_multipart`.

#### Cleanup

Once the tarball is successfully transferred over the HPCDME, it can be deleted from the local filesystem.

```bash
% rm -f /data/CCBR/projects/ccbr796.tar.gz
```

The contents of the local analysis folder can also be deleted.

```bash
% cd /data/CCBR/projects/ccbr796 && rm -rf *
```

A note can be added to the recently emptied folder stating where the contents are currently parked.

```bash
% cd /data/CCBR/projects/ccbr796
% echo "This folder was converted to a tarball (tar.gz) and pushed to HPCDME. Its new location is \`/CCBR_Archive/GRIDFTP/Project_CCBR-796/Analysis/ccbr796.tar.gz\` in HPCDME" > README.md
```

Done!

> **NOTE FOR LARGE FILES**: It is recommended by HPCDME staff that files to be transferred should not be too large (1TB or smaller). Hence, if the file to be transferred is larger than 1TB, it should be split into 1TB-size chunks and upload those.
> Splitting can be done like this:
> ```bash
> split -b 1T ccbr796.tar.gz "ccbr796.tar.gz.part_"
> ```
> Metadata needs to be individidually created for each of the parts, namely, `ccbr796.tar.gz.part_aa`, `ccbr796.tar.gz.part_ab`, etc 
> ```bash
> % /data/kopardevn/SandBox/pyrkit/src/meta combined --input /data/CCBR/projects/ccbr796.tar.gz.part_aa --output /CCBR_Archive/GRIDFTP/Project_CCBR-796/Analysis
> % /data/kopardevn/SandBox/pyrkit/src/meta combined --input /data/CCBR/projects/ccbr796.tar.gz.part_ab --output /CCBR_Archive/GRIDFTP/Project_CCBR-796/Analysis
> ...
> ```
> Next each 1TB part can be registered like so:
> ```bash
> % dm_register_dataobject_multipart /data/CCBR/projects/ccbr796.tar.gz.part_aa.metadata.json /CCBR_Archive/GRIDFTP/Project_CCBR-796/Analysis/ccbr796.tar.gz.part_aa /data/CCBR/projects/ccbr796.tar.gz.part_aa
> % dm_register_dataobject_multipart /data/CCBR/projects/ccbr796.tar.gz.part_ab.metadata.json /CCBR_Archive/GRIDFTP/Project_CCBR-796/Analysis/ccbr796.tar.gz.part_ab /data/CCBR/projects/ccbr796.tar.gz.part_ab
> ...
> ```
> Once these files are downloaded then can be joined together using the `cat` command before ungzipping/untaring.
> ```bash 
> % cat ccbr796.tar.gz.part_* > ccbr796.tar.gz
> ``` 