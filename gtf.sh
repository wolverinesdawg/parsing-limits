#!/bin/bash
echo "# A) GTF - data/chr21.gtf"
echo "# B) LINES CONTAINING gene / GENE LINES: \
$(grep 'gene' data/chr21.gtf | wc -l) / \
$(awk -F'\t' '$3=="gene"' data/chr21.gtf | wc -l)"
