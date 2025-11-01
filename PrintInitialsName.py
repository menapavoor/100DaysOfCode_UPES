# Program to print the initials of a name

# Step 1: Input full name
name = input().strip().split()

# Step 2: Collect initials
initials = ""
for word in name:
    initials += word[0].upper() + "."

# Step 3: Output
print(initials)
