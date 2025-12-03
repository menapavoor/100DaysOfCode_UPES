# Program to calculate electricity bill

# Step 1: Input
units = int(input("Enter units consumed: "))

# Step 2: Conditions
if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = (100 * 5) + (units - 100) * 7
elif units <= 300:
    bill = (100 * 5) + (100 * 7) + (units - 200) * 10
else:
    bill = (100 * 5) + (100 * 7) + (100 * 10) + (units - 300) * 12

# Step 3: Output
print("Bill: ₹", bill)