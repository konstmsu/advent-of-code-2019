#%%
import numpy as np

with open('day-01/input') as file:
  masses = np.array([int(a) for a in file.readlines()])

print(sum(masses // 3 - 2))

#%%
total = np.zeros_like(masses)

m = masses
while np.any(m > 0):
  m = m // 3 - 2
  m[m < 0] = 0
  total += m

print(sum(total))