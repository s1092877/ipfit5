from __future__ import print_function
import argparse
import os

__author__ = ["Cas van Andel"]
__date__ = 20180306
__description__ = "Directory tree walker"

parser = argparse.ArgumentParser(
    description=__description__,
    epilog="Developed by {} on {}".format(
    ", ".join(__author__), __date__)
)

parser.add_argument("DIR_PATH", help="Path to directory")
args = parser.parse_args()
Users/CasvanAndel/Documents/IpfnetCasvanAndel = args.DIR_PATH

for file_entry in files:
# create the relative path to the file
    file_path = os.path.join(root, file_entry)
    print(file_path)
