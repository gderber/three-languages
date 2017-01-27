#!/usr/bin/env python3

import os
import argparse

"""
Global Variables
"""
__version__='0.1.1'


def main():
    parser = argparse.ArgumentParser(description="Process parameters")
    parser.add_argument("-x",
                        default=0x000020,
                        #choices=["*k", "#ki"],
                        help="Set the size of the files to create")
    parser.add_argument("-y",
                        default=0x10ffff,
                        help="Set the number of directories to exist in the main directory")
    parser.add_argument("-V", "--version",
                        help="Print version information and exit",
                        action="version",
                        version="%(prog)s " + __version__)
    args = parser.parse_args()

    x = args.x
    y = args.y

    while x < y:
        print(chr(x))
        x = x + 1

    return 0

main()
