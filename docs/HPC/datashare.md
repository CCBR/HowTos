# Datashare on Helix

**Host data on helix that is publicly accessible through a URL**

## Setup

---

### Add data to Helix


To access Helix:

`ssh -Y username@helix.nih.gov`

The datashare folder is located at the path:

`/data/CCBR/datashare/`

Make a directory in the datashare folder, for example `mydata`

Now you can transfer your data to the new directory. One method is to use scp to copy data from your local machine to Helix. Here is an example of using scp from a local directory where the data is copy that data to Helix:

`scp file.txt username@helix.nih.gov:/data/CCBR/datashare/mydata/`

To copy multiple directories recursively, you can also include the -r command with scp and run that from the top level directory:

`scp -r data_folders/ username@helix.nih.gov:/data/CCBR/datashare/mydata/`

---

### Create public permissions for data on Helix


When the data has been successully copied to Helix, we need to open the permissions.

We can follow the instructions listed under the file `technicalnotes` in the datashare folder:



"""

How to share with UCSC  ( or just make avalable on the internet via wget/curl/http )

go to this directory : pwd= /data/CCBR/datashare
then make a directory with a good name like "MNase" in the example here ( don't use "MNase" , it's already used )

./setfacl.sh directory    # run this program on your directory ( from /data/CCBR/datashare )

Set chmod uog+r * on files for the directory
This sets world read permisson.  Be careful, don't put a real patient's bam file out there ( beware of patient HIPPA privacy ).

Then check with ( for example directory "MNase" ) ...

getfacl MNase/*
getfacl MNase/* | grep webcpu

Example on how to access:
wget http://hpc.nih.gov/~CCBR/MNase/GC-OHT-2D.bam.sorted.bam.new.bw
Test it out, see if you can download a file using wget or curl or firefox.

If setting up for UCSC browser, then we want a url pointing to this directory ("MNase")
like this http://hpc.nih.gov/~CCBR/MNase/filename

To make a link for UCSC
make a file that looks like this:

________start file_________
track type=bigWig name="samp1" description="GSM2184318" bigDataUrl=http://hpc.nih.gov/~CCBR/MNase/samp1.bw
track type=bigWig name="samp2" description="GSM2184319" bigDataUrl=http://hpc.nih.gov/~CCBR/MNase/samp2.bw
...
... for each sample ( bigwig, bam, bigbed, etc ) ...
...
________end file_________

Give it a good name , like "ccbr9999.uscslinks.txt"

Remember to run the chmod uog+r * and setfacl  again to make the new file world wide web readable.

The link to paste into  UCSC custom tracks page is
http://hpc.nih.gov/~CCBR/MNase/ccbr9999.uscslinks.txt

Custom tracks is available in UCSC browser via the links on the top of the browse page.

A ( still possibly working ) paste it link is :
http://hpc.nih.gov/~CCBR/MNase/may18.mm9.ucsclinks.txt

yay! it works.

"""