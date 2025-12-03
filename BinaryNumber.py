# Program to find 1's complement of a binary number

# Step 1: Input
binary = input("Enter a binary number: ")

# Step 2: Flip each bit
ones_complement = ""
for bit in binary:
    if bit == '0':
        ones_complement += '1'
    elif bit == '1':
        ones_complement += '0'
    else:
        print("Invalid binary number")
        exit()

# Step 3: Output
print(ones_complement)
