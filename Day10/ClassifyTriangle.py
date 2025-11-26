# Program to classify a triangle

# Step 1: Input
a, b, c = map(int, input("Enter three sides of the triangle: ").split())

# Step 2: Conditions
if a == b == c:
    print("Equilateral")
elif a == b or b == c or a == c:
    print("Isosceles")
else:
    print("Scalene")