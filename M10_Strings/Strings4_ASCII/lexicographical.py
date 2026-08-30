# Program 2: Lexicographically Next String
s = input("Enter the string: ")
i = len(s) - 1

# Find the rightmost character that is not 'z'
while i >= 0 and s[i] == 'z':
    i -= 1

if i >= 0:
    # Increment that character and keep the rest unchanged
    result = s[:i] + chr(ord(s[i]) + 1) + s[i+1:]

print("Next string:", result)