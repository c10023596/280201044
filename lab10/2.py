def hailstone(x, seq=[]):
  seq.append(str(x))
  if x == 1:
    return ",".join(seq)
  else:
    if x % 2 == 1:
      return hailstone(3*x + 1)
    else:
      return hailstone(x//2)


print(hailstone(5))