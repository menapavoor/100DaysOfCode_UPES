# Program to find the pivot index of an array

# Step 1: Input array
nums = list(map(int, input("Enter array: ").strip("[]").split(',')))

# Step 2: Compute total sum
total_sum = sum(nums)

# Step 3: Traverse and check pivot
left_sum = 0
pivot_index = -1

for i in range(len(nums)):
    right_sum = total_sum - left_sum - nums[i]
    if left_sum == right_sum:
        pivot_index = i
        break
    left_sum += nums[i]

# Step 4: Output
print(pivot_index)