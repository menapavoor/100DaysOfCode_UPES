def max_subarray_sum(arr):
    # Initialize with the first element
    max_ending_here = arr[0]
    max_so_far = arr[0]

    # Traverse the array
    for i in range(1, len(arr)):
        # Either extend the previous subarray or start new from current element
        max_ending_here = max(arr[i], max_ending_here + arr[i])
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far


if __name__ == "__main__":
    # Example 1
    arr1 = [2, 3, -8, 7, -1, 2, 3]
    print(max_subarray_sum(arr1))  # Output: 11

    # Example 2
    arr2 = [-2, -4]
    print(max_subarray_sum(arr2))  # Output: -2

    # Example 3
    arr3 = [5, 4, 1, 7, 8]
    print(max_subarray_sum(arr3))  # Output: 25
