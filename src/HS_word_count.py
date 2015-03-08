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
import string

def write_results(outputFileName,texttowrite):
    # write the word count to this file
    with open(outputFileName, 'a') as outfile:
        outfile.write(texttowrite)
        

def format_print(outputFileName, counterholder, is_reverse=False):
    # formating file contents to write into the results file
    listitems = counterholder.items()
    listitems.sort(key=lambda (a, b): (a, b),\
                   reverse=is_reverse)
    for word, count in listitems:
        texttowrite = "%-16s %16d \n" % (word, count)
        write_results(outputFileName,texttowrite)


def count_words(wcInputfolder,inputFileList):
    # word count function
    counterholder = Counter()
    for filename in inputFileList:
        inputFileName = wcInputfolder+"\\"+filename
        with open(inputFileName,"rU") as fileholder:
            for line in fileholder:
                line = line.strip().lower()
                # removes punctuation from the words
                lineout = line.translate(string.maketrans("",""), string.punctuation)
                if not lineout:
                    continue
                counterholder.update(x for x in \
                                 split("[^a-zA-Z']+",\
                                       lineout) if x)
    return counterholder

def case_insensitive_cmp(a, b):
    # This will arrange files alphabatically without
    # considering the case of the file name
    return cmp(a.upper(), b.upper())


def main(wcInputfolder,inputFileList,outputFileName):
    # The main function starts here calling other functions
    if os.path.isfile(outputFileName):
        os.remove(outputFileName)
    format_print(outputFileName,count_words(wcInputfolder,inputFileList),\
                 is_reverse=False)
    

if __name__ == "__main__":
    # Read the program arguments
    wcInputfolder = sys.argv[1] # input folder path
    inputFileList =  os.listdir(wcInputfolder) # list all files in input folder path
    inputFileList.sort(case_insensitive_cmp) # sort them alphabatically
    outputFileName = sys.argv[2] # output file path
    main(wcInputfolder,inputFileList,outputFileName)
