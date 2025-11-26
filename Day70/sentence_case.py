def to_sentence_case(s: str) -> str:
    # Split into words, capitalize each, then join back
    words = s.split()
    capitalized_words = [word.capitalize() for word in words]
    return " ".join(capitalized_words)


if __name__ == "__main__":
    # Example 1
    s1 = "I am trying to build logic."
    print(to_sentence_case(s1))  # Output: I Am Trying To Build Logic.

    # Example 2
    s2 = "The classes are supposed to start early."
    print(to_sentence_case(s2))  # Output: The Classes Are Supposed To Start Early.

    # Example 3
    s3 = "We are going to look at 26 different test cases."
    print(to_sentence_case(s3))  # Output: We Are Going To Look At 26 Different Test Cases.
