# Program to display day of the week based on number (1–7)

# Step 1: Input
day_num = int(input("Enter a number (1-7): "))

# Step 2: Mapping using dictionary
days = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday"
}

# Step 3: Output
print(days.get(day_num, "Invalid input"))
