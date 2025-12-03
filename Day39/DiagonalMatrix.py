# Program to check if diagonal elements of a matrix are distinct

# Step 1: Input rows and columns
rows, cols = map(int, input().split())

# Step 2: Read matrix
matrix = []
for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

# Step 3: Check distinctness of diagonal elements
diagonal = set()
distinct = True
for i in range(min(rows, cols)):
    if matrix[i][i] in diagonal:
        distinct = False
        break
    diagonal.add(matrix[i][i])

# Step 4: Output
print("True" if distinct else "False")