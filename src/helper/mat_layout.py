#!/bin/env python

import sys
import argparse

# Outputs a LED matrix layout
# A list converting LED string number to physical grid layout
# Start with top right and continue right then down
# For example, the string starts bottom right and has horizontal batons
# which loop on alternate rows.
#
# Creates a matrix layout from a chain for arbitrary rows and columns:
# For example, for a 12 x 8 matrix     -----------\
# The last index is number 95                     |
#                                      /----------/
#                                      |
#                                      \----------\
# The first idx is number 0                       |
# starts at the bottom left here:      -----------/



parser = argparse.ArgumentParser(description='Creates a matrix for a string of LEDs.')
parser.add_argument('--rows', metavar='r', type=int, dest='rows',
        required=True,
        help='number of rows in matrix')
parser.add_argument('--columns', metavar='c', type=int, dest='columns',
        required=True,
        help='number of columns in matrix')

args = parser.parse_args()

rows = args.rows
columns = args.columns

flipped = False

for r in reversed(range(1, rows + 1)):
    if flipped:
        for c in reversed(range(1, columns + 1)):
            curr = r * columns - c
            sys.stdout.write(str(curr) + ', ')
        sys.stdout.flush()
        sys.stdout.write('\n')
        flipped = not flipped
    else:
        for c in range(1, columns + 1):
            curr = r * columns - c
            sys.stdout.write(str(curr) + ', ')
        sys.stdout.flush()
        sys.stdout.write('\n')
        flipped = not flipped