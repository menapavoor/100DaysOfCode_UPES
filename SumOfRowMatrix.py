# Program to find the sum of each row of a matrix

# Step 1: Input rows and columns
rows, cols = map(int, input().split())

# Step 2: Read matrix
matrix = []
for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

# Step 3: Calculate row sums
row_sums = []
for i in range(rows):
    total = 0
    for j in range(cols):
        total += matrix[i][j]
    row_sums.append(total)

# Step 4: Output
for val in row_sums:
    print(val, end=" ")
