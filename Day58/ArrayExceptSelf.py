# Program to compute product of array except self (O(n), no division)

# Step 1: Input array
nums = list(map(int, input("Enter array: ").strip("[]").split(',')))
n = len(nums)

# Step 2: Initialize result array
answer = [1] * n

# Step 3: Prefix products
prefix = 1
for i in range(n):
    answer[i] = prefix
    prefix *= nums[i]

# Step 4: Suffix products (multiply into answer)
suffix = 1
for i in range(n - 1, -1, -1):
    answer[i] *= suffix
    suffix *= nums[i]

# Step 5: Output
print(answer)