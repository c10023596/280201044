#For a leap year, you'll ONLY need to divide it with 4.
year = int(input("The year: "))
if year % 400 == 0:
  print("It's a century leap year.")
elif (year % 100 == 0):
  print("Not a leap year somehow.")
elif (year % 4 == 0):
  print("It's a leap year woooo!")
else:
  print("Scram! This ain't leap year!")