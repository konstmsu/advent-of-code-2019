# %%
import numpy as np
with open('day-03/input') as file:
    wires = [l.split(',') for l in file.readlines()]

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


points = [set(get_path(wire)) for wire in wires]
crossings = points[0].intersection(points[1])
print(min(abs(p[0]) + abs(p[1]) for p in crossings))
