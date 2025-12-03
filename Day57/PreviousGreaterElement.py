# Program to find the previous greater element for each element (brute force)

# Step 1: Input array
arr = list(map(int, input("Enter array: ").strip("[]").split(',')))
n = len(arr)

# Step 2: Initialize result list
result = []

# Step 3: Nested loop to find previous greater element
for i in range(n):
    prev_greater = -1
    for j in range(i - 1, -1, -1):  # look leftwards
        if arr[j] > arr[i]:
            prev_greater = arr[j]
            break
    result.append(prev_greater)

# Step 4: Print in comma-separated format
print(",".join(map(str, result)))