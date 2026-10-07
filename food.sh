#!/bin/bash
echo "# A) FOOD.CSV - t"
echo "# B) LINES IN THE FILE / FOODS: \
$(wc -l < data/Food.csv) / \
$(grep -o "FOOD" data/Food.csv | wc -l)"
