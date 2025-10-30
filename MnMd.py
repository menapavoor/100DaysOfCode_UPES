# Program to display month name and number of days

# Step 1: Input
month_num = int(input("Enter month number (1-12): "))

# Step 2: Dictionary mapping
months = {
    1: ("January", 31),
    2: ("February", 28),   # ignoring leap year for now
    3: ("March", 31),
    4: ("April", 30),
    5: ("May", 31),
    6: ("June", 30),
    7: ("July", 31),
    8: ("August", 31),
    9: ("September", 30),
    10: ("October", 31),
    11: ("November", 30),
    12: ("December", 31)
}

# Step 3: Output
if month_num in months:
    name, days = months[month_num]
    print(f"{name}, {days} days")
else:
    print("Invalid month number")
