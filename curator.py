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

def main(cs_pwd, symbolic_links=None, target_pwd=None):
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


# GUIDE FOR USER

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Takes an exported cryosparc file from the CTF curation job, and writes a schedule.star file. Run the schedule.star file, and it will generate a relion job with all of the raw micrographs that you curated in CryoSPARC",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        "cs_pwd",
        help="The pathway directory to the .cs cryosparc file, from your current directory")
    
    parser.add_argument(
        "symbolic_links",
        nargs="?",
        default=True,  
        help="When set to True, the script will look through symbolic links for the files. This is optional argument is True by default, structural biology core convention is to produce a symbolic link within your working directory. If set to False, symbolic links will not be accessed. This speeds up the process slightly, but should only be used if your working directory is contains the raw micrograph files."
    )
    parser.add_argument(
        "target_pwd",
        nargs="?",
        default=os.getcwd(),
        help="If you want to run the search from somewhere else in the computer, specify the directory here. This is set to your current directory by default"
    )



