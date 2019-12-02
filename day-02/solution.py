#%%
with open('day-02/input') as file:
  codes = [int(v) for v in file.read().split(',')]

#%%
#codes = [1,9,10,3,2,3,11,0,99,30,40,50]
def run(noun, verb):
  c = codes[:]
  c[1] = noun
  c[2] = verb

  p = 0
  while True:
    op = c[p]

    if op == 99:
      return c[0]

    a1 = c[c[p+1]]
    a2 = c[c[p+2]]

    if op == 1:
      v = a1 + a2
    elif op == 2:
      v = a1 * a2
    else:
      raise Exception()

    c[c[p+3]] = v

    p += 4

print(run(12, 2))
# 133 is too low
# 12490719 is correct

#%%
%%timeit
for noun in range(100):
  for verb in range(100):
    if run(noun, verb) == 19690720:
      print(noun * 100 + verb)

# %%
import matplotlib.pyplot as plt
nouns = range(100)
verbs = range(100)
for verb in verbs:
  y = [run(noun, verb) for noun in nouns]
  plt.plot(nouns, y)