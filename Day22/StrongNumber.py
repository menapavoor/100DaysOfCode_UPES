# Program to check if a number is a Strong number

# Step 1: Input
num = int(input("Enter a number: "))

# Step 2: Function to calculate factorial
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

# Step 3: Calculate sum of factorials of digits
n = num
strong_sum = 0
while n > 0:
    digit = n % 10
    strong_sum += factorial(digit)
    n //= 10

# Step 4: Check condition
if strong_sum == num:
    print("Strong number")
else:
    print("Not strong number")