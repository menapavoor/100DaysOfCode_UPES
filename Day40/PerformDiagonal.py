# Program to perform diagonal traversal of a matrix

# Step 1: Input rows and columns
rows, cols = map(int, input().split())

# Step 2: Read matrix
matrix = []
for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

# Step 3: Diagonal traversal
result = []

# Traverse starting from first row
for col in range(cols):
    i, j = 0, col
    while i < rows and j >= 0:
        result.append(matrix[i][j])
        i += 1
        j -= 1

# Traverse starting from last column (excluding first row)
for row in range(1, rows):
    i, j = row, cols - 1
    while i < rows and j >= 0:
        result.append(matrix[i][j])
        i += 1
        j -= 1

# Step 4: Output
print(*result)