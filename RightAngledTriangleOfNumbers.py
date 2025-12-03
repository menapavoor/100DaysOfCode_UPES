# Program to print right-angled triangle of numbers

# Step 1: Input (fixed 5 rows as per problem)
rows = 5

# Step 2: Nested loops
for i in range(1, rows + 1):   # row loop
    for j in range(1, i + 1):  # print numbers from 1 to i
        print(j, end="")
    print()  # move to next line
