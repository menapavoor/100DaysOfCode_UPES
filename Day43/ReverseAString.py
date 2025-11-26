# Program to reverse a string

# Step 1: Input string
s = input()

# Step 2: Reverse manually
rev = ""
for ch in s:
    rev = ch + rev   # prepend each character

# Step 3: Output
print(rev)