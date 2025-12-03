# Program to check if a string is a palindrome

# Step 1: Input string
s = input()

# Step 2: Reverse string
rev = ""
for ch in s:
    rev = ch + rev

# Step 3: Check palindrome
if s == rev:
    print("Palindrome")
else:
    print("Not palindrome")