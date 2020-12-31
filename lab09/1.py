def harmonic(n: int):
  n = int(n)
  if n == 1:
    return 1
  elif n == 0:
    return "You can't divide with zero!"
  else:
    return n**(-1) + harmonic(n-1)


n = input("n for harmonic sum: ")

print(harmonic(n))