# Program to find the largest of three numbers

# Step 1: Input
a, b, c = map(int, input("Enter three numbers: ").split())

# Step 2: Conditions
if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

# Step 3: Output
print("Largest is", largest)