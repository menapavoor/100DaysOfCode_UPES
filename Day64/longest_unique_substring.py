def length_of_longest_substring(s: str) -> int:
    char_index = {}   # stores the last index of each character
    left = 0          # left pointer of the sliding window
    max_len = 0

    for right in range(len(s)):
        # If character already seen, move left pointer
        if s[right] in char_index and char_index[s[right]] >= left:
            left = char_index[s[right]] + 1

        # Update the last index of the current character
        char_index[s[right]] = right

        # Update max length
        max_len = max(max_len, right - left + 1)

    return max_len


if __name__ == "__main__":
    # Example 1
    s1 = "abcabcbb"
    print(length_of_longest_substring(s1))  # Output: 3

    # Example 2
    s2 = "bbbbb"
    print(length_of_longest_substring(s2))  # Output: 1

    # Example 3
    s3 = "pwwkew"
    print(length_of_longest_substring(s3))  # Output: 3
