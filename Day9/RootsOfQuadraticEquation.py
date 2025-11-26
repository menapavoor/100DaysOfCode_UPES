import math

# Program to find roots of a quadratic equation

# Step 1: Input coefficients
a, b, c = map(float, input("Enter coefficients a, b, c: ").split())

# Step 2: Calculate discriminant
D = b**2 - 4*a*c

# Step 3: Conditions
if D > 0:
    root1 = (-b + math.sqrt(D)) / (2*a)
    root2 = (-b - math.sqrt(D)) / (2*a)
    print("Roots are real and different:", round(root1, 2), ",", round(root2, 2))
elif D == 0:
    root = -b / (2*a)
    print("Roots are real and same:", round(root, 2))
else:
    print("Roots are complex")