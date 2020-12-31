def is_prime(x):
  if x <= 1:
    return False
  elif x == 2:
    return True
  else:
    for i in range(2, x/2):
      if x % i == 0:
        return False
    return True
def print_primes_between(a, b):
  primes = []
  for i in range(a, b):
    if is_prime(i) == True:
      primes.append(i)
  return primes
