# Program to find sum of digits of a number

# Step 1: Input
num = int(input("Enter a number: "))

# Step 2: Loop to extract digits and sum them
total = 0
while num > 0:
    digit = num % 10
    total += digit
    num //= 10

# Step 3: Output
print(total)