# Program to find maximum sum of subarrays of size k

# Step 1: Input array and k
arr = list(map(int, input("Enter array: ").strip("[]").split(',')))
k = int(input("Enter k: "))
n = len(arr)

# Step 2: Edge case
if k > n or k <= 0:
    print("Invalid k")
else:
    # Step 3: Compute sum of first window
    window_sum = sum(arr[:k])
    max_sum = window_sum

    # Step 4: Slide the window
    for i in range(k, n):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)

    # Step 5: Output
    print(max_sum)
