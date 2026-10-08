"""
compare_with_pandas.py - BIOINF 575 Homework 2

This script answers the same questions as your food.sh and gtf.sh, but with
pandas, a Python library that reads tables with a real file parser. You do not
need to know Python: read the comments to see what each step does, run the
script, and compare its output with your bash results.

How to run it (from your repository folder, with your own letter and your own
chromosome file):

    python3 compare_with_pandas.py c data/chr7.gtf > pandas_results.txt

If pandas is not installed:   pip install pandas   (or: conda install pandas)
"""

# "import" loads extra tools into Python.
# sys gives access to the words typed after the script name on the command line.
# pandas is the table library; "as pd" lets us write pd instead of pandas.
import sys
import pandas as pd

# sys.argv is the list of words on the command line:
#   sys.argv[0] is the script name, sys.argv[1] the letter, sys.argv[2] the GTF file.
# .lower() turns the letter into lower case, so "C" and "c" behave the same.
letter = sys.argv[1].lower()
gtf_file = sys.argv[2]


# =============================================================================
# PART 1 - Food.csv
# =============================================================================

# pd.read_csv reads a comma-separated file into a table (a "DataFrame").
# The first line of the file becomes the column names.
# Unlike cut, read_csv understands double quotes: a comma or a line break
# inside "..." stays part of the value. So every row of the table is exactly
# one food, however many lines its description takes in the file.
food = pd.read_csv("data/Food.csv")

# print() writes text to the output. These headers match your food.sh items.
print("# FOOD B) NUMBER OF FOODS")
# len(table) is the number of rows in the table, i.e. the number of foods.
print(len(food))

print("# FOOD C/D) TOP 5 FOOD GROUPS")
# food["food_group"] selects one column by its NAME (not by its position).
# .value_counts() counts how many times each distinct value appears, most
#   common first: the same job as  sort | uniq -c | sort -nr  in bash.
# .head(5) keeps the first 5 rows, like head -5.
# .to_string() turns the result into plain text for printing.
print(food["food_group"].value_counts().head(5).to_string())

print("# FOOD E) FOODS STARTING WITH " + letter + ": COUNT AND TOP 5 FOOD GROUPS")
# Keep only the rows (foods) whose name starts with your letter:
#   food["name"]           the name column
#   .str.lower()           each name in lower case
#   .str.startswith(letter) True if the name starts with your letter, else False
#   food[ ... ]            keeps the rows where the test is True (like grep)
mine = food[food["name"].str.lower().str.startswith(letter)]
print(len(mine))                                   # how many foods
print(mine["food_group"].value_counts().head(5).to_string())   # their top 5 groups


# =============================================================================
# PART 2 - your chromosome from the GTF file
# =============================================================================

# A GTF file has no header line, so we give the 9 columns names ourselves.
cols = ["chrom", "source", "feature", "start", "end",
        "score", "strand", "frame", "attributes"]

# Read the GTF as a table:
#   sep="\t"       columns are separated by tabs
#   header=None    the first line is data, not column names
#   names=cols     use our 9 names
#   comment="#"    ignore lines starting with #
#   dtype=str      read every value as text (we do no arithmetic here)
gtf = pd.read_csv(gtf_file, sep="\t", header=None, names=cols,
                  comment="#", dtype=str)

print("# GTF B) GENE LINES")
# gtf["feature"] == "gene" is True for rows whose 3rd column is exactly "gene"
# (a whole-value comparison, like awk '$3=="gene"', not a text search like grep).
genes = gtf[gtf["feature"] == "gene"]
print(len(genes))

print("# GTF D) GENES WITHOUT A gene_name / GENES WITH A gene_name")
# .str.extract(pattern) applies a regular expression to every row of column 9
# and returns the text captured by the parentheses ( ... ), like \( \) in sed.
# The pattern  gene_name "([^"]+)"  finds the key by its NAME, wherever it is
# in the column. When a row has no gene_name, extract returns an empty value
# (NaN, "not a number", pandas' marker for "missing") instead of the whole line.
# The r before the quotes means "raw text": backslashes are kept as typed.
names = genes["attributes"].str.extract(r'gene_name "([^"]+)"')[0]
print(names.isna().sum())    # isna(): True where the value is missing; sum() counts the Trues
print(names.notna().sum())   # notna(): True where a name was found

print("# GTF E) TAGS ON TRANSCRIPT LINES")
# Keep the transcript rows.
tx = gtf[gtf["feature"] == "transcript"]
# .str.findall(pattern) returns a LIST of every match in each row, so a row
# with  tag "basic"; tag "Ensembl_canonical"; tag "MANE_Select";  gives all
# three tags, like grep -o (sed with .* keeps only one).
# .explode() puts each tag of each list on its own row, and .dropna() drops
# the rows of transcripts that had no tag at all.
tags = tx["attributes"].str.findall(r'tag "([^"]+)"').explode().dropna()
print(tags.value_counts().to_string())
