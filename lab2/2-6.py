print("You have a quadratic equation. Now to calculate the amount of roots you have, you have to input parameters of the equation.")
a = int(input("The first parameter: "))
b = int(input("The second parameter: "))
c = int(input("The third parameter: "))

delta = b**2 - 4*a*c

if(delta<0):
  print("Two roots.")
elif(delta==0):
  print("One root.")
else:
  print("No root.")