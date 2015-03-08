#HS_runnning_median.py
"""
Program Description:..
Estimate the running median of the input file,
which keeps track of the median for a stream of numbers,
updating the median for each new number
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
        the running median count of each sfile
        
        e.g. output
        5.0
        4.5
        4.0
        4.5
"""
# Author: Harish Sangireddy
# Date: 3/3/2015
# Austin, Texas
# The University of Texas at Austin

# import all libraries here
import sys
import os
from re import split
import numpy as np
import string

def write_results(outputFileName,texttowrite):
    # write the word count to this file
    with open(outputFileName, 'a') as outfile:
        outfile.write(texttowrite)
        

def format_print(outputFileName, running_medianlist):
    listitems = running_medianlist
    for medianval in listitems:
        texttowrite = "%.1f \n" % (medianval)
        write_results(outputFileName,texttowrite)


def running_median(wcInputfolder,inputFileList):
    # the running median algo:
    word_count_perlinelist = []
    running_medianlist = []
    for filename in inputFileList:
        inputFileName = wcInputfolder+"\\"+filename
        with open(inputFileName,"rU") as fileholder:
            for line in fileholder:
                line = line.strip().lower()
                if not line:
                    word_count_perlinelist.append(1)
                else:
                    word_count_perlinelist.append(len(split("[^a-zA-Z']+",line)))
                    running_medianlist.append(np.median(word_count_perlinelist))
    return running_medianlist
    
def case_insensitive_cmp(a, b):
    # This will arrange files alphabatically without
    # considering the case of the file name
    return cmp(a.upper(), b.upper())

def main(wcInputfolder,inputFileList,outputFileName):
    # The main function starts here
    #print(inputFileName)
    #print(outputFileName)
    if os.path.isfile(outputFileName):
        os.remove(outputFileName)
    #running_median(inputFileName)
    format_print(outputFileName,running_median(wcInputfolder,inputFileList))
    

if __name__ == "__main__":
    # Read the program arguments
    wcInputfolder = sys.argv[1] # input folder path
    inputFileList =  os.listdir(wcInputfolder) # list all files in input folder path
    inputFileList.sort(case_insensitive_cmp) # sort them alphabatically
    outputFileName = sys.argv[2] # output file path
    main(wcInputfolder,inputFileList,outputFileName)
