# Program to merge two arrays

# Step 1: Input first array
n1 = int(input("Enter size of first array: "))
arr1 = list(map(int, input("Enter elements of first array: ").split()))

# Step 2: Input second array
n2 = int(input("Enter size of second array: "))
arr2 = list(map(int, input("Enter elements of second array: ").split()))

# Step 3: Merge arrays
merged = arr1 + arr2

# Step 4: Output
for i in merged:
    print(i, end=" ")
