def find_missing_number(nums):
    n = len(nums)  # array size is n, but numbers should be from 0..n
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum


if __name__ == "__main__":
    # Example 1
    nums1 = [0, 3, 2, 4]
    print(find_missing_number(nums1))  # Output: 1

    # Example 2
    nums2 = [1, 2, 3]
    print(find_missing_number(nums2))  # Output: 0

    # Example 3
    nums3 = [0, 4, 3, 1, 5]
    print(find_missing_number(nums3))  # Output: 2
