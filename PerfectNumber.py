# Program to check if a number is a perfect number

# Step 1: Input
num = int(input("Enter a number: "))

# Step 2: Find sum of divisors
div_sum = 0
for i in range(1, num):
    if num % i == 0:
        div_sum += i

# Step 3: Check condition
if div_sum == num:
    print("Perfect number")
else:
    print("Not perfect number")
