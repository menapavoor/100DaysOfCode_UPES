# Program to print all factors of a given number

# Step 1: Input
num = int(input("Enter a number: "))

# Step 2: Loop through possible factors
for i in range(1, num + 1):
    if num % i == 0:
        print(i, end=" ")
