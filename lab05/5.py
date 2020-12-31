#fibonacci
digits = int(input("How many digits of Fibonacci should be printed? "))
a = 0
b = 1
for i in range(digits):
  c = a
  a = b
  b = c + b
  print(a)