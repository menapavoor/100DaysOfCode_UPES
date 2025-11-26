# Program to convert a number to binary representation

# Step 1: Input
num = int(input("Enter a number: "))

# Step 2: Conversion using loop
binary = ""
n = num
while n > 0:
    remainder = n % 2
    binary = str(remainder) + binary  # prepend remainder
    n //= 2

# Step 3: Handle special case for 0
if num == 0:
    binary = "0"

# Step 4: Output
print(binary)