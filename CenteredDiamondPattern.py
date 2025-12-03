# Program to print centered diamond pattern (Q54)

rows = 4  # top half rows

# Top half
for i in range(1, rows + 1):
    # print spaces
    for s in range(rows - i):
        print(" ", end="")
    # print stars
    for j in range(2 * i - 1):
        print("*", end="")
    print()

# Bottom half
for i in range(rows - 1, 0, -1):
    # print spaces
    for s in range(rows - i):
        print(" ", end="")
    # print stars
    for j in range(2 * i - 1):
        print("*", end="")
    print()
