N = int(input("How many numbers? "))
even = 0
odd = 0
for i in range(N):
  integer = int(input("Input interger: "))
  if integer%2==0:
    even += 1
  else:
    odd += 1
print(even//(odd+even)*100,"%")