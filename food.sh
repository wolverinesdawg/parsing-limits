#!/bin/bash
echo "# A) FOOD.CSV - t"
echo "# B) LINES IN THE FILE / FOODS: \
$(wc -l < data/Food.csv) / \
$(grep -o "FOOD" data/Food.csv | wc -l)"
echo "# C) TOP 5 FOOD GROUPS - "
sed '1d' data/Food.csv | cut -d',' -f12 | sort| uniq -c | sort -nr | head -5
