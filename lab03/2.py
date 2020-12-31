a = int(input("First number:"))
b = int(input("Second number:"))
c = int(input("Third number:"))

if(a<=b)and(a<=c):
  print(a)
elif(c<=b)and(b<=a):
  print(b)
else:
  print(c)