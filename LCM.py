# Program to find LCM of two numbers

# Step 1: Input
a, b = map(int, input("Enter two numbers: ").split())

# Step 2: Find HCF using Euclidean Algorithm
x, y = a, b
while y != 0:
    x, y = y, x % y
hcf = x

# Step 3: Calculate LCM
lcm = (a * b) // hcf

# Step 4: Output
print(lcm)
