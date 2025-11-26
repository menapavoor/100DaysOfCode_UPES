# Program to count even and odd numbers in an array

# Step 1: Input size
n = int(input("Enter size of array: "))

# Step 2: Input elements
arr = list(map(int, input("Enter elements: ").split()))

# Step 3: Initialize counters
even_count = 0
odd_count = 0

# Step 4: Traverse array
for i in range(n):
    if arr[i] % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

# Step 5: Output
print("Even={}, Odd={}".format(even_count, odd_count))