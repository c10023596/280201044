n1 = int(input("First number: "))
n2 = int(input("Second number: "))
shared_digits = 0
while True:
  if (n1%10)==(n2%10):
    shared_digits += 1
  n1 //= 10
  n2 //= 10
  if (n1==0) and (n2==0):
    break
print(shared_digits)