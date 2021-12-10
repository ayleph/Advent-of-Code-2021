#!/usr/bin/env python

import argparse


parser = argparse.ArgumentParser()
parser.add_argument("file")
args = parser.parse_args()

with open(args.file, "r") as f:
    depths = f.read().splitlines()

# non-destructive method
n = 0
depthSums = []
while n < len(depths) - 2:
    depthSums.append(int(depths[n]) + int(depths[n + 1]) + int(depths[n + 2]))
    n = n + 1

n = 0
increaseCount = 0
while n < len(depthSums) - 1:
    if (depthSums[n + 1] > depthSums[n]):
        increaseCount = increaseCount + 1
    n = n + 1
print(increaseCount)

# quick and dirty destructive method
depthSums = []
while len(depths) > 2:
    depthSums.append(int(depths[0]) + int(depths[1]) + int(depths[2]))
    depths.pop(0)

increaseCount = 0
while len(depthSums) > 1:
    if (depthSums[1] > depthSums[0]):
        increaseCount = increaseCount + 1
    depthSums.pop(0)
print(increaseCount)
