#!/usr/bin/env python

import argparse


parser = argparse.ArgumentParser()
parser.add_argument("file")
args = parser.parse_args()

with open(args.file, "r") as f:
    depths = f.read().splitlines()

increaseCount = 0
while len(depths) > 1:
    if (depths[1] > depths[0]):
        increaseCount = increaseCount + 1
    depths.pop(0)

print(increaseCount)
