# Program to find first and last occurrence of target in sorted array

def find_first(nums, target):
    low, high = 0, len(nums) - 1
    first = -1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            first = mid
            high = mid - 1  # keep searching left
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return first

def find_last(nums, target):
    low, high = 0, len(nums) - 1
    last = -1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            last = mid
            low = mid + 1  # keep searching right
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return last

# ---- Main Program ----
nums = list(map(int, input("Enter sorted array: ").strip("[]").split(',')))
target = int(input("Enter target: "))

first = find_first(nums, target)
last = find_last(nums, target)

print(f"{first},{last}")