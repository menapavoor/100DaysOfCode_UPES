# Program to print all prime numbers from 1 to n

# Step 1: Input
n = int(input("Enter n: "))

# Step 2: Loop through numbers
for num in range(2, n + 1):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")