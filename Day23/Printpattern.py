# Program to print a 5x5 star pattern

# Step 1: Fixed rows and columns
rows = 5
cols = 5

# Step 2: Nested loops
for i in range(rows):
    for j in range(cols):
        print("*", end="")
    print()  # move to next line