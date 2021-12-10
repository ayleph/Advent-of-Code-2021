#!/usr/bin/env python

import argparse


parser = argparse.ArgumentParser()
parser.add_argument("file")
args = parser.parse_args()

with open(args.file, "r") as f:
    depths = f.read().splitlines()

n = 0
depthSums = []
while len(depths) > 2:
    depthSums.append(int(depths[0]) + int(depths[1]) + int(depths[2]))
    n = n + 1
    depths.pop(0)

increaseCount = 0
while len(depthSums) > 1:
    if (depthSums[1] > depthSums[0]):
        increaseCount = increaseCount + 1
    #print(depths[0], depths[1], increaseCount)
    depthSums.pop(0)

print(increaseCount)
