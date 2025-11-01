# Program to count vowels and consonants in a string

# Step 1: Input string
s = input().lower()   # convert to lowercase for easy comparison

# Step 2: Initialize counters
vowels = 0
consonants = 0

# Step 3: Check each character
for ch in s:
    if ch.isalpha():  # only consider alphabets
        if ch in "aeiou":
            vowels += 1
        else:
            consonants += 1

# Step 4: Output
print("Vowels={}, Consonants={}".format(vowels, consonants))
