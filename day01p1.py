#!/usr/bin/env python

with open("day01.input") as f:
    depths = f.read().splitlines()

increaseCount = 0
while len(depths) > 1:
    if (depths[1] > depths[0]):
        increaseCount = increaseCount + 1
    depths.pop(0)

print(increaseCount)
