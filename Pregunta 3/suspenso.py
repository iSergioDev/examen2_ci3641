def suspenso(a, b):
  if b == []:
    yield a
  else:
    yield a + b[0]
    for x in suspenso(b[0], b[1:]):
      yield x

for x in suspenso(0, [1]):
  print(x)