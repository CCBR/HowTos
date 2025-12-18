#!/usr/bin/env python3
""" Extract promoter regions around TSS for protein-coding genes from GTF files.

This script processes Gene Transfer Format (GTF) files to identify protein-coding genes
and extract their promoter regions around the Transcription Start Sites (TSS). The 
output is generated in BED format for downstream analysis.

Features:
- Filters for protein-coding genes only
- Strand-aware TSS identification and promoter region calculation
- Outputs standard 6-column BED format

Usage:
    python extract_promoters.py --gtf input.gtf.gz --out promoters.bed

Arguments:
    --gtf    Path to input GTF file (supports gzipped files)
    --out    Path to output BED file

Examples:
    # Basic usage with gzipped GTF
    python extract_promoters.py --gtf gencode.v45.annotation.gtf.gz --out promoters.bed
    
    # Using with uncompressed GTF
    python extract_promoters.py --gtf annotation.gtf --out promoter_regions.bed

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

# Constants
UPSTREAM_DISTANCE = 2000
DOWNSTREAM_DISTANCE = 200
PROTEIN_CODING_TYPE = "protein_coding"

def extract_feature_attribute(attribute_str):
    """Parse GTF attribute string into a dictionary of key-value pairs.
    
    Processes the 9th column (attributes) of GTF format lines, which contains
    semicolon-separated key-value pairs. Each pair is formatted as 'key "value"'.
    
    Args:
        attribute_str (str): The attribute string from GTF file (9th column)
                           Example: 'gene_id "ENSG00000186092"; gene_name "OR4F5"; gene_type "protein_coding";'
    
    Returns:
        dict: Dictionary mapping attribute names to their values (with quotes removed)
              Example: {'gene_id': 'ENSG00000186092', 'gene_name': 'OR4F5', 'gene_type': 'protein_coding'}
    
    Note:
        Assumes standard GTF format where attributes are space-separated key-value pairs
        with values enclosed in double quotes.
    """
    return { attr.strip().split(" ")[0]: attr.strip().split(" ")[1].strip('"')
             for attr in attribute_str.strip(";").split(";")
            }


def extract_genes(gtf_file, gene_type_filter=PROTEIN_CODING_TYPE):
    """
    Extract gene information from a GTF file and yield gene details including TSS coordinates.

    This function parses a GTF format file and extracts genes matching the specified gene type.
    For each matching gene, it calculates the Transcription Start Site (TSS) based on the strand
    orientation and yields relevant gene information.

    Args:
        gtf_file: An iterable file object containing GTF format data. Each line should be a
            tab-separated string following GTF specifications.
        gene_type_filter: A string specifying the type of genes to extract. Defaults to
            PROTEIN_CODING_TYPE. Only genes with a matching 'gene_type' attribute will be yielded.

    Yields:
        tuple: A 5-element tuple containing:
            - chrom (str): Chromosome name
            - tss (int): Transcription Start Site coordinate
            - strand (str): Strand orientation ('+' or '-')
            - gene_name (str): Name of the gene
            - gene_id (str): Unique gene identifier

    Raises:
        ValueError: If an unknown strand value (not '+' or '-') is encountered in the GTF file.

    Note:
        - Only processes lines with exactly 9 tab-separated fields
        - Only considers features marked as 'gene'
        - TSS is determined by the start position for '+' strand genes and end position for '-' strand genes
        - Requires extract_feature_attribute() function to parse GTF attributes
    """
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
                attr_dict = extract_feature_attribute(attribute)
                if attr_dict["gene_type"] == gene_type_filter:
                    if strand == "+":
                        tss = int(start)
                    elif strand == "-":
                        tss = int(end)
                    else:
                        raise ValueError(f"Unknown strand: {strand}")

                    yield chrom, tss, strand, attr_dict["gene_name"], attr_dict["gene_id"]


def parse_arguments():
    """Parse command line arguments.
    
    Returns:
        argparse.Namespace: Parsed arguments containing gtf and out file paths
    """
    parser = argparse.ArgumentParser(
        description="Extract promoter regions around TSS for protein-coding genes from GTF files"
    )
    parser.add_argument(
        "--gtf", 
        required=True, 
        help="Path to input GTF file"
    )
    parser.add_argument(
        "--out", 
        required=True, 
        help="Path to output BED file"
    )
    return parser.parse_args()


def main():
    """Main function to extract promoter regions from GTF file."""
    args = parse_arguments()

    # Parse GTF file and collect protein-coding genes
    
    with open(args.gtf, "rt") as gtf_file:
        genes = extract_genes(gtf_file)

        # Write BED file with promoter regions
        with open(args.out, "w") as bed_file:
            for chrom, tss, strand, gene_name, gene_id in genes:
                # Calculate promoter region based on strand
                if strand == "-":
                    start = tss - DOWNSTREAM_DISTANCE
                    end = tss + UPSTREAM_DISTANCE
                else:
                    start = tss - UPSTREAM_DISTANCE
                    end = tss + DOWNSTREAM_DISTANCE
                
                # Skip regions that would have negative coordinates
                if start <= 0:
                    continue
                
                # Create BED format region name
                # Only include regular chromosomes
                if chrom.startswith("chr"):
                    chrom = chrom
                    region_name = f"{chrom}:{start}-{end}|{gene_id}|{gene_name}"
                    
                    # Write BED line
                    bed_line = "\t".join([
                        chrom,
                        str(start),
                        str(end),
                        region_name,
                        ".",  # Score
                        strand
                    ])
                    bed_file.write(f"{bed_line}\n")


if __name__ == "__main__":
    main()
