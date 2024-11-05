from suspenso import suspenso

def misterio(n):
  if n == 0:
    yield [1]
  else:
    for x in misterio(n-1):
      r = []
      for y in suspenso(0, x):
        r = [*r, y]
      yield r
      

for x in misterio(5):
  print(x)