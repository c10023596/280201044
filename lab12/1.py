import math

class Cylinder:

  def __init__(self, radius, height):
    self.radius = radius
    self.height = height
  
  def area(height, radius):
    return (height*radius*2*math.pi) + (radius*radius*math.pi*2)
  
  def volume(height, radius):
    return (height*radius*radius*math.pi)
  

print("Area is " + f"{Cylinder.area(3,5)}.")
print("Volume is " + f"{Cylinder.area(3,5)}.")