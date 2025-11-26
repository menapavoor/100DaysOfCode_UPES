# Program to search for an element in an array using linear search

# Step 1: Input size
n = int(input("Enter size of array: "))

# Step 2: Input elements
arr = list(map(int, input("Enter elements: ").split()))

# Step 3: Input element to search
key = int(input("Enter element to search: "))

# Step 4: Linear search
found = -1
for i in range(n):
    if arr[i] == key:
        found = i
        break

# Step 5: Output
if found != -1:
    print("Found at index", found)
else:
    print(-1)