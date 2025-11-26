# Program to print all substrings of a string, comma-separated

# Step 1: Input string
s = input().strip()

# Step 2: Generate substrings
subs = []
n = 0
for _ in s:  # manual length count (if needed)
    n += 1

for i in range(n):
    for j in range(i + 1, n + 1):
        subs.append(s[i:j])

# Step 3: Output
print(",".join(subs))