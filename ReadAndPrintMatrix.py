# Program to read and print a matrix

# Step 1: Input rows and columns
rows, cols = map(int, input().split())

# Step 2: Read matrix
matrix = []
for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

# Step 3: Print matrix
for i in range(rows):
    for j in range(cols):
        print(matrix[i][j], end=" ")
    print()
