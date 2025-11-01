# Program to check if a matrix is symmetric

# Step 1: Input dimensions
rows, cols = map(int, input().split())

# Step 2: Read matrix
matrix = []
for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

# Step 3: Check symmetry
if rows != cols:
    print("False")  # non-square matrix cannot be symmetric
else:
    symmetric = True
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != matrix[j][i]:
                symmetric = False
                break
        if not symmetric:
            break

    # Step 4: Output
    print("True" if symmetric else "False")
