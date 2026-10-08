# parsing-limits
BIOINF 575 homework2and3
## Findings
Without elminating things in quotes, the code returns blank spaces and other incorrect labels, 
likely from pulling from the wrong section due to syntax issues seeing the quotes. 
When eliminating the quotes, you get back actual Food Groups correctly. 
If you filter for a single letter, T here, you reduce the field it is pulling from and it 
changes the input to reflect you pulling from a subset.
Created gtf.sh for Part IV that parses data/chr21.gtf made in Part II to count different
aspects of the files, like gene lines, transcripts with tag values, etc.
