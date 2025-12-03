# Program to classify a character

# Step 1: Input
ch = input("Enter a character: ")

# Step 2: Conditions
if 'A' <= ch <= 'Z':
    print("Uppercase alphabet")
elif 'a' <= ch <= 'z':
    print("Lowercase alphabet")
elif '0' <= ch <= '9':
    print("Digit")
else:
    print("Special character")