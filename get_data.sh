#!/bin/bash
# retrieves file from url, decompresses, and keeps only lines beginning with 21.
# outputs results to a .gtf file that now contains only chr21 data.
curl -s \
https://ftp.ensembl.org/pub/release-113/gtf/homo_sapiens/Homo_sapiens.GRCh38.113.gtf.gz \
| gzip -dc | grep "^21" > data/chr21.gtf
