#!/bin/bash
echo "# A) GTF - data/chr21.gtf"
echo "# B) LINES CONTAINING gene / GENE LINES: \
$(grep 'gene' data/chr21.gtf | wc -l) / \
$(awk -F'\t' '$3=="gene"' data/chr21.gtf | wc -l)"
echo "# C) THIRD KEY IN COLUMN 9: "
awk -F'\t' '{print $9}' data/chr21.gtf | awk -F';' '{print $3}' | sed 's/"[^"]*"//g' | sort | uniq -c
