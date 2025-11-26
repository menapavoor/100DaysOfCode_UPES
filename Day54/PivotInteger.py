# Program to find the pivot integer

import math

# Step 1: Input
n = int(input())

# Step 2: Compute total sum
total = n * (n + 1) // 2

# Step 3: Check if total is a perfect square
x = int(math.isqrt(total))  # integer square root
if x * x == total:
    print(x)
else:
    print(-1)