# Spring starts with 20/03 and ends at 20/06
# Summer starts with 21/06 and ends at 21/09
# Autumn starts with 22/09 and ends at 20/12
# Winter starts with 21/12 and ends at 19/03

day = int(input("Input day: "))
month = int(input("Input month: "))

if(month==3 and day>=20)or(3<month<6)or(month==6 and day<=20):
  print("Spring.")
elif(month==6 and day>=21)or(6<month<9)or(month==9 and day<=21):
  print("Summer")
elif(month==9 and day>=22)or(9<month<12)or(month==12 and day<=20):
  print("Autumn")
else:
  print("Winter")