# Program to print initials with surname in full

# Step 1: Input full name
name = input().strip().split()

# Step 2: Build initials for all except last word
initials = ""
for word in name[:-1]:
    initials += word[0].upper() + "."

# Step 3: Add surname in full
surname = name[-1]

# Step 4: Output
print(initials + " " + surname)
