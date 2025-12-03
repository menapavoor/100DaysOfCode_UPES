# Program to find the majority element in an array

# Step 1: Input array
nums = list(map(int, input("Enter array: ").strip("[]").split(',')))
n = len(nums)

# Step 2: Count frequencies
freq = {}
for num in nums:
    freq[num] = freq.get(num, 0) + 1

# Step 3: Check majority condition
majority = -1
for key, val in freq.items():
    if val > n // 2:
        majority = key
        break

# Step 4: Output
print(majority)
