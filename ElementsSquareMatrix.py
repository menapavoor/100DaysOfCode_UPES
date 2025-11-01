# Program to find the sum of main diagonal elements of a square matrix

# Step 1: Input rows and columns
rows, cols = map(int, input().split())

# Step 2: Read matrix
matrix = []
for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

# Step 3: Calculate diagonal sum
total = 0
for i in range(min(rows, cols)):
    total += matrix[i][i]

# Step 4: Output
print(total)
