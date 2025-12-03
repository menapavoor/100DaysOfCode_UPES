# Program to calculate factorial of a number

# Step 1: Input
n = int(input("Enter a number: "))

# Step 2: Factorial calculation using loop
factorial = 1
for i in range(1, n + 1):
    factorial *= i

# Step 3: Output
print(factorial)
