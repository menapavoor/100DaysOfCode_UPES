# Program to find sum of the series: 2/3 + 4/7 + 6/11 + ... up to n terms

# Step 1: Input
n = int(input("Enter number of terms: "))

# Step 2: Loop to calculate sum
total = 0
for i in range(1, n + 1):
    numerator = 2 * i
    denominator = 4 * i - 1
    total += numerator / denominator

# Step 3: Output (rounded for approximation)
print("Approximate sum:", round(total, 2))