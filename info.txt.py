import os

# Step 1: Create folder "day71" if it doesn't exist
folder_name = "day71"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)

# Step 2: Take input
name = input("Enter name: ")
age = input("Enter age: ")

# Step 3: Define file path inside folder
file_path = os.path.join(folder_name, "info.txt")

# Step 4: Open file in write mode and save data
with open(file_path, "w") as f:
    f.write(f"Name: {name} Age: {age}\n")

# Step 5: Confirmation
print(f"File created successfully! Data written to {file_path}")
