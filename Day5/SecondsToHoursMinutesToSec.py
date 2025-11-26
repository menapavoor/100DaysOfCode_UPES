# Program to convert seconds into hours:minutes:seconds

# Step 1: Input
total_seconds = int(input("Enter time in seconds: "))

# Step 2: Conversion
hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

# Step 3: Output
print(f"{hours}:{minutes}:{seconds}")