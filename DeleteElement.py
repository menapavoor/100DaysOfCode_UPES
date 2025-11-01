# Program to delete an element from an array

# Step 1: Input size
n = int(input("Enter size of array: "))

# Step 2: Input array
arr = list(map(int, input("Enter elements: ").split()))

# Step 3: Input element to delete
x = int(input("Enter element to delete: "))

# Step 4: Delete element if present
if x in arr:
    arr.remove(x)

# Step 5: Output
for i in arr:
    print(i, end=" ")
