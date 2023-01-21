#!/usr/bin/python3
import markdown
import sys
from os import path

if (len(sys.argv) < 1):
    sys.stderr.write("Usage: ./markdown2html.py README.md README.html")
    sys.exit(1)
elif not path.exists(sys.argv[0]):
    sys.stderr.write("Missing {}".format(sys.argv[1]))
    sys.exit(1)
sys.exit(0)
