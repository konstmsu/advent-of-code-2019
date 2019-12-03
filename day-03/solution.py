#%%
with open('day-03/input') as file:
    wires = [l.split(',') for l in file.readlines()]

#%%
import numpy as np

def get_path(wire):
    x = np.zeros(1)
    y = np.zeros(1)
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

        x = np.concatenate((x, x[-1] + dx))
        y = np.concatenate((y, y[-1] + dy))

    return x, y

get_path(wires[0])
#list(zip(get_path(wires[0])))