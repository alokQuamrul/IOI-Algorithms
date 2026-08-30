def remove_all_whitespace(string):
    """Remove all whitespace characters (spaces, tabs, newlines)"""
    return "".join(string.split())

# Example usage
text = """Hello   World
This is a test
    With tabs and new lines"""

result = remove_all_whitespace(text)
print("Original:", repr(text))
print("Cleaned :", result)