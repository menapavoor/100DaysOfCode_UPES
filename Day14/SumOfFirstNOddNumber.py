# Program to print the sum of the first n odd numbers

# Step 1: Input
n = int(input("Enter n: "))

# Step 2: Loop to generate odd numbers and sum them
total = 0
odd = 1
for i in range(n):
    total += odd
    odd += 2

# Step 3: Output
print("Sum =", total)