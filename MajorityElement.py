# Program to find the ceil of x in a sorted array

def find_ceil(arr, x):
    low, high = 0, len(arr) - 1
    result = -1  # default if no ceil exists
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] >= x:
            result = mid       # possible ceil found
            high = mid - 1     # look for earlier occurrence
        else:
            low = mid + 1      # move right
    
    return result

# ---- Main Program ----
arr = list(map(int, input("Enter sorted array: ").strip("[]").split(',')))
x = int(input("Enter x: "))

print(find_ceil(arr, x))
