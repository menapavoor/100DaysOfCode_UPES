# Program to rotate an array to the right by k positions

# Step 1: Input size
n = int(input("Enter size of array: "))

# Step 2: Input elements
arr = list(map(int, input("Enter elements: ").split()))

# Step 3: Input k
k = int(input("Enter k: "))

# Step 4: Normalize k
k = k % n

# Step 5: Rotate using slicing
rotated = arr[-k:] + arr[:-k]

# Step 6: Output
for i in rotated:
    print(i, end=" ")