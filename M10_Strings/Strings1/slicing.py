text = "Hello, Python World! 🌍"
print(text)          # Output: Hello, Python World! 🌍
print(len(text))     # Output: 22 (includes space, punctuation, and emoji)

"""
string[start:end:step]
"""

text = "Hello, Python World! 🌍"

print(text[0:5])      # Hello
print(text[7:13])     # Python
print(text[7:])       # Python World! 🌍   (from index 7 to end)
print(text[:5])       # Hello               (from start to index 5)
print(text[:])        # entire string (copy)

#negative indexing slicing
print(text[-6:])      # World! 🌍
print(text[-11:-6])   # Python
print(text[:-7])      # Hello, Python      (everything except last 7 chars)

# step parameter (skip characters)
print(text[::2])      # Hlo yhnWrd!🌍   (every 2nd character)
print(text[::-1])     # 🌍 !dlroW nohtyP ,olleH   (reverse the string)
print(text[7:13:2])   # Pto                (Python sliced every 2nd char)

#concatenation:Method 01
greeting = "Hello"
name = "Kamrul"
result = greeting + ", " + name + "!"
print(result)                    # Hello, Kamrul!

#Method 2: += (in-place looking, but still creates new string)
message = "Hello"
message += ", Python!"
print(message)                   # Hello, Python!

# Method 3: str.join() (best for joining many strings)
words = ["Hello", "Python", "World"]
joined = " ".join(words)
print(joined)                    # Hello Python World

# With custom separator
csv = ",".join(["apple", "banana", "cherry"])
print(csv)                       # apple,banana,cherry

# Replacing Substrings
# string.replace(old, new, count)
text = "Hello, Python World! 🌍"
new_text = text.replace("Python", "C")
print(new_text)                  # Hello, C World! 🌍

# Deletion / Removing Parts of a String
text = "Hello, Python World! 🌍"

# Delete first 7 characters
print(text[7:])                  # Python World! 🌍

# Delete last 7 characters
print(text[:-8])                 # Hello, Python

# Delete from index 5 to 13
print(text[:5] + text[13:])      # Hello World! 🌍