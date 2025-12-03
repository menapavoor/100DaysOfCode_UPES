# Program to reverse each word in a sentence without changing word order

# Step 1: Input sentence
s = input()

# Step 2: Reverse each word
words = s.split(' ')  # preserve spacing positions if multiple spaces
reversed_words = []
for w in words:
    rev = ""
    for ch in w:
        rev = ch + rev
    reversed_words.append(rev)

# Step 3: Output
print(' '.join(reversed_words))