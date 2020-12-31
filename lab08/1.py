def list_sum(a):
  summation = 0
  for x in range(len(a)):
    summation += a[x]
  return summation
a_list = [12, -7, 5, -89.4, 3, 27, 56, 57.3]
print(list_sum(a_list))