def two_sum(nums, target):
    seen = {}  # dictionary to store number -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return seen[complement], i
        seen[num] = i
    return -1, -1


if __name__ == "__main__":
    # Example 1
    nums1, target1 = [2, 7, 11, 15], 9
    i, j = two_sum(nums1, target1)
    print(i, j)  # Output: 0 1

    # Example 2
    nums2, target2 = [3, 2, 4], 6
    i, j = two_sum(nums2, target2)
    print(i, j)  # Output: 1 2

    # Example 3
    nums3, target3 = [3, 3], 6
    i, j = two_sum(nums3, target3)
    print(i, j)  # Output: 0 1
