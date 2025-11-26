# Program to print the number pattern

rows = 5
for i in range(1, rows + 1):
    for j in range(6 - i, 6):   # start from (6 - i) to 5
        print(j, end="")
    print()