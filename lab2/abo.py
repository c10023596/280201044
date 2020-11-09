n = int(input("The number: "))
zer0 = 0
for i in range(1, n):
  n *= i
while (n % 10 == 0):
  n //= 10
  zer0 += 1
print(zer0)