# Program to calculate library fine

# Step 1: Input
days = int(input("Enter number of late days: "))

# Step 2: Conditions
if days <= 5:
    fine = days * 2
    print("Fine ₹", fine)
elif days <= 10:
    fine = (5 * 2) + (days - 5) * 4
    print("Fine ₹", fine)
elif days <= 30:
    fine = (5 * 2) + (5 * 4) + (days - 10) * 6
    print("Fine ₹", fine)
else:
    print("Membership Cancelled")
