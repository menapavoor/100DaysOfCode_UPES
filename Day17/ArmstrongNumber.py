# Program to check if a number is an Armstrong number

# Step 1: Input
num = int(input("Enter a number: "))

# Step 2: Count digits
n = num
digits = 0
while n > 0:
    digits += 1
    n //= 10

# Step 3: Calculate sum of powers of digits
n = num
armstrong_sum = 0
while n > 0:
    digit = n % 10
    armstrong_sum += digit ** digits
    n //= 10

# Step 4: Check Armstrong
if armstrong_sum == num:
    print("Armstrong")
else:
    print("Not Armstrong")