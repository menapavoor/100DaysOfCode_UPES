# Program to replace spaces with hyphens in a string

# Step 1: Input string
s = input()

# Step 2: Replace manually
result = ""
for ch in s:
    if ch == " ":
        result += "-"
    else:
        result += ch

# Step 3: Output
print(result)