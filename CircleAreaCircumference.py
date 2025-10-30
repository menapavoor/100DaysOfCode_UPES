# Program to calculate area and circumference of a circle

import math

# Step 1: Input
radius = float(input("Enter radius: "))

# Step 2: Calculations
area = math.pi * radius ** 2
circumference = 2 * math.pi * radius

# Step 3: Output
print("Area = {:.2f}, Circumference = {:.2f}".format(area, circumference))
