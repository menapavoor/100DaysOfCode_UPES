# Program to calculate Simple and Compound Interest

# Step 1: Input
P, R, T = map(float, input("Enter Principal, Rate, and Time: ").split())

# Step 2: Calculations
simple_interest = (P * R * T) / 100
compound_interest = P * ((1 + R/100) ** T) - P

# Step 3: Output (rounded to 2 decimals if needed)
print("Simple Interest =", round(simple_interest, 2))
print("Compound Interest =", round(compound_interest, 2))