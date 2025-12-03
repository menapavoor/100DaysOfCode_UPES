# Program to check if a number is palindrome

# Step 1: Input
num = int(input("Enter a number: "))

# Step 2: Reverse the number
original = num
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10

# Step 3: Check palindrome
if original == rev:
    print("Palindrome")
else:
    print("Not palindrome")