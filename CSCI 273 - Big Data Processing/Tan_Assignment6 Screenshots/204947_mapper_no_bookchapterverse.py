#!/usr/bin/env python3


import sys
import re

line_number = 0
current_book = None
for line in sys.stdin:
    line_number += 1
    if line_number <= 107:  # Skip the preamble
        continue
        
    line = line.strip()
    
    # If the line is a book header, skip the line.
    if line.startswith("Book"):
        current_book = line
        continue
        
    if current_book:
        words = line.split()
        for word in words:
            if re.match(r'^\d{2}:\d{3}:\d{3}', word): # don't include the words with form: DD:DDD:DDD, where D is a digit 
                continue
            print("%s\t%d" % (current_book, 1))