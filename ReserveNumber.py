# Program to reverse a number

# Step 1: Input
num = int(input("Enter a number: "))

# Step 2: Reverse logic
rev = 0
while num > 0:
    digit = num % 10       # get last digit
    rev = rev * 10 + digit # build reversed number
    num //= 10             # remove last digit

# Step 3: Output
print(rev)
