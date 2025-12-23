#!/usr/bin/env python3
"""Extract promoter regions around TSS for protein-coding genes from GTF files.

Extract promoter regions from GTF file and write out to BED format.
The promoter BED file can then be intersected with ATAC-seq peaks to identify
genes with open chromatin in their promoters.

Usage:
    python extract_promoters.py --gtf [gtf] --out [bed]

Arguments:
    --gtf    Path to input GTF file (supports gzipped files)
    --out    Path to output BED file

"""

import argparse
import gzip

# Constants
UPSTREAM_DISTANCE = 2000
DOWNSTREAM_DISTANCE = 200
PROTEIN_CODING_TYPE = "protein_coding"


def parse_gtf_attributes(attribute_string):
    """Parse GTF attribute string into a dictionary.

    Args:
        attribute_string: GTF attribute field (9th column) containing
                         key-value pairs like 'gene_id "ENSG00001"; gene_name "TP53"'

    Returns:
        dict: Dictionary mapping attribute names to their values

    Example:
        >>> parse_gtf_attributes('gene_id "ENSG00001"; gene_name "TP53"')
        {'gene_id': 'ENSG00001', 'gene_name': 'TP53'}
    """
    return {
        attr.strip().split(" ")[0]: attr.strip().split(" ")[1].strip('"')
        for attr in attribute_string.strip(";").split(";")
        if attr.strip()  # Skip empty strings
    }


def extract_genes(gtf_file, gene_type_filter=PROTEIN_CODING_TYPE):
    """
    Extract genes from a GTF file with optional filtering by gene type.
    This function parses a GTF (Gene Transfer Format) file and yields information
    about genes that match the specified gene type filter. For each matching gene,
    it calculates the Transcription Start Site (TSS) based on the strand orientation.
    Args:
        gtf_file: An iterable of GTF format lines (e.g., an open file object).
            Each line should be tab-separated with 9 fields: chrom, source, feature,
            start, end, score, strand, frame, and attributes.
        gene_type_filter (str, optional): The gene type to filter by. Defaults to
            PROTEIN_CODING_TYPE. Only genes matching this type will be yielded.
    Yields:
        tuple: A tuple containing:
            - chrom (str): Chromosome name
            - tss (int): Transcription Start Site position
                (start position for '+' strand, end position for '-' strand)
            - strand (str): Strand orientation ('+' or '-')
            - gene_name (str): Gene name from GTF attributes
            - gene_id (str): Gene ID from GTF attributes
    Raises:
        ValueError: If an unknown strand value (not '+' or '-') is encountered.
    Note:
        Only features with type "gene" are processed. Malformed lines with fewer
        than 9 tab-separated fields are skipped.
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
                # TODO: move this line to a separate function
                attr_dict = parse_gtf_attributes(attribute)
                if attr_dict["gene_type"] == gene_type_filter:
                    if strand == "+":
                        tss = int(start)
                    elif strand == "-":
                        tss = int(end)
                    else:
                        raise ValueError(f"Unknown strand: {strand}")
                    # TODO: why yield instead of return?
                    yield (
                        chrom,
                        tss,
                        strand,
                        attr_dict["gene_name"],
                        attr_dict["gene_id"],
                    )


def parse_arguments():
    """Parse command line arguments.

    Returns:
        argparse.Namespace: Parsed arguments containing gtf and out file paths
    """
    parser = argparse.ArgumentParser(
        description="Extract promoter regions around TSS for protein-coding genes from GTF files"
    )
    parser.add_argument("--gtf", required=True, help="Path to input GTF file")
    parser.add_argument("--out", required=True, help="Path to output BED file")
    return parser.parse_args()


def main():
    """Main function to extract promoter regions from GTF file."""
    args = parse_arguments()

    # Open GTF file
    if args.gtf.endswith(".gz"):
        open_func = gzip.open
    else:
        open_func = open

    with open_func(args.gtf, "rt") as gtf_file:
        with open(args.out, "w") as bed_file:
            # Extract protein-coding genes and write promoter regions
            for chrom, tss, strand, gene_name, gene_id in extract_genes(gtf_file):
                # Only include standard chromosomes
                if not chrom.startswith("chr"):
                    continue

                # Calculate promoter region based on strand
                if strand == "+":
                    # For positive strand: TSS - 2000 to TSS + 200
                    start = tss - UPSTREAM_DISTANCE
                    end = tss + DOWNSTREAM_DISTANCE
                else:  # strand == "-"
                    # For negative strand: TSS - 200 to TSS + 2000
                    start = tss - DOWNSTREAM_DISTANCE
                    end = tss + UPSTREAM_DISTANCE

                # Ensure start is not negative
                if start < 0:
                    start = 0

                # Create BED format region name: chr:start-end|gene_id|gene_name
                region_name = f"{chrom}:{start}-{end}|{gene_id}|{gene_name}"

                # Write BED format: chr, start, end, name, score, strand
                bed_file.write(f"{chrom}\t{start}\t{end}\t{region_name}\t0\t{strand}\n")


if __name__ == "__main__":
    main()
