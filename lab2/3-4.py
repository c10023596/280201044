# a=2 b=3 result should be 8
a = int(input("The base: "))
b = int(input("The power: "))
total = 1
for i in range(b):
  total *= a
print(total)