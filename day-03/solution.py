# %%
import numpy as np


def parse_wires(lines):
    return [l.split(',') for l in lines]


with open('day-03/input') as file:
    wires = parse_wires(file.readlines())

# wires = parse_wires(
#     ["R75,D30,R83,U83,L12,D49,R71,U7,L72",
#      "U62,R66,U55,R34,D71,R55,D58,R83"])

# %%


def get_path(wire):
    x = [0]
    y = [0]
    for w in wire:
        direction = w[0]
        distance = int(w[1:])
        steps = np.arange(distance) + 1
        zeros = np.zeros_like(steps)
        if direction == 'D':
            dx = zeros
            dy = -steps
        elif direction == 'U':
            dx = zeros
            dy = steps
        elif direction == 'L':
            dx = -steps
            dy = zeros
        elif direction == 'R':
            dx = steps
            dy = zeros

        x += (x[-1] + dx).tolist()
        y += (y[-1] + dy).tolist()

    return zip(x[1:], y[1:])


paths = [list(get_path(wire)) for wire in wires]
points = [set(path) for path in paths]
crossings = points[0].intersection(points[1])
print(min(abs(p[0]) + abs(p[1]) for p in crossings))

# %%
distances = [{path[i]:i+1 for i in range(len(path))} for path in paths]
min([sum(d[c] for d in distances) for c in crossings])

# 43846 is too low

# %%
