#!/usr/bin/env bash
mkdir data
scp helix:/data/CCBR_Pipeliner/db/PipeDB/Indices/GTFs/hg38/gencode.v48.primary_assembly.annotation.gtf ./data
scp helix:/data/CCBR_Pipeliner/db/PipeDB/Indices/hg38_basic/Chromsomes/chrom.sizes ./data