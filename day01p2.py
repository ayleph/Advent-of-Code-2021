#!/usr/bin/env python

import argparse


parser = argparse.ArgumentParser()
parser.add_argument("file")
args = parser.parse_args()

with open(args.file, "r") as f:
    depths = f.read().splitlines()

# non-destructive method
depthSums = []
for i in range(len(depths) -2):
    depthSums.append(int(depths[i]) + int(depths[i + 1]) + int(depths[i + 2]))

increaseCount = 0
for i in range(len(depthSums) - 1):
    if (depthSums[i + 1] > depthSums[i]):
        increaseCount = increaseCount + 1
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
