#!/usr/bin/env python3


import sys

# Dictionary to store book counts
book_counts = {}

for input_line in sys.stdin:
    input_line = input_line.strip()
    this_book, count = input_line.split("\t", 1)
    count = int(count)    
    book_counts[this_book] = book_counts.get(this_book, 0) + count

for book, count in sorted(book_counts.items(), key=lambda x: x[1], reverse=True):
    print("%s\t%d" % (book, count))