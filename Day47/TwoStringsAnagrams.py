# Program to check if two strings are anagrams

# Step 1: Input two strings
s1 = input().strip()
s2 = input().strip()

# Step 2: Check lengths first
if len(s1) != len(s2):
    print("Not anagrams")
else:
    # Step 3: Sort and compare
    if sorted(s1) == sorted(s2):
        print("Anagrams")
    else:
        print("Not anagrams")