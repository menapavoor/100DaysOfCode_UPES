# Step 1: Open file in read mode
file_name = "info.txt"

try:
    with open(file_name, "r") as f:
        # Step 2: Read and print until EOF
        for line in f:
            print(line.strip())  # strip() removes newline characters
except FileNotFoundError:
    print(f"Error: Could not open file {file_name}")
