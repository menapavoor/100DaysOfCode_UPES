# Program to find the longest word in a sentence

# Step 1: Input sentence
sentence = input().strip()

# Step 2: Split into words
words = sentence.split()

# Step 3: Find longest word
longest = ""
for word in words:
    if len(word) > len(longest):
        longest = word

# Step 4: Output
print(longest)