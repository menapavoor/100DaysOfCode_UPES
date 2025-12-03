file_name = "Sample.py"

try:
    with open(file_name, "r") as f:
        text = f.read()  # read entire file content

        # Count characters (including spaces and newlines)
        char_count = len(text)

        # Count words (split by whitespace)
        word_count = len(text.split())

        # Count lines (split by newline)
        line_count = text.count("\n") + 1 if text else 0

    # Output results
    print(f"Characters: {char_count}")
    print(f"Words: {word_count}")
    print(f"Lines: {line_count}")

except FileNotFoundError:
    print(f"Error: Could not open file {file_name}")
