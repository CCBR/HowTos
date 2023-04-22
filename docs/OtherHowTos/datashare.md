# Datashare on Helix

Host data on helix that is publicly accessible through a URL

## Setup

---

### Access Helix

```
ssh -Y username@helix.nih.gov
```

Create a new dir (`tutorial`) in the datashare path:

```
cd /data/CCBR/datashare/
mkdir tutorial
```

## Processing
---
### Make a directory in the datashare folder

Now you can transfer your data to the new directory. One method is to use `scp` to copy data from your local machine to Helix. 

Here is an example of using `scp` to copy the file `file.txt` from a local directory to Helix:

```
scp /data/$USER/file.txt username@helix.nih.gov:/data/CCBR/datashare/tutorial/
```

To copy multiple directories recursively, you can also include the `-r` command with `scp` and from the top level directory:

```
scp -r /data/$USER/ username@helix.nih.gov:/data/CCBR/datashare/tutorial/
````

### Create public permissions for data on Helix

When the data has been successully copied to Helix, we need to open the permissions. 

```
# CD to the shared dir
cd /data/CCBR/datashare/tutorial/

# run CHMOD
chmod uog+r *

# run SETFACL
setfacl -m u:webcpu:r-x *
```

## Public Access
---
Files will be available for access through a browser, via tools like `wget` and `UCSC genome track browser` via the following format:

http://hpc.nih.gov/~CCBR/tutorial/file.txt

For more information and a tutorial for creating [UCSC tracks](https://ccbr.github.io/HowTos/UCSC/overview/), visit the [CCBR HowTo Page](https://ccbr.github.io/HowTos/).
