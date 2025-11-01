# Program to multiply two matrices

# Step 1: Input first matrix
r1, c1 = map(int, input().split())
A = []
for i in range(r1):
    row = list(map(int, input().split()))
    A.append(row)

# Step 2: Input second matrix
r2, c2 = map(int, input().split())
B = []
for i in range(r2):
    row = list(map(int, input().split()))
    B.append(row)

# Step 3: Check multiplication condition
if c1 != r2:
    print("Matrix multiplication not possible")
else:
    # Step 4: Initialize result matrix with zeros
    C = [[0] * c2 for _ in range(r1)]

    # Step 5: Perform multiplication
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                C[i][j] += A[i][k] * B[k][j]

    # Step 6: Print result
    for i in range(r1):
        for j in range(c2):
            print(C[i][j], end=" ")
        print()
