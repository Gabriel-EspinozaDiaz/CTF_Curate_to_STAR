#!/usr/bin/env python3
import argparse
import sys
import regex as re
import os

# FUNCTIONS
   
def file_check(cs_filename,pwd):
    if not os.path.exists(cs_filename):
        raise FileNotFoundError(f"Error: The chosen .cs file directory '{cs_filename}' doesn't exist", file=sys.stderr)
    if not os.path.exists(pwd):
        raise FileNotFoundError(f"Error: The chosen .cs file directory '{pwd}' doesn't exist", file=sys.stderr)
    ext1 = re.search(r'\.([^.]*)$', cs_filename)
    if ext1 != ".cs":
        raise TypeError(f'Error: {cs_filename} is a {ext1} file. You need to submit a .cs file from CryoSPARC')

# RUN

def main(cs_pwd, target_pwd=None):
    """
    Main function that processes the files.
    
    Args:
        input_file (str): Path to the required input file
        optional_file (str, optional): Path to the optional input file. Defaults to None.
    """
    # Checks that inputs are valid
    file_check(cs_pwd,target_pwd)
    # Reads in the cs file, without modifying the text yet
    with open(cs_pwd, 'r') as file:
        cs_raw = file.read()

    



