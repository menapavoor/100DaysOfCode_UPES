def kth_smallest(arr, k):
    # Sort the array
    arr.sort()
    # Return the kth smallest (1-based index)
    return arr[k-1]


if __name__ == "__main__":
    # Example 1
    arr1 = [10, 5, 4, 3, 48, 6, 2, 33, 53, 10]
    k1 = 4
    print(kth_smallest(arr1, k1))  # Output: 5

    # Example 2
    arr2 = [7, 10, 4, 3, 20, 15]
    k2 = 3
    print(kth_smallest(arr2, k2))  # Output: 7
