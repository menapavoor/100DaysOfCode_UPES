# Program to remove all vowels from a string

# Step 1: Input string
s = input()

# Step 2: Define vowels
vowels = "aeiouAEIOU"

# Step 3: Build result without vowels
result = ""
for ch in s:
    if ch not in vowels:
        result += ch

# Step 4: Output
print(result)
