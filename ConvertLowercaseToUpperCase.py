# Program to convert lowercase string to uppercase without built-in functions

# Step 1: Input string
s = input()

# Step 2: Convert manually
result = ""
for ch in s:
    if 'a' <= ch <= 'z':  # check if lowercase
        result += chr(ord(ch) - 32)
    else:
        result += ch  # keep as is (spaces, punctuation, etc.)

# Step 3: Output
print(result)
