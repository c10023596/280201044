NoL = int(input("The amount of lectures: "))
GPA = float(input("Your GPA is: "))

if(NoL<47)and(GPA<2.0):
  print("Not enough number of lectures and GPA to graduate!")
elif(NoL<47)and(GPA>=2.0):
  print("Not enough number of lectures!")
elif(NoL>=47)and(GPA<2.0):
  print("Not enough GPA!")
elif(NoL>=47)and(GPA>=2.0):
  print("GRADUATED!")