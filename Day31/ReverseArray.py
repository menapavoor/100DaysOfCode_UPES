# Program to reverse an array without extra space

# Step 1: Input size
n = int(input("Enter size of array: "))

# Step 2: Input elements
arr = list(map(int, input("Enter elements: ").split()))

# Step 3: Reverse in-place
start = 0
end = n - 1
while start < end:
    arr[start], arr[end] = arr[end], arr[start]  # swap
    start += 1
    end -= 1

# Step 4: Output
for i in range(n):
    print(arr[i], end=" ")