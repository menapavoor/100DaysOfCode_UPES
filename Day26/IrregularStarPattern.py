# Program to print irregular star pattern

# Define the sequence of stars per row
pattern = [1, 1, 2, 3, 4, 5, 3, 1]

# Loop through the sequence
for count in pattern:
    for j in range(count):
        print("*")
    print()  # blank line between groups