# Program to find the sum of all elements in a matrix

# Step 1: Input rows and columns
rows, cols = map(int, input().split())

# Step 2: Read matrix
matrix = []
for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

# Step 3: Calculate sum
total = 0
for i in range(rows):
    for j in range(cols):
        total += matrix[i][j]

# Step 4: Output
print(total)
