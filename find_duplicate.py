def find_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)
    return -1  # fallback, though problem guarantees one duplicate


if __name__ == "__main__":
    # Example 1
    nums1 = [1, 3, 3, 4]
    print(find_duplicate(nums1))  # Output: 3

    # Example 2
    nums2 = [1, 2, 2]
    print(find_duplicate(nums2))  # Output: 2

    # Example 3
    nums3 = [0, 4, 1, 1, 5]
    print(find_duplicate(nums3))  # Output: 1
