# Program to calculate area and perimeter of a rectangle

# Step 1: Input
length, breadth = map(int, input("Enter length and breadth: ").split())

# Step 2: Calculations
area = length * breadth
perimeter = 2 * (length + breadth)

# Step 3: Output
print("Area =", area, ", Perimeter =", perimeter)