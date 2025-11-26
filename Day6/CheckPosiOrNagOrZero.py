# Program to check whether a number is positive, negative, or zero

# Step 1: Input
num = int(input("Enter an integer: "))

# Step 2: Nested if–else
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive")
else:
    print("Negative")