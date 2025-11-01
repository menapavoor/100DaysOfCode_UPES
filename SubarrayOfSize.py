# Program to find maximum element in each subarray of size k (brute force)

# Step 1: Input array and k
arr = list(map(int, input("Enter array: ").strip("[]").split(',')))
k = int(input("Enter k: "))
n = len(arr)

# Step 2: Edge case
if k > n or k <= 0:
    print("Invalid k")
else:
    result = []
    # Step 3: Traverse all windows
    for i in range(n - k + 1):
        window_max = arr[i]
        for j in range(i, i + k):
            if arr[j] > window_max:
                window_max = arr[j]
        result.append(window_max)

    # Step 4: Print results space-separated
    print(" ".join(map(str, result)))
