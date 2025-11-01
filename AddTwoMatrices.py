# Program to add two matrices

# Step 1: Input first matrix dimensions
r1, c1 = map(int, input().split())
A = []
for i in range(r1):
    row = list(map(int, input().split()))
    A.append(row)

# Step 2: Input second matrix dimensions
r2, c2 = map(int, input().split())
B = []
for i in range(r2):
    row = list(map(int, input().split()))
    B.append(row)

# Step 3: Check if dimensions match
if r1 != r2 or c1 != c2:
    print("Matrix dimensions do not match!")
else:
    # Step 4: Add matrices
    C = []
    for i in range(r1):
        row = []
        for j in range(c1):
            row.append(A[i][j] + B[i][j])
        C.append(row)

    # Step 5: Print result
    for i in range(r1):
        for j in range(c1):
            print(C[i][j], end=" ")
        print()
