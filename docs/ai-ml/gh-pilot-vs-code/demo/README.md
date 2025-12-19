# Extract Gene Promoters to BED Format

```sh
# download data
# note: you will need to be on the VPN
bash setup.sh

# run the extraction script
python extract_promoters.py --gtf ./data/gencode.v48.primary_assembly.annotation.gtf --out hg38-48_promoters.bed
```
