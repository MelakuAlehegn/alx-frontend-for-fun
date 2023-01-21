#!/usr/bin/python3
import markdown
import sys

if (len(sys.argv) < 2):
    sys.stderr.write("Usage: ./markdown2html.py README.md README.html")
    sys.exit(1)
elif sys.argv[1]:
    print("Helyy")
