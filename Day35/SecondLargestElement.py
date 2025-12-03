# Program to find the second largest element in an array

# Step 1: Input size
n = int(input("Enter size of array: "))

# Step 2: Input elements
arr = list(map(int, input("Enter elements: ").split()))

# Step 3: Initialize largest and second largest
largest = second_largest = float('-inf')

# Step 4: Traverse array
for num in arr:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

# Step 5: Output
print(second_largest)