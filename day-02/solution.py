#%%
import numpy as np
 
with open('day-02/input') as file:
  codes = np.array([int(v) for v in file.read().split(',')])

codes[1] = 12
codes[2] = 2

#%%
#codes = [1,9,10,3,2,3,11,0,99,30,40,50]
c = np.copy(codes)

p = 0
while True:
  op = c[p]

  print(c)
  
  if op == 99:
    break

  a = c[p+1:p+3]

  if op == 1:
    v = np.sum(c[a])
  elif op == 2:
    v = np.prod(c[a])
  else:
    raise Exception()

  c[c[p+3]] = v

  p += 4

print(c[0])
# 133 is too low
# 12490719 is correct

#%%
