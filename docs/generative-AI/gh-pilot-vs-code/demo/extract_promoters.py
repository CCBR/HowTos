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
                # TODO: move this line to a separate function
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
                    # TODO: why yield instead of return?
                    yield chrom, tss, strand, attr_dict["gene_name"], attr_dict[
                        "gene_id"
                    ]


def main():
    parser = argparse.ArgumentParser(
        description="Extract promoter regions around TSS for protein-coding genes from GTF files"
    )
    parser.add_argument("--gtf", required=True, help="Path to input GTF file")
    parser.add_argument("--out", required=True, help="Path to output BED file")
    args = parser.parse_args()

    # Open GTF file
    # TODO: handle gzipped gtf files
    with open(args.gtf, "r") as gtf_file:

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

                # TODO: handle regions that would have negative coordinates

                # Create BED format region name: chr:start-end|gene_id|gene_name
                region_name = f"{chrom}:{start}-{end}|{gene_id}|{gene_name}"

                # Write BED format: chr, start, end, name, score, strand
                bed_file.write(f"{chrom}\t{start}\t{end}\t{region_name}\t0\t{strand}\n")


if __name__ == "__main__":
    main()
