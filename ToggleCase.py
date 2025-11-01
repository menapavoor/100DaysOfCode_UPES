# Program to toggle case of each character in a string

# Step 1: Input string
s = input()

# Step 2: Toggle case manually
result = ""
for ch in s:
    if 'a' <= ch <= 'z':  # lowercase → uppercase
        result += chr(ord(ch) - 32)
    elif 'A' <= ch <= 'Z':  # uppercase → lowercase
        result += chr(ord(ch) + 32)
    else:
        result += ch  # keep non-alphabet characters unchanged

# Step 3: Output
print(result)
