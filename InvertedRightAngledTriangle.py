# Program to print inverted right-angled triangle with spaces

rows = 5
for i in range(rows):
    # print spaces
    for s in range(i):
        print(" ", end="")
    # print stars
    for j in range(rows - i):
        print("*", end="")
    print()
