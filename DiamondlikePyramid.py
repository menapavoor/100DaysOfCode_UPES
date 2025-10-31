# Program to print pyramid pattern (Q53)

rows = 5  # maximum row count for top half

# Top half
for i in range(1, rows + 1):
    for j in range(2 * i - 1):
        print("*", end="")
    print()

# Bottom half
for i in range(rows - 1, 0, -1):
    for j in range(2 * i - 1):
        print("*", end="")
    print()
