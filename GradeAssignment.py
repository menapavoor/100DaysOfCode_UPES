# Program to assign grade based on percentage

# Step 1: Input
percentage = int(input("Enter percentage: "))

# Step 2: Conditions
if 90 <= percentage <= 100:
    print("Grade A")
elif 80 <= percentage < 90:
    print("Grade B")
elif 70 <= percentage < 80:
    print("Grade C")
elif 60 <= percentage < 70:
    print("Grade D")
elif 0 <= percentage < 60:
    print("Grade F")
else:
    print("Invalid percentage")
