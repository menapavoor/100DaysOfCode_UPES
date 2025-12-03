# Program to count positive, negative, and zero elements in an array

# Step 1: Input size
n = int(input("Enter size of array: "))

# Step 2: Input elements
arr = list(map(int, input("Enter elements: ").split()))

# Step 3: Initialize counters
pos_count = 0
neg_count = 0
zero_count = 0

# Step 4: Traverse array
for i in range(n):
    if arr[i] > 0:
        pos_count += 1
    elif arr[i] < 0:
        neg_count += 1
    else:
        zero_count += 1

# Step 5: Output
print("Positive={}, Negative={}, Zero={}".format(pos_count, neg_count, zero_count))
