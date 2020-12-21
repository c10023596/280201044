def harmonic(n: int):
  if n == 1:
    return 1
  elif n == 0:
    print("You can't divide with zero!")
  else:
    return n**(-1) + harmonic(n-1)


n = input("n for harmonic sum: ")

print(harmonic(n))