# Program to count frequency of a given character in a string

# Step 1: Input string
s = input()

# Step 2: Input character to search
ch = input()

# Step 3: Count manually
count = 0
for c in s:
    if c == ch:
        count += 1

# Step 4: Output
print(count)