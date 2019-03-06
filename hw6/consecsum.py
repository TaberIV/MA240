def checkNum(n):
  def checkStart(n, start):
    if (start == n):
      return None
    sequence = []
    _sum = 0
    for i in range(start, n):
      sequence.append(i)
      _sum += i
      if _sum == n:
        return sequence
      elif _sum > n:
        return checkStart(n, start + 1)
  for i in range(1, n):
    sequence = checkStart(n, int(1))
    if sequence != None:
      return sequence
  return None

def checkNum2(n):
  def checkStart(n, start):
    if (start == 0):
      return None
    sequence = []
    _sum = 0
    for i in range(start, n):
      sequence.append(i)
      _sum += i
      if _sum == n:
        return sequence
      elif _sum > n:
        return checkStart(n, start - 1)

  for i in range(1, n):
    sequence = checkStart(n, int(n/2))
    if sequence != None:
      return sequence
  return None

for i in range(2, 100):
  squence = checkNum(i)
  squence2 = checkNum2(i)

  string = str(squence2)

  if (squence2 != squence):
    string += ", " + str(squence)

  print(str(i) + ": " + string)
