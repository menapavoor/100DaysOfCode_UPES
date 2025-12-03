# Program to find HCF (GCD) of two numbers

# Step 1: Input
a, b = map(int, input("Enter two numbers: ").split())

# Step 2: Loop to find HCF
hcf = 1
for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        hcf = i

# Step 3: Output
print(hcf)
