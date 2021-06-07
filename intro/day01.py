#convert from degrees to radian
import math
print("This Program Converts a Value in Degrees to Radians")
degree = int(input("Enter value as degree: "))

#converting input to radians
radian = math.radians(degree)

# displaying result
print("Value in Radians: ",radian)


#surface area and volume of a circle
pi = 22/7

#getting radius 
r = float(input("Enter radius: "))
Area = 4 * pi * r**2

#displaying result
print("Area of sphere ", Area)

