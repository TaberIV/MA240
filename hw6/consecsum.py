def checkNum(n):
  def checkStart(n, start):
    sequence = []
    _sum = 0
    for i in range(start, n):
      sequence.append(i)
      _sum += i
      if _sum == n:
        return sequence
      elif _sum > n:
        return None
    return None

  for i in range(1, n):
    sequence = checkStart(n, i)
    if sequence != None:
      return sequence
  return None

for i in range(2, 65):
  print(str(i) + ": " + str(checkNum(i)))