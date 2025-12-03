# Program to insert an element in a sorted array

# Step 1: Input size
n = int(input("Enter size of array: "))

# Step 2: Input sorted array
arr = list(map(int, input("Enter elements: ").split()))

# Step 3: Input element to insert
x = int(input("Enter element to insert: "))

# Step 4: Find correct position
pos = n
for i in range(n):
    if arr[i] > x:
        pos = i
        break

# Step 5: Insert element at position
arr.insert(pos, x)

# Step 6: Output
for i in arr:
    print(i, end=" ")
