# Program to change date format from dd/mm/yyyy to dd-Mmm-yyyy

# Step 1: Input date
date_str = input().strip()  # e.g., 15/04/2025

# Step 2: Split into parts
dd, mm, yyyy = date_str.split('/')

# Step 3: Month map
month_map = {
    "01": "Jan", "02": "Feb", "03": "Mar", "04": "Apr",
    "05": "May", "06": "Jun", "07": "Jul", "08": "Aug",
    "09": "Sep", "10": "Oct", "11": "Nov", "12": "Dec"
}

# Step 4: Format output
print(f"{dd}-{month_map.get(mm, mm)}-{yyyy}")