# Program to print the number triangle with indentation

rows = 5
for i in range(1, rows + 1):
    # print spaces
    for s in range(rows - i):
        print(" ", end="")
    # print numbers
    for j in range(rows - i + 1, rows + 1):
        print(j, end="")
    print()