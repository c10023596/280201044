def f(n):
  if n == 0:
    return 0
  else:
    return f(n-1) + 3

print(f(6))