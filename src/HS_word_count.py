#HS_word_count.py
"""
Program Description:..
Word count program
-----------
Inputs ::
    (1) Input folder path containing the files to read
    (2) File path to the output file name
    
    e.g. input file
    So call a big meeting,
    Get everyone out out,
    Make every Who holler,
    Make every Who shout shout.
-----------
Outputs::
    (1) Writes an output file containing
        the count of each word in each file
        
        e.g. output
        a		1
        big		1
        call		1
        every		2
"""
# Author: Harish Sangireddy
# Date: 3/3/2015
# Austin, Texas
# The University of Texas at Austin

# import all libraries here
import sys
import os
from collections import Counter
from re import split

BANNER = "-" * 35

def format_print(counter, is_reverse=False):
    lst = counter.items()
    lst.sort(key=lambda (a, b): (b, a), reverse=is_reverse)
    print ("[Unique Words: %d]" % len(lst)).center(35, "=")
    print "%-16s | %16s" % ("Word", "Count")
    print BANNER
    for word, count in lst:
        print "%-16s | %16d" % (word, count)


def count_words(inputfileName):
    # count function
    counterholder = Counter()
    with open(inputfileName,"rU") as fileholder:
        for line in fileholder:
            line = line.strip().lower()
            if not line:
                continue
            counterholder.update(x for x in \
                                 split("[^a-zA-Z']+",\
                                       line) if x)
    return counterholder


def main(wcInput,outputFileName):
    # The main function starts here
    print(wcInput)
    print(outputFileName)
    #count_words(wcInput)
    format_print(count_words(wcInput),\
                 is_reverse=False)
    

if __name__ == "__main__":
    # Read the program arguments
    # into appropriate variables
    wcInput = sys.argv[1]
    outputFileName = sys.argv[2]
    main(wcInput,outputFileName)