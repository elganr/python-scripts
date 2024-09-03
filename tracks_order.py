#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Adds track numbers to files in a directory. 
Please note that *all* the files in the directory are renamed: at no point does 
the script check that the file being renamed is music. Also, the files are 
sorted according to the date of last modification.

This script was created for giving tracks number to files downloaded from Roger 
McGuinn's Folk Den: https://www.ibiblio.org/jimmy/folkden-wp/
"""

import os
from os import listdir
from os.path import isfile, join

import sys

# The working directory, if not given as an arg, will be the current workdir. 
args = sys.argv[1:]
path = args[0] if args else os.getcwd()

# Lists the files in 'last modified' order.
files = [f for f in listdir(path) if isfile(join(path, f))]
os.chdir(path)
files.sort(key=os.path.getmtime)

# For each file, prepends its track number.
for i, file in enumerate(files):
    new_file = f'{i+1}_' + file
    os.rename( file, new_file )

