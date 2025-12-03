# Program to print the product of even numbers from 1 to n

# Step 1: Input
n = int(input("Enter n: "))

# Step 2: Loop to calculate product
product = 1
for i in range(2, n + 1, 2):  # step = 2 ensures only even numbers
    product *= i

# Step 3: Output
print("Product =", product)