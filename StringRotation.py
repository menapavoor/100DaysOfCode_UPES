# Program to check if one string is a rotation of another

# Step 1: Input strings
s1 = input().strip()
s2 = input().strip()

# Step 2: Check rotation
if len(s1) != len(s2):
    print("Not rotation")
elif s2 in (s1 + s1):
    print("Rotation")
else:
    print("Not rotation")
