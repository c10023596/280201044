a = int(input("Please input the value of a:"))
b = int(input("Please input the value of b:"))
c = int(input("Please input the value of c:"))

xp = (-b + (b**2 - (4*a*c))**0.5) / (2*a)
xn = (-b - (b**2 - (4*a*c))**0.5) / (2*a)

print(xp,xn)