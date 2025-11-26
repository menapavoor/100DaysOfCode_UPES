# Program to find the sum of array elements

# Step 1: Input size
n = int(input("Enter size of array: "))

# Step 2: Input elements
arr = list(map(int, input("Enter elements: ").split()))

# Step 3: Calculate sum
total = 0
for i in range(n):
    total += arr[i]

# Step 4: Output
print(total)