#!/bin/sh -e
set -x

# -v: verbose output
# -s: show print statements
python -m pytest app/tests/ -v -s
