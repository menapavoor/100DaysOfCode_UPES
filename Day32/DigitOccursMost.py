# Program to find the digit that occurs the most times in an integer

# Step 1: Input number
num = int(input("Enter a number: "))

# Step 2: Initialize frequency array for digits 0-9
freq = [0] * 10

# Step 3: Count digit frequencies
n = num
while n > 0:
    digit = n % 10
    freq[digit] += 1
    n //= 10

# Step 4: Find digit with maximum frequency
max_freq = freq[0]
digit_with_max = 0
for d in range(10):
    if freq[d] > max_freq:
        max_freq = freq[d]
        digit_with_max = d

# Step 5: Output
print(digit_with_max)