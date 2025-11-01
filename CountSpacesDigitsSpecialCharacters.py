# Program to count spaces, digits, and special characters in a string

# Step 1: Input string
s = input()

# Step 2: Initialize counters
spaces = 0
digits = 0
special = 0

# Step 3: Traverse string
for ch in s:
    if ch == " ":
        spaces += 1
    elif ch.isdigit():
        digits += 1
    elif not ch.isalpha():  # not a letter
        special += 1

# Step 4: Output
print("Spaces={}, Digits={}, Special={}".format(spaces, digits, special))
