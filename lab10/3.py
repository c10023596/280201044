def sum_of_nested_list(x):
  if not isinstance(x, list):
    return x
  else:
    sum = 0
    for a in x:
      sum += sum_of_nested_list(a)
    return sum

print(sum_of_nested_list(45))