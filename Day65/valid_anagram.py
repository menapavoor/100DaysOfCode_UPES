def is_anagram(s: str, t: str) -> str:
    # If lengths differ, they can't be anagrams
    if len(s) != len(t):
        return "Not Anagram"
    
    # Compare sorted strings
    if sorted(s) == sorted(t):
        return "Anagram"
    else:
        return "Not Anagram"


if __name__ == "__main__":
    # Example 1
    s1, t1 = "anagram", "nagaram"
    print(is_anagram(s1, t1))  # Output: Anagram

    # Example 2
    s2, t2 = "rat", "car"
    print(is_anagram(s2, t2))  # Output: Not Anagram
