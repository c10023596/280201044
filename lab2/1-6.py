# Car_A is 70, B is 80, they are facing each other. The first distance is 490, the last distance is 150, question is the time taken in minutes.
car_A = int(input("The velocity of car A: "))
car_B = int(input("The velocity of car B: "))
distance1 = int(input("The first distance between two: "))
distance2 = int(input("The last distance between two: "))
car_direction = int(input("If cars are facing each other, type 0. "))
distance_change = distance1 - distance2
if(car_direction==0):
  velocity = car_A + car_B
  print(int(distance_change/velocity*60))
else:
  velocity = abs(car_A - car_B)
  print(int(distance_change/velocity*60))