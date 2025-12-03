# Program to swap two numbers using a third variable

# Step 1: Input
a, b = map(int, input("Enter two numbers: ").split())

# Step 2: Swap using a temporary variable
temp = a
a = b
b = temp

# Step 3: Output
print("After swap:", a, b)