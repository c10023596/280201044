def get_evens_recursive(a, c=0):
  if len(a) == 0:
    return c
  if a.pop() % 2 == 0:
    c += 1
  return get_evens_recursive(a, c)


def get_evens(a):
  return get_evens_recursive(a, c=0)

a = [0, 1, 2, 3, 4, 5]

print(get_evens(a))