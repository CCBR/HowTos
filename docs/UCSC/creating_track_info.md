# Generating Track information

## Single samples
It's recommended to create a text file of all sample track information to ease in editing and submission to the UCSC browser website. A single line of code is needed for each sample which will provide the track location, sample name, description of the sample, whether to autoscale the samples, max height of the samples, view limits, and color. An example is provided below.

```
track type=bigWig bigDataUrl=https://hpc.nih.gov/~CCBR/ccbr1155/${dir_loc}/bigwig/${complete_sample_id}.bigwig name=${sample_id} description=${sample_id} visibility=full autoScale=off maxHeightPixels=128:30:1 viewLimits=1:120 color=65,105,225
```

Users may find it helpful to create a single script which would create this text file for all samples. An example of this is listed below, which assumes that input files were generated using the CARLISLE pipeline. It can be edited to adapt to other output files, as needed.

Generally, each "track" line should have at least the following key value pairs:
- name : label for the track
- description : defines the center lable displayed
- type : BAM, BED, bigBed, bigWig, etc.
- bigDataUrl : URL of the data file
- for other options see [here](https://genome.ucsc.edu/goldenPath/help/hgTracksHelp.html)

## Inputs
- samples_list.txt: a single column text file with sampleID's
- track_dir: path to the linked files
- track_output: path to output file
- peak_list: all peak types to be included
- method_list: what method to be included
- dedupe_list: type of duplication to be included

```
# input arguments
sample_list_input=/"path/to/samples.txt"
track_dir="/path/to/shared/dir/"
track_output="/path/to/output/file/tracks.txt
peak_list=("norm.relaxed.bed" "narrowPeak" "broadGo_peaks.bed" "narrowGo_peaks.bed")
method_list=("fragmentsbased")
dedup_list=("dedup")

# read sample file
IFS=$'\n' read -d '' -r -a sample_list < $sample_list_input

run_sample_tracks (){
    sample_id=$1
    dedup_id=$2
    
    # sample name
    # eg siNC_H3K27Ac_1.dedup.bigwig
    complete_sample_id="${sample_id}.${dedup_id}"

    # set link location
    link_loc="${track_dir}/bigwig/${complete_sample_id}.bigwig"

    # echo track info
    echo "track type=bigWig bigDataUrl=https://hpc.nih.gov/~CCBR/ccbr1155/${dir_loc}/bigwig/${complete_sample_id}.bigwig name=${sample_id} description=${sample_id} visibility=full autoScale=off maxHeightPixels=128:30:1 viewLimits=1:120 color=65,105,225" >> $track_output
}

# iterate through samples
# at the sample level only DEDUP matters
for sample_id in ${sample_list[@]}; do
    for dedup_id in ${dedup_list[@]}; do
        run_sample_tracks $sample_id $dedup_id
    done
done
```

# Contrast samples
It's recommended to create a text file of all sample track information to ease in editing and submission to the UCSC browser website. A single line of code is needed for each contrast which will provide the track location, contrast name, file type, and whether to color the sample. An example is provided below.

```
track name=${sample_id}_${peak_type} bigDataUrl=https://hpc.nih.gov/~CCBR/ccbr1155/${dir_loc}/bigbed/${complete_sample_id}_fragmentsbased_diffresults.bigbed type=bigBed itemRgb=On
```

Users may find it helpful to create a single script which would create this text file for all contrasts. An example of this is listed below, which assumes that input files were generated using the CARLISLE pipeline. It can be edited to adapt to other output files, as needed.

## Inputs
- samples_list.txt: a single column text file with sampleID's
- track_dir: path to the linked files
- track_output: path to output file
- peak_list: all peak types to be included
- method_list: what method to be included
- dedupe_list: type of duplication to be included

```
# input arguments
sample_list_input=/"path/to/samples.txt"
track_dir="/path/to/shared/dir/"
track_output="/path/to/output/file/tracks.txt
peak_list=("norm.relaxed.bed" "narrowPeak" "broadGo_peaks.bed" "narrowGo_peaks.bed")
method_list=("fragmentsbased")
dedup_list=("dedup")

# read sample file
IFS=$'\n' read -d '' -r -a deg_list < $deg_list_input

run_comparison_tracks (){
    peak_type=$1
    method_type=$2
    dedup_type=$3
    sample_id=$4
    
    # sample name
    # eg siSmyd3_2m_Smyd3_0.25HCHO_500K_vs_siNC_2m_Smyd3_0.25HCHO_500K__no_dedup__norm.relaxed
    complete_sample_id="${sample_id}__${dedup_type}__${peak_type}"
    
    # set link location
    link_loc="${track_dir}/bigbed/${complete_sample_id}_${method_type}_diffresults.bigbed"

    # echo track info
    echo "track name=${sample_id}_${peak_type} bigDataUrl=https://hpc.nih.gov/~CCBR/ccbr1155/${dir_loc}/bigbed/${complete_sample_id}_fragmentsbased_diffresults.bigbed type=bigBed itemRgb=On" >> $track_info
}

# iterate through samples / peaks / methods / dedup
for sample_id in ${deg_list[@]}; do
    for peak_id in ${peak_list[@]}; do
        for method_id in ${method_list[@]}; do
            for dedup_id in ${dedup_list[@]}; do
                run_comparison_tracks $peak_id $method_id $dedup_id $sample_id
            done
        done
    done
done
```

# Other tips
Users can also change the colors of the tracks using standard HTML color features. Common colors used are provided below:
```
Red=205,92,92
Blue=65,105,225
Black=0,0,0
```