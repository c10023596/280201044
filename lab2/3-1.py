num = int(input("Input the number: "))
if num < 10:
  result = "0" + str(num)
  print(result)
else:
  d1 = num % 10
  d2 = num % 100 - d1
  result = d2 + d1
  print(result)