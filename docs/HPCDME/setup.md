### Background

[HPC_DME_APIs](https://github.com/CBIIT/HPC_DME_APIs/) provides command line utilities or CLUs to interface with HPCDME. This document describes some of the initial setup steps to get the CLUs working on [Biowulf](https://hpc.nih.gov/).

### Setup steps:

#### Clone repo:

The repo can be cloned at a location accessible to you:

```bash
cd /data/$USER/
git clone https://github.com/CBIIT/HPC_DME_APIs.git
```

#### Create dirs, log files needed for HPCMDE
```
mkdir -p /data/$USER/HPCDMELOG/tmp
touch /data/$USER/HPCDMELOG/tmp/hpc-cli.log
```


#### Copy properties template

`hpcdme.properties` is the file that all CLUs look into for various parameters like authentication password, file size limits, number of CPUs, etc. Make a copy of the template provided and prepare it for customization.

```bash
cd /data/$USER/HPC_DME_APIs/utils
cp hpcdme.properties-sample hpcdme.properties
```

#### Customize properties file

Some of the parameters in this file have become obsolete over the course of time and are commmented out. Change paths and default values, as needed

> Note: replace `$USER` with your actual username in the properties file. Bash variables will not be interpolated.

```bash
#HPC DME Server URL
#Production server settings
hpc.server.url=https://hpcdmeapi.nci.nih.gov:8080
hpc.ssl.keystore.path=hpc-client/keystore/keystore-prod.jks
#hpc.ssl.keystore.password=hpcdmncif
hpc.ssl.keystore.password=changeit

#UAT server settings
#hpc.server.url=https://fr-s-hpcdm-uat-p.ncifcrf.gov:7738/hpc-server
#hpc.ssl.keystore.path=hpc-client/keystore/keystore-uat.jks
#hpc.ssl.keystore.password=hpc-server-store-pwd

#Proxy Settings
hpc.server.proxy.url=10.1.200.240
hpc.server.proxy.port=3128

hpc.user=$USER

#Globus settings
#default globus endpoint to be used in registration and download
hpc.globus.user=$USER
hpc.default.globus.endpoint=ea6c8fd6-4810-11e8-8ee3-0a6d4e044368

#Log files directory
hpc.error-log.dir=/data/$USER/HPCDMELOG/tmp

###HPC CLI Logging START####
#ERROR, WARN, INFO, DEBUG
hpc.log.level=ERROR
hpc.log.file=/data/$USER/HPCDMELOG/tmp/hpc-cli.log
###HPC CLI Logging END####

#############################################################################
# Please use caution changing following properties. They don't change usually
#############################################################################
#hpc.collection.service=collection
#hpc.dataobject.service=dataObject
#Log files directory
#hpc.error-log.dir=.

#Number of thread to run data file import from a CSV file
hpc.job.thread.count=1

upload.buffer.size=10000000

#Retry count and backoff period for registerFromFilePath (Fixed backoff)
hpc.retry.max.attempts=3
#hpc.retry.backoff.period=5000

#Multi-part upload thread pool, threshold and part size configuration
#hpc.multipart.threadpoolsize=10
#hpc.multipart.threshold=1074790400
#hpc.multipart.chunksize=1073741824

#globus.nexus.url=nexus.api.globusonline.org
#globus.url=www.globusonline.org

#HPC DME Login token file location
hpc.login.token=tokens/hpcdme-auth.txt

#Globus Login token file location
#hpc.globus.login.token=tokens/globus-auth.txt
#validate.md5.checksum=false

# JAR version
#hpc.jar.version=hpc-cli-1.4.0.jar
```

> **NOTE**: The current java version used is:
> ```bash
java -version
> openjdk version "1.8.0_181"
> OpenJDK Runtime Environment (build 1.8.0_181-b13)
> OpenJDK 64-Bit Server VM (build 25.181-b13, mixed mode)
> ```

#### Edit `~/.bashrc`

Add the CLUs to PATH by adding the following to `~/.bashrc` file

```bash
# export environment variable HPC_DM_UTILS pointing to directory where 
# HPC DME client utilities are, then source functions script in there 
export HPC_DM_UTILS=/data/$USER/HPC_DME_APIs/utils
source $HPC_DM_UTILS/functions
```

Next, source it

```bash
source ~/.bashrc
``` 

#### Generate token

Now, you are all set to generate a token. This prevents from re-entering your password everytime.

```bash
dm_generate_token
```

If the token generation takes longer than 45 seconds, check the connection:
```bash
ping hpcdmeapi.nci.nih.gov
```

If the connection responds, try to export the following proxy, and then re-run the `dm_generate_tokens command`:
```bash
export https_proxy=http://dtn01-e0:3128
```

Done! You are now all set to use CLUs.

### References and Links

  *  [HPC_DME_APIs repo](https://github.com/CBIIT/HPC_DME_APIs/)
  *  [User guides](https://github.com/CBIIT/HPC_DME_APIs/tree/master/doc/guides)
  *  [Wiki pages](https://wiki.nci.nih.gov/display/DMEdoc/Getting+Started+with+DME+CLU)
  *  [Yuri Dinh](mailto:yuri.dinh@nih.gov)
