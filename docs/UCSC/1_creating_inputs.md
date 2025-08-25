## Generating Inputs
In order to use the genomic broswer features, sample files must be created.

### Individual sample files
For individual samples, where peak density is to be observed, bigwig formatted files must be generated. If using the CCBR pipelines these are automatically generated as outputs of the pipeline (`WORKDIR/results/bigwig`). In many cases, scaling or normalization of bigwig is required to visualize multiple samples in comparison with each other. See various [deeptools](https://deeptools.readthedocs.io/en/develop/content/tools/bamCompare.html?highlight=normalizeUsing#read-coverage-normalization-options) options for details/ideas. If not using CCBR pipelines, example code is provided below for the file generation.
```
modue load ucsc
        
fragments_bed="/path/to/sample1.fragments.bed"
bw="/path/to/sample1.bigwig"
genome_len="numeric_genome_length"
bg="/path/to/sample1.bedgraph"
bw="/path/to/sample2.bigwig"

# if using a spike-in scale, the scaling factor should be applied
# while not required, it is recommended for CUT&RUN experiements
spikein_scale="spike_in_value"

# create bed file
bedtools genomecov -bg -scale $spikein_scale -i $fragments_bed -g $genome_len > $bg

# create bigwig file
bedGraphToBigWig $bg $genome_len $bw
```

### Contrasts between samples
For contrasts, where peak differences are to be observed, bigbed formatted files must be generated. If using the CCBR/CARLISLE pipeline these are automatically generated as outputs of the pipeline (WORKDIR/results/peaks/contrasts/contrast_id/). If not using this pipeline, example code is provided below for the file generation.
```
module load ucsc

bed="/path/to/sample1_vs_sample2_fragmentsbased_diffresults.bed"
bigbed="/path/to/output/sample1_vs_sample2_fragmentsbased_diffresults.bigbed"
genome_len="numeric_genome_length"

# create bigbed file
bedToBigBed -type=bed9 $bed $genome_len $bigbed
```

## Sharing data
For all sample types, data must be stored on a shared directory. It is recommended that symlnks be created from the source location to this shared directory to ensure that minial disc space is being used. Example code for creating symlinks is provided below.

### single sample
```
# single sample
## set source file location
source_loc="/WORKDIR/results/bigwig/sample1.bigwig "

## set destination link location
link_loc="/SHAREDDIR/bigwig/sample1.bigwig"

## create hard links
ln $source_loc $link_loc
```

### contrast sample
```
# contrast
## set source file location
source_loc="WORKDIR/results/peaks/contrasts/sample1_vs_sample2/sample1_vs_sample2_fragmentsbased_diffresults.bigbed "

## set destination link location
link_loc="/SHAREDDIR/bigbed/sample1_vs_sample2.bigbed"

## create hard links
ln $source_loc $link_loc
```

Once the links have been generated, the data folder must be open to read and write access. 
```
## set destination link location
link_loc="/SHAREDDIR/bigbed/"

# open dir
chmod -R a+rX $link_loc
```