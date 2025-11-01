# Program to search in a sorted array using binary search

# Step 1: Input size
n = int(input("Enter size of array: "))

# Step 2: Input sorted array
arr = list(map(int, input("Enter elements: ").split()))

# Step 3: Input element to search
key = int(input("Enter element to search: "))

# Step 4: Binary search
low, high = 0, n - 1
found = -1

while low <= high:
    mid = (low + high) // 2
    if arr[mid] == key:
        found = mid
        break
    elif arr[mid] < key:
        low = mid + 1
    else:
        high = mid - 1

# Step 5: Output
if found != -1:
    print("Found at index", found)
else:
    print(-1)
