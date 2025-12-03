# Program to read and print elements of a 1D array

# Step 1: Input size
n = int(input("Enter size of array: "))

# Step 2: Input elements
arr = list(map(int, input("Enter elements: ").split()))

# Step 3: Print elements
for i in range(n):
    print(arr[i], end=" ")