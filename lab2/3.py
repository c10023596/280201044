a = input("Please input the value of a:")
b = input("Please input the value of b:")
c = input("Please input the value of c:")

p_x_top = -b + ((b**2) - (4*a*c))
n_x_top = -b - ((b**2) - (4*a*c))
x_bot = 2*a

p_x = p_x_top / x_bot
n_x = n_x_top / x_bot

print("The roots are:" (p_x , n_x))