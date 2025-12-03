# Program to insert an element in an array at a given position

# Step 1: Input size
n = int(input("Enter size of array: "))

# Step 2: Input array
arr = list(map(int, input("Enter elements: ").split()))

# Step 3: Input position and element
pos, x = map(int, input("Enter position and element: ").split())

# Step 4: Insert element at given position
arr.insert(pos, x)

# Step 5: Output
for i in arr:
    print(i, end=" ")