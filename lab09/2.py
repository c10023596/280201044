def get_reverse(a):
  a = list(a)
  if len(a) == 0:
    return []
  else:
    return [a.pop()] + get_reverse(a)
  

a = [1, 2, 3, 4]

print(get_reverse(a))