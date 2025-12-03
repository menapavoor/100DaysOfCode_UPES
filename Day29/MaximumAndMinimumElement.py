# Program to find maximum and minimum element in an array

# Step 1: Input size
n = int(input("Enter size of array: "))

# Step 2: Input elements
arr = list(map(int, input("Enter elements: ").split()))

# Step 3: Initialize max and min
max_val = arr[0]
min_val = arr[0]

# Step 4: Traverse array
for i in range(1, n):
    if arr[i] > max_val:
        max_val = arr[i]
    if arr[i] < min_val:
        min_val = arr[i]

# Step 5: Output
print("Max={}, Min={}".format(max_val, min_val))