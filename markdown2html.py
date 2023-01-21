#!/usr/bin/python3
"""A script that checks all the requirements"""

import sys
from os import path


if __name__ == "__main__":
    if (len(sys.argv) < 3):
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html")
        sys.exit(1)
    elif not path.exists(sys.argv[1]):
        sys.stderr.write("Missing {}".format(sys.argv[1]))
        sys.exit(1)
    sys.exit(0)
