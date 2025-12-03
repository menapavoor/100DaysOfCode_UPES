from collections import deque

def first_negative_in_window(arr, k):
    n = len(arr)
    q = deque()   # will store indices of negative numbers
    result = []

    # Process first window
    for i in range(k):
        if arr[i] < 0:
            q.append(i)

    # Process the rest of the windows
    for i in range(k, n):
        # Add result for previous window
        if q:
            result.append(arr[q[0]])
        else:
            result.append(0)

        # Remove elements out of this window
        while q and q[0] <= i - k:
            q.popleft()

        # Add current element if it is negative
        if arr[i] < 0:
            q.append(i)

    # For the last window
    if q:
        result.append(arr[q[0]])
    else:
        result.append(0)

    return result


if __name__ == "__main__":
    # Example 1
    arr1 = [-8, 2, 3, -6, 10]
    k1 = 2
    print(*first_negative_in_window(arr1, k1))  # Output: -8 0 -6 -6

    # Example 2
    arr2 = [12, -1, -7, 8, -15, 30, 16, 28]
    k2 = 3
    print(*first_negative_in_window(arr2, k2))  # Output: -1 -1 -7 -15 -15 0

    # Example 3
    arr3 = [12, 1, 3, 5]
    k3 = 3
    print(*first_negative_in_window(arr3, k3))  # Output: 0 0
