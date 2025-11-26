# Program to swap two numbers without using a third variable

# Step 1: Input
a, b = map(int, input("Enter two numbers: ").split())

# Step 2: Swap using arithmetic
a = a + b
b = a - b
a = a - b

# Step 3: Output
print("After swap:", a, b)