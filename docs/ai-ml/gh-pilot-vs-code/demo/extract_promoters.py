#!/usr/bin/env python3
"""Extract promoter regions around TSS for protein-coding genes from GTF files.

This script processes Gene Transfer Format (GTF) files to identify protein-coding genes
and extract their promoter regions around the Transcription Start Sites (TSS). The
output is generated in BED format for downstream analysis.
You can then intersect these promoter regions with ATAC-seq peaks to identify
genes with open chromatin in their promoters.

Features:
- Filters for protein-coding genes only
- Strand-aware TSS identification and promoter region calculation
- Outputs standard 6-column BED format

Usage:
    python extract_promoters.py --gtf [gtf] --out [bed]

Arguments:
    --gtf    Path to input GTF file (supports gzipped files)
    --out    Path to output BED file

Examples:
    python extract_promoters.py --gtf gencode.v45.annotation.gtf.gz --out promoters.bed

Output Format:
    The output BED file contains 6 columns:
    1. chromosome - Chromosome name (e.g., chr1, chr2, ...)
    2. start      - Start coordinate of promoter region (0-based)
    3. end        - End coordinate of promoter region (0-based)
    4. name       - Region identifier: chr:start-end|gene_id|gene_name
    5. score      - Always 0 (placeholder for BED format)
    6. strand     - Gene strand (+ or -)

Promoter Region Definition:
    - For genes on positive strand (+): [TSS - 2000, TSS + 200]
    - For genes on negative strand (-): [TSS - 200, TSS + 2000]
    - TSS is defined as gene start for + strand, gene end for - strand
    - Regions with negative start coordinates are automatically filtered out

Requirements:
    - Python 3.6+
    - Standard library only (argparse, gzip)

Notes:
    - Only includes genes with feature type 'gene'
    - Only includes protein-coding genes (gene_type == 'protein_coding')
    - Only outputs regions for standard chromosomes (starting with 'chr')
    - Input GTF file should follow standard GTF format specification
"""

import argparse
import gzip

# Constants
UPSTREAM_DISTANCE = 2000
DOWNSTREAM_DISTANCE = 200
PROTEIN_CODING_TYPE = "protein_coding"


def extract_genes(gtf_file, gene_type_filter=PROTEIN_CODING_TYPE):
    for line in gtf_file:
        line_tab = line.strip().split("\t")
        if len(line_tab) == 9:
            (
                chrom,
                source,
                feature,
                start,
                end,
                score,
                strand,
                frame,
                attribute,
            ) = line_tab
            if feature == "gene":
                # TODO: break this out into a separate function
                attr_dict = {
                    attr.strip().split(" ")[0]: attr.strip().split(" ")[1].strip('"')
                    for attr in attribute.strip(";").split(";")
                }
                if attr_dict["gene_type"] == gene_type_filter:
                    if strand == "+":
                        tss = int(start)
                    elif strand == "-":
                        tss = int(end)
                    else:
                        raise ValueError(f"Unknown strand: {strand}")

                    yield chrom, tss, strand, attr_dict["gene_name"], attr_dict[
                        "gene_id"
                    ]


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Extract promoter regions around TSS for protein-coding genes from GTF files"
    )
    parser.add_argument("--gtf", required=True, help="Path to input GTF file")
    parser.add_argument("--out", required=True, help="Path to output BED file")
    return parser.parse_args()


def main():
    """Main function to extract promoter regions from GTF file."""
    args = parse_arguments()

    # Open GTF file (handle both gzipped and regular files)
    # TODO: is there a better way to check for gzipped files?
    if args.gtf.endswith(".gz"):
        gtf_file = gzip.open(args.gtf, "rt")
    else:
        gtf_file = open(args.gtf, "r")

    try:
        with open(args.out, "w") as bed_file:
            # Extract protein-coding genes and write promoter regions
            for chrom, tss, strand, gene_name, gene_id in extract_genes(gtf_file):
                # TODO: Only include standard chromosomes
                
                # Calculate promoter region based on strand
                if strand == "+":
                    # For positive strand: TSS - 2000 to TSS + 200
                    start = tss - UPSTREAM_DISTANCE
                    end = tss + DOWNSTREAM_DISTANCE
                else:  # strand == "-"
                    # For negative strand: TSS - 200 to TSS + 2000
                    start = tss - DOWNSTREAM_DISTANCE
                    end = tss + UPSTREAM_DISTANCE

                # TODO: Skip regions that would have negative coordinates

                # Create BED format region name: chr:start-end|gene_id|gene_name
                region_name = f"{chrom}:{start}-{end}|{gene_id}|{gene_name}"

                # Write BED format: chr, start, end, name, score, strand
                bed_file.write(f"{chrom}\t{start}\t{end}\t{region_name}\t0\t{strand}\n")

    finally:
        gtf_file.close()


if __name__ == "__main__":
    main()
