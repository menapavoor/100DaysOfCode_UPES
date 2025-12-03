# Program to find the first repeating lowercase alphabet in a string

# Step 1: Input string
s = input()

# Step 2: Track seen characters
seen = set()
first_repeat = None

# Step 3: Traverse string
for ch in s:
    if 'a' <= ch <= 'z':  # only lowercase alphabets
        if ch in seen:
            first_repeat = ch
            break
        else:
            seen.add(ch)

# Step 4: Output
if first_repeat:
    print(first_repeat)
else:
    print("No repeating lowercase alphabet")