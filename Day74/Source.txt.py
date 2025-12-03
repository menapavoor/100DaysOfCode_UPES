# Q124: Copy file content character by character

source_file = input("Enter source filename: ")
dest_file = input("Enter destination filename: ")

try:
    with open(source_file, "r") as src, open(dest_file, "w") as dest:
        while True:
            ch = src.read(1)  # read one character
            if not ch:        # EOF reached
                break
            dest.write(ch)

    print(f"File copied successfully to {dest_file}")

except FileNotFoundError:
    print(f"Error: Could not open source file {source_file}")
