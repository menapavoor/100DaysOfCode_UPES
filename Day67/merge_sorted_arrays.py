def merge_sorted_arrays(nums1, nums2):
    i, j = 0, 0
    merged = []

    # Traverse both arrays
    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1

    # Add remaining elements
    while i < len(nums1):
        merged.append(nums1[i])
        i += 1

    while j < len(nums2):
        merged.append(nums2[j])
        j += 1

    return merged


if __name__ == "__main__":
    # Example 1
    nums1 = [2, 7, 11, 15]
    nums2 = [4, 8, 10]
    print(*merge_sorted_arrays(nums1, nums2))  # Output: 2 4 7 8 10 11 15

    # Example 2
    nums1 = [1, 2, 7]
    nums2 = [9, 10, 17]
    print(*merge_sorted_arrays(nums1, nums2))  # Output: 1 2 7 9 10 17

    # Example 3
    nums1 = [-10, -2, 7]
    nums2 = [-3, -1, 7]
    print(*merge_sorted_arrays(nums1, nums2))  # Output: -10 -3 -2 -1 7 7
