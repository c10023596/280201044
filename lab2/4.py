age = int(input("What is your age? "))

if(age<6)or(age>60):
  print("You get to ride it for free!")
elif(age>=6)and(age<18):
  print("You have to pay 1.5 dollars for the ride.")
else:
  print("You have to pay 3 dollars for the ride.")