from math import sqrt

# Input for the coordinates of the first point
x1 = float(input("Enter the x-coordinate of the first point: "))
y1 = float(input("Enter the y-coordinate of the first point: "))

# Input for the coordinates of the second point
x2 = float(input("Enter the x-coordinate of the second point: "))
y2 = float(input("Enter the y-coordinate of the second point: "))

# Calculate distance using the formula
distance = sqrt((x2 - x1)**2 + (y2 - y1)**2)

print("Distance between the points:", distance)