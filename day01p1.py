#!/usr/bin/env python

import argparse


parser = argparse.ArgumentParser()
parser.add_argument("file")
args = parser.parse_args()

with open(args.file, "r") as f:
    depths = f.read().splitlines()

# non-destructive method
increaseCount = 0
for i in range(len(depths) - 1):
    if (depths[i + 1] > depths[i]):
        increaseCount = increaseCount + 1
print(increaseCount)

# quick and dirty destructive method
increaseCount = 0
while len(depths) > 1:
    if (depths[1] > depths[0]):
        increaseCount = increaseCount + 1
    depths.pop(0)
print(increaseCount)
