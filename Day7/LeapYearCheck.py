# Program to check if a year is a leap year

# Step 1: Input
year = int(input("Enter a year: "))

# Step 2: Conditions
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap year")
else:
    print("Not a leap year")