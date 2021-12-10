#!/usr/bin/env python

import argparse


parser = argparse.ArgumentParser()
parser.add_argument("file")
args = parser.parse_args()

with open(args.file, "r") as f:
    commands = f.read().splitlines()

horizontal = 0
aim = 0
depth = 0

for i in range(len(commands)):
    direction = commands[i].split()[0]
    magnitude = int(commands[i].split()[1])
    if direction == "forward":
        horizontal = horizontal + magnitude
        depth = depth + aim * magnitude
    if direction == "down":
        aim = aim + magnitude
    if direction == "up":
        aim = aim - magnitude

print(horizontal, depth, horizontal * depth)
