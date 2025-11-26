# Program to check whether a character is a vowel or consonant

# Step 1: Input
ch = input("Enter a character: ")

# Step 2: Condition
if ch.lower() in ['a', 'e', 'i', 'o', 'u']:
    print("Vowel")
else:
    print("Consonant")