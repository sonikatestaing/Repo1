import math

Radius = float(input("Enter radius of circle:"))

Diameter = 2*Radius
Circumference = 3*Radius
Area=math.pi*Radius*Radius

print('Diameter of a circle with radius {0} is {1}'.format(Radius,Diameter))
print('Circumference of a circle with radius {0} is {1}'.format(Radius,Circumference))
print('Area of a circle with radius {0} is {1}'.format(Radius, Area))
