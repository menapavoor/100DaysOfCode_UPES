# Program to check if a number is prime

# Step 1: Input
num = int(input("Enter a number: "))

# Step 2: Prime check
if num <= 1:
    print("Not prime")
else:
    is_prime = True
    for i in range(2, int(num**0.5) + 1):  # check up to sqrt(num)
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime")
    else:
        print("Not prime")
