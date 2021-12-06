#!/usr/bin/env python

with open("day02.input") as f:
    commands = f.read().splitlines()

horizontal = 0
depth = 0
while len(commands) > 0:
    direction = commands[0].split()[0]
    magnitude = int(commands[0].split()[1])
    if direction == "forward":
        horizontal = horizontal + magnitude
    if direction == "down":
        depth = depth + magnitude
    if direction == "up":
        depth = depth - magnitude
    commands.pop(0)

print(horizontal, depth, horizontal * depth)
